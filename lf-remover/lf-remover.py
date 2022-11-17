#!/usr/bin/python

import os
import sys
import getopt
import pyperclip


# error message
def help(program):
    print(program)
    print('')
    print('Input :')
    print('\t-i <inputfile> | -c : copy from inputfile | clipboard')
    print('\t--ifile=<inputfile> | --copy : copy from inputfile | clipboard')
    print('')
    print('Output (facultative):')
    print('\t-o <outputfile> | -p : paste to outputfile | clipboard')
    print('\t--ofile=<outputfile> | --paste : paste to outputfile | clipboard')
    sys.exit()


# get data from inputfile
def get_data_from_file(inputfile):
    if not os.path.exists(inputfile):
        print('File \'' + inputfile + '\' does not exist.')
        sys.exit()

    f = open(inputfile, 'r')
    return ' '.join(f.read().splitlines())


# get data from clipboard
def get_data_from_clipboard():
    return pyperclip.paste().replace('\n', ' ')


# get data from inputfile or clipboaard if specified
def get_data(inputfile, copy_from_clipboard):
    if not inputfile and not copy_from_clipboard:
        print('You must add a file with the -i (--ifile=<inputfile>) option or specify copy from clipboard with the -c (--copy) option.')
        print('Use -h (--help) option for more informations.')
        sys.exit()

    if copy_from_clipboard and inputfile != '':
        print('Copy from clipboard and input file specified. Input file ignored.')

    return get_data_from_clipboard() if copy_from_clipboard else get_data_from_file(inputfile)


# write data in stdout, outputfile or clipboard if specified
def write_data(data, outputfile, paste_to_clipboard):
    if paste_to_clipboard and outputfile != '':
        print('Paste to clipboard and output file specified. Output file ignored.')

    if paste_to_clipboard:
        pyperclip.copy(data)
    else:
        stdout = sys.stdout if not outputfile else open(outputfile, 'w')
        print(data, file=stdout)


def main(argv):
    inputfile = ''
    outputfile = ''
    copy_from_clipboard = False
    paste_to_clipboard = False

    try:
        opts, args = getopt.getopt(
            argv[1:], 'hcpi:o:', ['help', 'copy', 'paste', 'ifile=', 'ofile='])
    except getopt.GetoptError:
        help(argv[0])

    for opt, arg in opts:
        # help
        if opt in ('-h', '--help'):
            help(argv[0])

        # clipboard options
        elif opt in ('-c', '--copy'):
            copy_from_clipboard = True
        elif opt in ('-p', '--paste'):
            paste_to_clipboard = True

        # input/output files option
        elif opt in ('-i', '--ifile'):
            inputfile = arg
        elif opt in ('-o', '--ofile'):
            outputfile = arg

    data = get_data(inputfile, copy_from_clipboard)
    write_data(data, outputfile, paste_to_clipboard)


if __name__ == '__main__':
    main(sys.argv)
