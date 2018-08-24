import os
import base64
import random
import binascii
import struct
import time 

from Crypto.Cipher import AES

BLOCK_SIZE = 16

pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * \
                chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)

unpad = lambda s: s[:-ord(s[len(s) - 1:])]

validate = lambda s:s[-1:]*s[-1]==s[-s[-1]:]

key = os.urandom(16)
iv = os.urandom(16)

def AES_CBC_encrypt(plaintext, key, iv):
	obj = AES.new(key, AES.MODE_CBC,iv)
	plaintext = pad(plaintext)
	ciphertext = obj.encrypt(plaintext)
	return ciphertext

def decrypt_and_check_padding(ciphertext, key, iv):
	obj = AES.new(key, AES.MODE_CBC, iv)
	result = bytearray(obj.decrypt(ciphertext))
	
	if validate(result) == True:
		return result
	else: return False

def split(s, chunk_size):
    a = zip(*[s[i::chunk_size] for i in range(chunk_size)])
    return [''.join(t) for t in a]

def add_chars(hash, ilosc):
	hash = 'A'*BLOCK_SIZE + 'A'*ilosc + hash
	return hash


hashes = 'MDAwMDAwTm93IHRoYXQgdGhlIHBhcnR5IGlzIGp1bXBpbmc=\n\
MDAwMDAxV2l0aCB0aGUgYmFzcyBraWNrZWQgaW4gYW5kIHRoZSBWZWdhJ3MgYXJlIHB1bXBpbic=\n\
MDAwMDAyUXVpY2sgdG8gdGhlIHBvaW50LCB0byB0aGUgcG9pbnQsIG5vIGZha2luZw==\n\
MDAwMDAzQ29va2luZyBNQydzIGxpa2UgYSBwb3VuZCBvZiBiYWNvbg==\n\
MDAwMDA0QnVybmluZyAnZW0sIGlmIHlvdSBhaW4ndCBxdWljayBhbmQgbmltYmxl\n\
MDAwMDA1SSBnbyBjcmF6eSB3aGVuIEkgaGVhciBhIGN5bWJhbA==\n\
MDAwMDA2QW5kIGEgaGlnaCBoYXQgd2l0aCBhIHNvdXBlZCB1cCB0ZW1wbw==\n\
MDAwMDA3SSdtIG9uIGEgcm9sbCwgaXQncyB0aW1lIHRvIGdvIHNvbG8=\n\
MDAwMDA4b2xsaW4nIGluIG15IGZpdmUgcG9pbnQgb2g=\n\
MDAwMDA5aXRoIG15IHJhZy10b3AgZG93biBzbyBteSBoYWlyIGNhbiBibG93'

list_of_hashes = hashes.split('\n')
selected_string = base64.b64decode(list_of_hashes[random.randint(0,len(list_of_hashes)-1)])
encrypted = AES_CBC_encrypt(selected_string, key, iv)

intermediate = bytearray()
encrypted = bytearray(encrypted)

i = 0
test = selected_string

while (len(encrypted) >= len((AES_CBC_encrypt(test,key,iv)))):
	test += 'A'
	i += 1 

expanded_hash = add_chars(selected_string, i-1)

encrypted = bytearray(AES_CBC_encrypt(expanded_hash,key,iv))
encrypted_splitted = split(str(encrypted),16)
decrypted_message = ''

for t in xrange(len(encrypted_splitted)-1): # Ocenic liczbe przejsc
	encrypted_iteration = bytearray(encrypted)
	temp = encrypted_splitted[-(2+t):] # [-2:], [-3:-1], [-4:-2]
	i_temporary = bytearray()
	test = bytearray(temp[0] + temp[1])
	encrypted_iteration = bytearray(temp[0] + temp[1])
	decrypted_iteration = ''
	pad = 0x01
	y = 0
	for q in range(BLOCK_SIZE):
		for y,z in enumerate(i_temporary):
			test[15-y] = i_temporary[y] ^ pad
		for x in xrange(256):
			if not i_temporary:
				test[15] = x
			else:
				test[15-y-1] = x
		
			if decrypt_and_check_padding(str(test),key,iv) != False:
				
				intermediate = x ^ pad

				if not i_temporary:
					c = x ^ pad ^ encrypted_iteration[15]
				else:
					c = x ^ pad ^ encrypted_iteration[15-y-1]
				i_temporary.append(intermediate)
				print chr(c) + '\t->\t' + hex(c)
				decrypted_iteration += chr(c)
				break
		pad += 1

	print '-> ' + decrypted_iteration[::-1]

	decrypted_message += decrypted_iteration
	del encrypted_iteration[:]

print '\nResult:\n' + decrypted_message[::-1][i-1:]

'''
$ python exploit2.py
	->	0x1
e	->	0x65
l	->	0x6c
b	->	0x62
m	->	0x6d
i	->	0x69
n	->	0x6e
 	->	0x20
d	->	0x64
n	->	0x6e
a	->	0x61
 	->	0x20
k	->	0x6b
c	->	0x63
i	->	0x69
u	->	0x75
-> uick and nimble
q	->	0x71
 	->	0x20
t	->	0x74
'	->	0x27
n	->	0x6e
i	->	0x69
a	->	0x61
 	->	0x20
u	->	0x75
o	->	0x6f
y	->	0x79
 	->	0x20
f	->	0x66
i	->	0x69
 	->	0x20
,	->	0x2c
-> , if you ain't q
m	->	0x6d
e	->	0x65
'	->	0x27
 	->	0x20
g	->	0x67
n	->	0x6e
i	->	0x69
n	->	0x6e
r	->	0x72
u	->	0x75
B	->	0x42
4	->	0x34
0	->	0x30
0	->	0x30
0	->	0x30
0	->	0x30
-> 00004Burning 'em
0	->	0x30
A	->	0x41
A	->	0x41
A	->	0x41
A	->	0x41
A	->	0x41
A	->	0x41
A	->	0x41
A	->	0x41
A	->	0x41
A	->	0x41
A	->	0x41
A	->	0x41
A	->	0x41
A	->	0x41
A	->	0x41
-> AAAAAAAAAAAAAAA0

Result:
000004Burning 'em, if you ain't quick and nimble
'''


