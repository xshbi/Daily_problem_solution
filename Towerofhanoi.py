'''
The Tower of Hanoi is a classic problem in recursion. The problem involves three rods and a number of disks of different sizes which can slide onto any rod. The objective is to move all the disks from the first rod to the third rod, with the following rules:

Only one disk can be moved at a time.
Each move consists of taking the top disk from one of the rods and placing it on top of the stack on another rod.
No disk may be placed on top of a smaller disk.
Here's the recursive solution to the Tower of Hanoi problem in Python:
'''



def tower_of_hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    tower_of_hanoi(n-1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    tower_of_hanoi(n-1, auxiliary, target, source)

# Test the function with 3 disks
n = 3
tower_of_hanoi(n, 'A', 'C', 'B')



'''
Explanation:

The function tower_of_hanoi takes 4 parameters: n is the number of disks to move, source is the starting rod, target is the destination rod, and auxiliary is the extra rod for assistance in moving disks.

When n == 1, it directly moves the disk from the source rod to the target rod.

Otherwise, it recursively moves n-1 disks from the source rod to the auxiliary rod. Then, it moves the remaining disk from the source rod to the target rod. Finally, it recursively moves n-1 disks from the auxiliary rod to the target rod.
'''