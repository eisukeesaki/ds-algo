def balancedStringSplit(s):
    cnt_r = 0
    cnt_l = 0
    cnt_balanced = False

    for i in range(len(s)):
        if s[i] == "R":
            cnt_r += 1
        if s[i] == "L":
            cnt_l += 1
        if cnt_l == cnt_r:
            cnt_balanced += 1

    return cnt_balanced


input = "LLLLRRRR"
# input = "RLRRRLLRLL"
# input = "RLRRLLRLRL"
res = balancedStringSplit(input)
print(res)

