def text_to_binary(text):
    # Convert each character to its ASCII binary equivalent
    binary = ' '.join(format(ord(char), '08b') for char in text)
    return binary

def binary_to_text(binary):
    # Split binary string into 8-bit chunks and convert each to character
    text = ''.join(chr(int(b, 2)) for b in binary.split())
    return text

def main():
    print("Choose an option:")
    print("1. Text to Binary")
    print("2. Binary to Text")
    choice = input("Enter 1 or 2: ")

    if choice == '1':
        text = input("Enter text to convert to binary: ")
        print("Binary code:", text_to_binary(text))
    elif choice == '2':
        binary = input("Enter binary code to convert to text: ")
        print("Text:", binary_to_text(binary))
    else:
        print("Invalid choice, please select 1 or 2.")

if __name__ == "__main__":
    main()
