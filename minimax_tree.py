trees = {
    'A': { 
        'B': {
            'D': 3,
            'E': 5,
        },
        'C': {
            'F': {
                'I': {
                    'M': 0,
                    'N': 7
                },
                'J': 5
            },
            'G': {
                'K': 7,
                'L': 8
            },
            'H': 4
        }
    }
}
MIN = -1
MAX = 1
def minimax(state,player):
    if player == MAX:
        best = -99999 # Max will try to maximize this
    else:
        best = +99999 # Min will try to minimize this
    if type(state) is not dict:
        score = state
        return score
    # Loop through every possible situations
    for children in state:
        score = minimax(state[children], -player)
        if player == MAX: # if the player is MAX
            if score > best:
                best = score  # max value
        else:
            if score < best: # if the player is MIN
                best = score  # min value
    return best
print("Value of A if A is Max: ")
print(minimax(trees['A'], MIN))