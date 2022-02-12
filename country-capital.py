'''
Davlatlar va ularning poytaxtlari lug'atini tuzing. Avval lug'atdagi davlatlarni, 
keyin poytaxtlarni alohida-alohida, alifbo ketma-ketligida konsolga chiqaring.
'''
davlatlar = {
    "o'zbekiston":'toshkent',
    'aqsh':'washington d.c.',
    'rossiya':'moskva',
    'tojikiston':'dushanbe',
    "qirg'iziston":'bishkek',
    'qozog\'iston':'nursulton',
    'malayziya':'kuala-lumpur',
    'singapur':'sungapur',
    'italiya':'rim'
    }

print('davlatlar \n')
for davlat in sorted(davlatlar):
    print(davlat.title())

print(' \npoytaxtlar \n')
for capital in sorted(davlatlar.values()):
    print(capital.title())