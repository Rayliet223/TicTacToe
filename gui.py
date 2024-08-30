import tkinter as tk

# Colors
WHITE = "#FFFFFF"
OFF_WHITE = "#F8FAFF"
BLACK = "#000000"
LIGHT_GREY = "#D3D3D3"
RED = "#FF0000"
BLUE = "#4169E1"

# Fonts
ARIAL_ITALIC_LARGE = ("Arial", 40, "italic", "bold")
ARIAL_BOLD_LARGE = ("Arial", 55, "bold")
ARIAL_BOLD_MEDIUM = ("Arial", 35, "bold")
ARIAL_SMALL = ("Arial", 20)
ARIAL_BOLD_SMALL = ("Arial", 20, "bold")


# Other
TITLE = "Tic Tac Toe"
CROSS = "X"
CIRCLE = "O"
EMPTY = ""

class TicTacToeGUI:
    turn = "x"
    draw = False
    three_together = False

    field_button_array = [[None] * 3 for i in range(3)]

    field_mark_array = [[EMPTY] * 3 for i in range (3)]

    def __init__(self):

        self.window = self.create_window()

        self.title_frame = self.create_title_frame()
        self.title = self.create_title_label()
        self.display_frame = self.create_display_frame()

        self.board_frame = self.create_board_frame()
        self.create_playing_board()

        self.window.mainloop()

    def create_window(self):
        window = tk.Tk()
        window.geometry("500x650")
        window.resizable(0, 0)
        window.title("Tic Tac Toe")

        return window

    #Banner
    def create_title_frame(self):
        title_frame = tk.Frame(self.window, bg = BLACK)
        title_frame.pack(fill = "both", expand = True)
        title_frame.pack_propagate(False)
        return title_frame

    def create_title_label(self):
        title_label = tk.Label(self.window, text = TITLE, anchor = "center", bg = BLACK, fg = WHITE,
                               font = ARIAL_ITALIC_LARGE)
        title_label.pack(expand = True, fill = "both")
        return title_label

    def create_display_frame(self):
        DISPLAY_FRAME_HEIGHT = 500

        display_frame = tk.Frame(self.window, height = DISPLAY_FRAME_HEIGHT, bg = WHITE)
        display_frame.pack(fill = "both", expand = True)
        display_frame.pack_propagate(False)
        return display_frame

    #Gamebaord
    def create_board_frame(self):
        BOARD_SIZE = 450

        board_frame = tk.Frame(self.display_frame, height = BOARD_SIZE, width = BOARD_SIZE)
        board_frame.place(relx = 0.5, rely = 0.5, anchor = "center")

        return board_frame

    def create_playing_board(self):

        for i in range(3):
            for j in range(3):
                square_button = tk.Button(self.board_frame,bg = LIGHT_GREY, fg = LIGHT_GREY,
                                          borderwidth = 3, font = ARIAL_BOLD_MEDIUM, text = "O",
                                          relief = tk.GROOVE, activebackground = LIGHT_GREY,
                                          activeforeground = LIGHT_GREY,
                                          command = lambda row = i, column = j: self.mark_field(row, column))
                square_button.grid(row = i, column = j, sticky = "NSEW")
                self.field_button_array[i][j] = square_button

        self.board_frame.grid_propagate(False)

        for x in range(3):
            self.board_frame.columnconfigure(x, weight = 1)
            self.board_frame.rowconfigure(x, weight = 1)

    #Endscreen
    def switch_to_end_screen(self):
        self.clear_display_frame()
        self.create_end_Label()
        self.create_restart_button()

    def create_end_Label(self):
        winner = self.turn

        if winner == "x":
            winner_color = RED
        else:
            winner_color = BLUE

        if self.three_together == True:
            end_label = tk.Label(self.display_frame, text=winner.upper() + " HAT GEWONNEN!", bg=LIGHT_GREY,
                                 fg=winner_color, font=ARIAL_BOLD_MEDIUM)
        else:
            end_label = tk.Label(self.display_frame, text="UNENTSCHIEDEN!", bg=LIGHT_GREY,
                                 fg=BLACK, font=ARIAL_BOLD_MEDIUM)

        end_label.place(relx=0.5, rely=0.25, anchor="center")

    def create_restart_button(self):
        restart_button = tk.Button(self.display_frame, text = "neues Spiel starten", bg = LIGHT_GREY, fg = BLACK,
                                   font = ARIAL_SMALL, command = lambda: self.start_new_round())
        restart_button.place(relx = 0.5, rely = 0.65, anchor = "center")

    #Game Logic
    def update_mark_on_button(self, row, column):

        if self.turn == "x":
            self.field_button_array[row][column].config(text = CROSS, font = ARIAL_BOLD_MEDIUM, fg = RED, padx = 0,
                                                        pady = 0, command = lambda: None)
        else:
            self.field_button_array[row][column].config(text = CIRCLE, fg = BLUE, font = ARIAL_BOLD_MEDIUM, padx = 0,
                                                        pady = 0, command = lambda: None)

    def mark_field(self, row, column):

        self.update_mark_on_button(row, column)
        self.update_field_mark_array(row, column)
        self.check_for_end()
        self.set_next_turn()

    def update_field_mark_array(self, row, column):
        if self.turn == "x":
            self.field_mark_array[row][column] = "x"
        else:
            self.field_mark_array[row][column] = "o"

    def check_for_end(self):
        board = self.field_mark_array
        current_mark = self.turn

        #check for a winner
        #check row
        for row in board:
            if row[0] == row [1] == row[2] == current_mark:
                self.three_together = True
        #check column
        for column in range(3):
            if board[0][column] == board[1][column] == board[2][column] == current_mark:
                self.three_together = True
        #check diagonal
        if board[0][0] == board[1][1] == board[2][2] == current_mark \
                or board[0][2] == board[1][1] == board[2][0] == current_mark:
            self.three_together = True

        #check for Draw
        self.draw = True

        for row in board:
            for column in row:
                if column == EMPTY:
                    self.draw = False

        #go to end
        if self.three_together == True or self.draw == True:
            self.switch_to_end_screen()

    def set_next_turn(self):
        if self.turn == "x":
            self.turn = "o"
        else:
            self.turn = "x"

    def clear_display_frame(self):
        for widget in self.display_frame.winfo_children():
            widget.destroy()

    def start_new_round(self):
        self.turn = "x"
        self.draw = False
        self.three_together = False

        self.field_button_array = [[None] * 3 for i in range(3)]

        self.field_mark_array = [[EMPTY] * 3 for i in range(3)]

        self.clear_display_frame()
        self.board_frame = self.create_board_frame()
        self.create_playing_board()