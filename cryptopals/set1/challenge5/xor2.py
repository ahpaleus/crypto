def repeating_xor(buffer, key):
	y = 0
	result = []
	for x in range(len(buffer)):
		xor = chr(ord(buffer[x]) ^ ord(key[y]))
		result.append(xor)
		if y != (len(key)-1):
			y += 1
		else:
			y = 0
	return ''.join(result).encode('hex')

buffer1 = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
key = "ICE"

print repeating_xor(buffer1,key)
