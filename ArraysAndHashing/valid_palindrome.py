"""
https://leetcode.com/problems/valid-palindrome/

125. Valid Palindrome
-->Easy<--


A phrase is a palindrome if, after converting all uppercase letters into 
lowercase letters and removing all non-alphanumeric characters, it reads the 
same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.

"""


class Solution:
    # Convert all uppercase letters into lowercase letters
    # remove all non-alphanumeric characters (everything but numbers and letters)
    # check if palindrome (same forward and backward)
    # return boolean
    def isPalindrome(self, s: str) -> bool:
        alpha_numeric = "abcdefghijklmnopqrstuvwxyz0123456789"
        s = s.lower()
        # FIXME: for loop wont work because you want to remove while looping, which
        # will mess up the index flow
        for index, letter in enumerate(s):
            if letter not in alpha_numeric:
                s.pop(index)


s = Solution()
s.isPalindrome()
