for i in range (1,100):
    if i % 3 ==0 and i % 5 == 0:
        print("fizzbuzz")
    elif i % 3 ==0:
        print("fizz")
    elif i % 5 ==0:
        print("buzz")
    else:
        print(i) 

        #Se muestran los numero del 1 al 100 cuando haya multiplos de 3 y 5 se mostrara fizzbuzz
        # Si solo hay multiplos de 3 se mostrara fizz 
        # y si solo hay multiplos de 5 se mostrara buzz
