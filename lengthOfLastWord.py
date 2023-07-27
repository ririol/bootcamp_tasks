class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        last_word = ''
        for char in s[::-1]:
            if char == ' ' and length == 0:
                continue
            elif char != ' ':
                last_word += char
                length = len(last_word)
            elif char == ' ':
                return length
        return length
    
# class Solution:
#     def lengthOfLastWord(self, s: str) -> int:

#         words = s.split()

#         if words:
#             return len(words[-1])
#         else:
#             return 0