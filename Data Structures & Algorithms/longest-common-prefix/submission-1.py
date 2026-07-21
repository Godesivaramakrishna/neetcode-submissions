class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(strs[0])):
            for s in strs:
                if i >= len(s) or s[i] != strs[0][i]: #s[i] means bat oka sare bag oka sare if we are at bag then s[i] is points 0 then bag lo 0th index char is b kada aa b and strs[0][0] b equal or not equal kada ame chayam oka vala bag lo g and bat lo t not equal kada so ekkada return chastam manam result ne 
                    return res
            res+=strs[0][i] #strs[0] is bat bat of i i.e 0 at strs[0][0] is b 0 index bat lo bat oka ith value b kada 
        return res