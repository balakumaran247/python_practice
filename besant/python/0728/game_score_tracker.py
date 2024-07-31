"""
Game Score Tracker
Description:
You are developing a game score tracker. The total score of a player is stored in a global variable, and each round's score is handled by a function using a local variable.

Task:
Define a global variable total_score to keep track of the player's total score.
Define a function play_round() that uses a local variable to store the score for each round.
Use the global keyword to update the total_score from within play_round().
Simulate multiple rounds and display the total score at the end.
"""
total_score = 0


def play_round():
    global total_score
    for ans in ("true", "false", "true"):
        choice = input("Guess true / false: ").lower()
        if ans == choice:
            total_score += 1
        else:
            total_score -= 1


rounds = int(input("enter the number of rounds to play: "))
for _ in range(rounds):
    play_round()
print(f"the total score: {total_score}")
