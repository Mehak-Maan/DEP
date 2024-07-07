import math

def calculate_score(state, misere):
    """
    Compute the score based on the remaining marbles.
    Each red marble is worth 2 points, and each blue marble is worth 3 points.
    In the misere version, the last move loses.
    """
    if misere and game_over(state):
        return -math.inf if state['red'] == 0 or state['blue'] == 0 else math.inf
    return 2 * state['red'] + 3 * state['blue']
def apply_move(state, move):
    """
    Execute the move on the current game state.
    Move specifies the color of marble and the amount to remove (always 1).
    """
    color, amount = move
    new_state = state.copy()  # Create a new state to avoid altering the original state
    new_state[color] -= amount
    return new_state

def game_over(state):
    """
    Determine if the game has ended.
    The game ends when either the red or blue pile is empty.
    """
    return state['red'] == 0 or state['blue'] == 0

def get_possible_moves(state):
    """
    Generate all possible moves from the current state.
    Moves involve removing one marble from either the red or blue pile.
    """
    if state['red'] > 0:
        yield ('red', 1)
    if state['blue'] > 0:
        yield ('blue', 1)

def red_blue_nim(state, alpha, beta, max_player, misere):
    """
    Minimax algorithm with alpha-beta pruning to decide the optimal move.
    """
    if game_over(state):
        score = calculate_score(state, misere)
        return score, None

    best_move = None

    for move in get_possible_moves(state):
        new_state = apply_move(state, move)
        eval, _ = red_blue_nim(new_state, alpha, beta, not max_player, misere)

        if max_player:
            if eval > alpha:
                alpha = eval
                best_move = move
        else:
            if eval < beta:
                beta = eval
                best_move = move

        if beta <= alpha:
            break

    return (alpha, best_move) if max_player else (beta, best_move)

def play_game():
    """
    Function to play the Red-Blue Nim game.
    Human player competes against the computer.
    """
    while True:
        game_type = input("Choose game type: standard or misere: ").strip().lower()
        if game_type in ['standard', 'misere']:
            break
        else:
            print("Invalid input. Please enter 'standard' or 'misere'.")

    misere = (game_type == 'misere')

    state = {'red': 5, 'blue': 6}
    print("Starting state:", state)

    while not game_over(state):
        _, computer_move = red_blue_nim(state, -math.inf, math.inf, True, misere)
        print("Computer's move:", computer_move)
        state = apply_move(state, computer_move)
        print("Current state:", state)

        if game_over(state):
            break

        valid_human_move = False
        while not valid_human_move:
            human_move_color = input("Choose a pile to take a marble from (red or blue): ")
            if human_move_color in state and state[human_move_color] > 0:
                valid_human_move = True
            else:
                print("Invalid move. Try again.")

        state = apply_move(state, (human_move_color, 1))
        print("Current state:", state)

    score = calculate_score(state, misere)
    if score == -math.inf:
        print("Human wins!")
    elif score == math.inf:
        print("Computer wins!")
    elif score > 0:
        print("Human wins with a score of", -score)
    elif score < 0:
        print("Computer wins with a score of", score)
    else:
        print("It's a tie!")

play_game()
