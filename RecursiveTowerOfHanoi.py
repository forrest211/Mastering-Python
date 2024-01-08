NUMBER_OF_DISKS = 4
A = list(range(NUMBER_OF_DISKS, 0, -1))
B = []
C = []

def move(n, source, auxiliary, target):
    if n <= 0:
        return
    # Move n - 1 disk from source to auxiliary, so they are out of the way
    move(n - 1, source, target, auxiliary)

    # Move the nth disk from source to target
    target.append(source.pop())

    # Display progress
    print(A, B, C, '\n')

    # Move n - 1 disks that we left on auxiliary onto target
    move(n - 1, auxiliary, source, target)

print('Initial state:', A, B, C, '\n')
move(NUMBER_OF_DISKS, A, B, C)