def isAnagram(s, t) -> bool:
    cnt_match = 0

    for i in range(len(s)):
        k = 0
        for k in range(len(t)):
            if s[i] == t[k]:
                cnt_match += 1
                break

    print(cnt_match)
    if cnt_match == len(s):
        return True
    else:
        return False

# s = "anagram"
# t = "nagaram"
# t = "rat"
# s = "car"
s = "fortytwo"
t = "rtwyoaat"
res = isAnagram(s, t)
print(res)
