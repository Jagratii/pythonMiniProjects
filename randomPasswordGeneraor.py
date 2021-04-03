
## random password generator for given length containing first alphabate capital
## and conataining one digit and one special character

import random
import string

if __name__ == "__main__":
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation

    length = int(input("Enter length of password : "))

    password = random.choice(s2)
    

    s=random.choice(s3)+random.choice(s4)

    for x in range(0,length-3):
        ch_ar = random.choice(s1)
        s+= ch_ar
    
    password = password + ''.join(random.sample(s, length-1))

    print("Your password is : ")
    print(password)
     

