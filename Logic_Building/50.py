#Write a program which accept accept range from user and display all numbers in between that range in reverse order. 

def DisplayRangeRev(No1,No2):

    if No1 > No2 :
        print("Invalid range") 

    Sum = 0
    for i in range(No2,No1-1,-1):
        print(i , end = " ")

def main():
    Value1 = int(input("Enter the first number : "))
    Value2 = int(input("Enter the second number : "))
        
    DisplayRangeRev(Value1, Value2)

if __name__ == "__main__":
    main()