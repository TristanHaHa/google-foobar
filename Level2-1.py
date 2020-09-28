from random import randrange

def solution(n, b):
    id_list = [n]
    # Floyd's Cycle Detection Algorithm
    slow_ptr = 0
    fast_ptr = 0
    while True:
        # add 2 values to "keep up" with fast_ptr
        id_list.append(get_minion_id(id_list[len(id_list)-1], b))
        id_list.append(get_minion_id(id_list[len(id_list)-1], b))
        slow_ptr += 1
        fast_ptr += 2
        # cycle is found once both pointers meet
        if id_list[slow_ptr] == id_list[fast_ptr]:
            cycle_length = 0
            while True:
                slow_ptr += 1
                cycle_length += 1
                if id_list[slow_ptr] == id_list[fast_ptr]:
                    return cycle_length

def get_minion_id(n, b):
    k = len(n)
    x = "".join(sorted(n,reverse=True))
    # reversing x instead of sorting n again is quicker: O(n) vs O(nlogn)
    y = x[::-1]
    z = base_subtraction(x, y, k, b)
    return z

def base_subtraction(x, y, k, b):
    # converts x and y to base 10, subtracts, and converts difference back to base b
    base10_difference = int(x, b) - int(y, b)
    baseb_difference = ""
    while base10_difference > 0:
      baseb_difference += str(base10_difference % b)
      base10_difference = int(base10_difference / b)
    return baseb_difference[::-1].zfill(k)

def generate_test_cases():
    k = randrange(2,10)
    b = randrange(2,11)
    n = ""
    for i in range(k):
        n += str(randrange(b))
    #print(solution(n,b), b)
    print(solution("210022",3))

generate_test_cases()
