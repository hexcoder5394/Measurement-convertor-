#temperature
def temp ():
    print("1. celcious to farenheit")
    print("2. farenheit to celcious")
    x = int(input("Select: "))
    #celcious to farenheit
    if (x == 1):
        t = int(input("Temperature: "))
        f = (t * 9/5) + 32
        print(f,"F")

    #harenheit to celcious
    elif (x == 2):
        t = int(input("Temperature: "))
        c = (t - 160)/9
        print(c,"C")
    else:
        print("Invalid input")

def length ():
    
    print("1. cm to mm")
    print("2. mm to cm")
    print("3. cm to m")
    print("4. m to cm")
    print("5. m to Km")
    print("6. Km to m")
    
    x = int(input("Select: "))
 #cm to mm  
    if (x == 1):
        l = int(input("Length: "))
        t = (l * 10)
        print(t,"mm")
 #mm to cm
    elif (x == 2):
        l = int(input("Length: "))
        t = (l/10)
        print(l,"cm")
 #cm to m        
    elif (x == 3):
        l = int(input("Length: "))
        t = (l/100)
        print(t,"m")
 #m to cm
    elif (x == 4):
        l = int(input("Length: "))
        t = (l * 100)
        print(t,"cm")
 #m to Km
    elif (x == 5):
        l = int(input("Length: "))
        t = (l/1000)
        print(t,"Km")
 #Km to m
    elif (x == 6):
        l = int(input("Length: "))
        t = (l*1000)
        print(t,"m")
    else:
        print("Invalid input")
 
def mass():
    print("1. g to Kg")
    print("2. Kg to g")
    print("3. Kg to T")
    print("4. T to Kg")
    
    x = int(input("Select: "))
    #g to Kg
    if (x == 1):
        l = int(input("Length: "))
        t = (l/1000)
        print(t,"Kg")
    #Kg to g
    elif (x == 2):
        l = int(input("Length: "))
        t = (l*1000)
        print(t,"g")
    #Kg to T 
    elif (x == 3):
        l = int(input("Length: "))
        t = (l/1000)
        print(t,"T")
    #T to Kg
    elif (x == 4):
        l = int(input("Length: "))
        t = (l*1000)
        print(t,"Kg")
    else:
        print("Invalid input ")        
       
print("1. Length")
print("2. Temperature")
print("3. Mass")
print ("4. Exit")

select = int(input("Select: "))

if (select == 1):
    length()
elif (select == 2):
    temp()
elif (select == 3):
    mass()
elif (select == 4):
    exit()
else:
    print("Invalid input")
