#Leon Luong 69139013 Lab section 9


class InvalidMoveError(Exception):
    pass

class GameOverError(Exception):
    pass


class Othello:
    def __init__(self):
        "Sets the turn, winner, discs, rule, and board attributes."
        self.TURN = 'B'
        self.WINNER = 'NONE'
        self.RULE = ">"
        self.FLIP = 'INVALID'
        self.black_discs = 0
        self.white_discs = 0
        self._othello = []
        

    """def start(self, rows: int, columns: int, first_player: str, top_right_player: int, rule: int):
        "Decides the number of rows, columns, first player, top right player, rule, and makes the board."
        self.NUMBER_OF_ROWS = rows
        self.NUMBER_OF_COLUMNS = columns
        for row_num in range(self.NUMBER_OF_ROWS):
            self._othello.append([])
            for col_num in range(self.NUMBER_OF_COLUMNS):
                self._othello[row_num].append('.')
                
        self._decide_first_player(first_player)
        self._decide_arrangement(top_right_player)
        self._decide_rules(rule)"""

    def start(self):
        self.NUMBER_OF_ROWS = 6
        self.NUMBER_OF_COLUMNS = 6
        self._othello = [['.','.','.','.','.','B'],
                         ['.','.','.','W','W','.'],
                         ['.','.','.','W','.','.'],
                         ['.','.','.','.','W','.'],
                         ['.','.','.','.','B','.'],
                         ['.','.','.','.','.','.']
                         ]
          

    def _decide_first_player(self, first_player: int):
        "Decides who goes first."
        if first_player == 'W':
            self.TURN = 'W'
        else:
            pass
        

    def _decide_arrangement(self, top_left_player: int):
        "Decides where the starting discs are arranged."
        if top_left_player == 'W':
            self._othello[int(self.NUMBER_OF_ROWS * 0.5)][int(self.NUMBER_OF_COLUMNS * 0.5) - 1] = 'B'
            self._othello[int(self.NUMBER_OF_ROWS * 0.5) - 1][int(self.NUMBER_OF_COLUMNS * 0.5)] = 'B'
            self._othello[int(self.NUMBER_OF_ROWS * 0.5)][int(self.NUMBER_OF_COLUMNS * 0.5)] = 'W'
            self._othello[int(self.NUMBER_OF_ROWS * 0.5) - 1][int(self.NUMBER_OF_COLUMNS * 0.5) - 1] = 'W'

        else:
            self._othello[int(self.NUMBER_OF_ROWS * 0.5)][int(self.NUMBER_OF_COLUMNS * 0.5) - 1] = 'W'
            self._othello[int(self.NUMBER_OF_ROWS * 0.5) - 1][int(self.NUMBER_OF_COLUMNS * 0.5)] = 'W'
            self._othello[int(self.NUMBER_OF_ROWS * 0.5)][int(self.NUMBER_OF_COLUMNS * 0.5)] = 'B'
            self._othello[int(self.NUMBER_OF_ROWS * 0.5) - 1][int(self.NUMBER_OF_COLUMNS * 0.5) - 1] = 'B'            

        
    def _decide_rules(self, rule: str):
        "Decides how to pick the winner."
        if rule == "<":
            self.RULE = "<"
        else:
            pass


    def gameplay(self):
        "Runs through the game until a winner is decided."
        try:
            while True:
                self.FLIP == 'INVALID'
                if self._check_for_possible_moves() == "GAME_OVER":
                    raise GameOverError
                self.black_discs = 0
                self.white_discs = 0
                self._count_discs()
                self._show_board()
                self._show_turn()
                self._make_move()
                if self._check_for_open_cells() == []:
                    raise GameOverError
                
        except GameOverError:
            self._show_winner()
            

            
    def _make_move(self):
        "Takes the input and makes a move on the board."
        while True:
            try:
                pick_move = input()
                row = int(pick_move.split(" ")[0]) - 1
                col = int(pick_move.split(" ")[1]) - 1
                if row <= self.NUMBER_OF_ROWS and col <= self.NUMBER_OF_COLUMNS:
                    if self._othello[row][col] == '.':
                        self._flip(row, col)
                        self._flip_turn(self.TURN)  
                        print('VALID')
                        return
                    else:
                        print("INVALID")
            
            except InvalidMoveError:
                print("INVALID")
                
            except ValueError:
                print("INVALID")



    def _flip(self, row: int, col: int):
        "Takes a move and flips the discs in every direction if valid."
        self.FLIP = 'INVALID'
        self._flip_up(row, col)
        self._flip_left(row, col)
        self._flip_up_left(row, col)
        try:
            self._othello[row + 1][col]
        except IndexError:
            pass
        else:
            self._flip_down(row, col)
            self._flip_down_left(row, col)
        
        try:
            self._othello[row][col + 1]
        except IndexError:
            pass
        else:
            self._flip_right(row, col)
            self._flip_up_right(row, col)

        try:
            self._othello[row + 1][col + 1]
        except IndexError:
            pass
        else:
            self._flip_down_right(row, col)


        if self.FLIP == 'VALID':   
            self._othello[row][col] = self.TURN
        else:
            raise InvalidMoveError



    def _check_flip_up(self, row: int, col: int):
        "Takes a move and checks if discs can flip in the up direction."
        self._up_list = []
        if self._othello[row - 1][col] == self._opposite_turn(self.TURN):
            for num in range(1, row + 1):
                if self._othello[row - num][col] == self.TURN:
                    for flip_num in range(1, num):
                        if self._othello[row - flip_num][col] == self.TURN:
                            break
                        else:
                            self._up_list.append(self._othello[row - flip_num][col])
                            
        if '.' not in self._up_list:
            if self._up_list != []:
                self.FLIP = 'VALID'
                
                            

    def _flip_up(self, row: int, col: int):
        "Flips the discs in the up direction."
        self._check_flip_up(row, col)
        if '.' not in self._up_list:
            if self._up_list != []:
                if self._othello[row - 1][col] == self._opposite_turn(self.TURN):
                    for num in range(1, row + 1):
                        if self._othello[row - num][col] == self.TURN:
                            for flip_num in range(1, num):
                                if self._othello[row - flip_num][col] == self._opposite_turn(self.TURN):
                                    self._othello[row - flip_num][col] = self.TURN
                                elif self._othello[row - flip_num][col] == self.TURN:
                                    return



    def _check_flip_down(self, row: int, col: int):
        "Takes a move and checks if discs can flip in the down direction."
        self._down_list = []
        if self._othello[row + 1][col] == self._opposite_turn(self.TURN):            
            for num in range(1, self.NUMBER_OF_ROWS - row - 1):
                if self._othello[row + num][col] == self.TURN:
                    for flip_num in range(1, num):
                        if self._othello[row + flip_num][col] == self.TURN:
                            break
                        else:
                            self._down_list.append(self._othello[row + flip_num][col])
     
        if '.' not in self._down_list:
            if self._down_list != []:
                self.FLIP = 'VALID'
                            
                        
    def _flip_down(self, row: int, col: int):
        "Flips the discs in the down direction."
        self._check_flip_down(row, col)
        if '.' not in self._down_list:
            if self._down_list != []:
                if self._othello[row + 1][col] == self._opposite_turn(self.TURN):            
                    for num in range(1, self.NUMBER_OF_ROWS - row - 1):
                        if self._othello[row + num][col] == self.TURN:
                            for flip_num in range(1, num):
                                if self._othello[row + flip_num][col] == self._opposite_turn(self.TURN):
                                    self._othello[row + flip_num][col] = self.TURN
                                elif self._othello[row + flip_num][col] == self.TURN:
                                    return          



    def _check_flip_left(self, row: int, col: int):
        "Takes a move and checks if discs can flip in the left direction."
        self._left_list = []
        if self._othello[row][col - 1] == self._opposite_turn(self.TURN):
            for num in range(1, col + 1):
                if self._othello[row][col - num] == self.TURN:
                    for flip_num in range(1, num):
                        if self._othello[row][col - flip_num] == self.TURN:
                            break
                        else:
                            self._left_list.append(self._othello[row][col - flip_num])
        if '.' not in self._left_list:
            if self._left_list != []:
                self.FLIP = 'VALID'
    

    def _flip_left(self, row: int, col: int):
        "Flips the discs in the left direction."
        self._check_flip_left(row, col)
        if '.' not in self._left_list:
            if self._left_list != []:
                if self._othello[row][col - 1] == self._opposite_turn(self.TURN):
                    for num in range(1, col + 1):
                        if self._othello[row][col - num] == self.TURN:
                            for flip_num in range(1, num):
                                if self._othello[row][col - flip_num] == self._opposite_turn(self.TURN):
                                    self._othello[row][col - flip_num] = self.TURN
                                elif self._othello[row][col - flip_num] == self.TURN:
                                    return


    def _check_flip_right(self, row: int, col: int):
        "Takes a move and checks if discs can flip in the right direction."
        self._right_list = []
        if self._othello[row][col + 1] == self._opposite_turn(self.TURN):
            for num in range(1, self.NUMBER_OF_COLUMNS - col):
                if self._othello[row][col + num] == self.TURN:
                    for flip_num in range(1, num):
                        if self._othello[row][col + flip_num] == self.TURN:
                            break
                        else:
                            self._right_list.append(self._othello[row][col + flip_num])
        if '.' not in self._right_list:
            if self._right_list != []:
                self.FLIP = 'VALID'
    

    def _flip_right(self, row: int, col: int):
        "Flips the discs in the right direction."
        self. _check_flip_right(row, col)
        if '.' not in self._right_list:
            if self._right_list != []:
                if self._othello[row][col + 1] == self._opposite_turn(self.TURN):
                    for num in range(1, self.NUMBER_OF_COLUMNS - col):
                        if self._othello[row][col + num] == self.TURN:
                            for flip_num in range(1, num):
                                if self._othello[row][col + flip_num] == self._opposite_turn(self.TURN):
                                    self._othello[row][col + flip_num] = self.TURN
                                elif self._othello[row][col + flip_num] == self.TURN:
                                    return


    def _check_flip_up_left(self, row: int, col: int):
        "Takes a move and checks if discs can flip in the up left direction."
        self._up_left_list = []
        if self._othello[row - 1][col - 1] == self._opposite_turn(self.TURN):
            for num in range(1, min(row, col) + 1):
                if self._othello[row - num][col - num] == self.TURN:
                    for flip_num in range(1, num):
                        if self._othello[row - flip_num][col - flip_num] == self.TURN:
                            break
                        else:
                            self._up_left_list.append(self._othello[row - flip_num][col - flip_num])
        if '.' not in self._up_left_list:
            if self._up_left_list != []:
                self.FLIP = 'VALID'


    def _flip_up_left(self, row: int, col: int):
        "Flips the discs in the up left direction."
        self._check_flip_up_left(row, col)
        if '.' not in self._up_left_list:
            if self._up_left_list != []:
                if self._othello[row - 1][col - 1] == self._opposite_turn(self.TURN):
                    for num in range(1, min(row, col) + 1):
                        if self._othello[row - num][col - num] == self.TURN:
                            for flip_num in (range(1, num)):
                                if self._othello[row - flip_num][col - flip_num] == self._opposite_turn(self.TURN):
                                    self._othello[row - flip_num][col - flip_num] = self.TURN
                                elif self._othello[row - flip_num][col - flip_num] == self.TURN:
                                    return



    def _check_flip_up_right(self, row: int, col: int):
        "Takes a move and checks if discs can flip in the up right direction."
        self._up_right_list = []        
        try:
            if self._othello[row - 1][col + 1] == self._opposite_turn(self.TURN):
                for num in range(1, min(self.NUMBER_OF_ROWS, self.NUMBER_OF_COLUMNS) + 1):
                    if row - num < 0:
                        return
                    else:
                        if self._othello[row - num][col + num] == self.TURN:
                            for flip_num in range(1, num):
                                if self._othello[row - flip_num][col + flip_num] == self.TURN:
                                    break
                                else:
                                    self._up_right_list.append(self._othello[row - flip_num][col + flip_num])
        except:
            pass
        
        if '.' not in self._up_right_list:
            if self._up_right_list != []:
                self.FLIP = 'VALID'
        

    def _flip_up_right(self, row: int, col: int):
        "Flips the discs in the up right direction."
        self._check_flip_up_right(row, col)           
        if '.' not in self._up_right_list:
            if self._up_right_list != []:
                self.FLIP = 'VALID'
                try:
                    if self._othello[row - 1][col + 1] == self._opposite_turn(self.TURN):
                        for num in range(1, min(self.NUMBER_OF_ROWS, self.NUMBER_OF_COLUMNS) + 1):
                            if row - num < 0:
                                    return
                            else:
                                if self._othello[row - num][col + num] == self.TURN:
                                    for flip_num in (range(1, num)):
                                        if self._othello[row - flip_num][col + flip_num] == self._opposite_turn(self.TURN):
                                            self._othello[row - flip_num][col + flip_num] = self.TURN
                                        elif self._othello[row - flip_num][col + flip_num] == self.TURN:
                                            return
                except:
                    pass
        




    def _check_flip_down_right(self, row: int, col: int) -> list:
        "Takes a move and checks if discs can flip in the down right direction."
        self._down_right_list = []
        try:
            if self._othello[row + 1][col + 1] == self._opposite_turn(self.TURN):
                for num in range(1, min(self.NUMBER_OF_ROWS, self.NUMBER_OF_COLUMNS) + 1):
                    if self._othello[row + num][col + num] == self.TURN:
                        for flip_num in range(1, num):
                            if self._othello[row + flip_num][col + flip_num] == self.TURN:
                                break
                            else:
                                self._down_right_list.append(self._othello[row + flip_num][col + flip_num])
        except:
            pass
        if '.' not in self._down_right_list:
            if self._down_right_list != []:
                self.FLIP = 'VALID'
        


                            
    def _flip_down_right(self, row: int, col: int):
        "Flips the discs in the down right direction."
        self._check_flip_down_right(row, col)
        if '.' not in self._down_right_list:
            if self._down_right_list != []:
                try:
                    if self._othello[row + 1][col + 1] == self._opposite_turn(self.TURN):
                        for num in range(1, min(self.NUMBER_OF_ROWS, self.NUMBER_OF_COLUMNS) + 1):
                                if self._othello[row + num][col + num] == self.TURN:
                                    for flip_num in (range(1, num)):
                                        if self._othello[row + flip_num][col + flip_num] == self._opposite_turn(self.TURN):
                                            self._othello[row + flip_num][col + flip_num] = self.TURN
                                        elif self._othello[row + flip_num][col + flip_num] == self.TURN:
                                            return
                except:
                    pass



    def _check_flip_down_left(self, row: int, col: int) -> list:
        "Takes a move and checks if discs can flip in the down left direction."
        self._down_left_list = []
        try:
            if self._othello[row + 1][col - 1] == self._opposite_turn(self.TURN):
                for num in range(1, min(self.NUMBER_OF_ROWS, self.NUMBER_OF_COLUMNS) + 1):
                    if col - num < 0:
                                return
                    else:
                        if self._othello[row + num][col - num] == self.TURN:
                            for flip_num in range(1, num):
                                if self._othello[row + flip_num][col - flip_num] == self.TURN:
                                    break
                                else:
                                    self._down_left_list.append(self._othello[row + flip_num][col - flip_num])
        except:
            pass
        if '.' not in self._down_left_list:
            if self._down_left_list != []:
                self.FLIP = 'VALID'

                 
    def _flip_down_left(self, row: int, col: int):
        "Flips the discs in the down left direction."
        self._check_flip_down_left(row, col)
        if '.' not in self._down_left_list:
            if self._down_left_list != []:
                self.FLIP = 'VALID'
                try:
                    if self._othello[row + 1][col - 1] == self._opposite_turn(self.TURN):
                        for num in range(1, min(self.NUMBER_OF_ROWS, self.NUMBER_OF_COLUMNS) + 1):
                            if col - num < 0:
                                return
                            else:
                                if self._othello[row + num][col - num] == self.TURN:
                                    for flip_num in (range(1, num)):
                                        if self._othello[row + flip_num][col - flip_num] == self._opposite_turn(self.TURN):
                                                self._othello[row + flip_num][col - flip_num] = self.TURN
                                        elif self._othello[row + flip_num][col - flip_num] == self.TURN:
                                            return
                except:
                    pass

        
    def _count_discs(self):
        "Counts the number of discs for each player."
        for row in self._othello:
            for cell in row:
                if cell == 'B':
                    self.black_discs += 1
                elif cell == 'W':
                    self.white_discs += 1
        print("B: {}  W: {}".format(self.black_discs, self.white_discs))
        
    
    def _show_turn(self):
        "Shows whose turn it is."
        print("TURN: {}".format(self.TURN))


    def _flip_turn(self, turn: str) -> str:
        "Flips the turn attribute."
        if turn == 'B':
            self.TURN = 'W'
        elif turn == 'W':
            self.TURN = 'B'
            

    def _opposite_turn(self, turn: str) -> str:
        "Shows the opposite side."
        if turn == 'B':
            return 'W'
        elif turn == 'W':
            return 'B'



    def _show_board(self):
        "Shows the board."
        for row in self._othello:
            print(" ".join(row))


    def _check_flip(self, row: int, col: int):
        "Checks if a flip can be made"
        self._check_flip_up(row, col)
        self._check_flip_left(row, col)
        self._check_flip_up_left(row, col)
        try:
            self._othello[row + 1][col]
        except IndexError:
            pass
        else:
            self._check_flip_down(row, col)
            self._check_flip_down_left(row, col)

        try:
            self._othello[row][col + 1]
        except IndexError:
            pass
        else:
            self._check_flip_right(row, col)
            self._check_flip_up_right(row, col)
        try:
            self._othello[row + 1][col + 1]
        except IndexError:
            pass
        else:
            self._check_flip_down_right(row, col)


    def _check_for_open_cells(self):
        "Checks for open cells on the board."
        open_cells = []
        for row in range(len(self._othello)):
            for cell in range(len(self._othello[row])):
                if self._othello[row][cell] == '.':
                    open_cells.append((row, cell))
        return open_cells


    def _check_for_possible_moves(self):
        "Checks if either player can still make a valid move."
        self.FLIP = "INVALID"
        for cell in self._check_for_open_cells():
            row = cell[0]
            col = cell[1]
            self._check_flip(row, col)
            
            
        if self.FLIP == 'INVALID':
            self._flip_turn(self.TURN)
            for cell in self._check_for_open_cells():
                row = cell[0]
                col = cell[1]
                self._check_flip(row, col)
                if self.FLIP == 'INVALID':
                    return "GAME_OVER"
                else:
                    self.FLIP = 'INVALID'

    def _decide_winner(self):
        "Decides the winner."
        if self.black_discs == self.white_discs:
            self.WINNER = 'NONE'
        else:
            if self.RULE == ">":
                if self.black_discs > self.white_discs:
                    self.WINNER = 'B'
                elif self.white_discs > self.black_discs:
                    self.WINNER = 'W'
            elif self.RULE == "<":
                if self.black_discs < self.white_discs:
                    self.WINNER = 'B'
                elif self.white_discs < self.black_discs:
                    self.WINNER = 'W'
                
    def _show_winner(self):
        "Shows the winner."
        self._decide_winner()
        self.black_discs = 0
        self.white_discs = 0
        self._count_discs()
        self._show_board()
        print("WINNER: {}".format(self.WINNER))


