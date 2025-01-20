from collections import deque

def compute_sequence_element(data_set_number, index):
    # Initialize the queue with the root node
    queue = deque([(1, 1)])  # (numerator, denominator)

    # Traverse the tree in level order until reaching the desired index
    for _ in range(index):
        # Dequeue the node from the front of the queue
        numerator, denominator = queue.popleft()
        
        # Enqueue left child (numerator remains the same, denominator doubles)
        queue.append((numerator, 2 * denominator))
        
        # Enqueue right child (numerator increments by 1, denominator doubles)
        queue.append((numerator + 1, 2 * denominator))

    # Output the fraction represented by the label of the last dequeued node
    print(f"{data_set_number} {numerator}/{denominator}")

# Read the number of data sets
num_data_sets = int(input())

# Process each data set
for _ in range(num_data_sets):
    data_set_number, index = map(int, input().split())
    compute_sequence_element(data_set_number, index)
