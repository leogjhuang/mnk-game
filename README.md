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
