def calculate_cost(gigabytes,cost_per_gb):
    sum=(gigabytes*cost_per_gb)
    return sum

print(calculate_cost(int(input("Enter GB used:?")),(float(input("Enter cost pe GB")))))
