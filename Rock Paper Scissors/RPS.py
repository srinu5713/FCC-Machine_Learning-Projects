# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

def player(prev_play, opponent_history=[]):
    n = 5
    
    # Append opponent's move to history if valid
    if prev_play in ["R", "P", "S"]:
        opponent_history.append(prev_play)

    # Default guess
    guess = "R"

    if len(opponent_history) > n:
        # Extract the last n moves as a string
        last_n_moves = "".join(opponent_history[-n:])
        
        # Dictionary to count occurrences of patterns
        pattern_counts = {"R": 0, "P": 0, "S": 0}

        # Count occurrences of each pattern
        for i in range(len(opponent_history) - n):
            pattern = "".join(opponent_history[i:i + n])
            next_move = opponent_history[i + n]
            if pattern == last_n_moves:
                pattern_counts[next_move] += 1
        
        # Predict opponent's next move based on most frequent pattern
        if pattern_counts["R"] >= pattern_counts["P"] and pattern_counts["R"] >= pattern_counts["S"]:
            guess = "P"
        elif pattern_counts["P"] >= pattern_counts["R"] and pattern_counts["P"] >= pattern_counts["S"]:
            guess = "S"
        elif pattern_counts["S"] >= pattern_counts["R"] and pattern_counts["S"] >= pattern_counts["P"]:
            guess = "R"

    return guess
