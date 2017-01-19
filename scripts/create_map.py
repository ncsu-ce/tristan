import sys
from operator import itemgetter

def map_files( file_a, file_b, file_out ):

    print 'Mapping ' + file_a + ' to ' + file_b

    a_dat = read_14( file_a )
    b_dat = read_14( file_b )
    matches = []

    for x, d_a in a_dat.items():

        if x in b_dat:

            d_b = b_dat[ x ]

            for y, i_a in d_a.items():

                if y in d_b:

                    i_b = d_b[ y ]

                    matches.append( [i_a, i_b] )

    with open( file_out, 'w' ) as f:

        f.write( '{},{}\n'.format( file_a, file_b ) )
        f.write( '{:d}\n'.format( len( matches ) ) )

        for m in sorted( matches, key=itemgetter(0) ):

            f.write( '{:d},{:d}\n'.format( m[0], m[1] ) )


def zip_files( file_a, file_b, file_out ):

    print 'Zipping files ' + file_a + ' and ' + file_b

    with open( file_a, 'r' ) as fa:

        with open( file_b, 'r' ) as fb:

            data = zip( list( fa ), list( fb ) )

    with open( file_out, 'w' ) as f:

        f.write( '{},{}\n'.format( file_a, file_b ) )

        for m in data:

            f.write( '{},{}\n'.format( m[0].strip(), m[1].strip() ) )

def print_usage( usage, depth=1 ):

    for line in usage:

        if isinstance( line, str ):

            print depth*'    ' + line

        if isinstance( line, list ):

            print_usage( line, depth+1 )

def read_14( file ):

    data = dict()

    with open( file ) as f:

        f.readline()
        dat_line = f.readline().split()
        num_nodes = int( dat_line[1] )

        for l in range( num_nodes ):

            line = f.next().split()
            n = int( line[0] )
            x = float( line[1] )
            y = float( line[2] )

            if x not in data:

                data[ x ] = dict()

            data[ x ][ y ] = n

    return data



if __name__ == "__main__":

    if len( sys.argv ) >= 2:

        if sys.argv[1] == '-z':

            zip_files( sys.argv[2], sys.argv[3], sys.argv[4] )

        if sys.argv[1] == '-m':

            map_files( sys.argv[2], sys.argv[3], sys.argv[4] )

    else:

        usage = [
            'Usage:',
            'Zip files to create mapping:',
            [
                'python create_map.py -z [file 1] [file 2] [output file]'
            ],
            'Map all possible nodes in two fort.14 files:',
            [
                'python create_map.py -m [file 1] [file 2] [output file]'
            ]
        ]

        print_usage( usage )


