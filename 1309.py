class Solution:
    def freqAlphabets(self, s: str) -> str:
        mapping = {
            "1": "a",
            "2": "b",
            "3": "c",
            "4": "d",
            "5": "e",
            "6": "f",
            "7": "g",
            "8": "h",
            "9": "i",
            "10#": "j",
            "11#": "k",
            "12#": "l",
            "13#": "m",
            "14#": "n",
            "15#": "o",
            "16#": "p",
            "17#": "q",
            "18#": "r",
            "19#": "s",
            "20#": "t",
            "21#": "u",
            "22#": "v",
            "23#": "w",
            "24#": "x",
            "25#": "y",
            "26#": "z",
        }
        
        decoded = ""
        i = len(s) - 1
        while i >= 0:
            c = s[i]
            if c == "#":
                c = s[i-2] + s[i-1] + c
                i -= 2
            
            decoded += mapping[c]
            i -= 1
            
        return "".join((reversed(decoded)))
               
