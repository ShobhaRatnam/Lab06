def print_menu():
    print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit ")#The menu

def encoder(password):
    emp_str = ""
    for i in range(len(password)):
        a = int(password[i])#Takes each character from string and converts it to an integer and adds three
        b = a + 3
        b = str(b)
        emp_str += b
    return emp_str

def decoder(encoded_password):
    password = ""
    for i in range(len(encoded_password)): #Takes every character from string, converts to interger and subtracts three.
        a = int(encoded_password[i])
        b = a - 3
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
            print("Your password has been encoded and stored!")#Encodes and stores the password
        if option == 2:
            decoded_password = decoder(encoded_password) #Decodes the encoded password
            print(f" The encoded password is {encoded_password}, and the original password is {decoded_password})
        if option == 3:
                  
         
            
            
            break
if __name__ == '__main__':
    main()
