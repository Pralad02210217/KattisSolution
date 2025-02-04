n = int(input())

for i in range(1, n + 1):
    test_lines, cols = map(int, input().split())
    matrix = [input() for _ in range(test_lines)]
    
    print(f'Test {i}')
    for row in reversed(matrix):
        print(row[::-1])
