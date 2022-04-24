from collections import deque

pizza_orders = deque([int(x) for x in input().split(', ')])
employee_capacity = [int(x) for x in input().split(", ")]

total_pizzas_made = 0
orders_completed = True
while True:
    if not pizza_orders or not employee_capacity:
        if  pizza_orders:
            orders_completed = False
        else:
            orders_completed = True
        break
    current_order = pizza_orders.popleft()
    if  current_order>10 or current_order <= 0:
        continue
    current_employee_capacity = employee_capacity.pop()

    if current_order <= current_employee_capacity:
        total_pizzas_made += current_order
        continue

    else:
        while True:
            if current_order:
                if current_order - current_employee_capacity < 0:
                    total_pizzas_made += current_order
                    break
                else:
                    total_pizzas_made += current_employee_capacity
                    current_order -= current_employee_capacity
                    pizza_orders.append(current_order)

                if employee_capacity:
                    current_order = pizza_orders.pop()
                    current_employee_capacity = employee_capacity.pop()
                else:
                    orders_completed = False
                    break

    if orders_completed:
                continue






if orders_completed:
        print("All orders are successfully completed!")
        print(f"Total pizzas made: {total_pizzas_made}")
        print(f"Employees: {', '.join(map(str, employee_capacity))}")

else:
    res = ""
    print("Not all orders are completed.")
    for element in sorted(pizza_orders):
        res += f"{element}, "
    res = res[:-2]
    print(f"Orders left: {res}")
