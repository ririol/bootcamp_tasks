class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        original = {i:s.count(i) for i in s}
        fake = {i:t.count(i) for i in t}

        for char, count in fake.items():
            if char not in original or count > original[char]:
                return char