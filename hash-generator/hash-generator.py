#!/usr/bin/python

import os
import stat
import sys
import getopt
import hashlib


# error message
def help():
    print('hash-generator.py -i <inputfile> -o <outputfile>')
    sys.exit()


# check if stdin is terminal or pipe/redirection
def is_stdin_console():
    mode = os.fstat(0).st_mode
    return not stat.S_ISFIFO(mode) and not stat.S_ISREG(mode)


# read data from stdin
def get_passwords(inputfile):
    if inputfile == '':
        return [input('Entrez votre mot de passe : ')] if is_stdin_console() else sys.stdin.read().splitlines()

    f = open(inputfile, 'r')
    return f.read().splitlines()


# write data in stdout
def write_encoded_passwords(encoded_passwords, outputfile):
    stdout = sys.stdout if not outputfile else open(outputfile, "w")
    for i, (password, encoded_password) in enumerate(encoded_passwords):
        if i > 0:
            print('', file=stdout)
        for hashType in encoded_password:
            print('(' + password + ')\t' + hashType + '\t-> ' +
                  str(encoded_password[hashType]), file=stdout)


# encode a single password into multiple hashs
def encode_password(password):
    encoded_password = {
        'md5': hashlib.md5(password.encode()).hexdigest(),
        'sha1': hashlib.sha1(password.encode()).hexdigest(),
        'sha224': hashlib.sha224(password.encode()).hexdigest(),
        'sha256': hashlib.sha256(password.encode()).hexdigest(),
        'sha384': hashlib.sha384(password.encode()).hexdigest(),
        'sha512': hashlib.sha512(password.encode()).hexdigest(),
    }

    return encoded_password


def main(argv):
    inputfile = ''
    outputfile = ''

    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
    except getopt.GetoptError:
        help()

    for opt, arg in opts:
        if opt == '-h':
            help()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg

    passwords = get_passwords(inputfile)
    encoded_passwords = [(password, encode_password(password))
                         for password in passwords]
    write_encoded_passwords(encoded_passwords, outputfile)


if __name__ == "__main__":
    main(sys.argv[1:])
