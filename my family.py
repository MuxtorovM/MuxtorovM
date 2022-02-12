'''
otam (onam, akam, ukam, va hokazo) degan lug'at yarating 
va lug'atga shu inson haqida kamida 3 ta m'alumot kiriting 
(ismi, tu'gilgan yili, shahri, manzili va hokazo). Lug'atdagi 
ma'lumotni matn shaklida konsolga chiqaring :Otamning ismi 
Mavlutdin, 1954-yilda, Samarqand viloyatida tug'ilgan
'''
otam = {
    'ism' : 'Ahror',
    't_yil' : 1974,
    't_shahar' : 'G\'ijduvon',
    'manzil' : 'Qorovulbozor tumani'
}

onam = {
    'ism' : 'Muqaddas',
    't_yil' : 1974,
    't_shahar' : 'G\'ijduvon',
    'manzil' : 'Qorovulbozor tumani'
}

ukam = {
    'ism' : 'Asrorjon',
    't_yil' : 2001,
    't_shahar' : 'G\'ijduvon',
    'manzil' : 'Qorovulbozor tumani'
}

ukam2 = {
    'ism' : 'G\'olibjon',
    't_yil' : 2005,
    't_shahar' : 'G\'ijduvon',
    'manzil' : 'Qorovulbozor tumani'
}

print('Otamning ismi ' + otam['ism'] + ', tug\'ilgan yili: ' + str(otam['t_yil']) + ',\n'
 'tug\'ilgan shahri: ' + otam['t_shahar'] + ', istiqomat qiladi: ' + otam['manzil'] + 'da.')

print('Onamning ismi ' + onam['ism'] + ', tug\'ilgan yili: ' + str(onam['t_yil']) + ',\n'
 'tug\'ilgan shahri: ' + onam['t_shahar'] + ', istiqomat qiladi: ' + onam['manzil'] + 'da.')

print('ukamning ismi ' + ukam['ism'] + ', tug\'ilgan yili: ' + str(ukam['t_yil']) + ',\n'
 'tug\'ilgan shahri: ' + ukam['t_shahar'] + ', istiqomat qiladi: ' + ukam['manzil'] + 'da.')

print('ukamning ismi ' + ukam2['ism'] + ', tug\'ilgan yili: ' + str(ukam2['t_yil']) + ',\n'
 'tug\'ilgan shahri: ' + ukam2['t_shahar'] + ', istiqomat qiladi: ' + ukam2['manzil'] + 'da.')