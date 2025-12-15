FirN = int(input("First Number:"))
SecN = int(input("Second Number :"))
Oper = input("Operation :")
if Oper == "+":
    print (FirN + SecN)
elif Oper == "-":
    print (FirN - SecN)
elif Oper == "*":
    print (FirN * SecN)
elif Oper == "/":
    if SecN == 0: 
        print ("Error")
    else:
        print (FirN / SecN)
