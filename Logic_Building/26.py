# Write a program which accept number from user and
#if number is less than 50 then print small ,
#if it is greater than 50 and less than 100 then print medium, 
#if it is greater than 100 then print large.

def Display(No):

    if No < 0 :
        No = -No

    if (No < 50):
        print("Small Number")
    elif(No > 50 and No < 100):
        print("Medium Number")
    else:
        print("Large Number")

def main():
    Value = int(input("Enter the number : "))

    Display(Value)

if __name__ == "__main__":
    main()