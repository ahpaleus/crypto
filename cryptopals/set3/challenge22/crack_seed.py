from random import randint
import time

index = 0

def initializeGenerator(seed):
	global MT
	MT = [0 for i in xrange(624)]
	index = 0
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


def print_number(any_seed):
	initializeGenerator(any_seed)
	return extractNumber()

# Wait a random number of fseconds between, I don't know, 20 and 1000

def routine():
	# print 'Wait a RANDOM number o seconds between, I don\'t know, 40 and 1000'
	wait = randint(1,3)
	time.sleep(wait)

	# Seeds the RNG with the current Unix timestamp:
	# print 'Seeds the RNG with the current Unix timestamp:' 
	unix_timestamp = int(time.time())

	print '( UNIX_TIMESTAMP to RNG: ' + str(unix_timestamp) + ') -> SECRET'
	# print 'Timestamp (seed): ' + str(unix_timestamp)
	initializeGenerator(unix_timestamp)

	# Wait a RANDOM number of seconds again
	# print 'Waits a random number of seconds again'
	time.sleep(wait)

	# Return the first 32 bit output of the RNG
	output = extractNumber()
	# print 'RNG = ' + str(output)

	print 'The first 32 bit: ',
	first_32_bits = output & 4294967295
	print str(first_32_bits)

	return first_32_bits

x = int(time.time())
first_bits = routine()
y = int(time.time())

time_difference = x + (y-x)/2 

# From the 32 bit RNG output, discover the seed

print 'Hacked seed = ' + str(time_difference)

MT = [0 for i in xrange(624)]
index = 0

print '--> RNG: ' + str(print_number(time_difference))

print 'Iteration hack: (works for 2 different - random time)'
now = int(time.time())

n = 0
rng = 0

while (int(first_bits) != rng):
	MT = [0 for i in xrange(624)]
	index = 0	
	ex = now - n
	rng = print_number(ex)
	print 'first_bits = ' + str(first_bits) + '\t !=\tprint_number(ex) = ' + str(print_number(ex))
	print 'Timestamp: ' + str(ex) + ", " + str(n) + ", " + 'Hash: ' + str(rng)
	n += 1

	print '-' * 50

print 'Iteration hacked seed = ' + str(ex)

'''
challenge22 $ python crack_seed.py
( UNIX_TIMESTAMP to RNG: 1535977358) -> SECRET
The first 32 bit:  818252820
Hacked seed = 1535977358
--> RNG: 818252820
Iteration hack: (works for 2 different - random time)
first_bits = 818252820	 !=	print_number(ex) = 3259854754
Timestamp: 1535977361, 0, Hash: 592105664
--------------------------------------------------
first_bits = 818252820	 !=	print_number(ex) = 1955139045
Timestamp: 1535977360, 1, Hash: 296205661
--------------------------------------------------
first_bits = 818252820	 !=	print_number(ex) = 1053643774
Timestamp: 1535977359, 2, Hash: 866375622
--------------------------------------------------
first_bits = 818252820	 !=	print_number(ex) = 2679069660
Timestamp: 1535977358, 3, Hash: 818252820
--------------------------------------------------
Iteration hacked seed = 1535977358
'''

