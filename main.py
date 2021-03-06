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
        return "\n".join((separator, str(message)))
    return separator


class Grid:
    # Initialize grid's rows, columns, and win length; create a two-dimensional list of blank cells
    def __init__(self, row_count, column_count, consecutive_win_length):
        self.rows = range(row_count)
        self.columns = range(column_count)
        self.win_length = consecutive_win_length
        self.cells = [[" " for _ in self.columns] for _ in self.rows]

    # Reset each cell in the grid to be empty
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
    def is_horizontal_win(self, row_index, column_index, symbol):
        horizontal = [symbol]
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
    def is_vertical_win(self, row_index, column_index, symbol):
        vertical = [symbol]
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
    def is_left_diagonal_win(self, row_index, column_index, symbol):
        left_diagonal = [symbol]
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

    # Return true if each element of a right diagonal has been occupied by a player's symbol
    def is_right_diagonal_win(self, row_index, column_index, symbol):
        right_diagonal = [symbol]
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
    def has_victory(self, row_index, column_index, symbol):
        position = (row_index, column_index, symbol)
        return any([self.is_horizontal_win(*position), self.is_vertical_win(*position),
                    self.is_left_diagonal_win(*position), self.is_right_diagonal_win(*position)])
    
    # Return true if each element of the grid has been occupied, i.e., a tie has occurred
    def is_full(self):
        for row_index in self.rows:
            for column_index in self.columns:
                if self.cells[row_index][column_index] == " ":
                    return False
        return True


class GravityDisabled(Grid):
    # Initialize gravity-disabled grid with the inherited constructor from the 'Grid' class
    def __init__(self, row_count, column_count, consecutive_win_length):
        super().__init__(row_count, column_count, consecutive_win_length)

    # Overload string representation of grid object with column and row indices; return the grid's cells in text format
    def __str__(self):
        grid_cells = ["\t" + " | ".join(self.cells[row_index][column_index] for column_index in self.columns)
                      + f"  {row_index + 1}\n" for row_index in self.rows]
        grid_lines = "\t" + "+".join("---" for _ in self.columns)[1:-1] + "\n"
        column_labels = "\t" + "   ".join(str(column_index + 1) for column_index in self.columns)
        return "\n".join((grid_lines.join(grid_cells), column_labels))

    # Add symbol to a cell with the given row index and column index; return the given row index and column index
    def add_symbol(self, row_index, column_index, symbol):
        self.cells[row_index][column_index] = symbol
        return row_index, column_index

    # Return a list of tuples containing the row index and column index of cells that are blank, i.e., a legal move
    def legal_moves(self):
        return [(row_index, column_index) for column_index in self.columns for row_index in self.rows
                if self.cells[row_index][column_index] == " "]


class GravityEnabled(Grid):
    # Initialize gravity-enabled grid with the inherited constructor from the 'Grid' class
    def __init__(self, row_count, column_count, consecutive_win_length):
        super().__init__(row_count, column_count, consecutive_win_length)

    # Overload string representation of grid object with column indices; return the grid's cells in text format
    def __str__(self):
        grid_cells = ["\t" + " | ".join(self.cells[row_index][column_index] for column_index in self.columns) + "\n"
                      for row_index in self.rows]
        grid_lines = "\t" + "+".join("---" for _ in self.columns)[1:-1] + "\n"
        column_labels = "\t" + "   ".join(str(column_index + 1) for column_index in self.columns)
        return "\n".join((grid_lines.join(grid_cells), column_labels))

    # Add symbol to a column such that it falls to the bottom of the grid according to gravity; return new indices
    def add_symbol(self, _, column_index, symbol):
        for row_index in self.rows:
            if self.cells[self.rows.stop - row_index - 1][column_index] == " ":
                self.cells[self.rows.stop - row_index - 1][column_index] = symbol
                return self.rows.stop - row_index - 1, column_index

    # Return a list containing the row index and column index of all legal moves
    def legal_moves(self):
        legal_moves = []
        for column_index in self.columns:
            for row_index in self.rows:
                if self.cells[self.rows.stop - row_index - 1][column_index] == " ":
                    legal_moves.append((self.rows.stop - row_index - 1, column_index))
                    break
        return legal_moves


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
        print(visual_separator(f"{self.name} ({self.symbol})"))
        while True:
            row_prompt = f"Enter the row you want to select ({grid.rows.start + 1}-{grid.rows.stop}): "
            column_prompt = f"Enter the column you want to select ({grid.columns.start + 1}-{grid.columns.stop}): "
            if isinstance(grid, GravityEnabled):
                column = validate_input(column_prompt, int, [column_index + 1 for column_index in grid.columns]) - 1
                if column in [position[1] for position in legal_moves]:
                    return 0, column
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
        print(visual_separator(f"{self.name} ({self.symbol})"))
        # Find optimal moves if the selected level of the CPU player is hard
        if self.level > 0:
            # Check for a potential winning move
            for row_index, column_index in legal_moves:
                if grid.has_victory(row_index, column_index, self.symbol):
                    print(f"Row: {row_index + 1}\nColumn: {column_index + 1}")
                    return row_index, column_index
            # Check for a potential blocking move
            opponent_symbols = set(grid.cells[row_index][column_index]
                                   for column_index in grid.columns for row_index in grid.rows
                                   if grid.cells[row_index][column_index] not in (" ", self.symbol))
            for row_index, column_index in legal_moves:
                for opponent_symbol in opponent_symbols:
                    if grid.has_victory(row_index, column_index, opponent_symbol):
                        print(f"Row: {row_index + 1}\nColumn: {column_index + 1}")
                        return row_index, column_index
        # Randomly select a legal move if the selected level is easy or no optimal move is found
        row_index, column_index = random.choice(legal_moves)
        print(f"Row: {row_index + 1}\nColumn: {column_index + 1}")
        return row_index, column_index


class Game:
    MIN_HEIGHT = MIN_WIDTH = MIN_WIN_LENGTH = 3
    MAX_HEIGHT = MAX_WIDTH = 9
    GRAVITY_MODES = ["disabled", "enabled"]
    BOARD_MODES = ["custom", "tic-tac-toe", "Connect Four", "Gomoku"]
    BOARD_MODES_SETTINGS = [None, (3, 3, 3, 0), (6, 7, 4, 1), (9, 9, 5, 0)]
    MIN_LOCAL_PLAYERS = 1
    MAX_LOCAL_PLAYERS = 2
    MAX_TOTAL_PLAYERS = 2
    LATIN_CHARACTERS = [chr(code_point) for code_point in range(33, 127)] + [""]
    SYMBOL_DEFAULTS = ["X", "O"]
    CPU_LEVELS = ["easy", "hard"]
    PLAY_AGAIN_MODES = ["yes", "no"]

    # Initialize game variables
    def __init__(self):
        self.play = True
        self.players = []
        self.board = self.set_board_options()
        self.local_player_count = self.set_local_player_count()

    # Ask the user for the height of the board; return height
    def set_board_height(self):
        lower_bound = self.MIN_HEIGHT
        upper_bound = self.MAX_HEIGHT
        board_height_prompt = f"Set board height ({lower_bound}-{upper_bound}): "
        return validate_input(board_height_prompt, int, range(lower_bound, upper_bound + 1))

    # Ask the user for the width of the board; return width
    def set_board_width(self):
        lower_bound = self.MIN_WIDTH
        upper_bound = self.MAX_WIDTH
        board_width_prompt = f"Set board width ({lower_bound}-{upper_bound}): "
        return validate_input(board_width_prompt, int, range(lower_bound, upper_bound + 1))

    # Ask the user for the length of consecutive symbols required to win; return win length
    def set_win_length(self, board_height, board_width):
        lower_bound = self.MIN_WIN_LENGTH
        upper_bound = max(board_height, board_width)
        win_length_prompt = f"Set length of consecutive symbols required to win ({lower_bound}-{upper_bound}): "
        return validate_input(win_length_prompt, int, range(lower_bound, upper_bound + 1))

    # Ask the user for the the gravity option for the board; return gravity toggle
    def set_board_gravity(self):
        gravity_options = "  ".join(f"[{mode}] {self.GRAVITY_MODES[mode]}" for mode in range(len(self.GRAVITY_MODES)))
        gravity_prompt = f"Set the gravity option for the board ({gravity_options}): "
        return validate_input(gravity_prompt, int, range(len(self.GRAVITY_MODES)))

    # Ask the user to set board properties; return GravityEnabled or GravityDisabled object
    def set_board_options(self):
        board_options = "  ".join(f"[{mode}] {self.BOARD_MODES[mode]}" for mode in range(len(self.BOARD_MODES)))
        board_prompt = f"Choose a preset or custom option for the board ({board_options}): "
        mode = validate_input(board_prompt, int, range(len(self.BOARD_MODES)))
        if self.BOARD_MODES[mode] == "custom":
            height = self.set_board_height()
            width = self.set_board_width()
            win_length = self.set_win_length(height, width)
            gravity_enabled = self.set_board_gravity()
        else:
            height, width, win_length, gravity_enabled = self.BOARD_MODES_SETTINGS[mode]
        if gravity_enabled:
            return GravityEnabled(height, width, win_length)
        return GravityDisabled(height, width, win_length)

    # Ask the user for the number of local players; return local player count
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
                # Set the level of the player if the player is CPU
                level_options = "  ".join(f"[{mode}] {self.CPU_LEVELS[mode]}" for mode in range(len(self.CPU_LEVELS)))
                level_prompt = f"Set the level of {player_type} player ({level_options}): "
                player_level = validate_input(level_prompt, int, range(len(self.CPU_LEVELS)))
            # Set the name of the player
            name_default = f"Player {player_index + 1}"
            name_prompt = f"Set the name of {player_type} player (default is '{name_default}'): "
            while True:
                player_name = validate_input(name_prompt, str) or name_default
                if player_name not in [player.name for player in self.players]:
                    break
                print("This name has already been taken.")
            # Set the symbol of the player
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

    # Exit game loop and update records if a win or tie has occurred; return true if game has finished
    def game_finished(self, row_index, column_index, player, round_count):
        if self.board.has_victory(row_index, column_index, player.symbol):
            print(visual_separator(f"{player.name} wins!"))
            player.update_record("win")
            self.players[1 - round_count % 2].update_record("loss")
            return True
        elif self.board.is_full():
            print(visual_separator("Game ends in a tie!"))
            player.update_record("tie")
            self.players[1 - round_count % 2].update_record("tie")
            return True
        return False

    # Ask the user whether they would like to play again; return true if user would like to play again
    def set_replay_status(self, player):
        play_again_prompt = f"{player.name}, would you like to play again? "
        return validate_input(play_again_prompt, str.lower, self.PLAY_AGAIN_MODES) == self.PLAY_AGAIN_MODES[0]

    # Loop until user chooses not to play again
    def run(self):
        self.initialize_players()
        while self.play:
            # Randomly determine which player's turn is first
            self.board.reset()
            round_count = random.randint(1, 2)
            print(visual_separator(self.board))
            # Loop until the game is finished either due to a win or a tie
            while True:
                # Determine which player's turn it is this round
                round_count += 1
                current_player = self.players[round_count % 2]
                # Update the game board based on the position that the current player chooses
                row, column = self.board.add_symbol(*current_player.take_turn(self.board), current_player.symbol)
                print(visual_separator(self.board))
                if self.game_finished(row, column, current_player, round_count):
                    break
            self.update_all_player_records()
            self.play = self.set_replay_status(self.players[0])


if __name__ == "__main__":
    game = Game()
    game.run()
