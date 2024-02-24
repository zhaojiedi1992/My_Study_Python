import getpass

print("=")
user = input('Enter your username: ')
print("==")
passwd = getpass.getpass()

def svc_login(user, passwd):
   if user=='root' and passwd == '123456':
      return True
   else:
      return False
   
if svc_login(user, passwd):    # You must write svc_login()
   print('Yay!')
else:
   print('Boo!')