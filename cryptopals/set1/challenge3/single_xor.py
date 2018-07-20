import itertools

message = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'.decode('hex')

for x in range(255):
	xor = [chr(ord(a)^x) for a,x in zip(message,itertools.repeat(x))]
	print ''.join(xor)


# Result:
# Cooking MC's like a pound of bacon

