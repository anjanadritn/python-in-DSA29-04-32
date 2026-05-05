# Assignment 4:
# Given two strings s and p, the task is to find the smallest substring in s that contains all characters of p,
#  including duplicates. If no such substring exists, return "". If multiple substrings of the same length are found,
#  return the one with the smallest starting index.

# Examples: 

# Input: s = "timetopractice", p = "toc"
# Output: toprac
# Explanation: "toprac" is the smallest substring in which "toc" can be found.

# Input: s = "zoomlazapzo", p = "oza"
# Output: apzo
# Explanation: "apzo" is the smallest substring in which "oza" can be found.

def min_substring(s, p):
    if not s or not p:
        return ""

    res = ""

    for i in range(len(s)):
        count = list(p)

        for j in range(i, len(s)):
            if s[j] in count:
                count.remove(s[j])

            if len(count) == 0:
                temp = s[i:j+1]

                if res == "" or len(temp) < len(res):
                    res = temp
                break

    return res