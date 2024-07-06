

def prime(starting_range, ending_range):
    lst = []
    flag = 0  # Declaring flag variable
    # elements range between starting and ending range
    for i in range(starting_range, ending_range):
        for j in range(2, i):
            if(i % j == 0):  
                flag = 1  
                break
            else:
                flag = 0
        if(flag == 0):  
            lst.append(i)
    return lst



starting_range = 2
ending_range = 7
lst = prime(starting_range, ending_range)
if len(lst) == 0:
    print("There are no prime numbers in this range")
else:
    print("The prime numbers in this range are: ", lst)
