#Accpet number and display favtor in reverse order
def FactRev(No):
    if No <= 0:
        No = -No
    
    No1 = (No//2)+1

    for i in range( No1,0,-1):
        if No  % i == 0 :
            print(i , end = " ")
    
    
def main():
    Value = int(input("Enter the number : "))
    FactRev(Value)

if __name__ == "__main__":
    main()