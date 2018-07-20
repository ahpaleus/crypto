with open('8.txt','r') as f:
	content = f.readlines()

y = 0

result = []

for x in content:
	for z in range(21):
		test = x[16*y:16*(y+1)]
		if y == 20: y = 0
		if x.count(test) > 1:
			if x not in result: print x
			result.append(x)
			print 'Segment: ' + test
		y += 1

'''
Result:
d880619740a8a19b7840a8a31c810a3d08649af70dc06f4fd5d2d69c744cd283e2dd052f6b641dbf9d11b0348542bb5708649af70dc06f4fd5d2d69c744cd2839475c9dfdbc1d46597949d9c7e82bf5a08649af70dc06f4fd5d2d69c744cd28397a93eab8d6aecd566489154789a6b0308649af70dc06f4fd5d2d69c744cd283d403180c98c8f6db1f2a3f9c4040deb0ab51b29933f2c123c58386b06fba186a

Segment: 08649af70dc06f4f
Segment: d5d2d69c744cd283
Segment: 08649af70dc06f4f
Segment: d5d2d69c744cd283
Segment: 08649af70dc06f4f
Segment: d5d2d69c744cd283
Segment: 08649af70dc06f4f
Segment: d5d2d69c744cd283
'''