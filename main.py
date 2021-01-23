import random


# Check if an input meets a set of criteria; return validated input
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
        if max_ is not None and input_ > max_:
            print(f"Input must be less than or equal to {max_}.")
        elif min_ is not None and input_ < min_:
            print(f"Input must be greater than or equal to {min_}.")
        elif range_ is not None and input_ not in range_:
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
        else:
            return input_


# Add visual separator to a string for improved readability; return updated string
def visual_separator(message=None):
    separator = "".join("=" for _ in range(42))
    if message is not None:
        return "\n".join((separator, message))
    return separator


class Grid:
    # Initialize grid's rows, columns, and win length; create a two-dimensional list of blank cells
    def __init__(self, column_count, row_count, consecutive_win_length):
        self.rows = range(row_count)
        self.columns = range(column_count)
        self.win_length = consecutive_win_length
        self.cells = [[" " for _ in self.columns] for _ in self.rows]

    # Reset each cell in the grid to empty
    def reset(self):
        self.cells = [[" " for _ in self.columns] for _ in self.rows]

    # Return true if there is a consecutive subsequence of symbols required for a win in a sequence
    def has_consecutive_identical_elements(self, sequence):
        if len(sequence) >= self.win_length:
            for i in range(len(sequence) - self.win_length + 1):
                subsequence = [sequence[j] for j in range(i, i + self.win_length)]
                if all(element == subsequence[0] for element in subsequence):
                    return True
        return False
    
    # Return true if each element of a row has been occupied by a player's symbol
    def is_horizontal_win(self, row_index, column_index):
        horizontal = [self.cells[row_index][column_index]]
        left_end_reached = False
        right_end_reached = False
        for i in range(1, self.win_length):
            if not left_end_reached:
                if column_index - i < 0:
                    left_end_reached = True
                else:
                    square = self.cells[row_index][column_index - i]
                    if square == " ":
                        left_end_reached = True
                    else:
                        horizontal.insert(0, square)
            if not right_end_reached:
                if column_index + i > self.columns.stop - 1:
                    right_end_reached = True
                else:
                    square = self.cells[row_index][column_index + i]
                    if square == " ":
                        right_end_reached = True
                    else:
                        horizontal.append(square)
            if left_end_reached and right_end_reached:
                break
        return self.has_consecutive_identical_elements(horizontal)

    # Return true if each element of a column has been occupied by a player's symbol
    def is_vertical_win(self, row_index, column_index):
        vertical = [self.cells[row_index][column_index]]
        left_end_reached = False
        right_end_reached = False
        for i in range(1, self.win_length):
            if not left_end_reached:
                if row_index - i < 0:
                    left_end_reached = True
                else:
                    square = self.cells[row_index - i][column_index]
                    if square == " ":
                        left_end_reached = True
                    else:
                        vertical.insert(0, square)
            if not right_end_reached:
                if row_index + i > self.rows.stop - 1:
                    right_end_reached = True
                else:
                    square = self.cells[row_index + i][column_index]
                    if square == " ":
                        right_end_reached = True
                    else:
                        vertical.append(square)
            if left_end_reached and right_end_reached:
                break
        return self.has_consecutive_identical_elements(vertical)

    # Return true if each element of a left diagonal has been occupied by a player's symbol
    def is_left_diagonal_win(self, row_index, column_index):
        left_diagonal = [self.cells[row_index][column_index]]
        left_end_reached = False
        right_end_reached = False
        for i in range(1, self.win_length):
            if not left_end_reached:
                if row_index - i < 0 or column_index - i < 0:
                    left_end_reached = True
                else:
                    square = self.cells[row_index - i][column_index - i]
                    if square == " ":
                        left_end_reached = True
                    else:
                        left_diagonal.insert(0, square)
            if not right_end_reached:
                if row_index + i > self.rows.stop - 1 or column_index + i > self.columns.stop - 1:
                    right_end_reached = True
                else:
                    square = self.cells[row_index + i][column_index + i]
                    if square == " ":
                        right_end_reached = True
                    else:
                        left_diagonal.append(square)
            if left_end_reached and right_end_reached:
                break
        return self.has_consecutive_identical_elements(left_diagonal)

    # Return true if each element of a left diagonal has been occupied by a player's symbol
    def is_right_diagonal_win(self, row_index, column_index):
        right_diagonal = [self.cells[row_index][column_index]]
        left_end_reached = False
        right_end_reached = False
        for i in range(1, self.win_length):
            if not left_end_reached:
                if row_index + i > self.rows.stop - 1 or column_index - i < 0:
                    left_end_reached = True
                else:
                    square = self.cells[row_index + i][column_index - i]
                    if square == " ":
                        left_end_reached = True
                    else:
                        right_diagonal.insert(0, square)
            if not right_end_reached:
                if row_index - i < 0 or column_index + i > self.columns.stop - 1:
                    right_end_reached = True
                else:
                    square = self.cells[row_index - i][column_index + i]
                    if square == " ":
                        right_end_reached = True
                    else:
                        right_diagonal.append(square)
            if left_end_reached and right_end_reached:
                break
        return self.has_consecutive_identical_elements(right_diagonal)

    # Return true if each element of a row, column, or diagonal has been occupied by a player's symbol
    def has_victory(self, row_index, column_index):
        return any([self.is_horizontal_win(row_index, column_index), self.is_vertical_win(row_index, column_index),
                    self.is_left_diagonal_win(row_index, column_index),
                    self.is_right_diagonal_win(row_index, column_index)])
    
    # Return true if each element of the grid has been occupied, i.e., a tie has occurred
    def is_full(self):
        for row in self.rows:
            for column in self.columns:
                if self.cells[row][column] == " ":
                    return False
        return True


class GravityDisabled(Grid):
    # Initialize gravity-disabled grid with the inherited constructor from the 'Grid' class
    def __init__(self, column_count, row_count, consecutive_win_length):
        super().__init__(column_count, row_count, consecutive_win_length)

    # Overload string representation of grid object with column and row indices; return the grid's cells in text format
    def __str__(self):
        lines = [" | ".join(self.cells[row][column] for column in self.columns) + f"  {row + 1}\n" for row in self.rows]
        splits = "+".join("---" for _ in self.columns)[1:-1] + "\n"
        column_indices = "   ".join(str(column + 1) for column in self.columns)
        return "\n".join((splits.join(lines), column_indices))

    # Add symbol to a cell with the given row_index and column_index
    def add_symbol(self, row_index, column_index, symbol):
        self.cells[row_index][column_index] = symbol
        return row_index, column_index

    # Return a list of tuples containing the row index and column index of cells that are blank, i.e., a legal move
    def legal_moves(self):
        return [(row, column) for column in self.columns for row in self.rows if self.cells[row][column] == " "]


class GravityEnabled(Grid):
    # Initialize gravity-enabled grid with the inherited constructor from the 'Grid' class
    def __init__(self, column_count, row_count, consecutive_win_length):
        super().__init__(column_count, row_count, consecutive_win_length)

    # Overload string representation of grid object with column indices; return the grid's cells in text format
    def __str__(self):
        lines = [" | ".join(self.cells[row][column] for column in self.columns) for row in self.rows]
        splits = "+".join("---" for _ in self.columns)[1:-1] + "\n"
        column_indices = "   ".join(str(column + 1) for column in self.columns)
        return "\n".join((splits.join(lines), column_indices))

    # Add symbol to a column such that it falls to the bottom of the grid according to gravity
    def add_symbol(self, column_index, symbol):
        for row_index in self.rows:
            if self.cells[self.rows.stop - row_index - 1][column_index] == " ":
                self.cells[self.rows.stop - row_index - 1][column_index] = symbol
                return self.rows.stop - row_index - 1, column_index

    # Return a list containing the column index of column that have a blank top cell
    def legal_moves(self):
        return [column for column in self.columns if self.cells[0][column] == " "]


class Player:
    # Initialize player's name and symbol; load record from player file if it exists
    def __init__(self, level, name, symbol):
        self.level = level
        self.name = name
        self.symbol = symbol
        try:
            with open(f"{self.name}.txt", "r") as file:
                record = [int(score) for score in file]
        except FileNotFoundError:
            record = [0, 0, 0]
        self.wins, self.losses, self.total_games = record

    # Save record to new or existing player file
    def save_record(self):
        record = (self.wins, self.losses, self.total_games)
        with open(f"{self.name}.txt", "w") as file:
            file.write("\n".join(str(score) for score in record))

    # Print player's record to the console
    def display_record(self):
        print(visual_separator(f"{self.name}'s statistics"))
        print(f"Wins: {self.wins}")
        print(f"Losses: {self.losses}")
        print(f"Total games: {self.total_games}")

    # Update player's record based on result
    def update_record(self, result):
        if result == "win":
            self.wins += 1
        elif result == "loss":
            self.losses += 1
        self.total_games += 1


class Local(Player):
    # Initialize local player object with the inherited constructor from the 'Player' class
    def __init__(self, level, name, symbol):
        super().__init__(level, name, symbol)

    # Validate local player's turn by verifying with the grid's legal moves; return tuple with row and column
    def take_turn(self, grid):
        legal_moves = grid.legal_moves()
        print(visual_separator(f"{self.name}'s turn"))
        while True:
            row_prompt = f"Enter the row you want to select ({grid.rows.start + 1}-{grid.rows.stop}): "
            column_prompt = f"Enter the column you want to select ({grid.columns.start + 1}-{grid.columns.stop}): "
            if isinstance(grid, GravityEnabled):
                column = validate_input(column_prompt, int, [column_index + 1 for column_index in grid.columns]) - 1
                if column in legal_moves:
                    return column
                print("The column you selected is full.")
            else:
                row = validate_input(row_prompt, int, [row_index + 1 for row_index in grid.rows]) - 1
                column = validate_input(column_prompt, int, [column_index + 1 for column_index in grid.columns]) - 1
                if (row, column) in legal_moves:
                    return row, column
                print("The cell you selected is occupied.")


class CPU(Player):
    # Initialize CPU player object with the inherited constructor
    def __init__(self, level, name, symbol):
        super().__init__(level, name, symbol)

    # Validate CPU player's turn by verifying with the grid's legal moves; return tuple with row and column
    def take_turn(self, grid):
        legal_moves = grid.legal_moves()
        print(visual_separator(f"{self.name}'s turn"))
        # Find optimal moves if the selected level of the CPU player is hard
        if self.level > 0:
            opponent_symbols = set()
            # Check for a potential winning move
            for row in grid.rows:
                for column in grid.columns:
                    if (row, column) in legal_moves:
                        grid.cells[row][column] = self.symbol
                        if grid.has_victory(row, column):
                            return row, column
                        else:
                            grid.cells[row][column] = " "
                    opponent_symbols.add(grid.cells[row][column])
            opponent_symbols.discard(" ")
            opponent_symbols.discard(self.symbol)
            # Check for a potential blocking move
            for row in grid.rows:
                for column in grid.columns:
                    if (row, column) in legal_moves:
                        for symbol in opponent_symbols:
                            grid.cells[row][column] = symbol
                            if grid.has_victory(row, column):
                                return row, column
                            else:
                                grid.cells[row][column] = " "
        # Randomly select a legal move if the selected level is easy or no optimal move is found
        return random.choice(legal_moves)


class Game:
    MIN_HEIGHT = MIN_WIDTH = MIN_WIN_LENGTH = 3
    MAX_HEIGHT = MAX_WIDTH = 9
    GRAVITY_OPTIONS = ["disabled", "enabled"]
    MIN_LOCAL_PLAYERS = 1
    MAX_LOCAL_PLAYERS = 2
    MAX_TOTAL_PLAYERS = 2
    LATIN_CHARACTERS = [chr(code_point) for code_point in range(33, 127)] + [""]
    SYMBOL_DEFAULTS = ["X", "O"]
    CPU_LEVELS = ["easy", "hard"]
    PLAY_AGAIN_OPTIONS = ["yes", "no"]

    # Initialize game variables
    def __init__(self):
        self.play = True
        self.players = []
        self.height = self.set_board_height()
        self.width = self.set_board_width()
        self.win_length = self.set_win_length()
        self.gravity_enabled = self.set_board_gravity()
        self.board = self.set_board_properties()
        self.local_player_count = self.set_local_player_count()

    # Ask the user for the height of the board
    def set_board_height(self):
        lower_bound = self.MIN_HEIGHT
        upper_bound = self.MAX_HEIGHT
        board_height_prompt = f"Set board height ({lower_bound}-{upper_bound}): "
        return validate_input(board_height_prompt, int, range(lower_bound, upper_bound + 1))

    # Ask the user for the width of the board
    def set_board_width(self):
        lower_bound = self.MIN_WIDTH
        upper_bound = self.MAX_WIDTH
        board_width_prompt = f"Set board width ({lower_bound}-{upper_bound}): "
        return validate_input(board_width_prompt, int, range(lower_bound, upper_bound + 1))

    # Ask the user for the length of consecutive symbols required to win
    def set_win_length(self):
        lower_bound = self.MIN_WIN_LENGTH
        upper_bound = max(self.height, self.width)
        win_length_prompt = f"Set length of consecutive symbols required to win ({lower_bound}-{upper_bound}): "
        return validate_input(win_length_prompt, int, range(lower_bound, upper_bound + 1))

    # Ask the user for the the gravity option for the board
    def set_board_gravity(self):
        gravity_options = "  ".join(f"[{i}] {self.GRAVITY_OPTIONS[i]}" for i in range(len(self.GRAVITY_OPTIONS)))
        gravity_prompt = f"Set the gravity option for the board ({gravity_options}): "
        return validate_input(gravity_prompt, int, range(len(self.GRAVITY_OPTIONS)))

    # Ask the user to set board properties
    def set_board_properties(self):
        if self.gravity_enabled:
            return GravityEnabled(self.height, self.width, self.win_length)
        return GravityDisabled(self.height, self.width, self.win_length)

    # Ask the user for the number of local players
    def set_local_player_count(self):
        lower_bound = self.MIN_LOCAL_PLAYERS
        upper_bound = self.MAX_LOCAL_PLAYERS
        local_player_count_prompt = f"Set the number of local players ({lower_bound}-{upper_bound}): "
        return validate_input(local_player_count_prompt, int, range(lower_bound, upper_bound + 1))

    # Initialize local and CPU player objects
    def initialize_players(self):
        for player_index in range(self.MAX_TOTAL_PLAYERS):
            if player_index < self.local_player_count:
                player_type = "local"
                player_subclass = Local
                player_level = 1
            else:
                player_type = "CPU"
                player_subclass = CPU
                level_options = "  ".join(f"[{i}] {self.CPU_LEVELS[i]}" for i in range(len(self.CPU_LEVELS)))
                level_prompt = f"Set the level of {player_type} player ({level_options}): "
                player_level = validate_input(level_prompt, int, range(len(self.CPU_LEVELS)))

            name_default = f"Player {player_index + 1}"
            name_prompt = f"Set the name of {player_type} player (default is '{name_default}'): "
            while True:
                player_name = validate_input(name_prompt, str) or name_default
                if player_name not in [player.name for player in self.players]:
                    break
                print("This name has already been taken.")

            symbol_default = self.SYMBOL_DEFAULTS[player_index]
            symbol_prompt = f"Set the symbol of {player_type} player (default is '{symbol_default}'): "
            while True:
                player_symbol = validate_input(symbol_prompt, str, self.LATIN_CHARACTERS) or symbol_default
                if player_symbol not in [player.symbol for player in self.players]:
                    break
                print("This symbol has already been taken.")

            self.players.append(player_subclass(player_level, player_name, player_symbol))

    # Save and display players' records after the game is finished
    def update_all_player_records(self):
        for player in self.players:
            player.save_record()
            player.display_record()

    # Ask the user whether they would like to play again
    def set_replay_status(self):
        play_again_prompt = f"{self.players[0].name}, would you like to play again? "
        return validate_input(play_again_prompt, str.lower, self.PLAY_AGAIN_OPTIONS) == self.PLAY_AGAIN_OPTIONS[0]

    # Loop until user chooses not to play again
    def run(self):
        self.initialize_players()
        while self.play:
            # Randomly determine which player's turn is first
            round_count = random.randint(1, 2)
            print(self.board)

            # Loop until the game is finished either due to a win or a tie
            while True:
                # Determine which player's turn it is this round
                round_count += 1
                current_player = self.players[round_count % 2]

                # Update the game board based on the position that the current player chooses
                row, column = self.board.add_symbol(current_player.take_turn(self.board), current_player.symbol)
                print(self.board)

                # Exit the game loop and update records if a win has occurred
                if self.board.has_victory(row, column):
                    print(visual_separator(f"{current_player.name} wins!"))
                    current_player.update_record("win")
                    self.players[1 - round_count % 2].update_record("loss")
                    break

                # Exit the game loop and update records if a tie has occurred
                elif self.board.is_full():
                    print(visual_separator("Game ends in a tie!"))
                    current_player.update_record("tie")
                    self.players[1 - round_count % 2].update_record("tie")
                    break

            self.update_all_player_records()
            self.play = self.set_replay_status()


if __name__ == "__main__":
    game = Game()
    game.run()
