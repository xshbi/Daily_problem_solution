#User function Template for python3

class Solution:
    def armstrongNumber (self, n):
        # code here 
        string = str(n)
        size = len(string)
        armstrongNum = 0
    
        for i in range (size):
            armstrongNum = armstrongNum + int(string[i])**size

        if armstrongNum == n:
            return "true"
        else:
            return "false"


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = input()
        n = int(n)
        ob = Solution()
        print(ob.armstrongNumber(n))

