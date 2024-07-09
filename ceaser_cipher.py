letters='abcdefghijklmnopqrstuvwxyz'
def cipher(text,mode,key):
    result=''
    if mode == 'd':
        key=-key
    for letter in text:
        if letter.isupper():
            flag=1
        else:
            flag=0
        letter=letter.lower()
        if not letter==' ' :
            index=letters.find(letter)
            if index == -1:
                result+=letter
            else:
                new_index=index+key
                if new_index>=26:
                    new_index-=26
                elif new_index<0:
                    new_index+=26
                if flag==1:
                    result+=letters[new_index].upper()
                else:
                    result+=letters[new_index]
        else:
            result+=' '
    return result

if __name__=='__main__':
    print("$$$  CAESAR CIPHER   $$$")
    print()
    print("What do you want to do?")
    print("""1. Encryption\n2. Decryption""")
    choice = input("Enter action(1/2): ")
    if choice=="1":
        print("Encryption mode selected")
        key=int(input("Enter Shift Value(1 to 26): "))
        if key in range(27):
            text=input("Enter text to encrypt: ")
            ciphertext=cipher(text,"e",key)
            print(f"Encoded text: {ciphertext}")
        else:
            print("Invalid key range")
    elif choice=="2":
        print("Decryption mode selected")
        key=int(input("Enter Shift Value(1 to 26): "))
        if key in range(27):
            text=input("Enter text to decrypt: ")
            plaintext=cipher(text,"d",key)
            print(f"Decoded text: {plaintext}")
        else:
            print("Invalid key range")
    else:
        print("Invalid option selected")