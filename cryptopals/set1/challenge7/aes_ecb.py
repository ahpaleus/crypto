# AES in ECB mode
import base64

from Crypto.Cipher import AES

with open('7.txt','r') as f:
	content = f.read()

ciphertext = base64.b64decode(content)
key = 'YELLOW SUBMARINE'

decryption = AES.new(key, AES.MODE_ECB)

print(decryption.decrypt(ciphertext))
