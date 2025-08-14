username_correct='corina'
password_correct='123456'

username_input=input('Insert username:')
password_input=input('insert password:' )

if username_input !=username_correct and password_input != password_correct:
    print('Access respins')
elif username_input !=username_correct or password_input != password_correct:
    print ('User/Password incorect')
else:
    print('Acces admis')