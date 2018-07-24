import base64
import os
import binascii
from Crypto.Cipher import AES

pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * \
                chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)

def enc(plaintext, key):
	obj = AES.new(key, AES.MODE_ECB)
	ciphertext = obj.encrypt(plaintext)
	return ciphertext

def recognize_mode(cipher):
	result = []
	chunks = len(cipher)/BLOCK_SIZE

	for x in range(chunks):
		result.append(cipher[x*16:(x+1)*16])

	for x in result:
		if cipher.count(x) > 1:
			return 'ECB'

		# print 'CBC i think..'

	return 'CBC?'


key = os.urandom(16)

unknown_string = 'Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK'

my_string = ''

result_string = my_string + base64.b64decode(unknown_string)

blocks = []
crypts = []
z = []

for x in range(1,100):
	try:
		my_string = 'A'*x
		result_string = my_string + base64.b64decode(unknown_string)
		block_size = len(result_string)
		crypts.append(enc(result_string, key))
		blocks.append(block_size)
		z.append(x)
	except ValueError:
		pass

BLOCK_SIZE = blocks[1]-blocks[0]

print 'Block size = ' + str(BLOCK_SIZE)

# Let's try for minimum value:


my_string = 'A'*z[3]
result_string = my_string + base64.b64decode(unknown_string)

ciphertext = enc(result_string, key)


print '---------CIPHERTEXT---------\n' + binascii.hexlify(ciphertext) + '\n---------CIPHERTEXT---------'
print 'The method is: ' + recognize_mode(ciphertext)

print '--> Result: \n\n'
'''
Knowing the block size, craft an input block that is exactly 1 byte short (for instance, if the block size is 8 bytes, make "AAAAAAA"). Think about what the oracle function is going to put in that last byte position.
'''

n = 255
found = []

for j in range(n,0,-1):
	my_string = 'a'*j

	result_string = my_string + base64.b64decode(unknown_string)
	result1 = enc(pad(result_string), key)

	for x in range(255):
		my_string = 'a'*j

		for z in found:
			my_string += z
		my_string += chr(x)

		result_string = my_string + base64.b64decode(unknown_string)
		result2 = enc(pad(result_string), key)
		if result1[0:n+1] == result2[0:n+1]:
			found_char = chr(x)
			found.append(found_char)
			break

decipher_text = ''
for x in found:
	decipher_text += x

print decipher_text

'''
Block size = 16
---------CIPHERTEXT---------
04915b292fe8f3f4cd3cd83b1a401bcc04915b292fe8f3f4cd3cd83b1a401bcc04915b292fe8f3f4cd3cd83b1a401bcc226eb349509a5403a00fd7ca916634c74d0089bc68aa4c31ea08df7bb7d3c17673c927f9f2cc350690988f5ae1034958d756b666d7ea37373d913342206d181ab823187a9c5ea01ad7438488c0e722e5b3a6d67ac5910a3525e888e135d449798d0a3c7b53f1e7202ccd83342b24179a81eb2064c68949f3ab1e25de09313170128940ccd4fa062e55e4b9b15e8b2104
---------CIPHERTEXT---------
The method is: ECB
--> Result:


Rollin' in my 5.0
With my rag-top down so my hair can blow
The girlies on standby waving just to say hi
Did you stop? No, I just drove by
'''

