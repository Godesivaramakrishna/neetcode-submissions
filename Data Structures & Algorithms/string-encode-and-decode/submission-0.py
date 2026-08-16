class Solution:

    def encode(self, strs: List[str]) -> str:
        res = "" #we encode the string by word length + # this symbol + word it will store like this 4#word when we decode we got word as how means when we read inter 4 then after next idx we see # then we decode that interger length charcters ex: 5#word#d len(word#d) == 5 wheater it contain # in the length included
        for s in strs:
            res += str(len(s)) + "#" + s
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#": #we move forward until we see # this 
                j+=1
            length = int(s[i:j]) #i:j means from idx i to j we got the word length
            res.append(s[j+1: j+1 + length]) #here from j+1 idx to length of length include j+1 word we got the string that string we append it to our result
            i = j+1 + length
        return res
