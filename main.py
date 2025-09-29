from pyscript import display, document
"""
def name(n):
    document.getElementById('out').innerHTML = " "
    n = document.getElementById('t1').value
    display(f'Hello {n}!', target="out")
"""
def data(d):
    document.getElementById('out').innerHTML = " "
    t1 = document.getElementById('t1').value
    n1 = document.getElementById('n1').value
    t2 = document.getElementById('t2').value
    uno = f'|| Name : \t{t1}'
    dos = f'\n|| Age : {n1}'
    tres = f'\n|| School : {t2}'
    mult = f'''{uno}\t 
    {dos}\t 
    {tres}'''
    display(f'{mult}', target="out")
    print(mult)
    display(f'Your name is {t1}, at {n1} years old, studying in {t2}. ', target="word")
"""
print(mult)

s1 = 'Harvey\'s Umbrella \nis pink'
l = 'pnuemonoultramicroscopicsilicovolcanoconiosis'
print(l[44])
print(len(l))
name  = "  Bruce Wayne  "
print(name.strip())
section = ['Emerald', 'Ruby', 'Sapphire', 'Topaz']
sec = 'The sections in Junior High School are '
print(sec, ','.join(section))
old = 'Like Ice Cream'
print(old.replace('Ice Cream', 'Pizza'))
vito_fav_book = 'harry potter by j.k. rowlings'
print(vito_fav_book.capitalize())
print(vito_fav_book.title())
print(vito_fav_book.lower())
print(vito_fav_book.upper())
print(vito_fav_book.swapcase())
"""