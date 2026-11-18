#Accept two numbers from user and display first number in second 
#number of times. 

def Display(No1,No2):
    for i in range(No2):
        print(No1 , end = " ")
        
def main():
    Value1 = int(input("Enter the number to print : "))
    Value2 = int(input("Enter the number(how many times) : "))
    Display(Value1,Value2)

if __name__ == "__main__":
    main()