# poker_sort
A solution that uses Python to sort the poker hands and find the winner between 2 players.

# About
1. Specific Poker rule details can be found in Poker Exercise pdf file.
2. As required, the solution only considers Ace as high only. (i.e. cannot be used as a low card below 2 in a straight).  
3. Due to short timeframe, the solution doesn't include the case when two hands really tie. (i.e. two hands having exact same ranking and card values but different suits, e.g. hand 1: 7C 6C 5C 9D 9H vs. hand 2: 7S 6S 5S 9C 9S)

# Running
This project requires Python 3 and a poker-hands data file.
*For Linux*: `cat poker-hands.txt | python3 poker_sort.py`
*For Windows PowerShell*: `Get-Content .\poker_hands.txt | python .\pocker_sort.py`

# Acknowledgements
I'd like to thank Peter Norvig(https://www.linkedin.com/in/pnorvig/) with his excellent Design of Computer Programs course(https://classroom.udacity.com/courses/cs212) and Brian Caffey(https://briancaffey.github.io/2018/01/02/checking-poker-hands-with-python.html/) as two main materials that I learned from when solving this challenge.  
