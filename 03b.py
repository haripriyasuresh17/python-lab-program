num_elements = int(input("Enter the number of elements in the list: "))

numbers = []
for i in range(num_elements):
    value = int(input(f"Enter the value - {i+1}: "))
    numbers.append(value)

ascending_order = True
for i in range(1, len(numbers)):
    if numbers[i] < numbers[i-1]:
        ascending_order = False
        break

print("Original list:", numbers)
if ascending_order:
    print("Yes, the list is in ascending order.")
else:
    print("No, the list is not in ascending order.")
