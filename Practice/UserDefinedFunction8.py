def BigBazar():
    print("Inside BigBazar")

    def Amul():
        print("Inside Amul Icecream Parlor")

def main():
    BigBazar()            # ALLOWED
    Amul()                # ERROR
    BigBazar.Amul()       # ERROR

if __name__=="__main__":
    main()