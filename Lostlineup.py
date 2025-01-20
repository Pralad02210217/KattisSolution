n = int(input())  # Get the total number of people in the lineup

# Initialize a list of empty lists called 'queue' for n-1 times
queue = [[] for i in range(1, n)]


# Read the list of positions as input and split it into a list
line = list(map(int, input().split()))

# Loop through the positions to reconstruct the lineup
for i in range(n - 1):
    # Get the queue position by selecting the first value from 'line'
    position = line[i]
    
    # Update the 'queue' list with the person's position
    queue[position] = i + 2
    
    # Print the 'queue' list after each update (for debugging purposes)
    print(queue)
    # do not forget to remove this print while actually testing

# Insert Jimmy at the front of the 'queue' list
queue.insert(0, 1)

# Print the reconstructed lineup
print(*queue)
