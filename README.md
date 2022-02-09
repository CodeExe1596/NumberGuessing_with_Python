# Number Guessing Program 
## Beginner Project using Python

### Description 

A Simple beginner Project in which user chooses 1 number among 3 generated randomdly.

- If the right number is typed : Game finished with Win .
- If the wrong Number is typed : Game Over with possibility to retry or quit .
- If none of the 3 numbers is typed : Loop until user types one of those .

### Features

Using _uniform()_ method from the module "random.py" to generate random numbers.

Basic knowledge of Python fundamental concepts (Functions, Loops, lists, tuples ,...)

### Requirements 

Having Python 3.x installed in computer with basic modules.

### Execution Sample 

Win the Game :

~~~~~sh
Choose a Number 84 , 98 , 85 : 98 # User Input 
The Number 98 belongs to the List
Congratulations ! You have won the Game !


Process finished with exit code 0
~~~~~~

Loose the Game : 

~~~~~sh 
Choose a Number 6 , 38 , 41 :  6 # User Input 
The Number 6 belongs to the List 
Sorry ! The Right Number was 38 
Retry the Game ? Y/N : P # User Input 
Please Type 'Y' to retry the Game or 'N' to quit !
Retry the Game ? Y/N : Y # User Input 
Game has been Reset !
Choose a Number 42 , 64 , 68 : 64 # User Input 
The Number 64 belongs to the List 
Sorry ! The Right Number was 68
Retry the Game ? Y/N : N
Closing the Game 


Process finished with exit code 0
~~~~~~

Type a Number not in the List : 

~~~~~~~sh 
Choose a Number 42 , 78 , 90 : 12 # User Input 
Number not in List ! Try Again ! Choose a Number 42 , 78 , 90 : 32 # User Input
Number not in List ! Try Again ! Choose a Number 42 , 78 , 90 : 90 # User Input 
The Number 90 belongs to the List 
Congratulations ! You have won the Game !


Process finished with exit code 0
~~~~~~~~