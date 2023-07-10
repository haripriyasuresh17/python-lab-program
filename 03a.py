numbers = list(map(int, input("Enter a list of numbers: ").split()))

element = int(input("Enter the element to be found: "))

positive_indexes = []
negative_indexes = []
occurrence_count = 0

for i in range(len(numbers)):
    if numbers[i] == element:
        occurrence_count += 1
        positive_indexes.append(i)
        negative_indexes.append(i - len(numbers))

print(f"Element {element} occurs {occurrence_count} times in the list.")
print("Positive Index:", ', '.join(map(str, positive_indexes)))
print("Negative Index:", ', '.join(map(str, negative_indexes)))
