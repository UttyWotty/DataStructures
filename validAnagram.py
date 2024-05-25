class Example:
    def isAnagram(self, s: str, t: str) -> bool:
        # If the lengths are different, they cannot be anagrams, so checking that at first
        if len(s) != len(t):
            return False

        # Creating dictionary to count characters in s
        count_s = {}
        for char in s:
            if char in count_s:
                count_s[char] += 1
            else:
                count_s[char] = 1

        # Creating dictionary to count characters in t
        count_t = {}
        for char in t:
            if char in count_t:
                count_t[char] += 1
            else:
                count_t[char] = 1

        # Comparing the two dictionaries
        return count_s == count_t  #should be same characters inside and same len

# using in an example with my name
solution = Example()
s = "utku"
t = "kutu"
print(f"Is '{s}' an anagram of '{t}'? {solution.isAnagram(s, t)}")
