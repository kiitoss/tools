# LF Remover

Deletes line breaks from a document or from the clipboard.

## How to use it?

```bash
# clone the repository
git clone git@github.com:kiitoss/lf-remover.git
# move to the folder
cd ./lf-remover
# run the program
python3 lf-remover.py --help
```

You can integrate your input and output files in the following ways:

```bash
# specify input with the -i option
python3 lf-remover.py -i inputfile

# specify files with the -i and -o options
python3 lf-remover.py -i inputfile -o outputfile

# specify output redirection
python3 lf-remover.py -i inputfile > outputfile

# specify input from clipboard
python3 lf-remover.py -c

# specify output from clipboard
python3 lf-remover.py -c -p
```

Enjoy :)
