from getpass import getpass

# variables
username = ''
password = ''
date_of_birth= ''
password_strength = 8
conditions = {'length':True,'English-letters':True,'specific_letters':True,'english_uppercase':True,'equal_to_username':True,'swapcase':True, 'username_with_SPECIAL_CHARACTERS':True,'CONVENTIONAL_PASSWORDS':True}

# constants
CONVENTIONAL_PASSWORDS = ("123456", "12345678", "12345", "111111", "123456789","qwerty", "asdfgh", "zxcvbnm","password", "admin","P@s$w0rd")
SPECIAL_CHARACTERS = ( "@", "$","!")
ENGLISH_LETTERS = ("abcdefghijklmnopqrstuvwxyz")
ENGLISH_UPPERCASE_LETTERS = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
PASSWORD_HINT = {'length':{True:'Password length is sufficient.', False :'Password is shorter than 8 characters.'},
                'English-letters':{True:'Password Contains at least one English letter.', False :'Password does not contain any English letters.'},
                'specific_letters':{True:'Password Contains at least one special character', False:'Password does not contain any special characters.'},
                'english_uppercase':{True:'Password Contains at least one uppercase letter.',False:'Password does not contain any uppercase letters.'},
                'equal_to_username':{True:'Password is not identical to the username.',False:'Password is identical to the username.'},
                'swapcase':{True:'Password is not the swapcase version of the username. ',False:'Password is the swapcase version of the username.'},
                'username_with_SPECIAL_CHARACTERS':{True:'Password is not a special-character version of the username. ',False:'Password is a special-character version of the username.'},
                'CONVENTIONAL_PASSWORDS':{True:'Password is Not a common password',False:'Password is one of the most common passwords.'}
                }

while not username.strip()  :
        username = input('Please enter your username:')
        if not username.strip() :
          print('⚠️ Username cannot be empty. Please try again.')  

# used getpass for extra activity
while not password.strip() :
    password = getpass('Please enter your password:')
    if not password.strip() :
        print('⚠️ password cannot be empty. Please try again.')  

while not date_of_birth.strip() :
    date_of_birth = input('Please enter your full date of birth:')
    if not date_of_birth.strip() :
        print('⚠️ date of birth cannot be empty. Please try again.')  

#1 check the length of the password
if len(password) <8 :
        password_strength -=1
        conditions['length'] = False

# 2 check if password includes at least one english character
for char in ENGLISH_LETTERS :
    if char in password :
        break
else :
    password_strength -=1       
    conditions['English-letters'] = False
#3 check if password includes at least one of specific character
for char in SPECIAL_CHARACTERS :
    if char in password :
        break
else:    
    password_strength -=1
    conditions['specific_letters'] = False
# 4 check if password includes at least one uppercase english character
for char in ENGLISH_UPPERCASE_LETTERS :
    if char in password :
        break
else :
    password_strength -=1       
    conditions['english_uppercase'] = False
#5 check if username is equal to password
if password == username :
    password_strength -=1   
    conditions['equal_to_username'] = False 
#6 check if username is swapcase of password    
if password.swapcase() == username:
    password_strength -=1      
    conditions['swapcase'] = False 
#7 check if password is equal to username with specific characters
if username.replace('a','@') ==  password  or username.replace('i','!') ==  password or username.replace('s','$') ==  password or username.replace('o','0') ==  password :
    password_strength -=1   
    conditions['username_with_SPECIAL_CHARACTERS'] = False 
# 8 check if password is equal to conventional passwords
if password in CONVENTIONAL_PASSWORDS :
    password_strength -=1       
    conditions['CONVENTIONAL_PASSWORDS'] = False 

#output of the program 
print(f'Username:{username}')
print(f'Password:{password}', end='\n\n')
print('✅ Filter checks:')
for key,value in conditions.items():
    checkmark = '✅' if value else  '❌'
    print(f'{checkmark} {PASSWORD_HINT[key][value]}')
print(f'\n🔐 Final Score: {password_strength} out of 8 ')
if password_strength >= 7 :
    print('🔒 Security Level: Strong \n🎉 Congratulations! Your password is highly secure and passed all security checks.')
elif password_strength >= 4 :
    print('🔒 Security Level: Medium \n 📌 Tip: Your password is fairly secure, but try to avoid using patterns based on your username.')
else :
    print('🔒 Security Level: Very Weak \n📌 Tip: Your password is too simple and easy to guess. Use a mix of letters, numbers, and symbols.')    

#extra activity for date of birth check
if date_of_birth in password : 
    print("🔐 For better security, avoid using your date of birth in your password.")   