from cryptography.fernet import Fernet
'''def write_key():
    key = Fernet.generate_key()
    with open("passwords.txt", "wb") as key_file:
        key_file.write(key)'''
'''write_key()'''
def load_key():
    file = open("passwords.txt", "rb")
    key = file.read()
    file.close()
    return key
#master pwd= tin
master_pwd = input("What is the Master Password? ").lower()
if master_pwd == "tin":
    pass
else:
    print("Wrong Password")
    quit()
key = load_key() + master_pwd.encode()
fer = Fernet(key)
def view():
        with open('passwords.txt', 'r') as f:
            for line in f.readlines():
                data = line.rstrip()
                user, passw = data.split("|")
                print("User:", user, "password:", fer.decrypt(passw.encode()).decode())
def add():
    name = input("Account Name: ")
    pwd = input("Password: ")
    with open("passwords.txt", "a") as f:
         f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")
while True:
    mode = input("Would you like to (Add) new Account or (View) existing one?, press Q to quit: ").lower()
    if mode == "q":
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("invalid mode.")
        continue
