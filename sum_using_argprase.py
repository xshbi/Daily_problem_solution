import sys
args = sys.argv[1:]
#Here sys.args slices the first element.
print(args)

#Here we have to import the system library which helps to take input in cmd.
sum = 0
for a in args:
    x = int(a)
    if x%2 ==0:
        sum+=x
        print('Sum of evens=',sum)
# This program is about arg prasing.
#To run this code we need to run it directly in cmd --py sum_using_argprase.py 1 2 3 4 5.
