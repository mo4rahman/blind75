"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
"""

# First Try
def valid_anagram(s, t):
    if len(s) != len(t):
        # cannot be anagrams if the lengths do not match
        return False
    check_list = [char for char in s]
    # we want to check every letter in the second word and remove each letter from 
    # the list. if we end up with an empty list, that means every letter is matched
    for letter in t:
        if letter in check_list:
            check_list.remove(letter)
    # if check_list:
    #     return False
    # else:
    #     return True
    return check_list == []


"""
Notes:
To check for anagram, we want to check in both words if they both have the same number of letters. For example, for anagram and nagaram, we need to check for 3 a's, 1 n, 1 g, 1 r, 1 m.
"""

# TODO: MAIN SOLUTION
# create a hash_map for each word
# count the occurrence of each letter
# match the counts in both words. If the count doesnt match or the letter doesn't exist in one word, return False
# Time: O(s + t) = O(n) iterate through both strings
# Space: O(s + t) = O(n) building 2 hash_maps, size of s and size of t.
# Downside, extra memory
def isAnagram(s, t):
    if len(s) != len(t):
        # cannot be anagrams if the lengths do not match
        return False
    hash_map_s = {}
    hash_map_t = {}
    # for letter in s:
    #     # if letter in hash_map_s:
    #     #     hash_map_s[letter] += 1
    #     # else:
    #     #     hash_map_s[letter] = 1
    #     # don't need to even check, this will try to receive and if it DNE, instantiate it
    #     hash_map_s[letter] = 1 + hash_map_s.get(letter, 0)
    # for letter in t:
    #     # if letter in hash_map_t:
    #     #     hash_map_t[letter] += 1
    #     # else:
    #     #     hash_map_t[letter] = 1
    #     hash_map_t[letter] = 1 + hash_map_t.get(letter, 0)
    
    # can do both passes in one for loop
    for i in range(len(s)):
        hash_map_s[s[i]] = 1 + hash_map_s.get(s[i], 0)
        hash_map_t[t[i]] = 1 + hash_map_t.get(t[i], 0)

    for letter in hash_map_s:
        if hash_map_s[letter] != hash_map_t.get(letter, 0):  # give 0 default if letter DNE
            return False
    return True

# Time: O(nlogn). Depends on sorting algo, good algos take O(nlogn)
# Space: O(1). A little iffy, some sorting algos take extra memory, but can be constant extra memory.  
def valid_anagram(s, t):
    if len(s) != len(t):
        # cannot be anagrams if the lengths do not match
        return False
    return sorted(s) == sorted(t)



print(isAnagram("drama", "amard"))  # True
print(isAnagram("car", "rat"))  # False
print(isAnagram("aacc", "ccac"))  # False

"""
MAIN POINTS:
- CREATE 2 HASH MAPS
- Loop through both words and count number of letters for each
- Compare both maps
"""