winning_combos = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7],
                  [2, 5, 8], [3, 6, 9], [3, 5, 7], [1, 5, 9]]
grid = [num for num in range(1, 10)]

player1_moves = []
player2_moves = []


def make_a_move(player_moves):
    print(f"""
        {grid[0]}|{grid[1]}|{grid[2]}
        -----
        {grid[3]}|{grid[4]}|{grid[5]}
        -----
        {grid[6]}|{grid[7]}|{grid[8]}
        """)

    if player_moves == player1_moves:
        sign = 'X'
    else:
        sign = 'O'

    while True:
        try:
            player_move = int(input(f'Place an "{sign}" (1-9): '))
            if player_move < 1 or player_move > 9:
                raise ValueError
            if grid[player_move - 1] in ['O', 'X']:
                print('Box already filled, try again.')
            else:
                break
        except ValueError:
            print('Invalid input, please enter a number between 1 and 9.')

    player_moves.append(player_move)
    grid[player_move - 1] = sign


def check(player_moves):
    for move in winning_combos:
        if all(elem in player_moves for elem in move):
            return True
    return False


for i in range(9):
    make_a_move(player1_moves)
    if check(player1_moves):
        print('Player 1 won!')
        break

    make_a_move(player2_moves)
    if check(player2_moves):
        print('Player 2 won!')
        break

if not check(player1_moves) and not check(player2_moves):
    print('It is a tie!')  