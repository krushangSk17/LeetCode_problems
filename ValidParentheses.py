class Solution:
    def isValid(self, s: str) -> bool:
        leftSymbols = []
        for c in s:
            if c in ['(','{','[']:
                leftSymbols.append(c)
            elif c == ')' and len(leftSymbols) != 0 and leftSymbols[-1] == '(':
                leftSymbols.pop()
            elif c == '}' and len(leftSymbols) != 0 and leftSymbols[-1] == '{':
                leftSymbols.pop()
            elif c == ']' and len(leftSymbols) != 0 and leftSymbols[-1] == '[':
                leftSymbols.pop()
            else:
                return False
        return leftSymbols == []
ob = Solution()
ob.isValid("()[]")
