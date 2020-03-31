import random
import string
import re
 
# uchars = Uppercase charaters
# lchars =  Lowercase charaters
# dchars = Digits
# schars = Punctuation or Special Charaters

# generates five uppercase, 5 lowercase, 3 digits and 2 punctuation
#print('Your Random String-2:', get_random_string(5, 5, 3, 2))

class CustomPasswordGenerator:

    def get_random_string(self,uchars = 3, lchars = 3, dchars = 2, schars = 2):
        # Generates a 10 characters long random string
        # with 3 upper case, 3 lowe case, 2 digits and 2 special characters
    
        str_uchars, str_lchars, str_dchars, str_schars = '', '', '', ''
    
        for i in range(uchars):
            str_uchars += random.SystemRandom().choice(string.ascii_uppercase)
    
        for i in range(lchars):
            str_uchars += random.SystemRandom().choice(string.ascii_lowercase)
    
        for i in range(dchars):
            str_uchars += random.SystemRandom().choice(string.digits)
    
        for i in range(schars):
            str_uchars += random.SystemRandom().choice(string.punctuation)
    
        random_str = str_uchars + str_lchars + str_dchars + str_schars
        random_str = ''.join(random.sample(random_str, len(random_str)))
        return random_str

    def get_random_string2(self,length="8"):
        alphabet = string.ascii_letters + string.digits
        password = ''.join(random.choice(alphabet) for i in range(int(length))) # for a n-character password
        return password

    def is_valid_password(self,password):
        #r"^(?=.*[\d])(?=.*[A-Z])(?=.*[a-z])(?=.*[@#$])[\w\d@#$]{6,12}$"
        #r"^(?=.*[\d])(?=.*[A-Z])(?=.*[a-z])[\w\d@#$]{8,}$"
        
        # Add any special characters as your wish I used only #@$
        if re.match(r"^(?=.*[\d])(?=.*[A-Z])(?=.*[a-z])[\w\d@#$]{8,}$", password):
            return True
        
        return False