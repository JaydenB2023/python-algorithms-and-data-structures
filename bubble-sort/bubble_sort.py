## APPLIED ALGORITHMS: 35290
## Course Intro | Programming Assignment 1
## Jayden Brown

import time
import matplotlib.pyplot as plt

numbers = [] # creates the empty list
with open('input3.txt') as file:
    for line in file: #goes through the file 1 line at a time
        number = int(line) #converts each line item to a number
        numbers.append(number) #adds integer to numbers list

def bubble(numbers):
    #indexed link where we make comparisons
    indexing_length =len(numbers)-1 #minus 1 because you cant perform a comparison on the last number in the list
    organized = False #breaks us out once the list is sorted

    #iterations
    while not organized:
        organized = True
        for i in range(0, indexing_length):
            if numbers[i] > numbers[i+1]: # i+1 is position to right of value
                organized = False
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i] #flip values to sort
    return numbers

#stores the 20 input sizes
input_sizes = list(range(500, 10001, 500))

#list for average time for each input size
average_times = []

for size in input_sizes:
    times = []

    #run each input size 3 times
    for i in range(3):
        #fresh input list for each run
        test_numbers = numbers[:size].copy()

        #start timer
        start = time.perf_counter()

        bubble(test_numbers)

        #stop timer
        end = time.perf_counter()

        elapsed = end - start
        times.append(elapsed)
    
    #average of 3 runs
    average_time = sum(times) / len(times)
    average_times.append(average_time)

    print(size, times, average_time)

#graph
plt.plot(input_sizes, average_times, marker='o')

plt.xlabel("Number of Inputs")
plt.ylabel("Average Running Times (seconds)")
plt.title("Bubble Sort Running Time")

plt.show()