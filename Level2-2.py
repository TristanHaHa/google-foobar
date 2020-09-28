from random import randrange
def solution(l):
    l = sorted(l, reverse=True)
    sum_digits = sum(l)
    # if sum of a number's digits is divisible by 3, then the number is divisible by 3
    if sum_digits % 3 == 0:
        return list_to_int(l)
    else:
        # case where only 1 digit needs to be removed
        for i in range(len(l) - 1, -1, -1):
            if (sum_digits - l[i]) % 3 == 0:
                del l[i]
                return list_to_int(l)
        # case where 2 digits need to be removed
        for i in range(len(l) - 1, 0, -1):
            if (sum_digits - l[i]*2) % 3 == 0:
                del l[i]
                del l[i-1]
                if sum(l) % 3 == 0:
                    return list_to_int(l)
                else:
                    break
        return 0
def list_to_int(l):
    return int("".join([str(i) for i in l]))

def generate_test_cases():
    list = []
    for i in range(randrange(1,10)):
        list.append(randrange(10))
    list = [1,2,1,1]
    print(list,solution(list))
generate_test_cases()
