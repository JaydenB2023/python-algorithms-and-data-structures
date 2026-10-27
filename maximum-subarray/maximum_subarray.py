## Applied Algorithms: 35290
## Programming Assignment 2
## Jayden Brown

import time
import matplotlib.pyplot as plt

numbers = [] #creates the empty list
with open('inputs.txt') as file:
    for line in file: #goes through the file 1 line at a time
        number = int(line) #converts each line item to a number
        numbers.append(number) #adds integer to numbers list

# ----------------------------
# Brute Force
# ----------------------------

def brute_force(numbers):
    max_sum = numbers[0]
    max_start = 0
    max_end = 0

    for i in range(len(numbers)):
        current_sum = 0
        for j in range(i, len(numbers)):
            current_sum += numbers[j]

            if current_sum > max_sum:
                max_sum = current_sum
                max_start = i
                max_end = j
    return max_start, max_end, max_sum

# ----------------------------
# Divide and Conquer
# ----------------------------

def max_crossing(numbers, left, mid, right):
    #left side
    current_sum = 0
    left_sum = float('-inf')
    max_left = mid

    for i in range(mid, left -1, -1):
        current_sum += numbers[i]

        if current_sum > left_sum:
            left_sum = current_sum
            max_left = i
    #right side
    current_sum = 0
    right_sum = float('-inf')
    max_right = mid + 1

    for j in range(mid + 1, right + 1):
        current_sum += numbers[j]

        if current_sum > right_sum:
            right_sum = current_sum
            max_right = j
    return max_left, max_right, left_sum + right_sum

def divide_conquer(numbers, left, right):

    if left == right:
        return left, right, numbers[left]
    
    mid = (left + right) // 2
    #find the crossing answer
    left_start, left_end, left_sum = divide_conquer(
        numbers, left, mid
    )

    right_start, right_end, right_sum = divide_conquer(
        numbers, mid + 1, right
    )

    cross_start, cross_end, cross_sum = max_crossing(
        numbers, left, mid, right
    )
    #pick the winner
    if left_sum >= right_sum and left_sum >= cross_sum:
        return left_start, left_end, left_sum
    elif right_sum >= left_sum and right_sum >= cross_sum:
        return right_start, right_end, right_sum
    else:
        return cross_start, cross_end, cross_sum


# ----------------------------
# Times
# ----------------------------

#stores the 20 input sizes
input_sizes = list(range(5000, 100001, 5000))

#list for average time for each input size
brute_force_times = []
divide_conquer_times = []

for size in input_sizes:

    test_numbers = numbers[:size]

    #Brute Force
    brute_times = []

    #run each input size 3 times
    for i in range(3):
        #start timer
        start = time.perf_counter()

        brute_force(test_numbers)

        #stop timer
        end = time.perf_counter()

        elapsed = end - start
        brute_times.append(elapsed)

    #average of 3 runs
    brute_average = sum(brute_times) / len(brute_times)
    brute_force_times.append(brute_average)

    #Divide and Conquer
    divide_times = []

    for i in range(3):
        start = time.perf_counter()

        divide_conquer(numbers, 0, size -1)

        end = time.perf_counter()
        divide_times.append(end - start)

    divide_average = sum(divide_times) / len(divide_times)
    divide_conquer_times.append(divide_average)

    print("input size:", size)
    print("Brute force:", size, brute_force_times)
    print("Divide and Conquer:", size, divide_conquer_times)

# ----------------------------
# Graph
# ----------------------------

plt.plot(input_sizes, brute_force_times,  label='Brute Force')
plt.plot(input_sizes, divide_conquer_times, label='Divide and Conquer')

plt.xlabel('Input Size')
plt.ylabel('Average Running Time (seconds)')
plt.title('Maximum Subarray Running Time Comparison')

plt.legend()
plt.grid()
plt.show()