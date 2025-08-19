username=input('Insert username:')
password=input('insert password:' )

if username =='corina' and password == '123456':
    print('Access permis')
elif username =='corina' and password != '123456':
    print ('User/Password incorect')
elif username !='corina' and password == '123456':
    print ('User/Password incorect')
else:
    print('Acces respins')