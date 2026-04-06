import math

board = [
    ['_', '_', '_'],
    ['_', '_', '_'],
    ['_', '_', '_']
]

def evaluate(b):
    for row in b:
        if row == ['O', 'O', 'O']:
            return 10
        if row == ['X', 'X', 'X']:
            return -10
    return 0


def minimax(board, depth, isMax):
    score = evaluate(board)

    if score == 10 or score == -10:
        return score

    if isMax:
        best = -math.inf

        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = 'O'
                    best = max(best, minimax(board, depth + 1, False))
                    board[i][j] = '_'

        return best

    else:
        best = math.inf

        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = 'X'
                    best = min(best, minimax(board, depth + 1, True))
                    board[i][j] = '_'

        return best