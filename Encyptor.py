from cryptography.fernet import Fernet
from termcolor import colored


# Technical Settings
global key
left = colored("[", 'red')
right = colored("]", 'red')
x = left + "+" + right
y = left + "!" + right
counter = 0
key = ""


print(colored("Hello user !", 'red') + "\nPlease choose one of the functions below :")
# Tries whole function and expect an error
try:
    # Determine if to decrypt or encrypt
    choise = int(input(left + "1" + right + " Encrypt a file\t\t" + left + "2" + right + " Decrypt a file\n"))
    while choise != 1 and choise != 2:
        choise = int(input(x + "Please use 1 or 2 only.\n" + y + str(3 - counter) + " more fails to abort."))
        counter + +1
        if counter == 3:
            quit()
    # Encrypting
    if choise == 1:
        try:
            # Determine weather to create a new key or use old one
            newFile = input(x + ' Do you wish to create a new key ?\n' + x + colored(' [Yes/No] ONLY !\n', 'red'))
            # Creating a new file
            if newFile.lower() == 'yes':
                key_hash = Fernet.generate_key()
                filename = input(x + ' Name key file : ')
                with open(filename, "wb") as keyfile:
                    keyfile.write(key_hash)
                    key = key_hash
                    keyfile.close()
            # Opening old key file
            elif newFile.lower() == 'no':
                filename = input(x + ' Enter key file name : ')
                with open(filename, "r") as keyfile:
                    key = keyfile.read()
                    keyfile.close()
            else:
                print(y + colored(' Wrong input. please try again later.', 'red'))
                quit()
        except ValueError as err:
            print(y + colored(' Something went wrong, please try again later.', 'red' + "\nError : " + err))
            quit()
        name = input(x + " Please enter the file you would like to encrypt : ")
        # Tries to encrypt and expect an error
        try:
            with open(name, "rb") as target_file:
                target = target_file.read()
                target_file.close()
            print(x + " STARTED ENCRYPTING " + name)
            fernet = Fernet(key)
            encrypted_file = fernet.encrypt(target)
            with open(name, "wb") as enc_file:
                enc_file.write(encrypted_file)
                enc_file.close()
            print(x + " " + colored(name, 'green') + " Was successfully encrypted !")
        except IOError as err:
            print(y + " Cant find file named " + name + "\nError : " + str(err))
    # Decrypting
    if choise == 2:
        name = input(x + " Please enter the file you would like to decrypt : ")
        filename = input(x + ' Enter key file name : ')
        # Tries to open key file
        try:
            with open(filename, "r") as keyfile:
                key = keyfile.read()
                keyfile.close()
        except IOError:
            print(y + " No such file as " + name)
        try:
            with open(name, "rb") as target_file:
                target = target_file.read()
                target_file.close()
            print(x + " STARTED DECRYPTING " + name)
            fernet = Fernet(key)
            decrypted_file = fernet.decrypt(target)
            with open(name, "wb") as dec_file:
                dec_file.write(decrypted_file)
                dec_file.close()
            print(x + " " + colored(name, 'green') + " Was successfully decrypted !")
        except IOError:
            print(y + " Cant find file named : " + name)
            quit()
except ValueError as v:
    print("\n" + x + " Something went wrong !\n" + str(v))