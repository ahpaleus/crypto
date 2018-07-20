# Write a function that takes two equal-length buffers and produces their XOR combination.

buffer1 = '1c0111001f010100061a024b53535009181c'.decode('hex')
buffer2 = '686974207468652062756c6c277320657965'.decode('hex')

xor = [chr(ord(a)^ord(b)) for a,b in zip(buffer1,buffer2)]

print ''.join(xor).encode('hex')