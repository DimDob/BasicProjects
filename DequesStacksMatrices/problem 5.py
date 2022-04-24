import collections

males = [int(x) for x in input().split()]
females = collections.deque([int(x) for x in input().split()])
matches = 0


while True:
    if not (males and females):
        break
    first_female = females.popleft()
    last_male = males.pop()

    if first_female <= 0 or last_male <= 0:
        if first_female <= 0:
            males.append(last_male)
        elif last_male <= 0:
            females.appendleft(first_female)
        continue

    if first_female % 25 == 0 or last_male % 25 == 0:
        if first_female % 25 == 0:
            first_female = females.popleft()
            males.append(last_male)

        elif last_male % 25 == 0:
            last_male = males.pop()
            females.appendleft(first_female)
        continue
    if first_female == last_male:
        matches += 1

    else:
        males.append(last_male-2)

print(f"Matches: {matches}")

if males:
    males = [str(x) for x in males]
    print(f"Males left: {', '.join(reversed(males))}")
else:
    print(f'Males left: none')
if females:
    print(f"Females left: {', '.join(map(str,females))}")
else:
    print(f'Females left: none')
