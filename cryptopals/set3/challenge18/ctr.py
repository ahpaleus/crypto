from base64 import b64decode
from Crypto.Cipher import AES
from Crypto.Util import Counter
from binascii import hexlify as hexa
from os import urandom
from struct import unpack, pack

BLOCK_SIZE = 16
# Useful usage of CTR:

k = urandom(16)
print "Key k = %s" % hexa(k)

# Starting value for counter:
nonce = unpack('<Q', urandom(8))[0]

# Encrypting: 
ctr = Counter.new(128, initial_value=nonce)

aes = AES.new(k, AES.MODE_CTR, counter=ctr)

p = '\x00\x01\x02\x03'

c= aes.encrypt(p)

print "enc(%s) = %s" % (hexa(p), hexa(c))

# Decrypting: -> Decryption is identical to encryption
ctr = Counter.new(128, initial_value=nonce)
aes = AES.new(k, AES.MODE_CTR, counter=ctr)
p = aes.encrypt(c)
print "enc(%s) = %s" % (hexa(c), hexa(p))

# Decrypting example:

'''
      format=64 bit unsigned little endian nonce,
             64 bit little endian block count (byte count / 16)

First 8 bytes (64 bits):
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00

Next 8 bytes:
\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00

Then:
\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00

'''


decrypted = ''
ciphertext = b64decode('L77na/nrFsKvynd6HzOoG7GHTLXsTVu9qvY/2syLXzhPweyyMTJULu/6/kXX0KSvoOLSFQ==')
key = "YELLOW SUBMARINE"

loop_counter = (len(ciphertext) / BLOCK_SIZE)+1

for h in xrange(loop_counter):
	message = pack("<Q",0)+pack("<Q",h)
	aes = AES.new(key,AES.MODE_ECB)
	result = aes.encrypt(message)

	print 'Nonce || Counter: ' + hexa(message)
	print 'Key: ' + key

	print 'AES: ' + hexa(result)
	
	ciphertext_temp = ciphertext[16*h:16*(h+1)]
	print 'ciphertext: ' + ciphertext_temp
	print 'ciphertext (hex): ' + hexa(ciphertext_temp)

	print 'AES ^ XOR: '

	plaintext = ''

	for x,y in enumerate(result):
		try:
			temp = chr(ord(result[x]) ^ ord(ciphertext_temp[x]))
			print str(x) + '.\t' + hexa(result[x]) + '\t^\t' + hexa(ciphertext_temp[x]) + '\t=\t' + temp
			plaintext += temp
		except:
			break

	print plaintext
	decrypted += plaintext
	print '-----------------------\n' + decrypted + '\n-----------------------\n'

'''
challenge18 $ python ctr.py
Key k = ff802eafb8f59197ce731e095459db56
enc(00010203) = ea0af3eb
enc(ea0af3eb) = 00010203
Nonce || Counter: 00000000000000000000000000000000
Key: YELLOW SUBMARINE
AES: 76d1cb4bafa246e2e3af035d6c13c372
ciphertext: /��k��¯�wz3�
                        ciphertext (hex): 2fbee76bf9eb16c2afca777a1f33a81b
AES ^ XOR:
0.	76	^	2f	=	Y
1.	d1	^	be	=	o
2.	cb	^	e7	=	,
3.	4b	^	6b	=
4.	af	^	f9	=	V
5.	a2	^	eb	=	I
6.	46	^	16	=	P
7.	e2	^	c2	=
8.	e3	^	af	=	L
9.	af	^	ca	=	e
10.	03	^	77	=	t
11.	5d	^	7a	=	'
12.	6c	^	1f	=	s
13.	13	^	33	=
14.	c3	^	a8	=	k
15.	72	^	1b	=	i
Yo, VIP Let's ki
-----------------------
Yo, VIP Let's ki
-----------------------

Nonce || Counter: 00000000000000000100000000000000
Key: YELLOW SUBMARINE
AES: d2ec6cdc986d12decfda1f93afee7318
ciphertext: ��L��M[���?�̋_8
ciphertext (hex): b1874cb5ec4d5bbdaaf63fdacc8b5f38
AES ^ XOR:
0.	d2	^	b1	=	c
1.	ec	^	87	=	k
2.	6c	^	4c	=
3.	dc	^	b5	=	i
4.	98	^	ec	=	t
5.	6d	^	4d	=
6.	12	^	5b	=	I
7.	de	^	bd	=	c
8.	cf	^	aa	=	e
9.	da	^	f6	=	,
10.	1f	^	3f	=
11.	93	^	da	=	I
12.	af	^	cc	=	c
13.	ee	^	8b	=	e
14.	73	^	5f	=	,
15.	18	^	38	=
ck it Ice, Ice,
-----------------------
Yo, VIP Let's kick it Ice, Ice,
-----------------------

Nonce || Counter: 00000000000000000200000000000000
Key: YELLOW SUBMARINE
AES: 2da08ecb117b374bc3dab726b2fc84cd
ciphertext: O��12T.���E�Ф�
ciphertext (hex): 4fc1ecb23132542eeffafe45d7d0a4af
AES ^ XOR:
0.	2d	^	4f	=	b
1.	a0	^	c1	=	a
2.	8e	^	ec	=	b
3.	cb	^	b2	=	y
4.	11	^	31	=
5.	7b	^	32	=	I
6.	37	^	54	=	c
7.	4b	^	2e	=	e
8.	c3	^	ef	=	,
9.	da	^	fa	=
10.	b7	^	fe	=	I
11.	26	^	45	=	c
12.	b2	^	d7	=	e
13.	fc	^	d0	=	,
14.	84	^	a4	=
15.	cd	^	af	=	b
baby Ice, Ice, b
-----------------------
Yo, VIP Let's kick it Ice, Ice, baby Ice, Ice, b
-----------------------

Nonce || Counter: 00000000000000000300000000000000
Key: YELLOW SUBMARINE
AES: c180ab3549fa6e55d14c6667c96fa5b0
ciphertext: ���
ciphertext (hex): a0e2d215
AES ^ XOR:
0.	c1	^	a0	=	a
1.	80	^	e2	=	b
2.	ab	^	d2	=	y
3.	35	^	15	=
aby
-----------------------
Yo, VIP Let's kick it Ice, Ice, baby Ice, Ice, baby
-----------------------
'''
