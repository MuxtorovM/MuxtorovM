dict = {'float' : 'o`nlik'}
require = input('type a required word: ')
if require:
    if require in dict:
        print( 'translation the above word is \'' + dict[require] + '\'')
    else:
        print( 'you typed a mistaken word or this word is not found in the dict')
else:
    print('you did not type any word')