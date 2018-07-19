import binascii
import base64

f = open('zero_one', 'r')

text = f.read()

text = text.replace("ZERO","0")
text = text.replace("ONE","1")
text = text.replace(" ","")
print text

ascii = int(text,2)
ascii_result =  binascii.unhexlify('%x' % ascii)
print ascii_result

base64_result = base64.b64decode(ascii_result)

print base64_result

# base64 is a morse alphabet, result is:
# alexctfth15o1so5up3ro5ecr3totxt
# O to -> {
# alexctf{th15_1s_5up3r_5ecr3t_txt}
