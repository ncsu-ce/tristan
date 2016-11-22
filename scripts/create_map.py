import sys

def map_files( file_a, file_b, file_out ):

    print 'Mapping ' + file_a + ' to ' + file_b


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

if __name__ == "__main__":

    if len( sys.argv ) == 5:

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


