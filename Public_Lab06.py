def print_menu():
    print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit ")

def encoder(password):
    emp_str = ""
    for i in range(len(password)):
        a = int(password[i])
        b = a + 3
        b = str(b)
        emp_str += b
    return emp_str

def decoder(encoded_password):
    password = ""
    for i in range(len(encoded_password)):
        a = int(encoded_password[i])
        b = a + 3
        b = str(b)
        password += b
    return password

def main():
    while True:
        print_menu()
        print("Please enter an option:", end = ' ')
        option = int(input())
        if option == 1:
            password = input("Enter your password to encode:")
            encoded_password = encoder(password)
            print("Your password has been encoded and stored!")
        if option == 3:
            break
if __name__ == '__main__':
    main()
