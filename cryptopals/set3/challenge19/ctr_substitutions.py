from Crypto.Cipher import AES
from Crypto.Util import Counter
from binascii import hexlify as hexa
from base64 import b64decode,b64encode
from os import urandom

BLOCK_SIZE = 16

example = 'SSBoYXZlIG1ldCB0aGVtIGF0IGNsb3NlIG9mIGRheQ==\n\
Q29taW5nIHdpdGggdml2aWQgZmFjZXM=\n\
RnJvbSBjb3VudGVyIG9yIGRlc2sgYW1vbmcgZ3JleQ==\n\
RWlnaHRlZW50aC1jZW50dXJ5IGhvdXNlcy4=\n\
SSBoYXZlIHBhc3NlZCB3aXRoIGEgbm9kIG9mIHRoZSBoZWFk\n\
T3IgcG9saXRlIG1lYW5pbmdsZXNzIHdvcmRzLA==\n\
T3IgaGF2ZSBsaW5nZXJlZCBhd2hpbGUgYW5kIHNhaWQ=\n\
UG9saXRlIG1lYW5pbmdsZXNzIHdvcmRzLA==\n\
QW5kIHRob3VnaHQgYmVmb3JlIEkgaGFkIGRvbmU=\n\
T2YgYSBtb2NraW5nIHRhbGUgb3IgYSBnaWJl\n\
VG8gcGxlYXNlIGEgY29tcGFuaW9u\n\
QXJvdW5kIHRoZSBmaXJlIGF0IHRoZSBjbHViLA==\n\
QmVpbmcgY2VydGFpbiB0aGF0IHRoZXkgYW5kIEk=\n\
QnV0IGxpdmVkIHdoZXJlIG1vdGxleSBpcyB3b3JuOg==\n\
QWxsIGNoYW5nZWQsIGNoYW5nZWQgdXR0ZXJseTo=\n\
QSB0ZXJyaWJsZSBiZWF1dHkgaXMgYm9ybi4=\n\
VGhhdCB3b21hbidzIGRheXMgd2VyZSBzcGVudA==\n\
SW4gaWdub3JhbnQgZ29vZCB3aWxsLA==\n\
SGVyIG5pZ2h0cyBpbiBhcmd1bWVudA==\n\
VW50aWwgaGVyIHZvaWNlIGdyZXcgc2hyaWxsLg==\n\
V2hhdCB2b2ljZSBtb3JlIHN3ZWV0IHRoYW4gaGVycw==\n\
V2hlbiB5b3VuZyBhbmQgYmVhdXRpZnVsLA==\n\
U2hlIHJvZGUgdG8gaGFycmllcnM/\n\
VGhpcyBtYW4gaGFkIGtlcHQgYSBzY2hvb2w=\n\
QW5kIHJvZGUgb3VyIHdpbmdlZCBob3JzZS4=\n\
VGhpcyBvdGhlciBoaXMgaGVscGVyIGFuZCBmcmllbmQ=\n\
V2FzIGNvbWluZyBpbnRvIGhpcyBmb3JjZTs=\n\
SGUgbWlnaHQgaGF2ZSB3b24gZmFtZSBpbiB0aGUgZW5kLA==\n\
U28gc2Vuc2l0aXZlIGhpcyBuYXR1cmUgc2VlbWVkLA==\n\
U28gZGFyaW5nIGFuZCBzd2VldCBoaXMgdGhvdWdodC4=\n\
VGhpcyBvdGhlciBtYW4gSSBoYWQgZHJlYW1lZA==\n\
QSBkcnVua2VuLCB2YWluLWdsb3Jpb3VzIGxvdXQu\n\
SGUgaGFkIGRvbmUgbW9zdCBiaXR0ZXIgd3Jvbmc=\n\
VG8gc29tZSB3aG8gYXJlIG5lYXIgbXkgaGVhcnQs\n\
WWV0IEkgbnVtYmVyIGhpbSBpbiB0aGUgc29uZzs=\n\
SGUsIHRvbywgaGFzIHJlc2lnbmVkIGhpcyBwYXJ0\n\
SW4gdGhlIGNhc3VhbCBjb21lZHk7\n\
SGUsIHRvbywgaGFzIGJlZW4gY2hhbmdlZCBpbiBoaXMgdHVybiw=\n\
VHJhbnNmb3JtZWQgdXR0ZXJseTo=\n\
QSB0ZXJyaWJsZSBiZWF1dHkgaXMgYm9ybi4='

example = example.split("\n")
example = [b64decode(x) for x in example]

key = urandom(16)
nonce = 0

example_encrypted = []

for x in example:
	ctr = Counter.new(128, initial_value=nonce)
	aes = AES.new(key, AES.MODE_CTR, counter=ctr)
	example_encrypted.append(aes.encrypt(x))

abcd = []

def guess(table, number, position, letter, result_table):
	
	result_table = abcd
	
	c = ord(table[number][position])
	p = ord(letter) # Assuming

	k = c ^ p

	for y,x in enumerate(table):
		if position <= len(x)-1:
			result_char = chr(ord(x[position])^k)
		else: 
			result_char = ' '
		if len(result_table) < len(table):
			result_table.append(result_char)
		else:
			result_table[y] += result_char

	for y,x in enumerate(result_table):
		print str(y) + '. ' + x

	print '-'*50

guess(example_encrypted,0,0,'I', abcd)

guess(example_encrypted,30,1,'h', abcd) # 16-> This?
guess(example_encrypted,30,2,'i', abcd) # 16-> This?
guess(example_encrypted,30,3,'s', abcd) # 16-> This?

# 4. I ha -> I have?
guess(example_encrypted,4,4,'v', abcd)
guess(example_encrypted,4,5,'e', abcd)
guess(example_encrypted,4,6,' ', abcd)

# 3. Eightee -> Eighteen?
guess(example_encrypted,3,7,'n', abcd)

# 39. A terrib -> A Terribl
guess(example_encrypted,39,8,'l', abcd)

# 3. Eighteent -> Eighteenth?
guess(example_encrypted,3,9,'h', abcd)

# 1. Coming wit -> Coming with?
guess(example_encrypted,1,10,'h', abcd)

# 27. He might ha -> He might have?
guess(example_encrypted,27,11,'v', abcd)
guess(example_encrypted,27,12,'e', abcd)
guess(example_encrypted,27,13,' ', abcd)

# 3. Eighteenth-cen -> Eighteenth-century ?
guess(example_encrypted,3,14,'t', abcd)
guess(example_encrypted,3,15,'u', abcd)
guess(example_encrypted,3,16,'r', abcd)
guess(example_encrypted,3,17,'y', abcd)
guess(example_encrypted,3,18,' ', abcd)

# 21. When young and beau -> beautiful?
guess(example_encrypted,21,19,'t', abcd)
guess(example_encrypted,21,20,'i', abcd)
guess(example_encrypted,21,21,'f', abcd)
guess(example_encrypted,21,22,'u', abcd)
guess(example_encrypted,21,23,'l', abcd)

# 23. This man had kept a scho -> school?
guess(example_encrypted,23,24,'o', abcd)
guess(example_encrypted,23,25,'l', abcd)

# 0. I have met them at close o -> of' '?
guess(example_encrypted,0,26,'f', abcd)
guess(example_encrypted,0,27,' ', abcd)

# 27. He might have won fame in th -> in the' ' ?
guess(example_encrypted,27,28,'e', abcd)
guess(example_encrypted,27,29,' ', abcd)

# 25. This other his helper and frie -> friend
guess(example_encrypted,25,30,'n', abcd)
guess(example_encrypted,25,31,'d', abcd)

# 27. He might have won fame in the en -> end?
guess(example_encrypted,27,32,'d', abcd)

# 4. I have passed with a nod of the h -> head
guess(example_encrypted,4,33,'e', abcd)
guess(example_encrypted,4,34,'a', abcd)
guess(example_encrypted,4,35,'d', abcd)

# 37. He, too, has been changed in his tur
guess(example_encrypted,37,36,'n', abcd)

'''
0. I
1. C
2. F
3. E
4. I
5. O
6. O
7. P
8. A
9. O
10. T
11. A
12. B
13. B
14. A
15. A
16. T
17. I
18. H
19. U
20. W
21. W
22. S
23. T
24. A
25. T
26. W
27. H
28. S
29. S
30. T
31. A
32. H
33. T
34. Y
35. H
36. I
37. H
38. T
39. A
--------------------------------------------------
0. I 
1. Co
2. Fr
3. Ei
4. I 
5. Or
6. Or
7. Po
8. An
9. Of
10. To
11. Ar
12. Be
13. Bu
14. Al
15. A 
16. Th
17. In
18. He
19. Un
20. Wh
21. Wh
22. Sh
23. Th
24. An
25. Th
26. Wa
27. He
28. So
29. So
30. Th
31. A 
32. He
33. To
34. Ye
35. He
36. In
37. He
38. Tr
39. A 
--------------------------------------------------
0. I h
1. Com
2. Fro
3. Eig
4. I h
5. Or 
6. Or 
7. Pol
8. And
9. Of 
10. To 
11. Aro
12. Bei
13. But
14. All
15. A t
16. Tha
17. In 
18. Her
19. Unt
20. Wha
21. Whe
22. She
23. Thi
24. And
25. Thi
26. Was
27. He 
28. So 
29. So 
30. Thi
31. A d
32. He 
33. To 
34. Yet
35. He,
36. In 
37. He,
38. Tra
39. A t
--------------------------------------------------
0. I ha
1. Comi
2. From
3. Eigh
4. I ha
5. Or p
6. Or h
7. Poli
8. And 
9. Of a
10. To p
11. Arou
12. Bein
13. But 
14. All 
15. A te
16. That
17. In i
18. Her 
19. Unti
20. What
21. When
22. She 
23. This
24. And 
25. This
26. Was 
27. He m
28. So s
29. So d
30. This
31. A dr
32. He h
33. To s
34. Yet 
35. He, 
36. In t
37. He, 
38. Tran
39. A te
--------------------------------------------------
0. I hav
1. Comin
2. From 
3. Eight
4. I hav
5. Or po
6. Or ha
7. Polit
8. And t
9. Of a 
10. To pl
11. Aroun
12. Being
13. But l
14. All c
15. A ter
16. That 
17. In ig
18. Her n
19. Until
20. What 
21. When 
22. She r
23. This 
24. And r
25. This 
26. Was c
27. He mi
28. So se
29. So da
30. This 
31. A dru
32. He ha
33. To so
34. Yet I
35. He, t
36. In th
37. He, t
38. Trans
39. A ter
--------------------------------------------------
0. I have
1. Coming
2. From c
3. Eighte
4. I have
5. Or pol
6. Or hav
7. Polite
8. And th
9. Of a m
10. To ple
11. Around
12. Being 
13. But li
14. All ch
15. A terr
16. That w
17. In ign
18. Her ni
19. Until 
20. What v
21. When y
22. She ro
23. This m
24. And ro
25. This o
26. Was co
27. He mig
28. So sen
29. So dar
30. This o
31. A drun
32. He had
33. To som
34. Yet I 
35. He, to
36. In the
37. He, to
38. Transf
39. A terr
--------------------------------------------------
0. I have 
1. Coming 
2. From co
3. Eightee
4. I have 
5. Or poli
6. Or have
7. Polite 
8. And tho
9. Of a mo
10. To plea
11. Around 
12. Being c
13. But liv
14. All cha
15. A terri
16. That wo
17. In igno
18. Her nig
19. Until h
20. What vo
21. When yo
22. She rod
23. This ma
24. And rod
25. This ot
26. Was com
27. He migh
28. So sens
29. So dari
30. This ot
31. A drunk
32. He had 
33. To some
34. Yet I n
35. He, too
36. In the 
37. He, too
38. Transfo
39. A terri
--------------------------------------------------
0. I have m
1. Coming w
2. From cou
3. Eighteen
4. I have p
5. Or polit
6. Or have 
7. Polite m
8. And thou
9. Of a moc
10. To pleas
11. Around t
12. Being ce
13. But live
14. All chan
15. A terrib
16. That wom
17. In ignor
18. Her nigh
19. Until he
20. What voi
21. When you
22. She rode
23. This man
24. And rode
25. This oth
26. Was comi
27. He might
28. So sensi
29. So darin
30. This oth
31. A drunke
32. He had d
33. To some 
34. Yet I nu
35. He, too,
36. In the c
37. He, too,
38. Transfor
39. A terrib
--------------------------------------------------
0. I have me
1. Coming wi
2. From coun
3. Eighteent
4. I have pa
5. Or polite
6. Or have l
7. Polite me
8. And thoug
9. Of a mock
10. To please
11. Around th
12. Being cer
13. But lived
14. All chang
15. A terribl
16. That woma
17. In ignora
18. Her night
19. Until her
20. What voic
21. When youn
22. She rode 
23. This man 
24. And rode 
25. This othe
26. Was comin
27. He might 
28. So sensit
29. So daring
30. This othe
31. A drunken
32. He had do
33. To some w
34. Yet I num
35. He, too, 
36. In the ca
37. He, too, 
38. Transform
39. A terribl
--------------------------------------------------
0. I have met
1. Coming wit
2. From count
3. Eighteenth
4. I have pas
5. Or polite 
6. Or have li
7. Polite mea
8. And though
9. Of a mocki
10. To please 
11. Around the
12. Being cert
13. But lived 
14. All change
15. A terrible
16. That woman
17. In ignoran
18. Her nights
19. Until her 
20. What voice
21. When young
22. She rode t
23. This man h
24. And rode o
25. This other
26. Was coming
27. He might h
28. So sensiti
29. So daring 
30. This other
31. A drunken,
32. He had don
33. To some wh
34. Yet I numb
35. He, too, h
36. In the cas
37. He, too, h
38. Transforme
39. A terrible
--------------------------------------------------
0. I have met 
1. Coming with
2. From counte
3. Eighteenth-
4. I have pass
5. Or polite m
6. Or have lin
7. Polite mean
8. And thought
9. Of a mockin
10. To please a
11. Around the 
12. Being certa
13. But lived w
14. All changed
15. A terrible 
16. That woman'
17. In ignorant
18. Her nights 
19. Until her v
20. What voice 
21. When young 
22. She rode to
23. This man ha
24. And rode ou
25. This other 
26. Was coming 
27. He might ha
28. So sensitiv
29. So daring a
30. This other 
31. A drunken, 
32. He had done
33. To some who
34. Yet I numbe
35. He, too, ha
36. In the casu
37. He, too, ha
38. Transformed
39. A terrible 
--------------------------------------------------
0. I have met t
1. Coming with 
2. From counter
3. Eighteenth-c
4. I have passe
5. Or polite me
6. Or have ling
7. Polite meani
8. And thought 
9. Of a mocking
10. To please a 
11. Around the f
12. Being certai
13. But lived wh
14. All changed,
15. A terrible b
16. That woman's
17. In ignorant 
18. Her nights i
19. Until her vo
20. What voice m
21. When young a
22. She rode to 
23. This man had
24. And rode our
25. This other h
26. Was coming i
27. He might hav
28. So sensitive
29. So daring an
30. This other m
31. A drunken, v
32. He had done 
33. To some who 
34. Yet I number
35. He, too, has
36. In the casua
37. He, too, has
38. Transformed 
39. A terrible b
--------------------------------------------------
0. I have met th
1. Coming with v
2. From counter 
3. Eighteenth-ce
4. I have passed
5. Or polite mea
6. Or have linge
7. Polite meanin
8. And thought b
9. Of a mocking 
10. To please a c
11. Around the fi
12. Being certain
13. But lived whe
14. All changed, 
15. A terrible be
16. That woman's 
17. In ignorant g
18. Her nights in
19. Until her voi
20. What voice mo
21. When young an
22. She rode to h
23. This man had 
24. And rode our 
25. This other hi
26. Was coming in
27. He might have
28. So sensitive 
29. So daring and
30. This other ma
31. A drunken, va
32. He had done m
33. To some who a
34. Yet I number 
35. He, too, has 
36. In the casual
37. He, too, has 
38. Transformed u
39. A terrible be
--------------------------------------------------
0. I have met the
1. Coming with vi
2. From counter o
3. Eighteenth-cen
4. I have passed 
5. Or polite mean
6. Or have linger
7. Polite meaning
8. And thought be
9. Of a mocking t
10. To please a co
11. Around the fir
12. Being certain 
13. But lived wher
14. All changed, c
15. A terrible bea
16. That woman's d
17. In ignorant go
18. Her nights in 
19. Until her voic
20. What voice mor
21. When young and
22. She rode to ha
23. This man had k
24. And rode our w
25. This other his
26. Was coming int
27. He might have 
28. So sensitive h
29. So daring and 
30. This other man
31. A drunken, vai
32. He had done mo
33. To some who ar
34. Yet I number h
35. He, too, has r
36. In the casual 
37. He, too, has b
38. Transformed ut
39. A terrible bea
--------------------------------------------------
0. I have met them
1. Coming with viv
2. From counter or
3. Eighteenth-cent
4. I have passed w
5. Or polite meani
6. Or have lingere
7. Polite meaningl
8. And thought bef
9. Of a mocking ta
10. To please a com
11. Around the fire
12. Being certain t
13. But lived where
14. All changed, ch
15. A terrible beau
16. That woman's da
17. In ignorant goo
18. Her nights in a
19. Until her voice
20. What voice more
21. When young and 
22. She rode to har
23. This man had ke
24. And rode our wi
25. This other his 
26. Was coming into
27. He might have w
28. So sensitive hi
29. So daring and s
30. This other man 
31. A drunken, vain
32. He had done mos
33. To some who are
34. Yet I number hi
35. He, too, has re
36. In the casual c
37. He, too, has be
38. Transformed utt
39. A terrible beau
--------------------------------------------------
0. I have met them 
1. Coming with vivi
2. From counter or 
3. Eighteenth-centu
4. I have passed wi
5. Or polite meanin
6. Or have lingered
7. Polite meaningle
8. And thought befo
9. Of a mocking tal
10. To please a comp
11. Around the fire 
12. Being certain th
13. But lived where 
14. All changed, cha
15. A terrible beaut
16. That woman's day
17. In ignorant good
18. Her nights in ar
19. Until her voice 
20. What voice more 
21. When young and b
22. She rode to harr
23. This man had kep
24. And rode our win
25. This other his h
26. Was coming into 
27. He might have wo
28. So sensitive his
29. So daring and sw
30. This other man I
31. A drunken, vain-
32. He had done most
33. To some who are 
34. Yet I number him
35. He, too, has res
36. In the casual co
37. He, too, has bee
38. Transformed utte
39. A terrible beaut
--------------------------------------------------
0. I have met them a
1. Coming with vivid
2. From counter or d
3. Eighteenth-centur
4. I have passed wit
5. Or polite meaning
6. Or have lingered 
7. Polite meaningles
8. And thought befor
9. Of a mocking tale
10. To please a compa
11. Around the fire a
12. Being certain tha
13. But lived where m
14. All changed, chan
15. A terrible beauty
16. That woman's days
17. In ignorant good 
18. Her nights in arg
19. Until her voice g
20. What voice more s
21. When young and be
22. She rode to harri
23. This man had kept
24. And rode our wing
25. This other his he
26. Was coming into h
27. He might have won
28. So sensitive his 
29. So daring and swe
30. This other man I 
31. A drunken, vain-g
32. He had done most 
33. To some who are n
34. Yet I number him 
35. He, too, has resi
36. In the casual com
37. He, too, has been
38. Transformed utter
39. A terrible beauty
--------------------------------------------------
0. I have met them at
1. Coming with vivid 
2. From counter or de
3. Eighteenth-century
4. I have passed with
5. Or polite meaningl
6. Or have lingered a
7. Polite meaningless
8. And thought before
9. Of a mocking tale 
10. To please a compan
11. Around the fire at
12. Being certain that
13. But lived where mo
14. All changed, chang
15. A terrible beauty 
16. That woman's days 
17. In ignorant good w
18. Her nights in argu
19. Until her voice gr
20. What voice more sw
21. When young and bea
22. She rode to harrie
23. This man had kept 
24. And rode our winge
25. This other his hel
26. Was coming into hi
27. He might have won 
28. So sensitive his n
29. So daring and swee
30. This other man I h
31. A drunken, vain-gl
32. He had done most b
33. To some who are ne
34. Yet I number him i
35. He, too, has resig
36. In the casual come
37. He, too, has been 
38. Transformed utterl
39. A terrible beauty 
--------------------------------------------------
0. I have met them at 
1. Coming with vivid f
2. From counter or des
3. Eighteenth-century 
4. I have passed with 
5. Or polite meaningle
6. Or have lingered aw
7. Polite meaningless 
8. And thought before 
9. Of a mocking tale o
10. To please a compani
11. Around the fire at 
12. Being certain that 
13. But lived where mot
14. All changed, change
15. A terrible beauty i
16. That woman's days w
17. In ignorant good wi
18. Her nights in argum
19. Until her voice gre
20. What voice more swe
21. When young and beau
22. She rode to harrier
23. This man had kept a
24. And rode our winged
25. This other his help
26. Was coming into his
27. He might have won f
28. So sensitive his na
29. So daring and sweet
30. This other man I ha
31. A drunken, vain-glo
32. He had done most bi
33. To some who are nea
34. Yet I number him in
35. He, too, has resign
36. In the casual comed
37. He, too, has been c
38. Transformed utterly
39. A terrible beauty i
--------------------------------------------------
0. I have met them at c
1. Coming with vivid fa
2. From counter or desk
3. Eighteenth-century h
4. I have passed with a
5. Or polite meaningles
6. Or have lingered awh
7. Polite meaningless w
8. And thought before I
9. Of a mocking tale or
10. To please a companio
11. Around the fire at t
12. Being certain that t
13. But lived where motl
14. All changed, changed
15. A terrible beauty is
16. That woman's days we
17. In ignorant good wil
18. Her nights in argume
19. Until her voice grew
20. What voice more swee
21. When young and beaut
22. She rode to harriers
23. This man had kept a 
24. And rode our winged 
25. This other his helpe
26. Was coming into his 
27. He might have won fa
28. So sensitive his nat
29. So daring and sweet 
30. This other man I had
31. A drunken, vain-glor
32. He had done most bit
33. To some who are near
34. Yet I number him in 
35. He, too, has resigne
36. In the casual comedy
37. He, too, has been ch
38. Transformed utterly:
39. A terrible beauty is
--------------------------------------------------
0. I have met them at cl
1. Coming with vivid fac
2. From counter or desk 
3. Eighteenth-century ho
4. I have passed with a 
5. Or polite meaningless
6. Or have lingered awhi
7. Polite meaningless wo
8. And thought before I 
9. Of a mocking tale or 
10. To please a companion
11. Around the fire at th
12. Being certain that th
13. But lived where motle
14. All changed, changed 
15. A terrible beauty is 
16. That woman's days wer
17. In ignorant good will
18. Her nights in argumen
19. Until her voice grew 
20. What voice more sweet
21. When young and beauti
22. She rode to harriers?
23. This man had kept a s
24. And rode our winged h
25. This other his helper
26. Was coming into his f
27. He might have won fam
28. So sensitive his natu
29. So daring and sweet h
30. This other man I had 
31. A drunken, vain-glori
32. He had done most bitt
33. To some who are near 
34. Yet I number him in t
35. He, too, has resigned
36. In the casual comedy;
37. He, too, has been cha
38. Transformed utterly: 
39. A terrible beauty is 
--------------------------------------------------
0. I have met them at clo
1. Coming with vivid face
2. From counter or desk a
3. Eighteenth-century hou
4. I have passed with a n
5. Or polite meaningless 
6. Or have lingered awhil
7. Polite meaningless wor
8. And thought before I h
9. Of a mocking tale or a
10. To please a companion 
11. Around the fire at the
12. Being certain that the
13. But lived where motley
14. All changed, changed u
15. A terrible beauty is b
16. That woman's days were
17. In ignorant good will,
18. Her nights in argument
19. Until her voice grew s
20. What voice more sweet 
21. When young and beautif
22. She rode to harriers? 
23. This man had kept a sc
24. And rode our winged ho
25. This other his helper 
26. Was coming into his fo
27. He might have won fame
28. So sensitive his natur
29. So daring and sweet hi
30. This other man I had d
31. A drunken, vain-glorio
32. He had done most bitte
33. To some who are near m
34. Yet I number him in th
35. He, too, has resigned 
36. In the casual comedy; 
37. He, too, has been chan
38. Transformed utterly:  
39. A terrible beauty is b
--------------------------------------------------
0. I have met them at clos
1. Coming with vivid faces
2. From counter or desk am
3. Eighteenth-century hous
4. I have passed with a no
5. Or polite meaningless w
6. Or have lingered awhile
7. Polite meaningless word
8. And thought before I ha
9. Of a mocking tale or a 
10. To please a companion  
11. Around the fire at the 
12. Being certain that they
13. But lived where motley 
14. All changed, changed ut
15. A terrible beauty is bo
16. That woman's days were 
17. In ignorant good will, 
18. Her nights in argument 
19. Until her voice grew sh
20. What voice more sweet t
21. When young and beautifu
22. She rode to harriers?  
23. This man had kept a sch
24. And rode our winged hor
25. This other his helper a
26. Was coming into his for
27. He might have won fame 
28. So sensitive his nature
29. So daring and sweet his
30. This other man I had dr
31. A drunken, vain-gloriou
32. He had done most bitter
33. To some who are near my
34. Yet I number him in the
35. He, too, has resigned h
36. In the casual comedy;  
37. He, too, has been chang
38. Transformed utterly:   
39. A terrible beauty is bo
--------------------------------------------------
0. I have met them at close
1. Coming with vivid faces 
2. From counter or desk amo
3. Eighteenth-century house
4. I have passed with a nod
5. Or polite meaningless wo
6. Or have lingered awhile 
7. Polite meaningless words
8. And thought before I had
9. Of a mocking tale or a g
10. To please a companion   
11. Around the fire at the c
12. Being certain that they 
13. But lived where motley i
14. All changed, changed utt
15. A terrible beauty is bor
16. That woman's days were s
17. In ignorant good will,  
18. Her nights in argument  
19. Until her voice grew shr
20. What voice more sweet th
21. When young and beautiful
22. She rode to harriers?   
23. This man had kept a scho
24. And rode our winged hors
25. This other his helper an
26. Was coming into his forc
27. He might have won fame i
28. So sensitive his nature 
29. So daring and sweet his 
30. This other man I had dre
31. A drunken, vain-glorious
32. He had done most bitter 
33. To some who are near my 
34. Yet I number him in the 
35. He, too, has resigned hi
36. In the casual comedy;   
37. He, too, has been change
38. Transformed utterly:    
39. A terrible beauty is bor
--------------------------------------------------
0. I have met them at close 
1. Coming with vivid faces  
2. From counter or desk amon
3. Eighteenth-century houses
4. I have passed with a nod 
5. Or polite meaningless wor
6. Or have lingered awhile a
7. Polite meaningless words,
8. And thought before I had 
9. Of a mocking tale or a gi
10. To please a companion    
11. Around the fire at the cl
12. Being certain that they a
13. But lived where motley is
14. All changed, changed utte
15. A terrible beauty is born
16. That woman's days were sp
17. In ignorant good will,   
18. Her nights in argument   
19. Until her voice grew shri
20. What voice more sweet tha
21. When young and beautiful,
22. She rode to harriers?    
23. This man had kept a schoo
24. And rode our winged horse
25. This other his helper and
26. Was coming into his force
27. He might have won fame in
28. So sensitive his nature s
29. So daring and sweet his t
30. This other man I had drea
31. A drunken, vain-glorious 
32. He had done most bitter w
33. To some who are near my h
34. Yet I number him in the s
35. He, too, has resigned his
36. In the casual comedy;    
37. He, too, has been changed
38. Transformed utterly:     
39. A terrible beauty is born
--------------------------------------------------
0. I have met them at close o
1. Coming with vivid faces   
2. From counter or desk among
3. Eighteenth-century houses.
4. I have passed with a nod o
5. Or polite meaningless word
6. Or have lingered awhile an
7. Polite meaningless words, 
8. And thought before I had d
9. Of a mocking tale or a gib
10. To please a companion     
11. Around the fire at the clu
12. Being certain that they an
13. But lived where motley is 
14. All changed, changed utter
15. A terrible beauty is born.
16. That woman's days were spe
17. In ignorant good will,    
18. Her nights in argument    
19. Until her voice grew shril
20. What voice more sweet than
21. When young and beautiful, 
22. She rode to harriers?     
23. This man had kept a school
24. And rode our winged horse.
25. This other his helper and 
26. Was coming into his force;
27. He might have won fame in 
28. So sensitive his nature se
29. So daring and sweet his th
30. This other man I had dream
31. A drunken, vain-glorious l
32. He had done most bitter wr
33. To some who are near my he
34. Yet I number him in the so
35. He, too, has resigned his 
36. In the casual comedy;     
37. He, too, has been changed 
38. Transformed utterly:      
39. A terrible beauty is born.
--------------------------------------------------
0. I have met them at close of
1. Coming with vivid faces    
2. From counter or desk among 
3. Eighteenth-century houses. 
4. I have passed with a nod of
5. Or polite meaningless words
6. Or have lingered awhile and
7. Polite meaningless words,  
8. And thought before I had do
9. Of a mocking tale or a gibe
10. To please a companion      
11. Around the fire at the club
12. Being certain that they and
13. But lived where motley is w
14. All changed, changed utterl
15. A terrible beauty is born. 
16. That woman's days were spen
17. In ignorant good will,     
18. Her nights in argument     
19. Until her voice grew shrill
20. What voice more sweet than 
21. When young and beautiful,  
22. She rode to harriers?      
23. This man had kept a school 
24. And rode our winged horse. 
25. This other his helper and f
26. Was coming into his force; 
27. He might have won fame in t
28. So sensitive his nature see
29. So daring and sweet his tho
30. This other man I had dreame
31. A drunken, vain-glorious lo
32. He had done most bitter wro
33. To some who are near my hea
34. Yet I number him in the son
35. He, too, has resigned his p
36. In the casual comedy;      
37. He, too, has been changed i
38. Transformed utterly:       
39. A terrible beauty is born. 
--------------------------------------------------
0. I have met them at close of 
1. Coming with vivid faces     
2. From counter or desk among g
3. Eighteenth-century houses.  
4. I have passed with a nod of 
5. Or polite meaningless words,
6. Or have lingered awhile and 
7. Polite meaningless words,   
8. And thought before I had don
9. Of a mocking tale or a gibe 
10. To please a companion       
11. Around the fire at the club,
12. Being certain that they and 
13. But lived where motley is wo
14. All changed, changed utterly
15. A terrible beauty is born.  
16. That woman's days were spent
17. In ignorant good will,      
18. Her nights in argument      
19. Until her voice grew shrill.
20. What voice more sweet than h
21. When young and beautiful,   
22. She rode to harriers?       
23. This man had kept a school  
24. And rode our winged horse.  
25. This other his helper and fr
26. Was coming into his force;  
27. He might have won fame in th
28. So sensitive his nature seem
29. So daring and sweet his thou
30. This other man I had dreamed
31. A drunken, vain-glorious lou
32. He had done most bitter wron
33. To some who are near my hear
34. Yet I number him in the song
35. He, too, has resigned his pa
36. In the casual comedy;       
37. He, too, has been changed in
38. Transformed utterly:        
39. A terrible beauty is born.  
--------------------------------------------------
0. I have met them at close of d
1. Coming with vivid faces      
2. From counter or desk among gr
3. Eighteenth-century houses.   
4. I have passed with a nod of t
5. Or polite meaningless words, 
6. Or have lingered awhile and s
7. Polite meaningless words,    
8. And thought before I had done
9. Of a mocking tale or a gibe  
10. To please a companion        
11. Around the fire at the club, 
12. Being certain that they and I
13. But lived where motley is wor
14. All changed, changed utterly:
15. A terrible beauty is born.   
16. That woman's days were spent 
17. In ignorant good will,       
18. Her nights in argument       
19. Until her voice grew shrill. 
20. What voice more sweet than he
21. When young and beautiful,    
22. She rode to harriers?        
23. This man had kept a school   
24. And rode our winged horse.   
25. This other his helper and fri
26. Was coming into his force;   
27. He might have won fame in the
28. So sensitive his nature seeme
29. So daring and sweet his thoug
30. This other man I had dreamed 
31. A drunken, vain-glorious lout
32. He had done most bitter wrong
33. To some who are near my heart
34. Yet I number him in the song;
35. He, too, has resigned his par
36. In the casual comedy;        
37. He, too, has been changed in 
38. Transformed utterly:         
39. A terrible beauty is born.   
--------------------------------------------------
0. I have met them at close of da
1. Coming with vivid faces       
2. From counter or desk among gre
3. Eighteenth-century houses.    
4. I have passed with a nod of th
5. Or polite meaningless words,  
6. Or have lingered awhile and sa
7. Polite meaningless words,     
8. And thought before I had done 
9. Of a mocking tale or a gibe   
10. To please a companion         
11. Around the fire at the club,  
12. Being certain that they and I 
13. But lived where motley is worn
14. All changed, changed utterly: 
15. A terrible beauty is born.    
16. That woman's days were spent  
17. In ignorant good will,        
18. Her nights in argument        
19. Until her voice grew shrill.  
20. What voice more sweet than her
21. When young and beautiful,     
22. She rode to harriers?         
23. This man had kept a school    
24. And rode our winged horse.    
25. This other his helper and frie
26. Was coming into his force;    
27. He might have won fame in the 
28. So sensitive his nature seemed
29. So daring and sweet his though
30. This other man I had dreamed  
31. A drunken, vain-glorious lout.
32. He had done most bitter wrong 
33. To some who are near my heart,
34. Yet I number him in the song; 
35. He, too, has resigned his part
36. In the casual comedy;         
37. He, too, has been changed in h
38. Transformed utterly:          
39. A terrible beauty is born.    
--------------------------------------------------
0. I have met them at close of day
1. Coming with vivid faces        
2. From counter or desk among grey
3. Eighteenth-century houses.     
4. I have passed with a nod of the
5. Or polite meaningless words,   
6. Or have lingered awhile and sai
7. Polite meaningless words,      
8. And thought before I had done  
9. Of a mocking tale or a gibe    
10. To please a companion          
11. Around the fire at the club,   
12. Being certain that they and I  
13. But lived where motley is worn:
14. All changed, changed utterly:  
15. A terrible beauty is born.     
16. That woman's days were spent   
17. In ignorant good will,         
18. Her nights in argument         
19. Until her voice grew shrill.   
20. What voice more sweet than hers
21. When young and beautiful,      
22. She rode to harriers?          
23. This man had kept a school     
24. And rode our winged horse.     
25. This other his helper and frien
26. Was coming into his force;     
27. He might have won fame in the e
28. So sensitive his nature seemed,
29. So daring and sweet his thought
30. This other man I had dreamed   
31. A drunken, vain-glorious lout. 
32. He had done most bitter wrong  
33. To some who are near my heart, 
34. Yet I number him in the song;  
35. He, too, has resigned his part 
36. In the casual comedy;          
37. He, too, has been changed in hi
38. Transformed utterly:           
39. A terrible beauty is born.     
--------------------------------------------------
0. I have met them at close of day 
1. Coming with vivid faces         
2. From counter or desk among grey 
3. Eighteenth-century houses.      
4. I have passed with a nod of the 
5. Or polite meaningless words,    
6. Or have lingered awhile and said
7. Polite meaningless words,       
8. And thought before I had done   
9. Of a mocking tale or a gibe     
10. To please a companion           
11. Around the fire at the club,    
12. Being certain that they and I   
13. But lived where motley is worn: 
14. All changed, changed utterly:   
15. A terrible beauty is born.      
16. That woman's days were spent    
17. In ignorant good will,          
18. Her nights in argument          
19. Until her voice grew shrill.    
20. What voice more sweet than hers 
21. When young and beautiful,       
22. She rode to harriers?           
23. This man had kept a school      
24. And rode our winged horse.      
25. This other his helper and friend
26. Was coming into his force;      
27. He might have won fame in the en
28. So sensitive his nature seemed, 
29. So daring and sweet his thought.
30. This other man I had dreamed    
31. A drunken, vain-glorious lout.  
32. He had done most bitter wrong   
33. To some who are near my heart,  
34. Yet I number him in the song;   
35. He, too, has resigned his part  
36. In the casual comedy;           
37. He, too, has been changed in his
38. Transformed utterly:            
39. A terrible beauty is born.      
--------------------------------------------------
0. I have met them at close of day  
1. Coming with vivid faces          
2. From counter or desk among grey  
3. Eighteenth-century houses.       
4. I have passed with a nod of the h
5. Or polite meaningless words,     
6. Or have lingered awhile and said 
7. Polite meaningless words,        
8. And thought before I had done    
9. Of a mocking tale or a gibe      
10. To please a companion            
11. Around the fire at the club,     
12. Being certain that they and I    
13. But lived where motley is worn:  
14. All changed, changed utterly:    
15. A terrible beauty is born.       
16. That woman's days were spent     
17. In ignorant good will,           
18. Her nights in argument           
19. Until her voice grew shrill.     
20. What voice more sweet than hers  
21. When young and beautiful,        
22. She rode to harriers?            
23. This man had kept a school       
24. And rode our winged horse.       
25. This other his helper and friend 
26. Was coming into his force;       
27. He might have won fame in the end
28. So sensitive his nature seemed,  
29. So daring and sweet his thought. 
30. This other man I had dreamed     
31. A drunken, vain-glorious lout.   
32. He had done most bitter wrong    
33. To some who are near my heart,   
34. Yet I number him in the song;    
35. He, too, has resigned his part   
36. In the casual comedy;            
37. He, too, has been changed in his 
38. Transformed utterly:             
39. A terrible beauty is born.       
--------------------------------------------------
0. I have met them at close of day   
1. Coming with vivid faces           
2. From counter or desk among grey   
3. Eighteenth-century houses.        
4. I have passed with a nod of the he
5. Or polite meaningless words,      
6. Or have lingered awhile and said  
7. Polite meaningless words,         
8. And thought before I had done     
9. Of a mocking tale or a gibe       
10. To please a companion             
11. Around the fire at the club,      
12. Being certain that they and I     
13. But lived where motley is worn:   
14. All changed, changed utterly:     
15. A terrible beauty is born.        
16. That woman's days were spent      
17. In ignorant good will,            
18. Her nights in argument            
19. Until her voice grew shrill.      
20. What voice more sweet than hers   
21. When young and beautiful,         
22. She rode to harriers?             
23. This man had kept a school        
24. And rode our winged horse.        
25. This other his helper and friend  
26. Was coming into his force;        
27. He might have won fame in the end,
28. So sensitive his nature seemed,   
29. So daring and sweet his thought.  
30. This other man I had dreamed      
31. A drunken, vain-glorious lout.    
32. He had done most bitter wrong     
33. To some who are near my heart,    
34. Yet I number him in the song;     
35. He, too, has resigned his part    
36. In the casual comedy;             
37. He, too, has been changed in his t
38. Transformed utterly:              
39. A terrible beauty is born.        
--------------------------------------------------
0. I have met them at close of day    
1. Coming with vivid faces            
2. From counter or desk among grey    
3. Eighteenth-century houses.         
4. I have passed with a nod of the hea
5. Or polite meaningless words,       
6. Or have lingered awhile and said   
7. Polite meaningless words,          
8. And thought before I had done      
9. Of a mocking tale or a gibe        
10. To please a companion              
11. Around the fire at the club,       
12. Being certain that they and I      
13. But lived where motley is worn:    
14. All changed, changed utterly:      
15. A terrible beauty is born.         
16. That woman's days were spent       
17. In ignorant good will,             
18. Her nights in argument             
19. Until her voice grew shrill.       
20. What voice more sweet than hers    
21. When young and beautiful,          
22. She rode to harriers?              
23. This man had kept a school         
24. And rode our winged horse.         
25. This other his helper and friend   
26. Was coming into his force;         
27. He might have won fame in the end, 
28. So sensitive his nature seemed,    
29. So daring and sweet his thought.   
30. This other man I had dreamed       
31. A drunken, vain-glorious lout.     
32. He had done most bitter wrong      
33. To some who are near my heart,     
34. Yet I number him in the song;      
35. He, too, has resigned his part     
36. In the casual comedy;              
37. He, too, has been changed in his tu
38. Transformed utterly:               
39. A terrible beauty is born.         
--------------------------------------------------
0. I have met them at close of day     
1. Coming with vivid faces             
2. From counter or desk among grey     
3. Eighteenth-century houses.          
4. I have passed with a nod of the head
5. Or polite meaningless words,        
6. Or have lingered awhile and said    
7. Polite meaningless words,           
8. And thought before I had done       
9. Of a mocking tale or a gibe         
10. To please a companion               
11. Around the fire at the club,        
12. Being certain that they and I       
13. But lived where motley is worn:     
14. All changed, changed utterly:       
15. A terrible beauty is born.          
16. That woman's days were spent        
17. In ignorant good will,              
18. Her nights in argument              
19. Until her voice grew shrill.        
20. What voice more sweet than hers     
21. When young and beautiful,           
22. She rode to harriers?               
23. This man had kept a school          
24. And rode our winged horse.          
25. This other his helper and friend    
26. Was coming into his force;          
27. He might have won fame in the end,  
28. So sensitive his nature seemed,     
29. So daring and sweet his thought.    
30. This other man I had dreamed        
31. A drunken, vain-glorious lout.      
32. He had done most bitter wrong       
33. To some who are near my heart,      
34. Yet I number him in the song;       
35. He, too, has resigned his part      
36. In the casual comedy;               
37. He, too, has been changed in his tur
38. Transformed utterly:                
39. A terrible beauty is born.          
--------------------------------------------------
0. I have met them at close of day      
1. Coming with vivid faces              
2. From counter or desk among grey      
3. Eighteenth-century houses.           
4. I have passed with a nod of the head 
5. Or polite meaningless words,         
6. Or have lingered awhile and said     
7. Polite meaningless words,            
8. And thought before I had done        
9. Of a mocking tale or a gibe          
10. To please a companion                
11. Around the fire at the club,         
12. Being certain that they and I        
13. But lived where motley is worn:      
14. All changed, changed utterly:        
15. A terrible beauty is born.           
16. That woman's days were spent         
17. In ignorant good will,               
18. Her nights in argument               
19. Until her voice grew shrill.         
20. What voice more sweet than hers      
21. When young and beautiful,            
22. She rode to harriers?                
23. This man had kept a school           
24. And rode our winged horse.           
25. This other his helper and friend     
26. Was coming into his force;           
27. He might have won fame in the end,   
28. So sensitive his nature seemed,      
29. So daring and sweet his thought.     
30. This other man I had dreamed         
31. A drunken, vain-glorious lout.       
32. He had done most bitter wrong        
33. To some who are near my heart,       
34. Yet I number him in the song;        
35. He, too, has resigned his part       
36. In the casual comedy;                
37. He, too, has been changed in his turn
38. Transformed utterly:                 
39. A terrible beauty is born.           
--------------------------------------------------
'''
