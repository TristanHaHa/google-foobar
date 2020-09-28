import math
def solution(area):
    answer = []
    while area > 0:
        maxIntSide = int(math.sqrt(area))
        answer.append(maxIntSide**2)
        area -= maxIntSide**2
    return answer
