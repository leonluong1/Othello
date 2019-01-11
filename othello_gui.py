#Leon Luong 69139013 Lab sec. 9

import tkinter

import othello_model

import othello_class

import math

#FULL

class DialogBox:
    DEFAULT_FONT = ('Helvetica', 16)
        
    def __init__(self):
        "Sets up the dialog window."
        self._dialog_window = tkinter.Toplevel()

        row_label = tkinter.Label(
            master = self._dialog_window, text = 'Number of Rows: ',
            font = DialogBox.DEFAULT_FONT)

        row_label.grid(
            row = 0, column = 0, columnspan = 2, padx = 10, pady = 10,
            sticky = tkinter.W)

        column_label = tkinter.Label(
            master = self._dialog_window, text = 'Number of Columns: ',
            font = DialogBox.DEFAULT_FONT)

        column_label.grid(
            row = 1, column = 0, columnspan = 2, padx = 10, pady = 10,
            sticky = tkinter.W)

        first_player_label = tkinter.Label(
            master = self._dialog_window, text = 'Who is going first? ',
            font = DialogBox.DEFAULT_FONT)

        first_player_label.grid(
            row = 2, column = 0, columnspan = 2, padx = 10, pady = 10,
            sticky = tkinter.W)

        top_left_label = tkinter.Label(
            master = self._dialog_window, text = 'Who is the top left? ',
            font = DialogBox.DEFAULT_FONT)

        top_left_label.grid(
            row = 3, column = 0, columnspan = 2, padx = 10, pady = 10,
            sticky = tkinter.W)

        rule_label = tkinter.Label(
            master = self._dialog_window, text = 'How do you decide who wins? ',
            font = DialogBox.DEFAULT_FONT)

        rule_label.grid(
            row = 4, column = 0, columnspan = 2, padx = 10, pady = 10,
            sticky = tkinter.W)

        
        self._row_var = tkinter.IntVar()
        self._row_var.set(4)
        self._row_option = tkinter.OptionMenu(self._dialog_window,
                                             self._row_var, 4, 6, 8, 10, 12, 16)

        self._row_option.grid(
            row = 0, column = 3, columnspan = 2, padx = 10, pady = 10,
            sticky = tkinter.W)


        self._col_var = tkinter.IntVar()
        self._col_var.set(4)
        self._column_option = tkinter.OptionMenu(self._dialog_window,
                                             self._col_var, 4, 6, 8, 10, 12, 16)

        self._column_option.grid(
            row = 1, column = 3, columnspan = 2, padx = 10, pady = 10,
            sticky = tkinter.W)

        self._first_var = tkinter.StringVar()
        self._first_var.set('B')
        self._first_player_option = tkinter.OptionMenu(self._dialog_window,
                                             self._first_var, 'B', 'W')

        self._first_player_option.grid(
            row = 2, column = 3, columnspan = 2, padx = 10, pady = 10,
            sticky = tkinter.W)


        self._top_left_var = tkinter.StringVar()
        self._top_left_var.set('B')
        self._top_left_option = tkinter.OptionMenu(self._dialog_window,
                                             self._top_left_var, 'B', 'W')

        self._top_left_option.grid(
            row = 3, column = 3, columnspan = 2, padx = 10, pady = 10,
            sticky = tkinter.W)

        self._rule_var = tkinter.StringVar()
        self._rule_var.set('>')
        self._rule_option = tkinter.OptionMenu(self._dialog_window,
                                             self._rule_var, '>', '<')

        self._rule_option.grid(
            row = 4, column = 3, columnspan = 2, padx = 10, pady = 10,
            sticky = tkinter.W)

        button_frame = tkinter.Frame(master = self._dialog_window)

        button_frame.grid(
            row = 5, column = 3, columnspan = 2, padx = 10, pady = 10,
            sticky = tkinter.E + tkinter.S)

        ok_button = tkinter.Button(
            master = button_frame, text = 'OK', font = DialogBox.DEFAULT_FONT,
            command = self._on_ok_button)

        ok_button.grid(row = 0, column = 0, pady = 10)

        cancel_button = tkinter.Button(
            master = button_frame, text = 'Cancel', font = DialogBox.DEFAULT_FONT,
            command = self._on_cancel_button)

        cancel_button.grid(row = 0, column = 1,  pady = 10)

        self._dialog_window.rowconfigure(0, weight = 1)
        self._dialog_window.rowconfigure(1, weight = 1)
        self._dialog_window.rowconfigure(2, weight = 1)
        self._dialog_window.rowconfigure(3, weight = 1)
        self._dialog_window.rowconfigure(4, weight = 1)
        self._dialog_window.rowconfigure(5, weight = 1)
        self._dialog_window.columnconfigure(0, weight = 1)
        self._dialog_window.columnconfigure(3, weight = 1)

        self._clicked_okay = False
        self._ROWS = 0
        self._COLUMNS = 0
        self._PLAYER_ONE = ''
        self._TOP_LEFT = ''
        self._RULE = ''

        

    def show(self):
        "Pauses the board window and focuses on the dialog window."
        self._dialog_window.grab_set()
        self._dialog_window.wait_window()

    def was_okay_clicked(self) -> bool:
        "Returns True or False whether or not okay was clicked."
        return self._clicked_okay


    def _on_ok_button(self):
        "Saves variables"
        self._clicked_okay = True
        self._ROWS = self._row_var.get()
        self._COLUMNS = self._col_var.get()
        self._PLAYER_ONE = self._first_var.get()
        self._TOP_LEFT = self._top_left_var.get()
        self._RULE = self._rule_var.get()
        
        self._dialog_window.destroy()


    def _on_cancel_button(self) -> None:
        self._dialog_window.destroy()

class OthelloApp:
    
    DEFAULT_FONT = ('Franklin Gothic Medium Cond', 18)
    
    def __init__(self, state: othello_model.OthelloState):
        """
        Opens the board window and the dialog window.
        If okay is clicked, the board is set up.
        """ 
        self._state = state
        self._root_window = tkinter.Tk()
        self._on_okay()
        if self.dialog.was_okay_clicked():
            self._state._game.start(self.ROWS, self.COLUMNS,
                                    self.PLAYER_ONE, self.TOP_LEFT, self.RULE)
            self._frame = tkinter.Frame(
                master = self._root_window, background = 'white')

            self.black_num = tkinter.StringVar()
            self.black_num.set('Black: 2')
            self.white_num = tkinter.StringVar()
            self.white_num.set('White: 2')
            self.turn = tkinter.StringVar()
            self.turn.set('Turn: {}'.format(self._state._game.TURN))
            
            self._black_score = tkinter.Label(
                master = self._frame, background = 'white',
                width = 30, height = 2, textvariable = self.black_num, font = OthelloApp.DEFAULT_FONT)
            self._white_score = tkinter.Label(
                master = self._frame, background = 'white',
                width = 30, height = 2, textvariable = self.white_num, font = OthelloApp.DEFAULT_FONT)
            
            self._board = tkinter.Canvas(
                master = self._root_window, width = 500, height = 500,
                background = '#ccff66')

            self._turn_label = tkinter.Label(
                master = self._root_window, width = 30, height = 2,
                background = 'white', textvariable = self.turn, font = OthelloApp.DEFAULT_FONT)

            self._black_score.grid(row = 0, column = 0, padx = 2, pady = 2,
                             sticky = tkinter.N + tkinter.S + tkinter.W + tkinter.E )
            self._white_score.grid(row = 0, column = 1, padx = 2, pady = 2,
                             sticky = tkinter.N + tkinter.S + tkinter.W + tkinter.E )

            self._frame.grid(row = 0, column = 0, padx = 2, pady = 2, columnspan = 2,
                             sticky = tkinter.N + tkinter.S + tkinter.W + tkinter.E )

            self._board.grid(row = 1, column = 0, padx = 2, pady = 2, columnspan = 2,
                             sticky = tkinter.N + tkinter.S + tkinter.W + tkinter.E )


            self._turn_label.grid(row = 2, column = 0, padx = 2, pady = 2, columnspan = 2,
                             sticky = tkinter.N + tkinter.S + tkinter.W + tkinter.E )
            self._root_window.rowconfigure(0, weight = 1)
            self._root_window.columnconfigure(1, weight = 1)
            self._root_window.rowconfigure(1, weight = 1)
            self._root_window.rowconfigure(2, weight = 1)

            self._board.bind('<Configure>', self.on_resized)
            self._board.bind('<Button-1>', self.on_left_click)

            self.width = self._board.winfo_width()
            self.height = self._board.winfo_height()
            for col in range(self.COLUMNS):
                for row in range(self.ROWS):
                    self._state.append_beginning_move(self,
                                                      col/self.COLUMNS,
                                                      row/self.ROWS,
                                                      self._state._game._othello[row][col])


    def _on_okay(self):
        "Opens dialogue box and saves the variables if okay is clicked."
        self.dialog = DialogBox()
        self.dialog.show()
        if self.dialog.was_okay_clicked():
            self.ROWS = int(self.dialog._ROWS)
            self.COLUMNS = int(self.dialog._COLUMNS)
            self.PLAYER_ONE = self.dialog._PLAYER_ONE
            self.TOP_LEFT = self.dialog._TOP_LEFT
            self.RULE = self.dialog._RULE
            


    
    def start(self):
        "Starts the game."
        if self.dialog.was_okay_clicked():
            self._root_window.mainloop()
        

    def on_resized(self, event: tkinter.Event):
        "Resizes the board when the canvas is changed."
        self._board.delete(tkinter.ALL)
        self._set_board()
        self._redraw_moves()
        

    def _set_board(self):
        "Sets the board."
        self.width = self._board.winfo_width()
        self.height = self._board.winfo_height()
        
        for row in range(self.ROWS):
            row_frac = row/self.ROWS
            new_row_size = row_frac *  self.height
            self._board.create_line(0, new_row_size,  self.width, new_row_size)
            
        for column in range(self.COLUMNS):
            col_frac = column/self.COLUMNS
            new_col_size = col_frac *  self.width
            self._board.create_line(new_col_size, 0, new_col_size,  self.height)
        



    def on_left_click(self, event: tkinter.Event):
        "Draws a disc when the left click is pushed."
        if self._state._game.WINNER == 'NO_WINNER':
            self._board.delete(tkinter.ALL)
            self._state._game.gameplay(str(math.floor(event.y/self.height * self.ROWS) + 1) + ' ' +
                                            str(math.floor(event.x/self.width * self.COLUMNS) + 1))
            if self._state._game.FLIP == 'VALID':
                self._state.append_valid_move(self, event, self.width, self.height)
                self._state.black_list.clear()
                self._state.white_list.clear()
                for col in range(self.COLUMNS):
                    for row in range(self.ROWS):
                        self._state.append_beginning_move(self, col/self.COLUMNS,
                                                          row/self.ROWS,
                                                          self._state._game._othello[row][col])
            self._redraw_moves()
            self.black_num.set('Black: {}'.format(self._state._game.black_discs))
            self.white_num.set('White: {}'.format(self._state._game.white_discs))
            self.turn.set('Turn: {}'.format(self._state._game.TURN))
            if self._state._game._check_for_possible_moves() == "GAME_OVER":
                if self._state._game.WINNER != 'NO_WINNER':
                    self.turn.set('Winner: {}'.format(self._state._game.WINNER))
            elif self._state._game._check_for_open_cells() == []:
                if self._state._game.WINNER != 'NO_WINNER':
                    self.turn.set('Winner: {}'.format(self._state._game.WINNER))

        
    def _redraw_moves(self):
        "Redraws the discs if the board is resized."
        self._set_board()
        radius_x = ((1/self.COLUMNS) * self.width)/2
        radius_y = ((1/self.ROWS) * self.height)/2
        for black in self._state.black_list:
            self._draw_disc(black)
        for white in self._state.white_list:
            self._draw_disc(white)
            
        
        
    def _draw_disc(self, move: tkinter.Event):
        "Draws the discs on the board."
        radius_x = ((1/self.COLUMNS) * self.width)/2
        radius_y = ((1/self.ROWS) * self.height)/2
        for black in self._state.black_list:
            x = math.floor(black._frac_x * self.COLUMNS )/self.COLUMNS + ((1/self.COLUMNS)/2)
            y = math.floor(black._frac_y * self.ROWS )/self.ROWS + ((1/self.ROWS)/2)
            center_x = x * self.width
            center_y = y * self.height
            self._board.create_oval(center_x - radius_x,
                                    center_y - radius_y,
                                    center_x + radius_x,
                                    center_y + radius_y, fill = 'black')
            
        for move in self._state.white_list:
            x = math.floor(move._frac_x * self.COLUMNS )/self.COLUMNS + ((1/self.COLUMNS)/2)
            y = math.floor(move._frac_y * self.ROWS )/self.ROWS + ((1/self.ROWS)/2)
            center_x = x * self.width
            center_y = y * self.height
            self._board.create_oval(center_x - radius_x,
                                    center_y - radius_y,
                                    center_x + radius_x,
                                    center_y + radius_y, fill = 'white')
        
        
    

if __name__ == '__main__':
    print('FULL')
    OthelloApp(othello_model.OthelloState).start()

