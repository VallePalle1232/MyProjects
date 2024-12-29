import hashlib
import getpass
from zxcvbn import zxcvbn #for checking password strength

import tkinter as tk
from tkinter import messagebox
from tkinter.simpledialog import askstring
from zxcvbn import zxcvbn

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


#______Check status of computer________
def check_status(): #TODO
    pass


#__________________CHECK PORT__________________
def port_scan():
    """Scan ports on a target IP."""
    target_ip = askstring("Port Scanner", "Enter target IP:")
    if not target_ip:
        return

def main():
    account =create_account()
    Login_success = login() #try to log in 
    if(Login_success):
        print("Login succeeded")
    else:
        print("Login succeeded")


#Tkinter buttons

# Main GUI window
root = tk.Tk()
root.title("Security Toolkit")
root.geometry("600x400")
root.resizable(False, False)

# Create a frame for layout
main_frame = tk.Frame(root, padding="20")
main_frame.pack(fill="both", expand=True)

# Title label
title_label = tk.Label(main_frame, text="Security Toolkit", font=("Helvetica", 24), anchor="center")
title_label.pack(pady=20)

# Create a grid layout for buttons
button_frame = tk.Frame(main_frame)
button_frame.pack(fill="both", expand=True, pady=10)

# Buttons for functionalities
tk.Button(button_frame, text="Create Account", command=create_account, width=25, height=2, font=("Helvetica", 14)).grid(row=0, column=0, padx=20, pady=10)
tk.Button(button_frame, text="Login", command=login, width=25, height=2, font=("Helvetica", 14)).grid(row=0, column=1, padx=20, pady=10)
tk.Button(button_frame, text="Port Scanner", command=port_scan, width=25, height=2, font=("Helvetica", 14)).grid(row=1, column=0, padx=20, pady=10)
tk.Button(button_frame, text="Status Check", command=check_status, width=25, height=2, font=("Helvetica", 14)).grid(row=1, column=1, padx=20, pady=10)

# Add some spacing for better layout
for i in range(2):
    button_frame.grid_rowconfigure(i, weight=1)
    button_frame.grid_columnconfigure(i, weight=1)

root.mainloop()



if __name__ == "__main__":
    main()