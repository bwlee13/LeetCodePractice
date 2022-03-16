"""
Write a function to detect calendar meeting conflicts between two evens
"""

start1 = 2
end1 = 4
start2 = 5
end2 = 7


def has_conflict(s1, e1, s2, e2):
    if s1 < s2 and e1 <= s2:
        return False
    elif s2 < s1 and e2 <= s1:
        return False
    else:
        return True


print(has_conflict(start1, end1, start2, end2))