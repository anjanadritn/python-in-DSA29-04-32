# counting the frequency of characters in a string
# leet code 387

def counting(s):
    d={}
    for ch in s:
        if ch in d:
            d[ch]=d.get(ch,0)+1
        else:
            d[ch]=1
    return d
print(counting("aaabcbb"))