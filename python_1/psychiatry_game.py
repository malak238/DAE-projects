import random
import time
import os

# Categories of questions and answers
categories = {
    "Conditions": {
        "Schizophrenia": "A severe mental disorder characterized by delusions, hallucinations, and disorganized thinking.",
        "Depression": "A mood disorder causing persistent feelings of sadness, loss of interest, and hopelessness.",
        "Bipolar Disorder": "A mental health condition characterized by extreme mood swings that include emotional highs (mania) and lows (depression).",
        "ADHD": "Attention-Deficit/Hyperactivity Disorder, a condition marked by persistent patterns of inattention, hyperactivity, and impulsivity.",
        "Autism": "A developmental disorder characterized by difficulties with social interaction, communication, and repetitive behaviors.",
    },
    "Treatments": {
        "Cognitive Behavioral Therapy (CBT)": "A type of psychotherapy that helps individuals identify and challenge negative thought patterns and behaviors.",
        "Medication": "Use of pharmacological substances to treat various psychiatric conditions.",
        "Electroconvulsive Therapy (ECT)": "A medical treatment for severe depression that involves electrically induced seizures.",
        "Transcranial Magnetic Stimulation (TMS)": "A non-invasive treatment that uses magnetic fields to stimulate nerve cells in the brain.",
    },
    "Therapies": {
        "Psychoanalysis": "A therapeutic approach that explores unconscious thoughts and feelings to uncover underlying psychological issues.",
        "Dialectical Behavior Therapy (DBT)": "A type of psychotherapy that teaches mindfulness, emotional regulation, and interpersonal effectiveness.",
        "Exposure Therapy": "A psychological treatment that helps individuals gradually face and overcome their fears.",
        "Mindfulness-Based Cognitive Therapy (MBCT)": "A therapeutic approach combining cognitive behavioral therapy with mindfulness practices.",
    }
}

# Game settings
time_limit = 10  # Time in seconds for each question
rounds = 5  # Number of rounds in the game

# Global variables
score = 0
high_score = 0

# Function to load high score from a file
def load_high_score():
    global high_score
    if os.path.exists("high_score.txt"):
        with open("high_score.txt", "r") as file:
            high_score = int(file.read().strip())

# Function to save the high score to a file
def save_high_score():
    global high_score
    with open("high_score.txt", "w") as file:
        file.write(str(high_score))

# Function to display the question and handle the timer
def ask_question(category):
    global score
    term, description = random.choice(list(category.items()))
    print(f"\nDescription: {description}")
    
    start_time = time.time()
    guess = input(f"You have {time_limit} seconds to guess: ").strip()
    elapsed_time = time.time() - start_time
    
    if elapsed_time > time_limit:
        print("Time's up! You took too long.")
        return 0  # No points for time-out
    
    if guess.lower() == term.lower():
        print("Correct!")
        points = max(10 - int(elapsed_time), 1)  # Bonus for fast answers
        print(f"You earned {points} points.")
        return points
    else:
        print(f"Incorrect! The correct answer was: {term}.")
        return 0

# Function to play the game
def play_game():
    global score
    load_high_score()
    print("Welcome to the Psychiatry Game!")
    print(f"High Score: {high_score}\n")

    global score
    score = 0
    rounds_played = 0

    while rounds_played < rounds:
        rounds_played += 1
        print(f"\nRound {rounds_played}/{rounds}")
        
        # Randomly select a category
        category_name = random.choice(list(categories.keys()))
        print(f"Category: {category_name}")

        points_earned = ask_question(categories[category_name])
        score += points_earned

        print(f"Current score: {score}")

        if rounds_played < rounds:
            continue_game = input("Do you want to continue to the next round? (yes/no): ").strip().lower()
            if continue_game != 'yes':
                break
    
    # End of game
    print(f"\nGame over! Your total score: {score}")
    
    # Save high score if applicable
    if score > high_score:
        high_score = score
        save_high_score()
        print("New high score achieved!")

# Main entry point
if __name__ == "__main__":
    play_game()
