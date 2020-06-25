def last_stone_weight(stones: list):
    while len(stones) > 1:
        stones.sort()
        if (first := stones[-1]) != (second := stones[-2]):
            stones.pop()
            stones.pop()
            stones.append(abs(first - second))
        elif first == second:
            stones.pop()
            stones.pop()

    return stones[0] if stones else 0


print(last_stone_weight([3, 7, 2]))
print(last_stone_weight([2, 7, 4, 1, 8, 1]))
