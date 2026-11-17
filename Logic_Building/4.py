def Divide(No1 , No = 5):
    if No1%No == 0 :
        return True
    else:
        return False
    
def main():
    Value = int(input("Enter First Number :")) 
    Ret = Divide(Value)

    if Ret == True:
        print(f"{Value} is divisible by 5")
    else:
        print(f"{Value} is not divisible by 5")
        

if  __name__ == "__main__":
    main()