from base64 import b64encode, b64decode
from binascii import hexlify as hexa
from isprintable import isprintable
import re

file = open("6.txt", "r")

unencrypted = file.read()
unencrypted = unencrypted.split("\n")
del unencrypted[-1]
unencrypted = [b64decode(y) for y in unencrypted]

result_string = ''

for x in unencrypted:
	result_string += x

def hamming_distance(s1, s2):
	if len(s1) == len(s2):
		s1 = bin(int(binascii.hexlify(s1),16))[2:]
		s2 = bin(int(binascii.hexlify(s2),16))[2:]
		return sum(ch1 != ch2 for ch1, ch2 in zip(s1,s2))
	return False

def total_ascii(text):
	ascii_string = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz, ")
	ascii_count = sum(c in ascii_string for c in text)
	return ascii_count

split_string = lambda x, n: [x[i:i+n] for i in range(0, len(x), n)]
normalized_results = []

for x in xrange(2,50):
	KEYSIZE = x
	splitted = split_string(result_string,KEYSIZE)
	distance = float(hamming_distance(splitted[0], splitted[1]))
	
	if distance != 0.0:
		# print 'Hamming Distance between first and second: ' + str(distance)
		normalized = distance/KEYSIZE
		normalized_results.append(normalized)
		# print 'Normalized: ' + str(normalized)
	else: break

print normalized_results

print 'Index: ' + str(normalized_results.index(min(normalized_results))) + '-> Value: ' + str(min(normalized_results))

for KEYSIZE in xrange(2,40):
	chunks = split_string(result_string, KEYSIZE)

	first_bytes = []

	for x in chunks:
		try:
			first_bytes.append(x[0])
		except:
			pass

	key = ''

	for elem in xrange(KEYSIZE):
		first_bytes = []

		for x in chunks:
			try:
				first_bytes.append(x[elem])
			except:
				pass

		number_ascii_chars = []
			
		for x in xrange(256):
			test = ''

			for item in first_bytes:
				res = chr(ord(item) ^ x)
				test += res

			if ((isprintable(test) == True) or ("\n" in test)):
				number_ascii_chars.append([chr(x),total_ascii(test)])

		key += max(number_ascii_chars, key=lambda x: x[1])[0]

	print 'Key:\t' + key

'''
challenge6 $ python repeating-key-xor.py
[2.5, 2.6666666666666665, 3.75, 3.0, 4.5, 3.0, 3.5, 3.5555555555555554, 3.2, 3.8181818181818183, 3.25, 4.076923076923077, 3.5714285714285716, 2.933333333333333, 3.9375, 2.9411764705882355, 3.6666666666666665, 3.6842105263157894, 2.7, 3.8095238095238093, 3.8636363636363638, 3.6956521739130435, 3.5416666666666665, 3.24, 3.6923076923076925, 3.4814814814814814, 3.8214285714285716, 3.9655172413793105, 3.1, 3.096774193548387, 3.78125, 3.484848484848485, 3.4411764705882355, 3.6857142857142855, 3.6944444444444446, 3.108108108108108, 2.8684210526315788, 3.282051282051282, 3.75, 3.268292682926829, 3.7857142857142856, 3.558139534883721, 3.590909090909091, 3.7777777777777777, 3.739130434782609, 3.765957446808511, 3.8333333333333335, 3.0816326530612246]
Index: 0-> Value: 2.5
Key:	ii
Key:	ioi
Key:	eiii
Key:	iiiio
Key:	eniioi
Key:	iiiiiie
Key:	iineeoir
Key:	ininiiioi
Key:	nBiioiiien
Key:	riIiiriteDo
Key:	eoeiooiniioY
Key:	rcironnriIoEi
Key:	iirrinnIoiiiie
Key:	niiiniiEooirioi
Key:	nnTCeiiriirioOer
Key:	IhiniOiTnoC~ocdei
Key:	nniBiirniiohEiiioY
Key:	oriIooiEiCnBiOinNei
Key:	nBiioionenoeCcoouisn
Key:	cnioNOnoU~riiciEoiine
Key:	enIinsiIriiCiTiinIteEn
Key:	iiOiohronirncoreopnKDcn
Key:	nnUiBoCoiioBcoinosiniBrr
Key:	oirrOoIneiDeicorroinEmrBi
Key:	riiOneornHoHiIoiroOIriIrXr
Key:	rnoEoOnnrimBhcrooeiOrKriiEh
Key:	cBrTronIoiTieInhOrinXcEoC~Oe
Key:	Terminator X: Bring the noise
Key:	nBeinConnhooNoOETienICEhoiEiOO
Key:	mOontConiXeco_rXUrioICaiorOBeii
Key:	nKrDeIQriCOnoOnIonoCiiiNChri Oer
Key:	eniiiMIneCnrrdoBSOIeDCCicXinCtnDs
Key:	IHinoICOnoT~OcXsirBCdIMirOEihrEoei
Key:	ciXHOieCBroHiciCOEinnBioiKOetYOXien
Key:	etNnoOrHiinhEIDiEoOnihiC
oeoCSEiMmTX
Key:	XrPXOEoODrMDDrimiiCiCNBBosOD~iiiIbXiO
Key:	oroBDXir_snBiOiNNH DiiHhOHXiCdECOinreD
Key:	Io~nni~tIXroKIEnOnooDiCiDCDgirOnDrOIoOi

So the key is:
Key:	Terminator X: Bring the noise

'''