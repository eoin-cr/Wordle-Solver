# Wordle solver
Word list is sorted from most common to least.  User enters letter info and it deletes any words that don't match the criteria and prints the top 10 that do.  In testing I just used it against random words in the list and it tends to get them in 3-4 guesses, and it's pretty rare for it not to get an answer.  If it says there are 0 words, try restarting the program and inputting everything again, when I've had that issue it's almost also a user error.  However, I have removed words from this list before in order to create my own wordle maker, so I removed about 9k uncommonly used words from the list.  Therefore, there's a chance there's a word missing that comes up.  If that happens feel free to make a pr to add the word!

I've added a file containing every word possible in wordle.  However, this file is sorted alphabetically, unlike the wiki-100k file which is sorted by most commonly used words first.  This may mean that some words are less likely to appear appear before more commonly used words as they come first alphabetically.  You can choose to use the wordle file list by changing which read file line is commented in the script

Link to the wordle site: https://www.powerlanguage.co.uk/wordle/

Personally I don't see the fun in using a program to beat the game, I just thought it would be a fun thing to code, but you do you ig.
