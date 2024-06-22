#Given a sentence containing several words and numbers. Find the largest number among them which does not contain 9. If no such number exists, return -1.





'''
Expected Time Complexity: O(n)
Expected Auxillary Space: O(n)

Constraints:
1<=n<=106
1<=answer<=1018

n is the length of a given sentence.
'''

class Solution:
    def ExtractNumber(self,sentence):

        arr = sentence.split();
        ans = -1
        for word in arr:
            cur = 0
            if not any(char == '9' for char in word):
                try:
                    cur = int(word)
                except:
                    continue
                ans = max(ans, cur)
        return ans



