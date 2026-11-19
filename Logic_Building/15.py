#Check whethwe char is vowel or not

def ChkVowel(char):

    if (char == "a" or char == "A" or char == "e" or char == "E" or char == "i" or char == "I" or
    char == "o" or char == "O" or char == "u" or char == "U"  ):
        return True
    else:
        return False

def main():
    Char = input("Enter Character : ")
    Ret = ChkVowel(Char)

    if Ret == True:
        print("Character is vowel")
    else:
        print("Character is not a vowel")

if __name__ == "__main__":
    main()