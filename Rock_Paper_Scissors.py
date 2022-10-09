#!/usr/bin/env python3
# Steven Vandegrift 2022

import random
import os

playing = True

def find_winner(player, com):
	if player == com:
		print("It's a tie!")
	elif player == 1 and com == 2: #Rock vs Paper
		print("ROCK VS PAPER")
		print("Paper beats Rock, Computer Wins!")
	elif player == 1 and com == 3: #Rock vs Scissors:
		print("ROCK VS SCISSORS")
		print("Rock beats Scissors, Player Wins!")
	elif player == 2 and com == 1: #Paper vs Rock
		print("PAPER VS ROCK")
		print("Paper beats Rock, Player Wins!")
	elif player == 2 and com == 3: #Paper vs Scissors
		print("PAPER VS SCISSORS")
		print("Scissors beats Paper, Computer Wins!")
	elif player == 3 and com == 1:
		print("SCISSORS VS ROCK")
		print("Rock beats Scissors, Computer Wins!")
	elif player == 3 and com == 2:
		print("PAPER VS SCISSORS")
		print("Scissors beats Paper, Player Wins!")

while playing: 
	user_choice = input("Pick 'Rock', 'Paper', or 'Scissors' \n")
	computer_choice = random.randint(1, 3)
	if user_choice.lower() == 'rock':
		user_choice = 1
	elif user_choice.lower() == 'paper':
		user_choice = 2
	elif user_choice.lower() == 'scissors':
		user_choice = 3
	else:
		print("That was not an option, try again")
		os.system('clear')
	find_winner(user_choice, computer_choice)
	keep_playing = input("Want to play again? 'y' or 'n'\n")
	os.system('clear')
	if keep_playing == 'n':
		playing = False
		
	