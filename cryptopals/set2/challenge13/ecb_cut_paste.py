import os
import re
import binascii
from Crypto.Cipher import AES

BLOCK_SIZE = 16

pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * \
                chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)

unpad = lambda s: s[:-ord(s[len(s) - 1:])]

key = os.urandom(16) # Random 16-byte key

def profile_for(email):
	if re.search('[&=]', email): 
		print 'Illegal characters!'
		exit()

	Object = {
		'email': email,
		'uid': 10,
		'role': 'user'
	}
	cookie = 'email={0}&uid={1}&role={2}'.format(Object['email'],Object['uid'],Object['role'])
	return cookie

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


def tamper(encrypted_profile, user_role, email):
	take_last_block = encrypted_profile
	admin_pad = pad(user_role)

	email_pad_chunk = 'email=' + email
	
	pad_email = 0
	while len(email_pad_chunk) % 16 != 0:
		email_pad_chunk += 'A'
		pad_email += 1

	unique_block = AES_ECB_encrypt(profile_for(email+'A'*pad_email+admin_pad), key)

	result = encrypted_profile[:BLOCK_SIZE*2] + unique_block[BLOCK_SIZE*4/2:(BLOCK_SIZE*4+BLOCK_SIZE*2)/2]
	return result


email = 'test@test.com'
user = profile_for(email)
encrypted_user = AES_ECB_encrypt(user, key)

print 'Your encrypted \'session\' cookie is: \n' + binascii.hexlify(encrypted_user)
print 'Decrypted session is:\n' + AES_ECB_decrypt(encrypted_user, key)

tampered = tamper(encrypted_user, "admin", email)

print '-'*50 + '\nTrying to tampering...\nTampered cookie: \n' + binascii.hexlify(tampered)
print 'Decrypted tampered cookie: '
print AES_ECB_decrypt(tampered, key)

'''
Your encrypted 'session' cookie is:
a32b1059ce2c3b3a36baa5bfda46c604ec1e8ad0f36d97b1e8c085000a7a6cc6122b6aa9a1014024f4c7e1de58605054
Decrypted session is:
email=test@test.com&uid=10&role=user
--------------------------------------------------
Trying to tampering...
Tampered cookie:
a32b1059ce2c3b3a36baa5bfda46c604ec1e8ad0f36d97b1e8c085000a7a6cc6f424a5bd80c489e61fe7b6f94960fc6a
Decrypted tampered cookie:
email=test@test.com&uid=10&role=admin
'''
