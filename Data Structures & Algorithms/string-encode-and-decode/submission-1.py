class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for word in strs:
            curr_word = str(len(word)) + '#' + word
            encoded_str += curr_word
        # print(encoded_str)
        return encoded_str
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            curr_len = int(s[i:j])
            fin_word = s[j + 1: j + 1 + curr_len]
            res.append(fin_word)
            i = j + 1 + curr_len
        print(res)
        return res