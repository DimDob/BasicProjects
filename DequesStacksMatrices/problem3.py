from collections import deque

firework_effects = deque([int(el) for el in input().split(', ')])
explosive_power = [int(el) for el in input().split(', ')]

palm_fireworks = 0
willow_fireworks = 0
crossette_fireworks = 0
success = False

while True:
    if palm_fireworks >= 3 and willow_fireworks >= 3 and crossette_fireworks >= 3:
        success = True
        break
    else:
        if firework_effects and explosive_power:
            first_firework = firework_effects.popleft()
            last_explosive_power = explosive_power.pop()

            if first_firework <= 0:
                explosive_power.append(last_explosive_power)
                continue
            elif last_explosive_power <= 0:
                firework_effects.appendleft(first_firework)
                continue

            current_sum = first_firework + last_explosive_power

            if current_sum % 3 == 0 and not current_sum % 5 == 0:
                palm_fireworks += 1

            elif current_sum % 5 == 0 and not current_sum % 3 == 0 :
                willow_fireworks += 1

            elif current_sum % 5 == 0 and current_sum % 3 == 0:
                crossette_fireworks += 1


            else:
                if first_firework > 0: #?
                    first_firework -= 1
                    firework_effects.append(first_firework)
                    explosive_power.append(last_explosive_power)
                    continue
        else:
            break
if success:
    print(f"Congrats! You made the perfect firework show!")
else:
    print(f"Sorry. You can't make the perfect firework show.")

if firework_effects:
    print(f"Firework Effects left: {', '.join(map(str,firework_effects))}")
if explosive_power:
    print(f"Explosive Power left: {', '.join(map(str,explosive_power))}")

print(f"Palm Fireworks: {palm_fireworks}")
print(f"Willow Fireworks: {willow_fireworks}")
print(f"Crossette Fireworks: {crossette_fireworks}")
