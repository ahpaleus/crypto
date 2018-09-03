import time

MT = [0 for i in xrange(624)]
index = 0


def initializeGenerator(seed):
	global MT
	MT[0] = seed

	for i in xrange(1,624):
		MT[i] = ( (1812433253 * MT[i-1]) ^ ((MT[i-1] >> 30 ) +i)) & 4294967295

def extractNumber():
	global index
	global MT

	if index == 0: generateNumbers()

	y = MT[index] 
	y ^= y >> 11
	y ^= (y << 7) & 2636928640	
	y ^= (y << 15) & 4022730752
	y ^= y >> 18

	index = (index+1) % 624
	return y

def generateNumbers():
	global MT

	for i in xrange(624): 
		y = (MT[i] & 2147483648) + (MT[(i + 1 ) % 624] & 2147483647)
		MT[i] = MT[(i + 397) % 624] ^ (y >> 1)

		if (y % 2) == 1:
			MT[i] ^= 2567483615

# Test:
for i in xrange(50):
	initializeGenerator(int(round(time.time() * 1000)))
	print extractNumber()


'''
challenge21 $ python rng.py
2026859662
2214313352
1069319010
3457100421
1620181598
1486550617
1506557677
813252092
38819332
2240735803
1749545115
711265639
3482614216
3409543901
1099143988
443231992
1476902533
881192715
208577524
2712541772
1477047934
2141429924
1877291140
2337075286
1831199813
1401698544
821149115
1300608354
855708572
3931444338
1707071029
4204228098
2745322167
1024388086
2054374492
992212596
3051680643
450568537
3396310169
3855773036
3546806164
3396378277
196626167
2104091236
232748731
4152665041
737629187
3561997493
1285220935
2570107137
'''