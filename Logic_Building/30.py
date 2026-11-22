#Display table in reverse

def RevTable(No):
    if No < 0:
        No = -No

    table = 1

    for i in range(10,0,-1):
        print(i*No , end = " ")
        

def main():
    Value = int(input("Enter the number :"))
    RevTable(Value)
if __name__ == "__main__":
    main()