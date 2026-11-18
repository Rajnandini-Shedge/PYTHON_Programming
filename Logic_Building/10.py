#Accept number from user and check whether number is even or 
#odd. 

def ChkEvenOdd(No):

    if No % 2 == 0:
        return True
    else:
        return False

def main():
    value = int(input("Enter number : "))
    Ret = ChkEvenOdd(value)

    if Ret == True:
        print("Number is even")
    else:
        print("Number is odd")

if __name__ == "__main__":
    main()