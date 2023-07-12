import tkinter as tk
from defs import *

def initial_board(root):
    cell_size = board_size // 8 # size of one square on the chess board
    colour = ["#FFCE9E", "#D18B47"] # colour of the light and dark squares
    
    canvas = tk.Canvas(root,width = board_size, height = board_size)
    canvas.pack()
    
    selected_piece_id = None
    selected_piece_pos = None
    pieces = {}
    
    def select_piece(event):
        nonlocal selected_piece_id, selected_piece_pos
        cell_x = event.x // cell_size
        cell_y = event.y // cell_size
        if selected_piece_id:
            # If there's a piece already at the target location, delete it
            if (cell_x, cell_y) in pieces:
                canvas.delete(pieces[(cell_x, cell_y)])
                del pieces[(cell_x, cell_y)]
            # Move the selected piece to the new cell and deselect it
            canvas.coords(selected_piece_id, (event.x // cell_size) * cell_size + int(cell_size / 2), 
                          (event.y // cell_size) * cell_size + int(cell_size / 2))
            pieces[(cell_x, cell_y)] = selected_piece_id
            del pieces[selected_piece_pos]
            selected_piece_id = None
            selected_piece_pos = None
        elif (cell_x, cell_y) in pieces:
            # Select piece
            selected_piece_id = pieces[(cell_x, cell_y)]
            selected_piece_pos = (cell_x, cell_y)
            

    canvas.bind("<Button-1>", select_piece)
    
    for i in range(8):
        for j in range(8):
            x0 = j * cell_size
            y0 = i * cell_size
            x1 = x0 + cell_size
            y1 = y0 + cell_size
            canvas.create_rectangle(x0,y0,x1,y1, fill = colour[(i+j)%2])
    
    # Create and place the pieces on the board
    piece_placement = [[b_rook, b_knight, b_bishop, b_queen, b_king, b_bishop, b_knight, b_rook],[w_rook, w_knight, w_bishop, w_queen, w_king, w_bishop, w_knight, w_rook]]
    for i in range(8):
        # Create black pieces
        piece_id = canvas.create_text(100*i + 50, 50, text=piece_placement[0][i], font=("Arial", 48))
        pieces[(i, 0)] = piece_id  # Add the piece to the pieces dictionary
        # Create black pawns
        piece_id = canvas.create_text(100*i + 50, 150, text=b_pawn, font=("Arial", 48))
        pieces[(i, 1)] = piece_id  # Add the piece to the pieces dictionary
        # Create white pawns
        piece_id = canvas.create_text(100*i + 50, 650, text=w_pawn, font=("Arial", 48))
        pieces[(i, 6)] = piece_id  # Add the piece to the pieces dictionary
        # Create white pieces
        piece_id = canvas.create_text(100*i + 50, 750, text=piece_placement[1][i], font=("Arial", 48))
        pieces[(i, 7)] = piece_id  # Add the piece to the pieces dictionary

def main():
    # Setting up an 800x800 non-reizable window with Chess as the title
    root = tk.Tk()
    root.title("Chess")
    root.geometry(f"{board_size}x{board_size}")
    root.resizable(False,False)
    root.pack_propagate(False)
    
    # Setting up the board
    initial_board(root)
    
    
    # Main loop
    root.mainloop()



if __name__ == "__main__":
    main()

