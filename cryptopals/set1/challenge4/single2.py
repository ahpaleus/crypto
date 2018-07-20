import itertools

with open('4.txt') as f:
	content = f.readlines()

for y in range(len(content)):
	for x in range(255):
		
		xor = [chr(ord(a)^x) for a,x in zip(content[y].rstrip("\n").decode('hex'),itertools.repeat(x))]
		result = ''.join(xor)
		
		if 'the' in result:
			print result

# FLAG: Now that the party is jumping