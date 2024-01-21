num = int(input("Number: "))
num_l = [ ]

def _sort_():
    def sort_acs(num_list):
        place = 0
        for i in range (len(num_list)):
            for x in range (len(num_list)):
                if (num_list[i] > num_list[x]) :
                    continue
                else:
                    place = num_list[i]
                    num_list[i] = num_list[x]
                    num_list[x] = place 
        print(num_list)

    def sort_decs (num_list):
        place = 0
        for i in range (len(num_list)):
            for x in range (len(num_list)):
                if (num_list[i] > num_list[x]):
                    place = num_list[i]
                    num_list[i] = num_list[x]
                    num_list[x] = place
                else:
                    continue
        print(num_list)

    print("1. Acsending Order")
    print("2. Decsending Order")

    x = int(input("Select: "))
    if (x == 1):
        sort_acs(num_l)
    elif (x == 2):
        sort_decs(num_l)
    else:
        print("Invalid Input")
    


while (num != 0 ) :
    num_l.append(num)
    num = int(input("Number: "))

_sort_()
