import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input-file',
                        help='input file (eg: screenshot.jpg)',
                        type=str)
    args = parser.parse_args()

    if args.input_file is None:
        parser.print_help()
    else:
        print 'Pfad: {}'.format(args.input_file)
