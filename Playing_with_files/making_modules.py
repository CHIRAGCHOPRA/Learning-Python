import os
os.mkdir('dirs')
os.chdir('dirs')


filesObject=open('mod1.py','w')
filesObject.write('def heya1:\n\tprint("mod 1 is called")')
filesObject.close()

filesObject=open('mod2.py','w')
filesObject.write('def heya2:\n\tprint("mod 2 is called")')
filesObject.close()

filesObject=open('__init__.py','w')
filesObject.write('from mod1 import heya1\nfrom mod2 import heya2')