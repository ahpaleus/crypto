from Crypto.Cipher import AES
from Crypto.Util import Counter
from base64 import b64encode, b64decode
from isprintable import isprintable
from binascii import hexlify as hexa
import re
import sys
import os


file = open("20.txt", "r")
unencrypted = file.read()
unencrypted = unencrypted.split("\n")
del unencrypted[-1]
unencrypted = [b64decode(y) for y in unencrypted]

key = os.urandom(16) 
nonce = 0

example_encrypted = []

for x in unencrypted:
	ctr = Counter.new(128, initial_value=nonce)
	aes = AES.new(key, AES.MODE_CTR, counter=ctr)
	ciph = aes.encrypt(x)
	example_encrypted.append(ciph)

first_bytes = ''
KEY = ''
PLAINTEXT_LIST = []
max_number = 0


for number in xrange(len(example_encrypted[0])):
	first_bytes = ''
	print '-'*100
	print 'number: ' + str(number),
	for x in example_encrypted:
		try:
			first_bytes += x[number]
		except: pass	
	i = 0

	for x in xrange(256):
		test = ''

		for byte in first_bytes:
			test += chr(ord(byte) ^ x)

		if bool(re.search("[^a-zA-Z0-9'\s./?,\-\!\"\;\:]",test)) == False and test.count("\"") < 3:
			print ' -> ' + hexa(chr(x)) + '\n' + test

			KEY += chr(x)
			PLAINTEXT_LIST.append([test,''])
			if i != 0: 
				print '\t\t\t\t\t\t\t\t\x1b[6;30;42m---------------->DOUBLE\x1b[0m'
				PLAINTEXT_LIST[len(PLAINTEXT_LIST)-1][1] = test

			i += 1
	
	max_number = number

print 'POSSIBLE KEY: '
print hexa(KEY) + '\n\n\n'

# print PLAINTEXT_LIST

for z in xrange(number):
	for x in PLAINTEXT_LIST:
		for y in x:
			try:
				sys.stdout.write(y[z])
			except:
				pass
	print ""


# challenge20 $ python ctr2.py
# ----------------------------------------------------------------------------------------------------
# number: 0  -> b5
# ICBYSMHDFTTFWFTSMTMIHSICLMYTAPMOBYINYWKOCITSSIIBSSAF'SR'YATA
# ----------------------------------------------------------------------------------------------------
# number: 1  -> 4b
# 'uuauuaerheoolhoChe ahfuyaohnrupao ooeakh hoo  ueo iCoaConun
# ----------------------------------------------------------------------------------------------------
# number: 2  -> fb
# mzt dsvaiirrraeo'elbza zrkuedosetuwv lraewi  nuta psu ka,drd
# ----------------------------------------------------------------------------------------------------
# number: 3  -> 4b
#    tdietdsr ssnns olakn ie n gint aoRlaycanIIes rIehzniu  n
# ----------------------------------------------------------------------------------------------------
# number: 4  -> b3
# rIdrecnha oteh   fdereoyc w Irc ltkca, ,knk  eenc n, omsIc w
# ----------------------------------------------------------------------------------------------------
# number: 5  -> 3d
# a oen'' yirh bttdiisd tossan aayeheak L  nidsddohw  Iw,e ode
# ----------------------------------------------------------------------------------------------------
# number: 6  -> a5
# tcnmlstw s otahheeeso',u unodmlo'i iicestanit  w aaw    huo
# ----------------------------------------------------------------------------------------------------
# number: 7  -> c6
# ea'by  it ishceecns ut rortno  usnynmhwoh 'gamt flnhdtcmenwo
# ----------------------------------------------------------------------------------------------------
# number: 8  -> c7
# dmtl tyshoneak  ad-tsim fe cnimr ka ,ei ih  rooIokdioohyatnu
# ----------------------------------------------------------------------------------------------------
# number: 9  -> 96
#  e eyhohef  nsbly uh lya  th'na t  e cswseoitn  r  cn e r  t
# ----------------------------------------------------------------------------------------------------
# number: 10  -> e0
# " b oeu, ftt  eyionetl bftoattdmeywawk h afn erl uah'tcg ott
# ----------------------------------------------------------------------------------------------------
# number: 11  -> 7b
# Rbelu   t hhaiarnfm o souh l onimoish ioor tmyoeap  tekiwuha
# ----------------------------------------------------------------------------------------------------
# number: 12  -> 79
# "a i ceshlea ntig ac yourehac enputeats u aoy,la  pi s rhre
# ----------------------------------------------------------------------------------------------------
# number: 13  -> fd
# .cakflvoii tnt c,akhyouty enatsdt'h th wts    lrntaslttla  h
# ----------------------------------------------------------------------------------------------------
# number: 14  -> 3a
# .kfeeue rms ieia  aioul !satrhs,ir t'ioe,ommmI nihp i h tmbe
# ----------------------------------------------------------------------------------------------------
# number: 15  -> ec
# . r eerctitogrslcrblur't yrlee  nehhssu  mayi ueneemktii oar
# ----------------------------------------------------------------------------------------------------
# number: 16  -> 22
# ttaal, oetyphf  uhldr loAs y  Myg ue  rrses supde ryeossynse
# ----------------------------------------------------------------------------------------------------
# number: 17  -> 5d
# hoi   hmeslptehfzye, cl  ts isCo.rn uo oi tpss,  s,     oes
# ----------------------------------------------------------------------------------------------------
# number: 18  -> 9d
# i dalween,eomryo m, hl sfeotfp u.udppualnoeoie ttt ftsoduy /
# ----------------------------------------------------------------------------------------------------
# number: 19  -> b7
# sa liha t ssaesrte teereemme ee .fra?tglcfrcodtooraaoeue' d
# ----------------------------------------------------------------------------------------------------
# number: 20  -> 05
#  tickerohs,er,tmh phaaeea'eltevwwfei ,eie  kn h  e v etfr/oY
# ----------------------------------------------------------------------------------------------------
# number: 21  -> aa
# itnoendn,o  e eaeoaelrl rs lhdeihedn/ nn tpe,tiefesod ,ie wo
# ----------------------------------------------------------------------------------------------------
# number: 22  -> 8f
# sa h   ,  nt,yrtynt t,eai s e rlars  st'whlt osaittrri n Yn,
# ----------------------------------------------------------------------------------------------------
# number: 23  -> 4d
#  ctoyIo wyeo ai   teh a floy o lt, iYi, eea,l  rv eiefyiso
# ----------------------------------------------------------------------------------------------------
# number: 24  -> 84
# akhlo fsaov y cintea msdiouowfm e oton w mn ebinewrta ota,/w
# ----------------------------------------------------------------------------------------------------
# number: 25  -> 3d
#   eiuc tluebosasehrrsaeieunuh afvtf ,cwit  aaes ,heemI ey  h
# ----------------------------------------------------------------------------------------------------
# number: 26  -> 6d
# wo croaekrreutl ventok!sddd otdieh m eotad/lv  ' io   /liwAa
# ----------------------------------------------------------------------------------------------------
# number: 27  -> 8e
# atd, m pi    a se -h e a  swlhenretiI rhle leaacis,dag ynent
# ----------------------------------------------------------------------------------------------------
# number: 28  -> 46
# rha ieM nveldr/urmu,b /sfw hee,d nhg'Nd kf'    uft iboY gld
# ----------------------------------------------------------------------------------------------------
# number: 29  -> 26
# nermn Ctgireot p in ei trhta    s ohmo ti Cmmshz lasotom l h
# ----------------------------------------------------------------------------------------------------
# number: 30  -> 08
# irku y-o srvn Tescet tTreehtcrseusut ruhnruyyto Ii hu ua/ la
# ----------------------------------------------------------------------------------------------------
# number: 31  -> a0
# ns,saom dioe'thrt shf hoena rhevius dbpeghz  ilI nt tp d cep
# ----------------------------------------------------------------------------------------------------
# number: 32  -> db
# g  c uutoorltoaiatcerdeus tioyeetfasoy n y mrcd's'a/ ug Shtp
# ----------------------------------------------------------------------------------------------------
# number: 33  -> 66
# ,iilhrrhwn-   toyha ii stI twm rsfnai /?omaoek mt p glo/oe e
# ----------------------------------------------------------------------------------------------------
# number: 34  -> 7a
#  nneo dinsfohh reapgess y n deiy edvnW  veins-u rteBel   ctn
# ----------------------------------------------------------------------------------------------------
# number: 35  -> 4d
# y  srwes  iraem dtaonacslmom',t yrsegaZWesneiuprih ut t'lkhe
# ----------------------------------------------------------------------------------------------------
# number: 36  -> 42
# asa rar Eal vaa/  bddpeieetes 'wa    laer,'ydp,iviott/oCe ed
# ----------------------------------------------------------------------------------------------------
# number: 37  -> ac
#  p tore/lrenerk /ylslpng!n a pso!tohttk   t e  gesf i  att
# ----------------------------------------------------------------------------------------------------
# number: 38  -> 73
# bipirnr mese :eF oe yeeh tonar r hfiheir/y inkah   wnHyu'hbt
# ----------------------------------------------------------------------------------------------------
# number: 39  -> 58
# etag e?H   xt saTu a a t/in  e/d/e merao onsciit///i'iossieo
# ----------------------------------------------------------------------------------------------------
# number: 40  -> 74
# terhfd ySb/to/ ch /n/ri  oltwp '  v  s lTuu edne   t tue sa
# ----------------------------------------------------------------------------------------------------
# number: 41  -> ef
# t-ktl /stl    Eeek d ,s/TnyoiaNlFco/k alh ts  'oTFMhp r j tp
# ----------------------------------------------------------------------------------------------------
# number: 42  -> d5
# e  ei/ truItsTrs nA A   h   trolool niniikhp//tuheeoat iuo e
# ----------------------------------------------------------------------------------------------------
# number: 43  -> 37
# r//nc Teernolhi so b mrAe/pmnew rntIosdnsnie   see uihgtsuja
# ----------------------------------------------------------------------------------------------------
# number: 44  -> 7a
#     kAhrerd eecocwhomae   oee  b ssfw  ' onnTSn nlatdei ttuc
#  -> 7d
# ''''lFoubuc'bbdhdpohjfb'''hbb''e'ttap'' 'hiiSTi'ikfscbn'ssrd
# 								---------------->DOUBLE
# ----------------------------------------------------------------------------------------------------
# number: 45  -> 4b
# vSNu piityete  fe omakcp"Pu staewe  lo4 dw'thou/ in   rt ,se
# ----------------------------------------------------------------------------------------------------
# number: 46  -> 4a
# otop/osc  ehpRg n/rbtereRhn/son oq/neutwe   i t mndn/slop t?
# ----------------------------------------------------------------------------------------------------
# number: 47  -> cc
# irt  c a//di -ode n t er"rd !  /ru odrhifwb/nIhIa' o t ouy
# ----------------------------------------------------------------------------------------------------
# number: 48  -> a2
# di /Yail   saA e I tetaf asS se deMtg  t hu k i y E Suhkmok/
# ----------------------------------------------------------------------------------------------------
# number: 49  -> ed
#  ka ols YAI  -gaotihrhtois t/tmFsni,eaahbatSitnfbormodo p e
# ----------------------------------------------------------------------------------------------------
# number: 50  -> 54
# /e Wuy iol'/wKetf'fe eersebr aeu cc ,gn et onh'eeuio iuu EeP
# ----------------------------------------------------------------------------------------------------
# number: 51  -> 87
#   sh ptdulm i-th s  o dm suiIrrrte-E edRa s 'i e tcnIosstlpe
# ----------------------------------------------------------------------------------------------------
# number: 52  -> ce
# Plcagshe   InI  a wrfn,ai tc'tgihstrEn utIwI nflI  e ,e hi a
# ----------------------------------------------------------------------------------------------------
# number: 53  -> b8
# oirtreeacyk k-ar oae e nnt tm eee!oi.cBs 'e hku 'oByd  teoc
# ----------------------------------------------------------------------------------------------------
# number: 54  -> 19
# eke'a   oana M ecnnslxrc hpl /nr  -c,yrhrmado nglf, i'ao ne
# ----------------------------------------------------------------------------------------------------
# number: 55  -> 6e
# teasbNdfm oi/ amrlttiteetalya c s/m  ,o i tiwonrl  igcnom
# ----------------------------------------------------------------------------------------------------
# number: 56  -> 6d
# s m  oeoeswn ixaiy  f i hte  Ryte oBm a/gs g fye pat ud ur
# ----------------------------------------------------------------------------------------------------
# number: 57  -> 75
#  l tywar en'Tn im t/e/nne'abth,hnIu.ard hai c  asln'iz lso
# ----------------------------------------------------------------------------------------------------
# number: 58  -> 97
# aioho,t ie-th aneoh   ce ssuey at't'niwOtyndoa/ttadsn Ioic
# ----------------------------------------------------------------------------------------------------
# number: 59  -> ec
# rgrau han y eyn neFaAavh esatonemhs gaf iseul ,ac  tI'nck
# ----------------------------------------------------------------------------------------------------
# number: 60  -> 38
# eh trw   ioa odee onfreof irhp n   Ihy hniellS yeaso'lg i
# ----------------------------------------------------------------------------------------------------
# number: 61  -> 03
#  ta, hplmsu pu v srdtnrueyn meecnrt't Re'dpd ts   t ml un
# ----------------------------------------------------------------------------------------------------
# number: 62  -> f2
# pn  heeyy rdarcect  ea saoey'nveeehm?iur?ee tooa'nit  tp'
# ----------------------------------------------------------------------------------------------------
# number: 63  -> 4d
# aiclennr t ei hraytdrtaerusos-e,vse  sse  rIhp lcilhpgo
# ----------------------------------------------------------------------------------------------------
# number: 64  -> b5
# rnria airhevneoyplhe eg-srsu hr eu t/ h /m  e miucleao
# ----------------------------------------------------------------------------------------------------
# number: 65  -> 2e
# a'ygrIlceexi'ap aeoatdato   oe,trsjr ott ybg savze  i d
# ----------------------------------------------------------------------------------------------------
# number: 66  -> 32
# n,,ht'taa ilsrsnb sth,iomeIaua h cuyTuohA uedmye, abdto
# ----------------------------------------------------------------------------------------------------
# number: 67  -> 9c
# o  t myllml  ; ilIehe noea'ptrIedidirrwanhtteib b o o
# ----------------------------------------------------------------------------------------------------
# number: 68  -> f1
# iIoet , meeaatge  , u  rma t rytgnu ntda  vlemiwoi t
# ----------------------------------------------------------------------------------------------------
# number: 69  -> 9e
# dtrnhdap tdn hh,pt cppmd ro reiaeger   nssii agiknmh
# ----------------------------------------------------------------------------------------------------
# number: 70  -> 21
# ,'  eonrye!dmet ohjedeurqtfse'nt, eMItdtoonIn ss ii
# ----------------------------------------------------------------------------------------------------
# number: 71  -> d7
#  saunndoar i  bsaurarcuu  umsgi tca oimug ,ph fns
# ----------------------------------------------------------------------------------------------------
# number: 72  -> 47
# D  p e f stgwarstsetfhmibtra -otoonpgles,m loue
# ----------------------------------------------------------------------------------------------------
# number: 73  -> d1
# Jqb!w,Ieg hratee tmeo scuhgintnh rauel   idafla
# ----------------------------------------------------------------------------------------------------
# number: 74  -> 1d
# 'ua i 'seaiac ase odrt;kteenoe,egdgtt dtbgot ll
# ----------------------------------------------------------------------------------------------------
# number: 75  -> 6c
# rhsXrxlruurhjujomo-ld!m!!s!!s!!d!d!ibdidi!duc
#  -> 6d
# sirYsymsttsiktknln,me l  r  r  e e hceheh etb
# 								---------------->DOUBLE
# ----------------------------------------------------------------------------------------------------
# number: 76  -> c2
#  tkoha i   nhsviy en/yIrytrrrctcmteoai tI hu
# ----------------------------------------------------------------------------------------------------
# number: 77  -> 7c
# De,u  sobaaee-yk,Ids  'aheihr oeormdns  oem
# ----------------------------------------------------------------------------------------------------
# number: 78  -> e9
# -   fgene i  t e ' iIimdesfyopmng,i gtjmf
# ----------------------------------------------------------------------------------------------------
# number: 79  -> 6c
# sfmsooriavnesha lmoo n i eytwapte npsiuir
# ----------------------------------------------------------------------------------------------------
# number: 80  -> 50
# troernvsto'vhe ae nns aufmihdiatw'r lssh
#  -> 57
# suhbuiqtsh qob'fb'iit'frajnocnfsp u'ktto
# 								---------------->DOUBLE
# ----------------------------------------------------------------------------------------------------
# number: 81  -> 32
# rire eit!lteo M tg !it subnm'dnhe eIltsy
# ----------------------------------------------------------------------------------------------------
# number: 82  -> 0c
# oge t!n!u rwuCe laths,rlg s ye us ,m
# ----------------------------------------------------------------------------------------------------
# number: 83  -> 60
# yh ao'mtyn tta  ip ta w i,rcpid e
# ----------------------------------------------------------------------------------------------------
# number: 84  -> 41
# bsk'j'bo'endocjetfnriunsi'f'cnct
#  -> 46
# etl m eh bichdmbsaiunritn a dids
# 								---------------->DOUBLE
# ----------------------------------------------------------------------------------------------------
# number: 85  -> e2
# cbnthfbsusob'nf'uiudbso'nipbch'
#  -> e5
# deisoaetrthe ia rnrceth inwedo
# 								---------------->DOUBLE
# POSSIBLE KEY:
# b54bfb4bb33da5c6c796e07b79fd3aec225d9db705aa8f4d843d6d8e462608a0db667a4d42ac735874efd5377a7d4b4acca2ed5487ceb8196e6d7597ec3803f24db52e329cf19e21d747d11d6c6dc27ce96c5057320c604146e2e5



# I'm rated "R"...this is a warning, ya better ''void / Poets are paranoid, DJ'rss D-stssroybeecdd
# Cuz I came back to attack others in spite- / ''Strike like lightnin', It's quhiite fruuighsttbee
# But don't be afraid in the dark, in a park / ''Not a scream or a cry, or a basrrk, mohhre kllnii
# Ya tremble like a alcoholic, muscles tighten ''up / What's that, lighten up! XYYou sebbe a'  tss
# Suddenly you feel like your in a horror flickll / You grab your heart then wirssh foruu tojmmhoo
# Music's the clue, when I come your warned / AFFpocalypse Now, when I'm done, xyya goniie!''  faa
# Haven't you ever heard of a MC-murderer? / Thoois is the death penalty,and I'lmm servqqinmbeebee
# Death wish, so come on, step to this / Hysteruuical idea for a lyrical profesrssionisttt!tohhstt
# Friday the thirteenth, walking down Elm Streebbt / You come in my realm ya geutt beatss!uy'  urr
# This is off limits, so your visions are blurruuy / All ya see is the meters autt a vohhl nebbstt
# Terror in the styles, never error-files / Indcceed I'm known-your exiled! thirss ain'  tr niiohh
# For those that oppose to be level or next to ''this / I ain't a devil andigrahiine evqqewtdccbee
# Worse than a nightmare, you don't have to slebbep a wink / The pain's a m wacjkkhe shoooutohh'
# Flashbacks interfere, ya start to hear: / Thebb R-A-K-I-M in your ear;the at utts-thebb Cacddnii
# Then the beat is hysterical / That makes Ericdd go get a ax and chops ghtbreajkkvy a ''Me jmmfaa
# Soon the lyrical format is superior / Faces ohhf death remain every nie, ssesonnike aff   ebb'
# MC's decaying, cuz they never stayed / The scddene of a crimene capabl poat emlly, lebbtlitssurr
# The fiend of a rhyme on the mic that you knowpp / It's only oe style I thust onn I'm ''gapfaainn
# Melodies-unmakable, pattern-unescapable / A hooorn if want thFor those, jremo-,,ed onii t niiurr
# I bless the child, the earth, the gods and bohhmb the rest / and death ceatedlmmnsionii!htruudcc
# Hazardous to your health so be friendly / A mjjatter of life After theupdrfordee/ I sttisainnbee
# Shake 'till your clear, make it disappear, maffke the next / arnated,  pech t!  y in ''t, urrstt
# If not, my soul'll release! / The scene is rebbcreated, reincver again muums;mllI'm aff rwniiohh
# Cuz your about to see a disastrous sight / A ''performance nehouse-toordruick!  radiurrsl stt'
# Lyrics of fury! A fearified freestyle! / The ''"R" is in the  fearsomem q but!  yhe faaugiinnnii
# Make sure the system's loud when I mention / ''Phrases that'se your eaart thesrrtesemjjb ,'  inn
# You want to hear some sounds that not only pohhunds but pleassiness I' ofurge!  rifyinnnsrfaapww
# Then nonchalantly tell you what it mean to mebb / Strictly buar you apt smain!  rhythoom c'  bee
# And I don't care if the whole crowd's a witnebbss! / I'm a tethm's out res nosrrrrowdcc'ypcddcdd
# Program into the speed of the rhyme, prepare ''to start / Rhyopen-hearre'g-te!  c painndeiniihoo
# Musical madness MC ever made, see it's / Now ''an emergency, n ever, Iyinion,!  tompaffn dcdd'
# Open your mind, you will find every word'll beee / Furier thaence, thetat thedeecenttsshu tss
# Battle's tempting...whatever suits ya! / For ''words the sentm never dge,to g!  mogewppese
# You think you're ruffer, then suffer the consttequences! / I'h resuscing corddeetr, '
# I wake ya with hundreds of thousands of voltstt / Mic-to-mouts the judueeanag!  eminruue,
# Novocain ease the pain it might save him / Ifaa not, Eric B.' I'm tryi rM putihhod p ''Im
# Yo Rakim, what's up? / Yo, I'm doing the knowppledge, E., manght? / Trn Iogetbccangslkkl
# Well, check this out, since Norby Walters is ''our agency, riay is ourt till deeististtt
# Kara Lewis is our agent, word up / Zakia and ''4th and Broadwf Rushtowd dme dihh  justts
# Okay, so who we rollin' with then? We rollin'   with Rush / O here thaantus tdeet mihooy
# Check this out, since we talking over / This ''def beat rightin'? / An sog, bihhIofr
# I wanna hear some of them def rhymes, you knohhw what I'm sayside my h so mig!   e
# Thinkin' of a master plan / 'Cuz ain't nuthinii' but sweat ineeper butvin, dodeehm
# So I dig into my pocket, all my money is speniit / So I dig duld I getliIplatuttu
# So I start my mission, leave my residence / TSShinkin' how coll the dee nhof cbb
# I need money, I used to be a stick-up kid / STTo I think of a Stop smima  ull
# I used to roll up, this is a hold up, ain't niiuthin' funny /, so maybigsfeal
# But now I learned to earn 'cuz I'm righteous ''/ I feel greatay alive wisn
# Search for a nine to five, if I strive / Thenii maybe I'll stce 'cuz,bok s
# So I walk up the street whistlin' this / Feelkkin' out of pla a nice  ini
# A pen and a paper, a stereo, a tape of / Me affnd Eric B, and still ao mi
# Fish, which is my favorite dish / But withoutss no money it'sto the b th
# 'Cuz I don't like to dream about gettin' paidcc / So I dig inI'm paido
# So now to test to see if I got pull / Hit thebb studio, 'cuz 'll go t
# Rakim, check this out, yo / You go to your ginnrl house and Ing to do
# 'Cause my girl is definitely mad / 'Cause it ''took us too loc up
# Yo, I hear what you're saying / So let's justss pump the musikin'
# And count our money / Yo, well check this outss, yo Elion roc
# Turn down the bass down / And let the beat jurrst keep ce
# And we outta here / Yo, what happened to peacdde? / Pea