import random


# Adds visual separator to a string for improved readability; returns updated string
def visual_separator(message=None):
    separator = "".join("=" for _ in range(42))
    if message is not None:
        return "\n".join((separator, message))
    return separator


# Checks if an input meets a set of criteria; returns validated input
def validate_input(prompt="Enter a valid input: ", type_=None, range_=None, min_=None, max_=None):
    if range_ is not None and not range_:
        raise ValueError("argument for 'range_' is an empty sequence")
    if min_ is not None and max_ is not None and min_ > max_:
        raise ValueError("argument for 'min_' is greater than argument for 'max_'")
    while True:
        input_ = input(prompt)
        if type_ is not None:
            try:
                input_ = type_(input_)
            except ValueError:
                print(f"Input type must be {type_.__name__}.")
                continue
        if range_ is not None and input_ not in range_:
            if isinstance(range_, range):
                print(f"Input must be between {range_.start} and {range_.stop - 1}.")
            else:
                elements = [str(element) for element in range_]
                if len(range_) < 3:
                    selection = " or ".join(elements)
                else:
                    elements[-1] = " ".join(("or", elements[-1]))
                    selection = ", ".join(elements)
                print(f"Input must be {selection}.")
        elif min_ is not None and input_ < min_:
            print(f"Input must be greater than or equal to {min_}.")
        elif max_ is not None and input_ > max_:
            print(f"Input must be less than or equal to {max_}.")
        else:
            return input_


class Grid:
    # Initializes grid's rows and columns; creates a two-dimensional list of blank cells
    def __init__(self, column_count, row_count):
        self.columns = range(column_count)
        self.rows = range(row_count)
        self.cells = [[" " for _ in self.columns] for _ in self.rows]

    # Overloads string representation of grid object; returns the grid's cells in text format
    def __str__(self):
        lines = [" | ".join(self.cells[row][column] for column in self.columns) + f"\t{row + 1}\n" for row in self.rows]
        gridlines = "+".join("---" for _ in self.columns)[1:-1] + "\n"
        column_indices = "\n" + "   ".join(str(column + 1) for column in self.columns)
        return "\n" + gridlines.join(lines) + column_indices

    # Returns a list of tuples containing the row index and column index of cells that are blank, i.e., a legal move
    def legal_moves(self):
        return [(row, column) for column in self.columns for row in self.rows if self.cells[row][column] == " "]

    # Checks if each element of a row, column, or diagonal has been occupied by a player's symbol; returns true or false
    def check_win(self, row_index, column_index):
        horizontal = [self.cells[row_index][column] for column in self.columns]
        if horizontal.count(self.cells[row_index][0]) == self.columns.stop:
            return True
        vertical = [self.cells[row][column_index] for row in self.rows]
        if vertical.count(self.cells[0][column_index]) == self.rows.stop:
            return True
        if self.rows == self.columns:
            if row_index == column_index:
                left_diagonal = [self.cells[index][index] for index in self.rows]
                if left_diagonal.count(self.cells[0][0]) == self.rows.stop:
                    return True
            elif row_index + column_index + 1 == self.rows.stop:
                right_diagonal = [self.cells[index][self.rows.stop - 1 - index] for index in self.rows]
                if right_diagonal.count(self.cells[0][self.rows.stop - 1]) == self.rows.stop:
                    return True
        return False
    
    # Checks if each element of a row has been occupied by a player's symbol; returns true or false
    def is_horizontal_win(self, row_index, column_index):
        pass
    
    # Checks if each element of a column has been occupied by a player's symbol; returns true or false
    def is_vertical_win(self, row_index, column_index):

    # Checks if each element of the grid has been occupied, i.e., a tie has occurred; returns true or false
    def check_tie(self):
        for row in self.rows:
            for column in self.columns:
                if self.cells[row][column] == " ":
                    return False
        return True


class Player:
    # Initializes player's name and symbol; loads record from player file if it exists
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
        try:
            with open(f"{self.name}.txt", "r") as file:
                record = [int(score) for score in file]
        except FileNotFoundError:
            record = [0, 0, 0]
        self.wins, self.losses, self.total_games = record

    # Saves record to new or existing player file
    def save_record(self):
        record = (self.wins, self.losses, self.total_games)
        with open(f"{self.name}.txt", "w") as file:
            file.write("\n".join(str(score) for score in record))

    # Prints player's record to the console
    def display_record(self):
        print(visual_separator(f"{self.name}'s statistics"))
        print(f"Wins: {self.wins}")
        print(f"Losses: {self.losses}")
        print(f"Total games: {self.total_games}")

    # Updates player's record based on result
    def update_record(self, result):
        if result == "win":
            self.wins += 1
        elif result == "loss":
            self.losses += 1
        self.total_games += 1


class Local(Player):
    # Initializes local player object with the inherited constructor from the 'Player' class
    def __init__(self, name, symbol):
        super().__init__(name, symbol)

    # Validates local player's turn by verifying with the grid's legal moves; returns tuple with row and column
    def take_turn(self, grid):
        legal_moves = grid.legal_moves()
        print(visual_separator(f"{self.name}'s turn"))
        while True:
            row_prompt = "Enter the row you would like to select: "
            column_prompt = "Enter the column you would like to select: "
            row = validate_input(row_prompt, int, [row_index + 1 for row_index in grid.rows]) - 1
            column = validate_input(column_prompt, int, [column_index + 1 for column_index in grid.columns]) - 1
            if (row, column) in legal_moves:
                return row, column
            else:
                print("The cell you selected is occupied.")


class CPU(Player):
    # Initializes CPU player object with the inherited constructor; initializes name based on difficulty
    def __init__(self, difficulty, symbol, opponent_symbol):
        self.difficulty = difficulty
        if self.difficulty > 1:
            name = "HardBot"
        else:
            name = "EasyBot"
        super().__init__(name, symbol)
        self.opponent_symbol = opponent_symbol

    # Validates CPU player's turn by verifying with the grid's legal moves; returns tuple with row and column
    def take_turn(self, grid):
        legal_moves = grid.legal_moves()
        print(visual_separator(f"{self.name}'s turn"))
        # Finds optimal moves if the selected difficulty of the CPU player is hard
        if self.difficulty > 1:
            # Checks for a potential winning move
            for row in grid.rows:
                for column in grid.columns:
                    if (row, column) in legal_moves:
                        grid.cells[row][column] = self.symbol
                        if grid.check_win(row, column):
                            return row, column
                        else:
                            grid.cells[row][column] = " "
            # Checks for a potential blocking move
            for row in grid.rows:
                for column in grid.columns:
                    if (row, column) in legal_moves:
                        grid.cells[row][column] = self.opponent_symbol
                        if grid.check_win(row, column):
                            return row, column
                        else:
                            grid.cells[row][column] = " "
        # Randomly selects a legal move if the selected difficulty is easy or no optimal move is found
        return random.choice(legal_moves)


class Game:
    # Initializes variables for running the game
    play = True
    symbols = ["X", "O"]
    players = []

    # Initializes game prompts and messages
    length_prompt = "What length would you like your board to be (2 to 10)? "
    width_prompt = "What width would you like your board to be (2 to 10)? "
    mode_prompt = "How many players will be playing (1 or 2)? "
    name_prompt = "What would you like your name to be? "
    difficulty_prompt = "What difficulty would you like to choose (1 or 2)? "
    play_again_prompt = "Would you like to play again (yes or no)? "
    end_message = "Thanks for playing!"

    # Asks the user for the size of the board and the number of local players
    length = validate_input(length_prompt, int, range(2, 11))
    width = validate_input(width_prompt, int, range(2, 11))
    player_count = validate_input(mode_prompt, int, [1, 2])

    # Asks the user for the name(s) of the local player(s); creates local player object(s)
    for player_index in range(player_count):
        print(f"Player {player_index + 1}: ", end="")
        player_name = validate_input(name_prompt, str)
        print(f"Player {player_index + 1} is now {player_name}.")
        players.append(Local(player_name, symbols[player_index]))

    # Asks the user for the difficulty of the CPU player if there is only one player; creates CPU player object
    if player_count == 1:
        cpu_difficulty = validate_input(difficulty_prompt, int, [1, 2])
        players.append(CPU(cpu_difficulty, symbols[1], symbols[0]))
        print(f"Player 2 is now {players[1].name}.")

    # Loops until user chooses not to play again
    while play:
        # Randomly determines which player's turn is first
        round_count = random.randint(1, 2)
        game_board = Grid(length, width)
        print(game_board)

        # Loops until the game is finished either due to a win or a tie
        while True:
            # Determines which player's turn it is this round
            round_count += 1
            current_player = players[round_count % 2]

            # Updates the game board based on the position that the current player chooses
            position_row, position_column = current_player.take_turn(game_board)
            game_board.cells[position_row][position_column] = current_player.symbol
            print(game_board)

            # Exits the game loop and update records if a win has occurred
            if game_board.check_win(position_row, position_column):
                print(visual_separator(f"{current_player.name} wins!"))
                current_player.update_record("win")
                players[1 - round_count % 2].update_record("loss")
                break

            # Exits the game loop and update records if a tie has occurred
            elif game_board.check_tie():
                print(visual_separator("Game ends in a tie!"))
                current_player.update_record("tie")
                players[1 - round_count % 2].update_record("tie")
                break

        # Saves and displays players' records after the game is finished
        for player in players:
            player.save_record()
            player.display_record()

        # Asks the user whether they would like to play again
        play = validate_input(visual_separator(play_again_prompt), str.lower, ["yes", "no"]) == "yes"

    print(visual_separator(end_message))


if __name__ == "__main__":
    game = Game()
