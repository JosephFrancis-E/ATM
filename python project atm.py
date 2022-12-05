
while True:
    print(" ")
    print("*******************")
    print(" ")      
    print("WELCOME TO LPU BANK")
    print(" ")
    print("*******************")
    print(" ")
    print("~~~~~~~~~~~~~~~~")
    print("| #PIN IS 1234 |")
    print("~~~~~~~~~~~~~~~~")
    print(" ")
    p=int(input("Enter your 4 digit pin number :> "))
    print(" ")
    
    m = 25000.00
    if(p == 1234):
        while True:
            print(" ")
            print("*******************")
            print("       MENU")
            print("*******************")
            print(" ")
            print("(1)-BALANCE ENQUIRY")
            print("(2)-WITHDRAW CASH")
            print("(3)-DEPOSIT CASH")
            print("(4)-LOGOUT")
            print(" ")
     
            c = int(input("=>  ENTER THE NUMBER TO PROCEED :> "))
            if (c == 2):
                print(" ")
                print(">>>>>>>>>>>>>>~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<<<<<<<<<<<<<<")
                print(" ")
                w=float(input("=>            ENTER AMOUNT YOU WANT TO WITHDRAW :> ₹ "))
                
                
                if (w < m):
                    print(" ")
                    print("=>            PLEASE TAKE YOUR AMOUNT           :> ₹","{0:.2f}".format(w))
                    print(" ")
                    print("=>            YOUR NEW BALANCE IS               :> ₹","{0:.2f}".format(m-w,))
                    print(" ")
                    print(">>>>>>>>>>>>>>~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<<<<<<<<<<<<<<")
                    if (m-w)<5000:
                        print("=>            YOU HAVE LOW BALANCE")
                elif w>m:
                    print(" ")
                    print("-------*****************************---------")
                    print("       YOU HAVE INSUFFICIENT BALANCE")
                    print("-------*****************************---------")
                

            elif(c==1):
                print(" ")
                print(">>>>>>>>>>>>>>~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<<<<<<<<<<<<<<")
                print(" ")
                print("=>            YOUR CURRENT BALANCE IS :> ₹","{0:.2f}".format(m))
                print(" ")
                print(">>>>>>>>>>>>>>~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<<<<<<<<<<<<<<")
                print(" ")

            elif (c == 3):
                print(" ")
                print(">>>>>>>>>>>>>>~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<<<<<<<<<<<<<<")
                print(" ")
                d=float(input("=>           ENTER AMOUNT YOU WANT TO DEPOSIT :> ₹ "))
                print(" ")
                print("=>           YOUR NEW BALANCE IS              :> ₹","{0:.2f}".format(d+m))
                print(" ")
                print(">>>>>>>>>>>>>>~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<<<<<<<<<<<<<<")
            elif (c==4):
                break
            else:
                print(" ")
                print("-------************---------")
                print("       WRONG CHOICE")
                print("-------************---------")
    else:
        print(" ")
        print("-------****************---------")
        print("       WRONG PIN NUMBER")
        print("-------****************---------")
        
