# Board Game with Q-Learning

In this term project you are required to develop a Machine Learning Application for the board game below.

Rules:
 - There is a 7x7 board and one piece for each player. Initial position of these pieces is shown in Figure 1.
![Ekran Alıntısı](https://user-images.githubusercontent.com/28456852/83419100-38b39c00-a42d-11ea-82a6-a231c1767c6a.PNG)

In this figure red square symbolizes player 1 and blue square symbolizes player 2 and always player 1 starts the game. On each turn current player makes two subsequent moves 
1. The player has to move his/her piece to one of its eight neighbors (The piece can be moved vertically, horizontally or diagonally.  It can’t be moved to a blocked square or to its opponent’s square) 
2. The player has to  block a square on the board (it can’t be an already blocked one or a square with a piece in it)
 If a player blocks a square,  then his/her piece also can’t be moved to that square.
Game ends when one of the players has no unblocked neighbor to move.

![Ekran Alıntısı](https://user-images.githubusercontent.com/28456852/83419404-b081c680-a42d-11ea-95fe-059de0abacaa.PNG)

### Starting the Game

The game will be played between AI and the  user. In the beginning, your program will input if the user will be player 1 or 2. If the user is player 1, then he/she will make the first move. Else the computer will make the first move.
### Computer’s Turn
Computer will first move its piece and print the coordinates of the new position. 
g5
 This means that computer has moved its piece to g5.
And then it will block a square from board and print the coordinates of that square.
c4
In this example computer blocks the square c4.
Then the current configuration of the board will be displayed.
### User’s  Turn
The user will type his/her move in same structure as the computer. First, the new coordinates of the piece will be given and after that the coordinates of the square that will be blocked. For example
b2 a4
This input means that the user moves his/her piece to b2 and blocks a4 from the board.
You can assume the user will always input correctly and make a legal move. (Obviously your AI system must do the same too!)
Your coordinate system must be same with the one used in Figure 1. Columns are represented with numbers between 1 and 7 and rows are represented with  letters between a-g. a1 is top left square and g7 is bottom right. First player starts at g4 and second player starts at a4.
