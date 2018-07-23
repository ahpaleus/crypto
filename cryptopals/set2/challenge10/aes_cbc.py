import binascii
import sys
from Crypto.Cipher import AES

def pkcsa_pad(message, pad):
	message = bytearray(message)
	string_length = len(message)
	byte_to_pad = pad - string_length
	for x in range(byte_to_pad):
		message.append(byte_to_pad)
	return message

def repeating_xor(buffer, key):
	y = 0
	result = bytearray()
	for x in range(len(buffer)):
		xor = chr(buffer[x] ^ ord(key[y]))
		result.append(xor)
		if y != (len(key)-1):
			y += 1
		else:
			y = 0
	return result

def enc(message, iv, key):
	if len(message) % 16 != 0:
		ilosc_czesci = (len(message)/16+1)*16
	else:
		ilosc_czesci = len(message)/16

	message = pkcsa_pad(message, ilosc_czesci)
	x = len(message)
	y = x/16 
	cipher = []
	result = []
	after_iv = []

	for z in range(y):
		if z == 0: 
			after_iv.append(repeating_xor(message[16*z:16*(z+1)],iv))
			
		else: 
			after_iv.append(repeating_xor(message[16*z:16*(z+1)],str(result[z-1])))
		cipher.append(AES.new(key, AES.MODE_ECB))
		result.append(cipher[z].encrypt(str(after_iv[z])))
	return result

def pkcsa_pad_delete(cipher):
	x = ord(cipher[-1][-1:])
	z = cipher[-1][-x:]
	if len(set(z)) == 1 and len(z) < 16:
		del cipher[-1][-x:]
	return cipher

def dec(cipher, iv, key):
	plaintext = []
	z = 0
	for x in cipher:
		if z == 0:
			decryption = AES.new(key, AES.MODE_ECB)
			result = decryption.decrypt(cipher[z])
			result = bytearray(result)
			plaintext.append(repeating_xor(result,iv))
		else:
			decryption = AES.new(key, AES.MODE_ECB)
			result = decryption.decrypt(cipher[z])
			result = bytearray(result)
			plaintext.append(repeating_xor(result,cipher[z-1]))
		z += 1
	plaintext = pkcsa_pad_delete(plaintext)
	return plaintext

plaintext = "This is super confidential info!"*4
iv = "vec"
key = "C"*16

print "ENCRYPTING: \n"+plaintext

ciphertext = enc(plaintext, iv, key)

print '-> in hex value: '
for x in ciphertext:
	print binascii.hexlify(x)

print '\nDECRYPTING:'

decrypted = dec(ciphertext, iv, key)

for x in decrypted: sys.stdout.write(x)


'''
python aes_cbc.py
ENCRYPTING:
This is super confidential info!This is super confidential info!This is super confidential info!This is super confidential info!
-> in hex value:
fcb84bbbc55050589fa48ae603bc91ce
d6ab9186f12caa3919c78694b3918cce
3ae0a74c2595eb10dc9b50260c2d3db9
c98decba42ab5ef3db3abc40cdc98f07
e6a7bcca5444406ff07e77c2a5e15874
033084bcb0898adb9fc897db29fbc4c7
ef10714a73ce5e6e45e58b9d55e483f0
59f1c8d6d797ffdeb82ef0a1d300f13e

DECRYPTING:
This is super confidential info!This is super confidential info!This is super confidential info!This is super confidential info!
'''
