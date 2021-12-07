# her vil eg laga 10000 filer.

import os

mNavn = input("kva vil du at mapa skal heiste?")
os.mkdir(mNavn)
os.chdir(mNavn)

filami = ("fil.txt","w")