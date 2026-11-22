#Display table 

def Table(No):
    if No < 0:
        No = -No

    table = 1

    for i in range(1,11):
        print(i*No , end = " ")
        

def main():
    Value = int(input("Enter the number :"))
    Table(Value)
if __name__ == "__main__":
    main()