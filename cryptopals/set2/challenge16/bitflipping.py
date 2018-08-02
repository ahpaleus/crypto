import binascii
import re
import os
from Crypto.Cipher import AES

pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * \
                chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)

unpad = lambda s: s[:-ord(s[len(s) - 1:])]

BLOCK_SIZE = 16
key = os.urandom(16)
iv = os.urandom(16)

def AES_CBC_encrypt(plaintext, key, iv):
	obj = AES.new(key, AES.MODE_CBC,iv)
	plaintext = pad(plaintext)
	ciphertext = obj.encrypt(plaintext)
	return ciphertext

def AES_CBC_decrypt(ciphertext, key, iv):
	obj = AES.new(key, AES.MODE_CBC, iv)
	result = obj.decrypt(ciphertext)
	result = unpad(result)
	return result

def quote_out(input):
	if re.search('[;=]', input):
		exit('Illegal characters!\nEXIT!!')
	return input

def check_admin(ciphertext):
	plaintext = AES_CBC_decrypt(ciphertext, key, iv)
	print plaintext
	if ";admin=true" in plaintext: return 'ADMIN ACCOUNT!'
	else: return 'REGULAR USER ACCOUNT'

userdata = 'XXXXXXXXXXX'
prepend = "comment1=cooking%20MCs;userdata="
append = ";comment2=%20like%20a%20pound%20of%20bacon"

res = prepend + quote_out(userdata) + append
test2 = AES_CBC_encrypt(res, key, iv)

print check_admin(str(test2))

test4 = bytearray(test2)
plain = bytearray(userdata)
want = bytearray(';admin=true')
z = bytearray()

i = 0

for x in range(len(userdata)):
	xor = test4[16+i]^plain[i]^want[i]
	z.append(xor)

	print(hex(test4[16+i]) 
	+ ' ( ' 
	+ chr(test4[16+i]) 
	+ ' )' 
	+ '\t^\t' 
	+ hex(plain[i]) 
	+ ' ( ' 
	+ chr(plain[i])
	+ ' ) '  
	+ '\t^\t' 
	+ hex(want[i]) 
	+ ' ( ' 
	+ chr(want[i]) 
	+ ' )' 
	+ '\t=\t' 
	+ hex(xor) 
	+ ' ( ' 
	+ chr(xor) 
	+ ' )')

	test4[16+i] = z[i]
	i+=1

print check_admin(str(test4))

'''
challenge16 $ python bitflipping.py
comment1=cooking%20MCs;userdata=XXXXXXXXXXX;comment2=%20like%20a%20pound%20of%20bacon
REGULAR USER ACCOUNT
0x54 ( T )      ^       0x58 ( X )      ^       0x3b ( ; )      =       0x37 ( 7 )
0x93 ( � )      ^       0x58 ( X )      ^       0x61 ( a )      =       0xaa ( � )
0x9b ( � )      ^       0x58 ( X )      ^       0x64 ( d )      =       0xa7 ( � )
0x76 ( v )      ^       0x58 ( X )      ^       0x6d ( m )      =       0x43 ( C )
0x8d ( � )      ^       0x58 ( X )      ^       0x69 ( i )      =       0xbc ( � )
0x4f ( O )      ^       0x58 ( X )      ^       0x6e ( n )      =       0x79 ( y )
0x95 ( � )      ^       0x58 ( X )      ^       0x3d ( = )      =       0xf0 ( � )
0x68 ( h )      ^       0x58 ( X )      ^       0x74 ( t )      =       0x44 ( D )
0x1 (  )        ^       0x58 ( X )      ^       0x72 ( r )      =       0x2b ( + )
0x54 ( T )      ^       0x58 ( X )      ^       0x75 ( u )      =       0x79 ( y )
0x49 ( I )      ^       0x58 ( X )      ^       0x65 ( e )      =       0x74 ( t )
comment1=cookingLQm����{�4+��;admin=true;comment2=%20like%20a%20pound%20of%20bacon
ADMIN ACCOUNT!
'''
