def calculate_total(*numbers):
    total = sum(numbers)
    avg = total / len(numbers) if numbers else 0
    return total, avg

total, avg = calculate_total(10, 20, 30, 40)
print("\nTotal:", total)
print("Average:", avg)