#Except single digit numner and print in in word

def Display(No):

    Words = ["Zero","One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]

    if No < 0 :
        No = -No

    if (No >= 10):
        print("Invalid Number")

    for i , value in enumerate(Words):
        if (i == No):
            print( value)

def main():
    Value = int(input("Enter the number : "))

    Display(Value)

if __name__ == "__main__":
    main()