def test_continue():
    s = "hello"
    for i in range(len(s)):
        print(s[i])
        if s[i] == "l":
            break

test_continue()
