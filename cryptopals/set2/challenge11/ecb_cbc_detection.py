import os
import binascii
import random
from Crypto.Cipher import AES

def recognize_mode(cipher):
	result = []
	chunks = len(cipher)/BLOCK_SIZE

	for x in range(chunks):
		result.append(cipher[x*16:(x+1)*16])

	for x,y in enumerate(result):
		if cipher.count(y) > 1:
			return 'ECB'

		# print 'CBC i think..'

	return 'CBC?'


BLOCK_SIZE = 16

pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * \
                chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)

unpad = lambda s: s[:-ord(s[len(s) - 1:])]

key = os.urandom(16)

print 'Random key: (hex) '+binascii.hexlify(key)

rand_before = os.urandom(random.randint(5,10))
rand_after = os.urandom(random.randint(5,10))
iv = os.urandom(16)

input = "A"*500

print 'Random before string (5-10 bytes): (hex) ' + binascii.hexlify(rand_before)
print 'Random after string (5-10 bytes): (hex) ' + binascii.hexlify(rand_after)
print 'Random iv: (hex) ' + binascii.hexlify(iv)
print 'Input: ' + input

result = rand_before + input + rand_after
print 'Result input: ' + result

if random.randint(0,1) == 0:
	print 'Random mode: ECB'
	obj = AES.new(key, AES.MODE_ECB)
	ciphertext = obj.encrypt(pad(result))
	
else:
	print 'Random mode: CBC'

	obj = AES.new(key, AES.MODE_CBC, iv)
	ciphertext = obj.encrypt(pad(result))

print '---------------------------------'

print 'Recognized mode of encrypt:'

print '---> ' + recognize_mode(ciphertext)

'''
Random key: (hex) dadd29df5974fba8b289754b0153bdbd
Random before string (5-10 bytes): (hex) 0d4025012639998a0d
Random after string (5-10 bytes): (hex) 0d85a368cfc648
Random iv: (hex) ace509a87971bef4828d84816f6c660c
Input: AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA��h��HAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
Random mode: ECB
---------------------------------
Recognized mode of encrypt:
---> ECB
'''
