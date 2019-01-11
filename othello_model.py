# Leon Luong 69139013

import tkinter

import coordinates

import othello_class


class OthelloState:
    black_list = []
    white_list = []
    _game = othello_class.Othello()



    def append_beginning_move(self, frac_x: int, frac_y: int, parameter: str):
        """
        Appends the old Points to a list depending on it's color.
        """
        valid_point = coordinates.frac_to_point(frac_x, frac_y)
        if parameter == 'B':
                OthelloState.black_list.append(valid_point)
        if parameter == 'W':
                OthelloState.white_list.append(valid_point)

            
    
    def append_valid_move(self, event: tkinter.Event, width: float, height: float):
        """
        Takes an event and turns it into a Point object.
        Appends the new Point object to a list depending on it's color.
        """
        if OthelloState._game.FLIP:
            valid_point = coordinates.pixel_to_point(event.x, event.y,
                                                     self.width, self.height)
            if OthelloState._game.TURN == 'B':
                OthelloState.black_list.append(valid_point)
            elif OthelloState._game.TURN == 'W':
                OthelloState.white_list.append(valid_point)





