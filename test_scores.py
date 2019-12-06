#!/usr/bin/env python3

import statistics

def display_welcome():
    print("The Test Scores program")
    print("Enter 'x' to exit")
    print("")

# Getting said "Score"
def get_scores():
    scores = []

    while True:
        score = input("Enter test score: ")
        if score == "x":
            return  scores

        else:
            score = int(score)
            if score >= 0 and score <= 100:
                scores.append(score)

            else:
                print("Test score must be from 0 through 100. " +
                    "score discarded. Try again")

def process_scores(scores):
    
    # defines variables
    total = 0
    count = len(scores)
    median = 0
    

    # calculate total score
    for i in range(0, len(scores)):
        total = total + int(scores[i])

    # calculate average score
    average = total / count

    # calculate lowest score
    low_score = min(scores)

    # calcualte highest score
    high_score = max(scores)

    # calcualte median score
    median = statistics.median(scores)
                
    # format and display the result
    print()
    print("Score total:       ", total)
    print("Number of Scores:  ", count)
    print("Average Score:     ", average)
    print("Low Score:         ", low_score)
    print("High Score:        ", high_score)
    print("Median Score:      ", median)

#Displays in a more compact form factor
def main():
    display_welcome()
    scores = get_scores()
    process_scores(scores)
    print("")
    print("Bye!")

# if started as the main module, call the main function
if __name__ == "__main__":
    main()

