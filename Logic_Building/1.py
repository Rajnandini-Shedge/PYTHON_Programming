def Divide(No1 , No2):
    if(No2 == 0):
        return - 1

    Ans = No1/No2
    return Ans

def main():
    Value1 = int(input("Enter First Number :")) 
    Value2 = int(input("Enter second Number :"))
    Ret = Divide(Value1 , Value2)

    print(f'{Value1} divided by {Value2} is : ',Ret)

if  __name__ == "__main__":
    main()