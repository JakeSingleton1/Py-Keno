#Jacob Singleton 
#Casino Project: Keno
#80 numbers
# up to 20 picks
#https://en.wikipedia.org/wiki/Keno
#https://www.youtube.com/watch?v=X0T5ZR8vRzE -- How To Play Keno - Positively Vegas 
#https://www.youtube.com/watch?v=078DzWRRo8w -- How to play keno for beginners
#https://www.casino.org/keno/how-to-play/ - How to Play Keno - Casino.org
#https://www.playngo.com/games/keno - Play keno online 

#Note: While the casino games rules sheet I was handed said between 1 and 20 most all examples of the game being played that I found only chose 10 numbers for the pick , and then 20 numbers are drawn.
#P.S. Sorry if my comments look really long, I'm doing this project on my big monitor


import random  #Import random module to generate random numbers for the draw

# prompt user to select how many numbers they would like to play and what numbers they would like to choose for the draw
def select_numbers():
    while True:  #Condition controlled loop until we get a valid input that returns true
        try: #try and except to handle value errors
            number_select = int(input("How many numbers would you like to play (you can select up to 10)?: ")) # prompts the user to select the amount of numbers they would like to play
            if 1 <= number_select <= 10:  #Check if the selected number is within valid range between 1 and 10
                break
            else:
                print("Enter a number between 1 and 10") # error handling for invalid input in range
        except ValueError:
            print('Please enter a valid number') # error handling for an invalid input for anything other than a number

    player_numbers = []  # Store players chosen numbers in a list
    count = 0  #Keeps track of how many numbers the player has entered

    while count < number_select:  #Condition controlled loop to make sure 'count' variable reaches 'number_select'
        try:
            number = int(input(f"Enter a number between 1 and 80 {count + 1}: ")) #prompts user to enter the numbers they want to pick to match in the draw
            if 1 <= number <= 80 and number not in player_numbers:  # makes sure a valid number between 1 and 80 is chosen and is not entered twice using logical operators
                player_numbers.append(number)  # Adds the number to the list player_numbers if it is valid. 
                count += 1 # 'count' will remain at 0 and the condition will never be false and we will have an infinite loop, so we use +=1 to make sure count = count +1 instead of count = 0
            else:
                print("Pick a valid number that you have not chosen") # error handling to make sure a valid number is chosen
        except ValueError:
            print("Please enter a valid number.") # error handling to make sure a number is entered.

    return player_numbers  # return the players selected numbers for the draw

#prompt the user to place their bets for their selected numbers
def place_bet():
    while True:  # Loop until a valid bet is entered 
        try:
            bet = float(input("How much would you like to bet(minimum of $0.25 and maximum of $1000)? $"))  
            if 0.25 <= bet <= 1000:  # bet must be between 0.25 and 1000
                return bet  # Return bet amount 
            else:
                print('Please enter a number between $0.25 and $1000')
        except ValueError:
            print("Please enter a valid number for your bet")

#draw our 20 random numbers
def draw():
    numbers_drawn = []  #Store drawn numbers
    count = 0  #Count the drawn numbers, using this variable again since we don't need to store the value.
    while count < 20:  #Ensure 20 numbers are drawn
        number = random.randint(1, 80)  #selects 20 random integers between 1 and 80
        if number not in numbers_drawn:  #checks to make sure the number has not been drawn more than once
            numbers_drawn.append(number) #if the number is only drawn once, returns to the empty list we created "numbers_drawn"
            count += 1
    return numbers_drawn  # Return the drawn numbers to main

#match up the selected numbers and drawn numbers and calculate how much the player makes
def calculate_win(player_numbers, drawn_numbers, bet):
    matches = []  # Store the numbers the player matched in a list
    hit = 0  # Track the number of matches

    for number in player_numbers:  # For loop to iterate random numbers over the players numbers
        if number in drawn_numbers:  # Check if player's number is in drawn numbers
            matches.append(number) #stores the matched numbers in matches list
            hit += 1 # everytime a match is found our hit value will increase by 1

    # Payout table using if else statements

    if hit == 0: # no reward for 0 hits at my casino. Some casinos and lotteries you win big, like a $600 payout if you have 0 matches but I dont really get that.
        win = 0
    elif hit == 1: # no reward for matching 1 is most common among all payouts
        win = 0
    elif hit == 2: #The minimum you have to play to hit and win at most casinos is 2 numbers, so I started my payout at 2 hits
        win = 0.5 * bet
    elif hit == 3: # win your money back after 3 hits
        win = 1 * bet
    elif hit == 4: # increase payout as hits increase all the way up to 10
        win = 2 * bet
    elif hit == 5:
        win = 5 * bet
    elif hit == 6:
        win = 15 * bet
    elif hit == 7:
        win = 40 * bet
    elif hit == 8:
        win = 100 * bet
    elif hit == 9:
        win = 250 * bet
    elif hit == 10:
        win = 1000 * bet
    else:
        win = 10000 * bet  # 10 hits or more is gonna pay you 10,000 according to the video I watche so thats what I went with.

    return hit,win, matches



#main function to call all others
def main():
    total_winnings = 0  #starts our total winnings off as 0, and we will continue to add to this as we play
    total_spent = 0 #starts our total spent off as 0, and we will continue to add to this as we play

    while True: # loop for playing multiple games
        player_numbers = select_numbers()  #gets the players numbers and stores them in main
        bet = place_bet()  #get the players bet amount and store in main
        drawn_numbers = draw()  #draw our randoms
        hit, win, matches = calculate_win(player_numbers, drawn_numbers, bet)  #calculates amount of money won in game

        total_spent += bet #Adds our money spent from the current game to total_spent
        total_winnings += win # Adds our earnings from the current games win variable to the total winnings to keep track

        print('\n')
        print("Numbers drawn:", drawn_numbers)
        print("Your numbers:", player_numbers)
        print("Matched numbers:", matches)
        print(f"You matched {hit} numbers") 
        print(f"You won: ${win:.2f}")
        print(f"Your total winnings so far: ${total_winnings:.2f}")
        print(f"You have spent ${total_spent:.2f} so far")

        play_again = input("Would you like to play again? (y/n): ").lower() # prompts the user to see if they wanna continue playing
        if play_again != 'y':
            print(f"Thank you for playing! Your total winnings were: ${total_winnings:.2f}") #tells the users their total earnings while played
            break # exits the loop if they do not want to continue playing
    

# calls main to run the program
main()  
