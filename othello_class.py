#Leon Luong 69139013 Lab section 9


class InvalidMoveError(Exception):
    pass

class GameOverError(Exception):
    pass


class Othello:
    
    _othello = []
    TURN = 'B'
    FLIP = 'INVALID'
    WINNER = 'NO_WINNER'
    RULE = '>'
    black_discs = 0
    white_discs = 0
    
    def __init__(self):
        "Sets the turn, winner, discs, rule, and board attributes."
        pass

    def start(self, rows: int, columns: int, first_player: str, top_right_player: int, rule: int):
        "Decides the number of rows, columns, first player, top right player, rule, and makes the board."
        self.NUMBER_OF_ROWS = rows
        self.NUMBER_OF_COLUMNS = columns
        for row_num in range(self.NUMBER_OF_ROWS):
            Othello._othello.append([])
            for col_num in range(self.NUMBER_OF_COLUMNS):
                Othello._othello[row_num].append('.')
                
        self._decide_first_player(first_player)
        self._decide_arrangement(top_right_player)
        self._decide_rules(rule)
          

    def _decide_first_player(self, first_player: int):
        "Decides who goes first."
        if first_player == 'W':
            Othello.TURN = 'W'
        else:
            pass
        

    def _decide_arrangement(self, top_left_player: int):
        "Decides where the starting discs are arranged."
        if top_left_player == 'W':
            Othello._othello[int(self.NUMBER_OF_ROWS * 0.5)][int(self.NUMBER_OF_COLUMNS * 0.5) - 1] = 'B'
            Othello._othello[int(self.NUMBER_OF_ROWS * 0.5) - 1][int(self.NUMBER_OF_COLUMNS * 0.5)] = 'B'
            Othello._othello[int(self.NUMBER_OF_ROWS * 0.5)][int(self.NUMBER_OF_COLUMNS * 0.5)] = 'W'
            Othello._othello[int(self.NUMBER_OF_ROWS * 0.5) - 1][int(self.NUMBER_OF_COLUMNS * 0.5) - 1] = 'W'

        else:
            Othello._othello[int(self.NUMBER_OF_ROWS * 0.5)][int(self.NUMBER_OF_COLUMNS * 0.5) - 1] = 'W'
            Othello._othello[int(self.NUMBER_OF_ROWS * 0.5) - 1][int(self.NUMBER_OF_COLUMNS * 0.5)] = 'W'
            Othello._othello[int(self.NUMBER_OF_ROWS * 0.5)][int(self.NUMBER_OF_COLUMNS * 0.5)] = 'B'
            Othello._othello[int(self.NUMBER_OF_ROWS * 0.5) - 1][int(self.NUMBER_OF_COLUMNS * 0.5) - 1] = 'B'            

        
    def _decide_rules(self, rule: str):
        "Decides how to pick the winner."
        if rule == "<":
            Othello.RULE = "<"
        else:
            pass


    def gameplay(self, pick_move: str):
        "Runs through the game until a winner is decided."
        try:
            Othello.FLIP == 'INVALID'
            if self._check_for_possible_moves() == "GAME_OVER":
                raise GameOverError
            self._make_move(pick_move)
            self._count_discs()
            if self._check_for_open_cells() == []:
                raise GameOverError
                
        except GameOverError:
            self._show_winner()
            

            
    def _make_move(self, pick_move: str):
        "Takes the input and makes a move on the board."
        try:
            row = int(pick_move.split(" ")[0]) - 1
            col = int(pick_move.split(" ")[1]) - 1
            if row <= self.NUMBER_OF_ROWS and col <= self.NUMBER_OF_COLUMNS:
                if Othello._othello[row][col] == '.':
                    self._flip(row, col)
                    self._flip_turn(Othello.TURN)
                    return
                else:
                    pass
            if self._check_for_open_cells() == []:
                    raise GameOverError
            
        except InvalidMoveError:
            pass
            
        except ValueError:
            pass




    def _flip(self, row: int, col: int):
        "Takes a move and flips the discs in every direction if valid."
        Othello.FLIP = 'INVALID'
        self._flip_up(row, col)
        self._flip_left(row, col)
        self._flip_up_left(row, col)
        try:
            Othello._othello[row + 1][col]
        except IndexError:
            pass
        else:
            self._flip_down(row, col)
            self._flip_down_left(row, col)
        
        try:
            Othello._othello[row][col + 1]
        except IndexError:
            pass
        else:
            self._flip_right(row, col)
            self._flip_up_right(row, col)

        try:
            Othello._othello[row + 1][col + 1]
        except IndexError:
            pass
        else:
            self._flip_down_right(row, col)


        if Othello.FLIP == 'VALID':   
            Othello._othello[row][col] = Othello.TURN
        else:
            raise InvalidMoveError



    def _check_flip_up(self, row: int, col: int):
        "Takes a move and checks if discs can flip in the up direction."
        self._up_list = []
        if Othello._othello[row - 1][col] == self._opposite_turn(Othello.TURN):
            for num in range(1, row + 1):
                if Othello._othello[row - num][col] == Othello.TURN:
                    for flip_num in range(1, num):
                        if Othello._othello[row - flip_num][col] == Othello.TURN:
                            break
                        else:
                            self._up_list.append(Othello._othello[row - flip_num][col])
                            
        if '.' not in self._up_list:
            if self._up_list != []:
                Othello.FLIP = 'VALID'
                
                            

    def _flip_up(self, row: int, col: int):
        "Flips the discs in the up direction."
        self._check_flip_up(row, col)
        if '.' not in self._up_list:
            if self._up_list != []:
                if Othello._othello[row - 1][col] == self._opposite_turn(Othello.TURN):
                    for num in range(1, row + 1):
                        if Othello._othello[row - num][col] == Othello.TURN:
                            for flip_num in range(1, num):
                                if Othello._othello[row - flip_num][col] == self._opposite_turn(Othello.TURN):
                                    Othello._othello[row - flip_num][col] = Othello.TURN
                                elif Othello._othello[row - flip_num][col] == Othello.TURN:
                                    return



    def _check_flip_down(self, row: int, col: int):
        "Takes a move and checks if discs can flip in the down direction."
        self._down_list = []
        if Othello._othello[row + 1][col] == self._opposite_turn(Othello.TURN):            
            for num in range(1, self.NUMBER_OF_ROWS - row - 1):
                if Othello._othello[row + num][col] == Othello.TURN:
                    for flip_num in range(1, num):
                        if Othello._othello[row + flip_num][col] == Othello.TURN:
                            break
                        else:
                            self._down_list.append(Othello._othello[row + flip_num][col])
                            
        if '.' not in self._down_list:
            if self._down_list != []:
                Othello.FLIP = 'VALID'
                            
                        
    def _flip_down(self, row: int, col: int):
        "Flips the discs in the down direction."
        self._check_flip_down(row, col)
        if '.' not in self._down_list:
            if self._down_list != []:
                if Othello._othello[row + 1][col] == self._opposite_turn(Othello.TURN):            
                    for num in range(1, self.NUMBER_OF_ROWS - row - 1):
                        if Othello._othello[row + num][col] == Othello.TURN:
                            for flip_num in range(1, num):
                                if Othello._othello[row + flip_num][col] == self._opposite_turn(Othello.TURN):
                                    Othello._othello[row + flip_num][col] = Othello.TURN
                                elif Othello._othello[row + flip_num][col] == Othello.TURN:
                                    return          



    def _check_flip_left(self, row: int, col: int):
        "Takes a move and checks if discs can flip in the left direction."
        self._left_list = []
        if Othello._othello[row][col - 1] == self._opposite_turn(Othello.TURN):
            for num in range(1, col + 1):
                if Othello._othello[row][col - num] == Othello.TURN:
                    for flip_num in range(1, num):
                        if Othello._othello[row][col - flip_num] == Othello.TURN:
                            break
                        else:
                            self._left_list.append(Othello._othello[row][col - flip_num])
        if '.' not in self._left_list:
            if self._left_list != []:
                Othello.FLIP = 'VALID'
    

    def _flip_left(self, row: int, col: int):
        "Flips the discs in the left direction."
        self._check_flip_left(row, col)
        if '.' not in self._left_list:
            if self._left_list != []:
                if Othello._othello[row][col - 1] == self._opposite_turn(Othello.TURN):
                    for num in range(1, col + 1):
                        if Othello._othello[row][col - num] == Othello.TURN:
                            for flip_num in range(1, num):
                                if Othello._othello[row][col - flip_num] == self._opposite_turn(Othello.TURN):
                                    Othello._othello[row][col - flip_num] = Othello.TURN
                                elif Othello._othello[row][col - flip_num] == Othello.TURN:
                                    return


    def _check_flip_right(self, row: int, col: int):
        "Takes a move and checks if discs can flip in the right direction."
        self._right_list = []
        if Othello._othello[row][col + 1] == self._opposite_turn(Othello.TURN):
            for num in range(1, self.NUMBER_OF_COLUMNS - col):
                if Othello._othello[row][col + num] == Othello.TURN:
                    for flip_num in range(1, num):
                        if Othello._othello[row][col + flip_num] == Othello.TURN:
                            break
                        else:
                            self._right_list.append(Othello._othello[row][col + flip_num])
        if '.' not in self._right_list:
            if self._right_list != []:
                Othello.FLIP = 'VALID'
    

    def _flip_right(self, row: int, col: int):
        "Flips the discs in the right direction."
        self. _check_flip_right(row, col)
        if '.' not in self._right_list:
            if self._right_list != []:
                if Othello._othello[row][col + 1] == self._opposite_turn(Othello.TURN):
                    for num in range(1, self.NUMBER_OF_COLUMNS - col):
                        if Othello._othello[row][col + num] == Othello.TURN:
                            for flip_num in range(1, num):
                                if Othello._othello[row][col + flip_num] == self._opposite_turn(Othello.TURN):
                                    Othello._othello[row][col + flip_num] = Othello.TURN
                                elif Othello._othello[row][col + flip_num] == Othello.TURN:
                                    return


    def _check_flip_up_left(self, row: int, col: int):
        "Takes a move and checks if discs can flip in the up left direction."
        self._up_left_list = []
        if Othello._othello[row - 1][col - 1] == self._opposite_turn(Othello.TURN):
            for num in range(1, min(row, col) + 1):
                if Othello._othello[row - num][col - num] == Othello.TURN:
                    for flip_num in range(1, num):
                        if Othello._othello[row - flip_num][col - flip_num] == Othello.TURN:
                            break
                        else:
                            self._up_left_list.append(Othello._othello[row - flip_num][col - flip_num])
        if '.' not in self._up_left_list:
            if self._up_left_list != []:
                Othello.FLIP = 'VALID'


    def _flip_up_left(self, row: int, col: int):
        "Flips the discs in the up left direction."
        self._check_flip_up_left(row, col)
        if '.' not in self._up_left_list:
            if self._up_left_list != []:
                if Othello._othello[row - 1][col - 1] == self._opposite_turn(Othello.TURN):
                    for num in range(1, min(row, col) + 1):
                        if Othello._othello[row - num][col - num] == Othello.TURN:
                            for flip_num in (range(1, num)):
                                if Othello._othello[row - flip_num][col - flip_num] == self._opposite_turn(Othello.TURN):
                                    Othello._othello[row - flip_num][col - flip_num] = Othello.TURN
                                elif Othello._othello[row - flip_num][col - flip_num] == Othello.TURN:
                                    return



    def _check_flip_up_right(self, row: int, col: int):
        "Takes a move and checks if discs can flip in the up right direction."
        self._up_right_list = []        
        try:
            if Othello._othello[row - 1][col + 1] == self._opposite_turn(Othello.TURN):
                for num in range(1, min(self.NUMBER_OF_ROWS, self.NUMBER_OF_COLUMNS) + 1):
                    if row - num < 0:
                        return
                    else:
                        if Othello._othello[row - num][col + num] == Othello.TURN:
                            for flip_num in range(1, num):
                                if Othello._othello[row - flip_num][col + flip_num] == Othello.TURN:
                                    break
                                else:
                                    self._up_right_list.append(Othello._othello[row - flip_num][col + flip_num])
        except:
            pass
        
        if '.' not in self._up_right_list:
            if self._up_right_list != []:
                Othello.FLIP = 'VALID'
        

    def _flip_up_right(self, row: int, col: int):
        "Flips the discs in the up right direction."
        self._check_flip_up_right(row, col)           
        if '.' not in self._up_right_list:
            if self._up_right_list != []:
                Othello.FLIP = 'VALID'
                try:
                    if Othello._othello[row - 1][col + 1] == self._opposite_turn(Othello.TURN):
                        for num in range(1, min(self.NUMBER_OF_ROWS, self.NUMBER_OF_COLUMNS) + 1):
                            if row - num < 0:
                                    return
                            else:
                                if Othello._othello[row - num][col + num] == Othello.TURN:
                                    for flip_num in (range(1, num)):
                                        if Othello._othello[row - flip_num][col + flip_num] == self._opposite_turn(Othello.TURN):
                                            Othello._othello[row - flip_num][col + flip_num] = Othello.TURN
                                        elif Othello._othello[row - flip_num][col + flip_num] == Othello.TURN:
                                            return
                except:
                    pass
        




    def _check_flip_down_right(self, row: int, col: int) -> list:
        "Takes a move and checks if discs can flip in the down right direction."
        self._down_right_list = []
        try:
            if Othello._othello[row + 1][col + 1] == self._opposite_turn(Othello.TURN):
                for num in range(1, min(self.NUMBER_OF_ROWS, self.NUMBER_OF_COLUMNS) + 1):
                    if Othello._othello[row + num][col + num] == Othello.TURN:
                        for flip_num in range(1, num):
                            if Othello._othello[row + flip_num][col + flip_num] == Othello.TURN:
                                break
                            else:
                                self._down_right_list.append(Othello._othello[row + flip_num][col + flip_num])
        except:
            pass
        if '.' not in self._down_right_list:
            if self._down_right_list != []:
                Othello.FLIP = 'VALID'
        


                            
    def _flip_down_right(self, row: int, col: int):
        "Flips the discs in the down right direction."
        self._check_flip_down_right(row, col)
        if '.' not in self._down_right_list:
            if self._down_right_list != []:
                try:
                    if Othello._othello[row + 1][col + 1] == self._opposite_turn(Othello.TURN):
                        for num in range(1, min(self.NUMBER_OF_ROWS, self.NUMBER_OF_COLUMNS) + 1):
                                if Othello._othello[row + num][col + num] == Othello.TURN:
                                    for flip_num in (range(1, num)):
                                        if Othello._othello[row + flip_num][col + flip_num] == self._opposite_turn(Othello.TURN):
                                            Othello._othello[row + flip_num][col + flip_num] = Othello.TURN
                                        elif Othello._othello[row + flip_num][col + flip_num] == Othello.TURN:
                                            return
                except:
                    pass



    def _check_flip_down_left(self, row: int, col: int) -> list:
        "Takes a move and checks if discs can flip in the down left direction."
        self._down_left_list = []
        try:
            if Othello._othello[row + 1][col - 1] == self._opposite_turn(Othello.TURN):
                for num in range(1, min(self.NUMBER_OF_ROWS, self.NUMBER_OF_COLUMNS) + 1):
                    if col - num < 0:
                                return
                    else:
                        if Othello._othello[row + num][col - num] == Othello.TURN:
                            for flip_num in range(1, num):
                                if Othello._othello[row + flip_num][col - flip_num] == Othello.TURN:
                                    break
                                else:
                                    self._down_left_list.append(Othello._othello[row + flip_num][col - flip_num])
        except:
            pass
        if '.' not in self._down_left_list:
            if self._down_left_list != []:
                Othello.FLIP = 'VALID'

                 
    def _flip_down_left(self, row: int, col: int):
        "Flips the discs in the down left direction."
        self._check_flip_down_left(row, col)
        if '.' not in self._down_left_list:
            if self._down_left_list != []:
                Othello.FLIP = 'VALID'
                try:
                    if Othello._othello[row + 1][col - 1] == self._opposite_turn(Othello.TURN):
                        for num in range(1, min(self.NUMBER_OF_ROWS, self.NUMBER_OF_COLUMNS) + 1):
                            if col - num < 0:
                                return
                            else:
                                if Othello._othello[row + num][col - num] == Othello.TURN:
                                    for flip_num in (range(1, num)):
                                        if Othello._othello[row + flip_num][col - flip_num] == self._opposite_turn(Othello.TURN):
                                                Othello._othello[row + flip_num][col - flip_num] = Othello.TURN
                                        elif Othello._othello[row + flip_num][col - flip_num] == Othello.TURN:
                                            return
                except:
                    pass

        
    def _count_discs(self):
        "Counts the number of discs for each player."
        Othello.black_discs = 0
        Othello.white_discs = 0
        for row in Othello._othello:
            for cell in row:
                if cell == 'B':
                    Othello.black_discs += 1
                elif cell == 'W':
                    Othello.white_discs += 1
        
    
    def _show_turn(self):
        "Shows whose turn it is."
        print("TURN: {}".format(Othello.TURN))

    def _flip_turn(self, turn: str) -> str:
        "Flips the turn attribute."
        if turn == 'B':
            Othello.TURN = 'W'
        elif turn == 'W':
            Othello.TURN = 'B'
            

    def _opposite_turn(self, turn: str) -> str:
        "Shows the opposite side."
        if turn == 'B':
            return 'W'
        elif turn == 'W':
            return 'B'



    def _show_board(self):
        "Shows the board."
        self._count_discs()
        for row in Othello._othello:
            print(" ".join(row))
        if Othello.WINNER == 'NO_WINNER':
            self._show_turn()


    def _check_flip(self, row: int, col: int):
        "Checks if a flip can be made"
        self._check_flip_up(row, col)
        self._check_flip_left(row, col)
        self._check_flip_up_left(row, col)
        try:
            Othello._othello[row + 1][col]
        except IndexError:
            pass
        else:
            self._check_flip_down(row, col)
            self._check_flip_down_left(row, col)

        try:
            Othello._othello[row][col + 1]
        except IndexError:
            pass
        else:
            self._check_flip_right(row, col)
            self._check_flip_up_right(row, col)
        try:
            Othello._othello[row + 1][col + 1]
        except IndexError:
            pass
        else:
            self._check_flip_down_right(row, col)


    def _check_for_open_cells(self):
        "Checks for open cells on the board."
        open_cells = []
        for row in range(len(Othello._othello)):
            for cell in range(len(Othello._othello[row])):
                if Othello._othello[row][cell] == '.':
                    open_cells.append((row, cell))
        return open_cells


    def _check_for_possible_moves(self):
        "Checks if either player can still make a valid move."
        Othello.FLIP = "INVALID"
        for cell in self._check_for_open_cells():
            row = cell[0]
            col = cell[1]
            self._check_flip(row, col)
            
            
        if Othello.FLIP == 'INVALID':
            self._flip_turn(Othello.TURN)
            for cell in self._check_for_open_cells():
                row = cell[0]
                col = cell[1]
                self._check_flip(row, col)
                if Othello.FLIP == 'INVALID':
                    return "GAME_OVER"
                else:
                    Othello.FLIP = 'INVALID'

    def _decide_winner(self):
        "Decides the winner."
        if Othello.black_discs == Othello.white_discs:
            Othello.WINNER = 'NONE'
        else:
            if Othello.RULE == ">":
                if Othello.black_discs > Othello.white_discs:
                    Othello.WINNER = 'B'
                elif Othello.white_discs > Othello.black_discs:
                    Othello.WINNER = 'W'
            elif Othello.RULE == "<":
                if Othello.black_discs < Othello.white_discs:
                    Othello.WINNER = 'B'
                elif self.white_discs < Othello.black_discs:
                    Othello.WINNER = 'W'
                
    def _show_winner(self):
        "Shows the winner."
        self._decide_winner()
        self._count_discs()


