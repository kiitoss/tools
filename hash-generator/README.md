# Hash generator

Generates the main hashes of a password.
Displays the results obtained with the following hashes:

- md5,
- sha1,
- sha224,
- sha256,
- sha384,
- sha512

## How to use it?

```bash
# clone the repository
git clone git@github.com:kiitoss/hash-generator.git
# move to the folder
cd ./hash-generator
# run the program
python3 hash-generator.py
```

You can integrate your input and output files in the following ways:

```bash
# specify files with the -i and -o options
python3 hash-generator.py -i inputfile -o outputfile

# specify files with redirections
python3 hash-generator.py < inputfile > outputfile

# specify files with mixed pipes and redirections
echo test | python3 hash-generator.py > outputfile

```

The output file looks like this:

```
(test)	md5	-> 098f6bcd4621d373cade4e832627b4f6
(test)	sha1	-> a94a8fe5ccb19ba61c4c0873d391e987982fbbd3
(test)	sha224	-> 90a3ed9e32b2aaf4c61c410eb925426119e1a9dc53d4286ade99a809
(test)	sha256	-> 9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08
(test)	sha384	-> 768412320f7b0aa5812fce428dc4706b3cae50e02a64caa16a782249bfe8efc4b7ef1ccb126255d196047dfedf17a0a9
(test)	sha512	-> ee26b0dd4af7e749aa1a8ee3c10ae9923f618980772e473f8819a5d4940e0db27ac185f8a0e1d5f84f88bc887fd67b143732c304cc5fa9ad8e6f57f50028a8ff
```

This allows the program to be combined with useful functions like _grep_.

Enjoy :)
