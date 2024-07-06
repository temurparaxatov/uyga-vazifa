def my_sort(numbers):
    if not all(isinstance(n, int) and n > 0 for n in numbers):
        raise ValueError("Barcha elementlar musbat butun sonlar bo'lishi kerak.")
    
    def digit_sum(n):
        return sum(int(digit) for digit in str(n))
    
    sorted_numbers = sorted(numbers, key=digit_sum)
    return sorted_numbers

print(my_sort([14, 30, 103]))  
print(my_sort([5, 31, 123, 80, 11]))  
