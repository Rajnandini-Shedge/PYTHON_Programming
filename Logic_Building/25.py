#accept number from user and print first 5 multiple of number  

def DisplayMultiple(No):

    for i in range(1,6):
            print( i * No ,end=" ")

def main():
    Value = int(input("Enter the number : "))
    DisplayMultiple(Value)

if __name__ == "__main__":
    main()