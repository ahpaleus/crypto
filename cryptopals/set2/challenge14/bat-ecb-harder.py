import string
import os
import binascii
from random import *
from Crypto.Cipher import AES

BLOCK_SIZE = 16

pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * \
                chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)

unpad = lambda s: s[:-ord(s[len(s) - 1:])]

key = os.urandom(16)

def generate_random_string():
	min_char = 16
	max_char = 16
	allchar = string.ascii_letters + string.punctuation + string.digits
	random_prefix = "".join(choice(allchar) for x in range(randint(min_char, max_char)))
	return random_prefix

def AES_ECB_encrypt(plaintext, key):
	obj = AES.new(key, AES.MODE_ECB)
	plaintext = pad(plaintext)
	ciphertext = obj.encrypt(plaintext)
	return ciphertext

def AES_ECB_decrypt(ciphertext, key):
	obj = AES.new(key, AES.MODE_ECB)
	result = obj.decrypt(ciphertext)
	result = unpad(result)
	return result

def generate_ciphertext(attacker_controlled):
	random_prefix = generate_random_string()
	attacker_controlled = attacker_controlled
	target_bytes = 'These are random bytes!!!!'
	plaintext = random_prefix + attacker_controlled + target_bytes
	obj = AES.new(key, AES.MODE_ECB)
	ciphertext = obj.encrypt(pad(plaintext))
	return ciphertext

def check_blocksize(ciphertext):
	blocksize = 0
	last = [0]
	for z in range(1, len(ciphertext)):
		for x in range(len(ciphertext)):
			if ciphertext.count(ciphertext[z:x]) > 1 and len(ciphertext[z:x]) > max(last):
				blocksize = len(ciphertext[z:x])
				last.append(len(ciphertext[z:x]))
	return blocksize

def print_blocks(ciphertext):
	repeated = []
	for x in range(len(ciphertext)/BLOCK_SIZE):
		if ciphertext.count(ciphertext[x*BLOCK_SIZE:(x+1)*BLOCK_SIZE]) > 1:
			repeated.append(ciphertext[x*BLOCK_SIZE:(x+1)*BLOCK_SIZE])
	return repeated

def cut_prefix(ciphertext):
	z = ''
	for x,y in enumerate(print_blocks(ciphertext)):
		z = y
	cut = ciphertext[ciphertext.find(z):]
	return cut

def cut_bytes(ciphertext, amount = BLOCK_SIZE):
	result = ciphertext[amount:]
	return result

amount = 0
block = 'A'*BLOCK_SIZE + 'A'*BLOCK_SIZE

test4 = generate_ciphertext(block)
amount = len(print_blocks(test4))

print binascii.hexlify(test4)
print 'Length: ' + str(len(test4))

print '\nRepeated blocks:'
z = ''
amount = 0
for x,y in enumerate(print_blocks(test4)):
	print str(x) + ': ' + binascii.hexlify(y)
	z = y
	amount = x
	

print '\nWe must specify the length of the first (random) block:'
print str(test4.find(z))

print '\nWe must specify the length of the last (important) block (with pad):'

suffix_len = len((test4[test4.find(z)+len(z)*(amount+1):]))
print len((test4[test4.find(z)+len(z)*(amount+1):]))

print '\nCut the prefix: '
cut = cut_bytes(test4)

print binascii.hexlify(cut)
print 'Now the magic'
found = []

suffix_len -= 1

for x in range(suffix_len, 0, -1):
	for y in range(255):
		input = 'A'*x
		for z in found: input += z
		input += chr(y)
		result1 = cut_bytes(generate_ciphertext(input))
		compare = 'A'*x
		result2 = cut_bytes(generate_ciphertext(compare))

		if result1[0:suffix_len] == result2[0:suffix_len]:
			print 'It matches! ' + 'add : ' + chr(y)
			found.append(chr(y))
			break

print found

result = ''
for x in found: result += x 
result = unpad(result)
print result

'''
challenge14 $ python bat-ecb-harder.py
b82db67c4aed4d5bcf0c25a135da8c0c2dd340c16d14cfa3de627a47811aa16c2dd340c16d14cfa3de627a47811aa16c3b8aa858f1817936784462747d07c86587d018ce5975003e8ab1c9f82ae51aee
Length: 80

Repeated blocks:
0: 2dd340c16d14cfa3de627a47811aa16c
1: 2dd340c16d14cfa3de627a47811aa16c

We must specify the length of the first (random) block:
16

We must specify the length of the last (important) block (with pad):
32

Cut the prefix:
2dd340c16d14cfa3de627a47811aa16c2dd340c16d14cfa3de627a47811aa16c3b8aa858f1817936784462747d07c86587d018ce5975003e8ab1c9f82ae51aee
Now the magic
It matches! add : T
It matches! add : h
It matches! add : e
It matches! add : s
It matches! add : e
It matches! add :
It matches! add : a
It matches! add : r
It matches! add : e
It matches! add :
It matches! add : r
It matches! add : a
It matches! add : n
It matches! add : d
It matches! add : o
It matches! add : m
It matches! add :
It matches! add : b
It matches! add : y
It matches! add : t
It matches! add : e
It matches! add : s
It matches! add : !
It matches! add : !
It matches! add : !
It matches! add : !
It matches! add :
['T', 'h', 'e', 's', 'e', ' ', 'a', 'r', 'e', ' ', 'r', 'a', 'n', 'd', 'o', 'm', ' ', 'b', 'y', 't', 'e', 's', '!', '!', '!', '!', '\x01']
These are random bytes!!!!
'''

