#HYBRID APPLICATION
ChkEven=lambda No:(No % 2 == 0)  #Functional
    
def main():                      #Procedural
    Value=int(input("Enter number:"))
    Ret=ChkEven(Value)           #Ret=(Value%2==0)

    if(Ret==True):  
        print("Number is Even")
    else:s
        print("Number is Odd")


if __name__=="__main__":
    main()