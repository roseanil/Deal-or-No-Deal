import random

def openbox(n):
        i=0
        while(i<n):
                printbox()
                user_option=int(input("\n............................CHOOSE A BOX :"))
                if key[user_option-1] in s:
                        print(".....................CHOOSE A VALID BOX")
                else:
                        g=key[user_option-1]
                        s.append(g)
                        b.append(g)
                        print
                        print ("****************************************")
                        print ("*                                      *")
                        if d[g]>99:
                                print ("*    THE BOX CONTAINS RS",d[g],"          *")
                        elif d[g]<10:
                                print ("*   THE BOX CONTAINS RS",d[g],"             *")
                        else:
                                print ("*   THE BOX CONTAINS RS",d[g],"            *")
                        print ("*                                      *")
                        print ("****************************************")
                        print

                        i=i+1


def printbox():
        print
        print("...........BOXES AVAILABLE ARE......................")
        t=1
        for i in key:
            if i not in s:
                print ("---------")
                print ("|",i,"|")
                print ("---------")
        print


def banker():
        sum=d[yourbox]
        k=1

        for i in key:
                if i not in s:
                        sum=sum+d[i]
                        k=k+1
        total=0.9*(sum/k)
        return total




def decision(am):
        print
        print ("***************************************")
        print ("*                                     *")
        print ("*         BANKER OFFERS YOU",int(am),"       *")
        print ("*                                     *")
        print ("***************************************")
        print
        print ("..........AMOUNT LEFT..............")
        r=[]

        for i in key:
                if i not in b:
                        u=d[i]
                        r.append(u)

        r.sort()
        for y in r:
                print(y)
        p=1
        while p>0:

                ds=input("\n\t\t\tDEAL OR NO DEAL(d/n)")
                if ds=='d' or ds=='n':
                        return ds
                        break

def endlin():
        print ("THANK YOU FOR PLAYING")




def end(hm):
        print ("******************************************")
        print ("CONGRATS YOU WON  RS",int(hm))
        print ("******************************************")
        print ("\nYOUR PERSONEL BOX CONTAINS RS",d[yourbox])
        print ("\n.....game over.........")
        endlin()




print("\t\t\t\tWELCOME TO")
print("\t\t\t\tdeal or no deal")

box=[1,2,5,10,20,50,75,100,150,200]
key=['box-1','box-2','box-3','box-4','box-5','box-6','box-7','box-8','box-9','box-10']

random.shuffle(box)
d={}
for i in range(10):
        d[key[i]]=box[i]
print
for i in key:
    print ("---------")
    print ('|',i,'|')
    print ("---------")


print
n=int(input("\n.............CHOOSE YOUR BOX:"))

if n<11 and n>0:
        yourbox=key[n-1]
        print ("\nCONGRATS YOUR BOX IS",yourbox)

        b=[]
        s=[yourbox]
        sl=0


        print ("\nCHOOSE 4 BOXES")
        openbox(4)
        print ("\t\t\t\t\t\tCALLING BANKER")

        bank_deal_1=banker()
        user_decision_1=decision(bank_deal_1)

        if user_decision_1=="d":
                end(bank_deal_1)
        else:
                print ("\nCHOOSE THREE BOX")
                openbox(3)

                print ("\t\t\t\t\t\tCALLING BANKER")
                bank_deal_2=banker()
                user_decision_2=decision(bank_deal_2)




                if user_decision_2=="d":
                        end(bank_deal_2)
                else:

                        print ("CHOOSE 1 BOX")
                        openbox(1)
                        for m in key:
                                if m not in s:
                                        lastbox=m
                        print ("\t\t\t\t\t\tCALLING BANKER")
                        bank_deal_3=banker()
                        user_decision_3=decision(bank_deal_3)


                        if user_decision_3=='n':

                                l="CHOOSE BETWEEN YOURBOX |"+yourbox+"| AND THE BOX LEFT |"+lastbox+"|  :"
                                print
                                x=int(input(l))

                                final=key[x-1]



                                print ("CONGRATS YOU WON  RS",d[final])
                                endlin()
else:
        redo()
