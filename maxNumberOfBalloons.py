class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon = {
            'b': 1,
            'a': 1,
            'l': 2,
            'o': 2,
            'n': 1,
        }
        word_count = 0
        text_balloon = {i:text.count(i) for i in text if i in balloon}
        if len(text_balloon) != len(balloon): return 0

        while min(text_balloon.values()) > 0:
            for key, value in text_balloon.items():
                text_balloon[key] -= balloon[key]
                if text_balloon[key] < 0:
                    return word_count
            word_count += 1

        return word_count