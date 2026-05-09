# longest nice substring

class Solution(object):
    def longestNiceSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """

        # Base case
        if len(s) < 2:
            return ""

        charSet = set(s)

        for i in range(len(s)):

            # If both uppercase and lowercase exist
            if s[i].lower() in charSet and s[i].upper() in charSet:
                continue

            # Split and solve recursively
            left = self.longestNiceSubstring(s[:i])
            right = self.longestNiceSubstring(s[i + 1:])

            # Return longer substring
            if len(left) >= len(right):
                return left
            else:
                return right

        # Entire string is nice
        return s