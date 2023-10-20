import random
import string

def generate_password(length):
    characters = {'letters': string.ascii_letters, 'digits': string.digits, 'punctuation': string.punctuation}
    password = ''.join(random.choice(''.join(characters.values())) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator App!")
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                print("Please enter a valid length (greater than 0).")
                continue
            password = generate_password(length)
            print("Generated Password:", password)
        except ValueError:
            print("Please enter a valid integer length.")
        choice = input("Do you want to generate another password? (yes/no): ")
        if choice.lower() != 'yes':
            print("Thank you for using the Password Generator App!")
            break

if __name__ == '__main__':
    main()
    