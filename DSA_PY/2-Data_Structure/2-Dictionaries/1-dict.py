# Google Question
# Given an array = [2,5,1,2,3,5,1,2,4]:
# It should return 2
#
# Given an array = [2,1,1,2,3,5,1,2,4]:
# It should return 1
#
# Given an array = [2,3,4,5]:
# It should return undefined

def rec(arr: list) -> int:

    seen = set()

    for num in arr:
        if num in seen:
            return num
        else:
            seen.add(num)



