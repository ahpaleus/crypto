import re
from Crypto.Cipher import AES
from Crypto.Util import Counter
from binascii import hexlify as hexa
from os import urandom
from struct import unpack

k = urandom(16)
nonce = unpack('<Q', urandom(8))[0]

def quote_out(input):
	if re.search('[;=]', input):
		exit('Illegal characters!\nEXIT!!')
	return input

def check_admin(plaintext):
	if ";admin=true" in plaintext: return 'ADMIN ACCOUNT!'
	else: return 'REGULAR USER ACCOUNT'

def encrypt(plaintext, k, nonce):
	ctr = Counter.new(128,initial_value = nonce)
	aes = AES.new(k, AES.MODE_CTR, counter = ctr)
	c = aes.encrypt(str(plaintext))
	return c

userdata = 'XadminXtrue'

prepend = "comment1=cooking%20MCs;userdata="
append = ";comment2=%20like%20a%20pound%20of%20bacon"

res = prepend + quote_out(userdata) + append

ciphertext = bytearray(encrypt(res, k, nonce))
print 'Session encrypted: ' + hexa(ciphertext)
decrypted = encrypt(ciphertext, k, nonce)
print 'Session decrypted: ' + decrypted

print check_admin(decrypted)
print '\n\nTRYING TO TAMPER:'

decrypted = ''

for x in xrange(255):
	ciphertext[32] = x
	for y in xrange(255):
		ciphertext[38] = y
		decrypted = encrypt(ciphertext, k, nonce)
		if bool(re.search(r";admin=true",decrypted))==True:
			print 'First char tampered: ' + hexa(chr(x))
			print 'Second char tampered: ' + hexa(chr(y))
			print decrypted
			print check_admin(decrypted)
			break

'''
challenge26 $ python test.py
Session encrypted: cab0d8db7c31ec3a48f51eb1aa147d5542f287ee41dede99d15aee97b0cf9700b092410c6d2dbdd59a7c54dbd24ef23d8ea0417071f43bd9fbcaac25ac29b7f19667378d791565013a5c8470fbecc5e893a8672d05
Session decrypted: comment1=cooking%20MCs;userdata=XadminXtrue;comment2=%20like%20a%20pound%20of%20bacon
REGULAR USER ACCOUNT

TRYING TO TAMPER:
First char tampered: d3
Second char tampered: d8
comment1=cooking%20MCs;userdata=;admin=true;comment2=%20like%20a%20pound%20of%20bacon
ADMIN ACCOUNT!
'''