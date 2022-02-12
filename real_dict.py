'''
Foydalanuvchidan biror so'z kiritishni so'rang va so'zning tarjimasini yuqoridagi 
lug'atdan chiqarib bering. 
Agar so'z lu'gatda mavjud bo'lmasa, "Bunda so'z mavjud emas" degan xabarni chiqaring.
'''

py_dict = {
    'int' : 'but',
    'float' : 'suzuvchi',
    'str' : 'qator',
    'bool' : 'mantiq',
    'def' : 'funksiya ta`rifi',
    'print' : 'chop etmoq',
    'for' : 'uchun',
    'if' : 'agar',
    'elif' : 'agar-aksincha',
    'else' : 'aks holda'
}

require = input('type requared word: ')
if require:
    if require in py_dict:
        print( 'translation of word you asked for: ' + py_dict[require])
    else:
        print( 'this wor is not found in the dictionary - py_dict!')
else:
    print('you did not type any word!')