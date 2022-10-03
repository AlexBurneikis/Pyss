from evaluate import evaluate
from search_captures import search_captures
from transposition import transpositions

def minimax(board, depth, alpha, beta):
    try:
        return transpositions[board.fen()]
    except:
        pass

    if depth == 0 or board.is_game_over():
        evaluation = evaluate(board)
        transpositions[board.fen()] = evaluation
        return evaluation
    if board.turn:
        maxEval = -9999
        for move in board.legal_moves:
            board.push(move)
            eval = minimax(board, depth - 1, alpha, beta)
            board.pop()
            maxEval = max(maxEval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return maxEval
    else:
        minEval = 9999
        for move in board.legal_moves:
            board.push(move)
            eval = minimax(board, depth - 1, alpha, beta)
            board.pop()
            minEval = min(minEval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return minEval