# Write a program which accept range from user and display all even numbers in between that range. 

def RangeDisplayEven(No1,No2):

    if No1 > No2 :
        print("Invalid Range")

    for i in range(No1,No2+1):
        if i % 2 == 0:
            print(i , end = " ")
        
def main():
    Value1 = int(input("Enter the first number : "))
    Value2 = int(input("Enter the second number : "))
        
    RangeDisplayEven(Value1, Value2)

if __name__ == "__main__":
    main()