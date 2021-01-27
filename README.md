# The Game of m,n,k

## Description and end product
I am proposing a game for this final project titled The Game of MNK, based on the abstract mathematical board game often used in many branches of game theory. Essentially, a k-in-a-row game on an m·n board can be concisely referred to as an m,n,k-game. Two players will take turns choosing a position on the m·n board and placing their symbol within the square in that position. The winner of the game will be the first player who can place k of their symbols in a row without interference either vertically, horizontally, or diagonally. The game will allow players to choose the dimensions of the board and the length of the line required for a win. The innovative twist I will add to the game is the enabling of gravity, which players can toggle to be on or off. This allows for more complex gameplay and ensures variety and replayability within the game. Preset options will give players a sense of flexibility without needing to select customized settings, e.g., tic-tac-toe will be the 3,3,3-game and Connect Four will be the 7,6,4-game with gravity enabled.

## Program components
### Essential components
- [ ] Validate all numerical and text input with an error trapping function
- [ ] Create a board with size m·n and functions that return the board in text form
- [ ] Check the current status of a board and analyze if a win has occurred such that there are k symbols in a row horizontally, vertically, or diagonally if m = n
- [ ] Create the class Player with file streaming capabilities
- [ ] Create the subclass Local with input-taking capabilities for move selection
- [ ] Create the subclass CPU with randomized and semi-perfect move selection
- [ ] Construct game loop and initial setting prompts for m, n, and k
- [ ] Enable preset options for m, n, and k for popular m,n,k-games
- [ ] Create a gravity setting toggle that will force all symbols placed to fall toward the bottom of the board
### Extra components
- [ ] Create a graphical user-friendly menu that serves as the start of the game
- [ ] Enable the direction of gravity to be toward the top or sides of the board
- [ ] Enable the direction of gravity to be toward a particular area of the board, e.g. a corner or the centre
- [ ] nable a special gravity mode such that the direction of gravity rotates after each turn
- [ ] Enable three or more players in a game
- [ ] Construct a CPU player that plays perfectly in all solved m,n,k-games

## Functionality
I will dedicate this project to mastering object-oriented programming in Python, ensuring that most components of the game will be built through the use of classes and features like inheritance. Basic elements like if-statements and for-loops will be used effectively. Classes like Grid and Player will each involve complex methods that return different types and also call other methods. The main array generated in the project will be the game board itself, and I will use features such as list comprehension and splicing to guarantee efficient functionality within the game. Finally, I will handle player files with more intricate statistics such as “Game mode played most” and “Win percentage”. These unique game characteristics will help me demonstrate proficiency in many of Python’s useful features such as methods, arrays, and file streaming.

## Analysis
An (m,n,k)-game is played on a rectangular grid of size m x n, where m is the number of rows and n is the number of columns. Each player chooses a cell on the grid to place their symbol in alternating turns until one of the players manages to consecutively align k symbols horizontally, vertically, or diagonally. My project seeks to replicate this concept as a terminal application, introducing new variants that involve a gravity toggle, where symbols placed in the grid fall toward the lower horizontal edge such that each piece either lands on the bottom edge or on top of another piece.

The most essential goal in the completion of this final project is demonstrating the programming skills and principles I have learned throughout Computer Science 20. I will go about this goal by incorporating elements I’ve been taught such as file streaming and methods, while implementing the entire program using classes and objects. Some of the essential components of this project will be a flexible input validation function, gravity-enabled and gravity-disabled subclasses of a grid class with overloading capabilities, local and CPU player subclasses of a player class with file streaming capabilities, and, most importantly, a game class that connects the methods in each subclass to form a functional product. If time permits, extra components I may include are a graphical user-friendly menu, variable direction of gravity, and a semi-perfect AI (m,n,k)-game player.

The main social indicator of success will be related to the reaction of an audience after playing the game. If players are able to finish a game with increased appreciation and regard, along with a willingness to play again, the project has succeeded. On the other hand, a functional indicator of success for this game involves my ability as a programmer to code this according to my level of skill. The expectation is to reach 400 lines of code, using at least 10 different coding techniques that have been taught this semester.
