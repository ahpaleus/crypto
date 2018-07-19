# AES in ECB mode

import base64
from Crypto.Cipher import AES


ciphertextb64 = "ACw5ftWAMhGPpxkbT1iun8aLQ55rGrYUMjeyZfIlYd8Whz8TwCMg1AgeTA83J7qt"
keyb64 = "zb9v8uGYo/BWzbhouenY2g=="

ciphertext = base64.b64decode(ciphertextb64)
key = base64.b64decode(keyb64)

decryption = AES.new(key, AES.MODE_ECB)

print(decryption.decrypt(ciphertext))

flag{do_not_let_machines_win_68fa218c}__________
