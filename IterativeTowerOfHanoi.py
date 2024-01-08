NUMBER_OF_DISKS = 4
number_of_moves = 2 ** NUMBER_OF_DISKS - 1

# Disks are represented as integers stacked on top of each other, the smallest and topmost disk being 1
rods = {
    'A': list(range(NUMBER_OF_DISKS, 0, -1)),
    'B': [],
    'C': []
}

def make_allowed_move(rod1, rod2):
    # When True, a disk can be moved from rod1 to rod2, and vice-versa when False
    forward = False

    # If rod2 is empty, a disk can be moved onto it
    if not rods[rod2]:
        forward = True

    # rod1 has at least one disk, and the top disk is smaller than the top one on rod2
    elif rods[rod1] and rods[rod1][-1] < rods[rod2][-1]:
        forward = True

    # If forward is True, a disk is moved from rod1 to rod2
    if forward:
        print(f'Moving disk {rods[rod1][-1]} from {rods[rod1]} to {rods[rod2]}')
        rods[rod2].append(rods[rod1].pop())

    # Otherwise, a disk must be moved from rod2 to rod1
    else:
        print(f'Moving disk {rods[rod2][-1]} from {rods[rod2]} to {rods[rod1]}')
        rods[rod1].append(rods[rod2].pop())
    
    # Display progress
    print(rods, '\n')

def move(n, source, auxiliary, target):
    # Display starting configuration
    print(rods, '\n')
    for i in range(number_of_moves):
        remainder = (i + 1) % 3
        if remainder == 1:
            if n % 2 != 0:
                print(f'Move {i + 1} allowed between {source} and {target}')
                make_allowed_move(source, target)
            else:
                print(f'Move {i + 1} allowed between {source} and {auxiliary}')
                make_allowed_move(source, auxiliary)
        elif remainder == 2:
            if n % 2 != 0:
                print(f'Move {i + 1} allowed between {source} and {auxiliary}')
                make_allowed_move(source, auxiliary)
            else:
                print(f'Move {i + 1} allowed between {source} and {target}')
                make_allowed_move(source, target)
        elif remainder == 0:
            print(f'Move {i + 1} allowed between {auxiliary} and {target}')
            make_allowed_move(auxiliary, target)

# Initiate call from source A to target C with auxiliary B
move(NUMBER_OF_DISKS, 'A', 'B', 'C')
