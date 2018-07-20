import binascii

def pkcsa_pad(message, pad):
	message = bytearray(message)

	string_length = len(message)
	print string_length

	byte_to_pad = pad - string_length
	print byte_to_pad

	print byte_to_pad

	for x in range(byte_to_pad):
		message.append(byte_to_pad)
	return message

print binascii.hexlify(pkcsa_pad("YELLOW SUBMARINE", 25))