"""
Given a String, get the run length encoding of the string.
ex: input= "wwwwaaadexxxxxx" output = "w4a3d1e1x6"
"""


def run_len_encoding(s):
    out = ""
    i=0
    while i < len(s)-1:
        count = 1
        while i<len(s)-1 and s[i] == s[i+1]:

            count += 1
            i += 1

        out += s[i]
        out += str(count)
        i += 1
    return out

print(run_len_encoding("wwwwaaadexxxxxxywww"))