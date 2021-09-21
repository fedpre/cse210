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
    is_finished = False
    number_chosen = []

    while game_finished != True:
        x_selection = int(input(f"x's turn to choose a square (1-{max_val}): "))
        while incorrect_number != False:
            if x_selection < 1 or x_selection > max_val:
                incorrect_number = True
                x_selection = int(input(f"Incorrect value. Please choose a value between 1 and {max_val}: "))
            elif x_selection in number_chosen:
                incorrect_number = True
                x_selection = int(input(f"Value already chosen. Please choose a value between 1 and {max_val} not already chosen: "))
            else:
                incorrect_number = False
        number_chosen.append(x_selection)
        updated_grid = change_element(x_selection, grid, player_x)
        draw_grid(updated_grid, n_digits)
        status = status_checker(updated_grid, player_x, player_o, max_val)
        
        if status == 'player_x':
            print(f"Congratulations player X! You won the game")
            game_finished = True
        elif status == 'player_o':
            print(f"Congratulations player X! You won the game")
            game_finished = True
        elif status == 'draw':
            print('Draw. Thanks for playing the game.')
            game_finished = True
        
        incorrect_number = True
        o_selection = int(input(f"o's turn to choose a square (1-{max_val}): "))
        while incorrect_number != False:
            if o_selection < 1 or o_selection > max_val:
                incorrect_number = True
                o_selection = int(input(f"Incorrect value. Please choose a value between 1 and {max_val}: "))
            elif o_selection in number_chosen:
                incorrect_number = True
                o_selection = int(input(f"Value already chosen. Please choose a value between 1 and {max_val} not already chosen: "))
            else:
                incorrect_number = False

        number_chosen.append(o_selection)
        updated_grid = change_element(o_selection, grid, player_o)
        draw_grid(updated_grid, n_digits) 

        
        status = status_checker(updated_grid, player_x, player_o, max_val)
        
        if status == 'player_x':
            print(f"Congratulations player X! You won the game")
            game_finished = True
        elif status == 'player_o':
            print(f"Congratulations player X! You won the game")
            game_finished = True
        elif status == 'draw':
            print('Draw. Thanks for playing the game.')
            game_finished = True

        incorrect_number = True
            


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
            print('|', end = ' ')
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
                if _ == range(len(row))[-1] and n_digits >= 2:
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

def status_checker(grid_array, player_x, player_o, max_val):
    result1 = horizontal_checker(grid_array, player_x, player_o)
    result2 = vertical_checker(grid_array, player_x, player_o)
    result3 = diagonal_checker(grid_array, player_x, player_o)
    result4 = draw_checker(grid_array, player_x, player_o, max_val)
    
    if result1 != None:
        return result1
    elif result2 != None:
        return result2
    elif result3 != None:
        return result3
    elif result4 != None:
        return result4
    else:
        return None


def horizontal_checker(grid_array, player_x, player_o):
    player_x_counter = 0
    player_o_counter = 0
    for row in grid_array:
        for element in row:
            if element == player_x:
                player_x_counter += 1
            elif element == player_o:
                player_o_counter += 1
        if player_x_counter == len(row):
            return 'player_x'
        elif player_o_counter == len(row):
            return 'player_o'
        else:
            player_o_counter = 0
            player_x_counter = 0
    return None

def vertical_checker(grid_array, player_x, player_o):
    return None


def diagonal_checker(grid_array, player_x, player_o):
    return None

def draw_checker(grid_array, player_x, player_o, max_val):
    accumulator = 0
    for row in grid_array:
        for element in row:
            if element == player_x or element == player_o:
                accumulator += 1
    if accumulator == max_val:
        return 'draw'
    else:
        return None            

if __name__ == '__main__':
    main()