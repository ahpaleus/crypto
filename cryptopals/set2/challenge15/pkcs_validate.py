def pkcs_validate(plaintext):
	chunk = ''
	i = 1
	for x in plaintext:
		if len(set(plaintext[-i:])) == True:
			chunk = plaintext[-i:]
			i+=1
	if ord(chunk[0]) == len(chunk):
		return True
	return False

test = [
"ICE ICE BABY\x04\x04\x04\x04",
"ICE ICE BABY\x05\x05\x05\x05",
"ICE ICE BABY\x01\x02\x03\x04" ]

for x in test:
	print pkcs_validate(x)

'''
challenge15 $ python pkcsa_validate.py
True
False
False
'''