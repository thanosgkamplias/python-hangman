"""
Project: Hangman Game
Author: Gkamplias Thanos
Date: January 2026
Description: 
    A text-based implementation of the classic Hangman game using Python.
    Features include input validation, cross-platform screen clearing, 
    and ASCII art integration.
"""


import random
import os
from hangman_art import logo, stages
from hangman_words import word_list

def clear_screen():
    """
    Clears the console screen based on the operating system.
    Windows uses 'cls', Unix-based systems use 'clear'.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

# --- GAME SETUP ---

# Initial screen clear and logo display
clear_screen()
print(logo)

# Randomly select a word from the imported list
chosen_word = random.choice(word_list)

# Set to store all unique guesses (prevents penalizing duplicate guesses)
guessed_letters = set()

# Initialize the display list with placeholders (underscores)
display = ["_"] * len(chosen_word)

# Game State Variables
game_over = False
lives = 6
current_stage_index = 0

# Initial display of the empty word
print(f"{' '.join(display)}")

# --- MAIN GAME LOOP ---

while not game_over:
    print(f'\n****************** {lives}/6 LIVES LEFT *******************')
    
    # User Input
    guess = input("Guess a letter: ").lower()

    # --- UI UPDATE ---
    # Clear the screen to refresh the game state visualization
    clear_screen()
    print(logo) 

    # --- 1. INPUT FORMAT VALIDATION ---
    # Ensure input is a single character and is an alphabet letter
    if len(guess) != 1 or not guess.isalpha():
        print("⚠️  Invalid input. Please enter a single letter.")
        print(f"{' '.join(display)}")
        print(stages[current_stage_index])
        continue
    
    # --- 2. HISTORY CHECK ---
    # Check if the user has already guessed this letter
    if guess in guessed_letters:
        print(f"⚠️  You've already guessed '{guess}'. Try another one.")
        print(f"{' '.join(display)}")
        print(stages[current_stage_index])
        continue # Skip the rest of the loop
    
    # Add valid new guess to history
    guessed_letters.add(guess)

    # --- GAME LOGIC ---
    
    # Check if the guessed letter is in the chosen word
    if guess in chosen_word:
        print(f"✅ Good job! '{guess}' is in the word.")
        
        # Update the display list at the correct indices
        for position in range(len(chosen_word)):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = guess
    else:
        # Incorrect guess handling
        print(f"❌ You guessed '{guess}', that's not in the word. You lose a life.")
        lives -= 1
        current_stage_index += 1
    
    # --- RENDER CURRENT STATE ---
    print(f"{' '.join(display)}")
    print(stages[current_stage_index])

    # --- WIN / LOSS CONDITIONS ---
    
    # Check for Win: No underscores left in the display
    if "_" not in display:
        game_over = True
        print("\n****************** YOU WIN! *******************")

    # Check for Loss: No lives left
    if lives == 0:
        game_over = True
        print(f"\n****************** GAME OVER *******************")
        print(f"The word was: '{chosen_word}'")