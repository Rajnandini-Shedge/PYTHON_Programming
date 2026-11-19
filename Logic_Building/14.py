# Convert Case of given character

def DisplayConvert(Char):
    Char = ord(Char)
    if Char >= 97 or Char <= 122:
        Capital = Char - 32
        print(chr(Capital))

    elif Char >= 65 or Char <= 90:
        Small = Char + 32
        print(chr(Small))

def main():
    Value = input("Enter Character : ")
    DisplayConvert(Value)

if __name__ == "__main__":
    main()