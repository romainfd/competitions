n = int(input())

salaries = []
for _ in range(n):
    salaries.append(int(input()))

salaries.sort()

# Calculate the revenue with the area of the rectangle under the OK customers
max_revenue = 0
for i, sal in enumerate(salaries):
    if sal * (n - i) > max_revenue:
        max_revenue = sal * (n - i)

print(max_revenue)
