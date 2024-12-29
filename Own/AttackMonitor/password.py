import hashlib
import getpass
from zxcvbn import zxcvbn #for checking password strength
from nmap import nmap 



#_____________ACCOUNT___________________
account = {} #users account
time_to_break:int #time it took to break the password.
def create_account()->dict:
    # Get the username and password

    username = input("Enter your username: ")
    while len(username)<=2:
        username = input("Re-enter your username: ")
    password = create_password()
    if(strong_password(password)):
        print("Strong password")
    else:
        print("Password is too weak")
        password = create_password()
    # Hash the password
    hashed_password = hashlib.sha256(password.encode()).hexdigest() #encrypt and hash the passwor to 256 bits
    #create our account
    account[username]=hashed_password
    
    return account


def create_password()->str:

    Password = getpass.getpass("Please enter your password: ")
    while len(Password)<=2:
        Password = getpass.getpass("Please re-enter your password: ")        
    return Password
 

def login()->bool:
    username = input("Please enter user name:")
    Password = getpass.getpass("Please enter your password: ")
    hashed_password = hashlib.sha256(Password.encode()).hexdigest() #encrypt and hash the passwor to 256 bits
    for user in account: #iterate from all possible accounts
        print(user)
        if username == username and account[username] == hashed_password: #We have found a user in our account log
            return True
    return False

def strong_password(password:str )->bool:
    information = zxcvbn(password) #check the password strength
    print(f"Score: {information['score']} (0 = weak, 4 = strong)")
    print(f"Crack Time (Online): {information['crack_times_display']['online_no_throttling_10_per_second']}") #How long would i take to crack it
    #print(f"Suggestions: {information['feedback']['suggestions']}")

    if(information["score"]>=3): #sufficient password
        print("Sufficient password")
        return True
    return False





#__________________CHECK PORT__________________


def main():
    account =create_account()
    Login_success = login() #try to log in 
    if(Login_success):
        print("Login succeeded")
    else:
        print("Login succeeded")


if __name__ == "__main__":
    main()