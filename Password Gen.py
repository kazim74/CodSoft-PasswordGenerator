import string
import random

def PassGen(len):
    
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    passw = ''.join(random.choice(all_characters) for _ in range(len))
    return passw

def main():
    valid_len = False

    while not valid_len:
        len_input = input("Enter length of your password: ")

        if len_input.isdigit():
            len = int(len_input)
            if len >= 6:
                valid_len = True
            else:
                print("Minimun length sould be 6!")
        else:
            print("Enter numeric value only!")

    passw = PassGen(len)
    print("Your password:", passw)

if __name__ == "__main__":
    main()
