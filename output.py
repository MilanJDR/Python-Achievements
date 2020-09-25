>>> 2 + 2
4
>>> e * 10
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    e * 10
NameError: name 'e' is not defined
>>> 3 * 10
30
>>> 100 - 10
90
>>> 25 / 5
5.0
>>> 10 / 3
3.3333333333333335
>>> 10 // 3
3
>>> 
>>> # Verander <JOUW NAAM HIER> in je eigen naam
>>> naam = "Milan"
>>> print(naam)
Milan
>>> print(naam.upper())
MILAN
>>> print(naam[0:2])
Mi
>>> print(naam[::-1])
naliM
>>> #Verander dit in je eigen leeftijd
>>> leeftijd = 15
>>> print('Hallo ' + naam + ' ben je al ' + str(leeftijd) + 'jaar?')
Hallo Milan ben je al 15jaar?
>>> leeftijd = leeftijd + 1
>>> leeftijd
16
>>> leeftijd -= 1
>>> leeftijd
15
>>> if leeftijd < 18:
	hoelang_tot18jaar = 18 - leeftijd
	print('Over ' + str(hoelang_tot18jaar) + ' jaar geleden dat 18 werd ;-)')
	elif leeftijd > 18:
		
SyntaxError: invalid syntax
>>> elif leeftijd > 18:
	
SyntaxError: invalid syntax
>>> else:
	
SyntaxError: invalid syntax
>>> # Willekeurige getallen genereren
>>> from random import randint
>>> randint(0,1000)
876
>>> wellekeurig_getal = randint(0,1000)
>>> wellekeurig_getal
659
>>> print('willekeurig getal tussen 0 en 1000: ' + str(wellekeurig_getal))
willekeurig getal tussen 0 en 1000: 659
>>> 
>>> 
>>> 3.
3.0
>>> 
>>> # Datum en tijd
>>> from datetime import datetime
>>> datum = datetime
>>> datum = datetime.now()
>>> print(datum)
2020-09-25 11:56:29.767907
>>> datum.strftime('%A %d %B
	       

>>> datum.strftime('%A %d %B %Y')
'Friday 25 September 2020'
>>> # Nu in een andere taal
>>> import locale

>>> locale.setlocale(locale.LC_TIME, 'nl_NL')
'nl_NL'
>>> datum.strftime
<built-in method strftime of datetime.datetime object at 0x035D9FE0>
>>> datum.strftime('
	       
>>> datum.strftime('%A %d %B %Y')
'vrijdag 25 september 2020'
>>> locale.setlocale(locale.LC_TIME, 'it_IT')
'it_IT'
>>> datum.strftime('%A %d %B %Y')
'venerdì 25 settembre 2020'
