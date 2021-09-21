# Assignment "Tic-Tac-Toe" by Federico Pregnolato
# Create a Tic-Tac-Toe game to play in Python
import math

def main():
    grid_squared = int(input('How many squares do you want on your grid? '))
    max_val = grid_squared**2
    n_digits = int(math.log10(max_val)) + 1

    grid = create_grid(grid_squared)
    draw_grid(grid, n_digits)

    game_finished = False;
    incorrect_number = True
    player_x = 'X'
    player_o = 'O'

    while game_finished != True:
        x_selection = int(input(f"x's turn to choose a square (1-{max_val}): "))
        while incorrect_number != False:
            if x_selection < 1 or x_selection > max_val:
                incorrect_number = True
                x_selection = int(input(f"Incorrect value. Please choose a value between 1 and {max_val}): "))
            else:
                incorrect_number = False

        updated_grid = change_element(x_selection, grid, player_x)
        draw_grid(updated_grid, n_digits)

        o_selection = int(input(f"o's turn to choose a square (1-{max_val}): "))
        while incorrect_number != False:
            if x_selection < 1 or x_selection > max_val:
                incorrect_number = True
                x_selection = int(input(f"Incorrect value. Please choose a value between 1 and {max_val}): "))
            else:
                incorrect_number = False

        updated_grid = change_element(o_selection, grid, player_o)
        draw_grid(updated_grid, n_digits) 
        game_finished = win_checker(updated_grid)
        break
            


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

def change_element(number, grid_array, player):
    for row in grid_array:
        for element in row:
            if number == element:
                element_index = row.index(element)
                row[element_index] = player
                return grid_array

def win_checker(grid_array):
    pass


if __name__ == '__main__':
    main()