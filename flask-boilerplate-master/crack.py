#!/usr/bin/env python3
n1=735023
string1=[50829, 295278, 422602, 345802, 90850, 389841, 560006, 595977, 357704]
n2=999941
string2=[520934, 30360, 157684, 815907, 560955, 124923, 295088, 331059, 92786 ]
e=3

def crack(n, string):
    for r in string:
        i=0
        notdone=True
        while notdone:
            i+=1
            guess= (n*i+r)**(1.0/e)
            #print(guess)
            if (guess-int(guess)>0.9999):
                print(round(guess))
            elif len(str(round(guess)))>3:
                notdone=False
if __name__=="__main__":
    crack(n1, string1)
    print("\n")
    crack(n2, string2)