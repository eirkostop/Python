#Python Simple Exercises
### Ladder
Create a program which asks the user for the number of floors and prints a ladder of * of equal floors. For example for floors = 5 it prints:
```
*
**
***
****
*****
```
### Pyramid
Create a program which asks the user for the number of floors and prints a symmetrical pyramid f * of equal floors. For examples for floors = 4 it prints:   
```
   *
  ***
 *****
*******
```
### Factorial
Create the function **factorial(n)** which calculates the factorial of the number n.
### Fibonacci
Create the function **fibonacci(n)** which returns the n'th fibonacci number.
### FizzBuzz
Create the procedure **FizzBuzz(n)** which prints the numbers [1 - n] or Fizz if the number is a multiple of 3, Buzz if the number is a multiple of 5, or FizzBuzz if the number is a multiple of both3 and 5.
### Custom Range
Create the function **custom_range(start, end, step)** which returns a list containing numbers in the range [start, end) and increase by step in each iteration.Larger than SumCreate the function larger_than_sum(L) which returns True if for every item of list L it holds thatL[i] > sum(L[i+1] + L[i+2] + ... + L[len(L)-1]]) or False otherwise.
### Palindrome
Create the function **isPalindrome(L)** which returns True if the list L is symmetrical or False otherwise. That is, L[0] == L[len(L)-1], L[1] == L[len(L)-2] etc.
### Rock - Scissors - Paper Person vs Computer
Create a game for one player. Player chooses between rock / scissors / paper and the same isdone by the computer in a random way. If someone wins the round he gets 1 point. The game is finished when someone gets 3 points.
### Hangman Player vs Computer
Create a game for one player against the computer. The computer has a 'word bank', a list ofwords, from where it chooses one for the game. The player tries to guess it, character by character with a maximum of 7 wrong guesses. If he manages to guess it he wins otherwise heloses. The game continually provides visual aid about the state of the game. 
### Hangman Player vs Player
Create a game for two players, player Red and player Blue. Every round, Red player chooses a secret word and the other player tries to guess it, character by character with maximum of 7 guesses. Then, player Blue chooses a word and Red tries to guess it. If both players guess theword, or both fail then the round is a tie, otherwise one players gets 1 point. The game ends when a player reaches 3 points. The game continually provides visual aid about the state of the game.