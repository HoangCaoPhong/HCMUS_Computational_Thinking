try:
    a = float(input("Input a = "))
    b = float(input("Input b = "))
except:
    print("a, b must be integer")
else: 
    try:
        print(a / b)
    except:
        print("b cannot be zero")



    
