## Applied Algorithms: 35290
## Programming Assignment 4
## Jayden Brown

def sift_down(heap, i, size, is_min=True):
    while True:
        left = 2 * i + 1
        right = 2 * i + 2
        target = i

        if left < size:
            if is_min and heap[left] < heap[target]:
                target = left
            elif not is_min and heap[left] > heap[target]:
                target = left

        if right < size:
            if is_min and heap[right] < heap[target]:
                target = right
            elif not is_min and heap[right] > heap[target]:
                target = right

        if target == i:
            break

        heap[i], heap[target] = heap[target], heap[i]
        i = target

def build_heap(heap, is_min=True):
    n = len(heap)

    for i in range(n // 2 - 1, -1, -1):
        sift_down(heap, i, n, is_min)

def mergeMinHeaps(H1, H2):
    merged = H1 + H2
    build_heap(merged, True)
    return merged

def mergeAsMaxHeap(H1, H2):
    merged = H1 + H2
    build_heap(merged, False)
    return merged

if __name__ == "__main__":
    H1 = [1, 3, 5, 7]
    H2 = [2, 4, 6, 8]

    print("Original H1: ", H1)
    print("Original H2: ", H2)

    print("Merged min-heap: ", mergeMinHeaps(H1, H2))
    print("Merged max-heap: ", mergeAsMaxHeap(H1, H2))

    # Additional Test Cases
    test_cases = [
        ([], []), #both empty
        ([1, 2, 3], []), #second heap empty
        ([], [4, 5, 6]), #first heap empty
        ([1, 1, 2], [1, 2, 2]), #duplicate values
        ([2], [1, 3, 4, 5]) #different sized heaps
    ]

    for H1, H2, in test_cases:
        print("\nInputs: ", H1, H2)
        print("min-heap: ", mergeMinHeaps(H1, H2))
        print("max-heap: ", mergeAsMaxHeap(H1, H2))