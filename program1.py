class Solution(object):
    def isValid(self, s):
        stack = []
    matching_pairs = {')': '(', '}': '{', ']': '['}
        for char in s:
        if char in matching_pairs:  # Closing parenthesis
            if not stack or stack.pop() != matching_pairs[char]:
                return False
        else:  # Opening parenthesis
            stack.append(char)

    return not stack  # True if stack is empty
        pass
    


  

