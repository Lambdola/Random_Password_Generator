import random as rd 


MINI_SEPARATION = "*" * 24
SEPARATION = MINI_SEPARATION * 3
EROOR_MESAAGE = "\n=> YOU NEED TO INPUT AN INTEGER <= "

password_template = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789!@#&"
length = len(password_template)

def Style(n):
    print(SEPARATION )
    print( f"●●● {n} ●●●".center(63, " "))
    print(SEPARATION )    
Style("RANDOM PASSWORD GENERATOR")

def randompasswordgenerator():
       
    password = ""
    
    try:
        n_char = int(input('>>>> How many characters do you want your random password to have: '))
    except:
           print(EROOR_MESAAGE)
           return randompasswordgenerator()
        
    
    try:
        n = int(input(">>>>> Enter any number greater than 0: "))
    except: 
        print(EROOR_MESAAGE)
        print(f"\n{MINI_SEPARATION}")
        return randompasswordgenerator()
      
    
    for x in range(n_char):
        
        id_no = rd.randint(0,(length-1))
       
        id_char = password_template[id_no]
       
        password += id_char
            
        
    print (f"=> Your Random {n_char} characters Password Is: ", password)
    print(f"\n{MINI_SEPARATION}")
   
    return rerun()
    
def rerun():
    return randompasswordgenerator()
    
rerun()
    
