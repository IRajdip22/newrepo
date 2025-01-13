while True:
    n = int(input("Enter the number for Fibonnaci series: "))

    a,b=0,1
    count = 0

    while True:
        if n<=0:
            print("Enter positive integer number!!!")
        elif n==1:
            print("Fibonnaci series upto",n,":",a)
        else:
            print("Fibonnaci sequnce")        

        while count<n:
            print(a)
            nth = a+b
            a = b
            b = nth
            count += 1
        break    
