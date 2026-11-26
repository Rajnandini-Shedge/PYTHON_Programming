#.Write a program which accept range from user and display all numbers in between that range. 

def RangeDisplay(No1,No2):

    if No1 > No2 :
        print("Invalid Range")

    for i in range(No1,No2+1):
        print(i , end = " ")
        
def main():
    Value1 = int(input("Enter the first number : "))
    Value2 = int(input("Enter the second number : "))
        
    RangeDisplay(Value1, Value2)

if __name__ == "__main__":
    main()