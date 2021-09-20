# Assignment "Tic-Tac-Toe" by Federico Pregnolato
# Create a Tic-Tac-Toe game to play in Python
import math

def main():
    grid_squared = int(input('How many squares do you want on your grid? '))
    max_val = grid_squared**2
    n_digits = int(math.log10(max_val)) + 1

    grid = create_grid(grid_squared)
    draw_grid(grid, n_digits)


def create_grid(n_rows_cols=3):
    rows = []
    k = 1
    for _ in range(n_rows_cols):
        new_row = []
        for __ in range(n_rows_cols):
            new_row.append(k)
            k += 1
        rows.append(new_row)
    
    return rows


def draw_grid(grid_array, n_digits):
    print()
    for row in grid_array:
        for element in row:
            print(f"{element:{n_digits}}", end=' ')
            if element == row[-1]:
                continue
            print('|', end = ' ')
        if row == grid_array[-1]:
            print()
            continue
        print()
        if n_digits == 1:
            print('--', end = '')
            for _ in range(len(row)):
                if _ == range(len(row))[-1]:
                    continue
                print('+---', end = '')   
            print()
        else:
            print('---', end = '')
            for _ in range(len(row)):
                if _ == range(len(row))[-1]:
                    continue
                print('+----', end = '')   
            print()
    print()




if __name__ == '__main__':
    main()