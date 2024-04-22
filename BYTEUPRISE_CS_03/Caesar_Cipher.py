# Aditya Mandwekar 
# Task 03: Develop a Python script capable of encoding and decoding text using the Caesar Cipher algorithm. Enable users to input a message and a shift value to carry out both encryption and decryption processes effortlessly.
# Code:

def caesar_cipher(text, shift, mode):
  
# This function performs Caesar cipher encryption or decryption.

# The Arguments used are :
#      text: The text to be encrypted or decrypted.
#     shift: The number of positions to shift the letters.
#      mode: "encrypt" or "decrypt"

# Returns: The encrypted or decrypted text.

  alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
  result = ''
  for char in text:
    if char in alphabet:
      new_index = (alphabet.find(char) + shift) % len(alphabet)
      result += alphabet[new_index]
    else:
      result += char
  return result

def main():

# This function gets user input and performs encryption or decryption.
  
  while True:
    print("Caesar Cipher")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")
    choice = input("Enter your choice (1-3): ")

    if choice == '1':
      mode = "encrypt"
    elif choice == '2':
      mode = "decrypt"
    elif choice == '3':
      break
    else:
      print("Invalid choice. Please try again.")
      continue

    text = input("Enter your message: ")
    shift = int(input("Enter the shift value: "))

    result = caesar_cipher(text, shift, mode)
    if mode == "encrypt":
      print("Encrypted text:", result)
    else:
      print("Decrypted text:", result)

if __name__ == "__main__":
  main()
