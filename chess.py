import tkinter as tk
from defs import *

def is_white(piece_id):
    if piece_id % 4 == 0 or piece_id % 4 == 3:
        return True
    return False

def check_for_check(pieces):
    pass
    #for pieces.values():
        

# =============================================================================
    # Rules for pieces
# =============================================================================
    
# Black pawns
def black_pawn_movement(selected_piece_pos, pieces):
    available_pos = []
    # Is pawn on starting row?
    if selected_piece_pos[1]==1:
        for i in range(2):
            if (selected_piece_pos[0],selected_piece_pos[1]+i+1) in pieces.keys():
                break
            available_pos += [(selected_piece_pos[0],selected_piece_pos[1]+i+1)]
    # If pawn is not on starting row
    elif (selected_piece_pos[0],selected_piece_pos[1]+1) not in pieces.keys():
        available_pos += [(selected_piece_pos[0],selected_piece_pos[1]+1)]
    # Checks for possible white pieces to take on diagonals
    for i in range(-1,2,2):
        if (selected_piece_pos[0]+i,selected_piece_pos[1]+1) in pieces.keys() and is_white(pieces[selected_piece_pos[0]+i,selected_piece_pos[1]+1]):
            available_pos += [(selected_piece_pos[0]+i,selected_piece_pos[1]+1)]
    return available_pos

# White pawns
def white_pawn_movement(selected_piece_pos, pieces):
    available_pos = []
    # Is pawn on starting row?
    if selected_piece_pos[1]==6:
        for i in range(2):
            if (selected_piece_pos[0],selected_piece_pos[1]-i-1) in pieces.keys():
                break
            available_pos += [(selected_piece_pos[0],selected_piece_pos[1]-i-1)]
    # If pawn is not on starting row
    elif (selected_piece_pos[0],selected_piece_pos[1]+1) not in pieces.keys():
        available_pos += [(selected_piece_pos[0],selected_piece_pos[1]-1)]
    # Checks for possible white pieces to take on diagonals
    for i in range(-1,2,2):
        if (selected_piece_pos[0]+i,selected_piece_pos[1]-1) in pieces.keys() and not is_white(pieces[selected_piece_pos[0]+i,selected_piece_pos[1]-1]):
            available_pos += [(selected_piece_pos[0]+i,selected_piece_pos[1]-1)]
    return available_pos

# Rooks
def rook_movement(selected_piece_pos, pieces):
    available_pos = []
    # Check right for pieces and break once hit a piece
    for i in range(1,8):
        if (selected_piece_pos[0]+i, selected_piece_pos[1]) in pieces:
            if is_white(pieces[selected_piece_pos]) ^ is_white(pieces[(selected_piece_pos[0]+i, selected_piece_pos[1])]):
                available_pos += [(selected_piece_pos[0]+i, selected_piece_pos[1])]
            break
        available_pos += [(selected_piece_pos[0]+i, selected_piece_pos[1])]
    # Check down for pieces and break once hit a piece
    for i in range(1,8):
        if (selected_piece_pos[0], selected_piece_pos[1]+i) in pieces:
            if is_white(pieces[selected_piece_pos]) ^ is_white(pieces[(selected_piece_pos[0], selected_piece_pos[1]+i)]):
                available_pos += [(selected_piece_pos[0], selected_piece_pos[1]+i)]
            break
        available_pos += [(selected_piece_pos[0], selected_piece_pos[1]+i)]
    # Check left for pieces and break once hit a piece
    for i in range(1,8):
        if (selected_piece_pos[0]-i, selected_piece_pos[1]) in pieces:
            if is_white(pieces[selected_piece_pos]) ^ is_white(pieces[(selected_piece_pos[0]-i, selected_piece_pos[1])]):
                available_pos += [(selected_piece_pos[0]-i, selected_piece_pos[1])]
            break
        available_pos += [(selected_piece_pos[0]-i, selected_piece_pos[1])]
    # Check up for pieces and break once hit a piece
    for i in range(1,8):
        if (selected_piece_pos[0], selected_piece_pos[1]-i) in pieces:
            if is_white(pieces[selected_piece_pos]) ^ is_white(pieces[(selected_piece_pos[0], selected_piece_pos[1]-i)]):
                available_pos += [(selected_piece_pos[0], selected_piece_pos[1]-i)]
            break
        available_pos += [(selected_piece_pos[0], selected_piece_pos[1]-i)]
    return available_pos

# Knights
def knight_movement(selected_piece_pos, pieces):
    available_pos = []
    available_pos += [(selected_piece_pos[0]-1, selected_piece_pos[1]-2)]
    available_pos += [(selected_piece_pos[0]-2, selected_piece_pos[1]-1)]
    available_pos += [(selected_piece_pos[0]-1, selected_piece_pos[1]+2)]
    available_pos += [(selected_piece_pos[0]-2, selected_piece_pos[1]+1)]
    available_pos += [(selected_piece_pos[0]+1, selected_piece_pos[1]-2)]
    available_pos += [(selected_piece_pos[0]+2, selected_piece_pos[1]-1)]
    available_pos += [(selected_piece_pos[0]+1, selected_piece_pos[1]+2)]
    available_pos += [(selected_piece_pos[0]+2, selected_piece_pos[1]+1)]
    for loc in available_pos:
        if loc in pieces and not (is_white(pieces[selected_piece_pos])^is_white(pieces[loc])):
            available_pos.remove(loc)
    return available_pos

# Bishops
def bishop_movement(selected_piece_pos, pieces):
    available_pos = []
    # Up & left diagonal
    for i in range(1,8):
        if (selected_piece_pos[0]-i, selected_piece_pos[1]-i) in pieces:
            if is_white(pieces[selected_piece_pos]) ^ is_white(pieces[(selected_piece_pos[0]-i, selected_piece_pos[1]-i)]):
                available_pos += [(selected_piece_pos[0]-i, selected_piece_pos[1]-i)]
            break
        available_pos += [(selected_piece_pos[0]-i, selected_piece_pos[1]-i)]
    # Down & left diagonal
    for i in range(1,8):
        if (selected_piece_pos[0]-i, selected_piece_pos[1]+i) in pieces:
            if is_white(pieces[selected_piece_pos]) ^ is_white(pieces[(selected_piece_pos[0]-i, selected_piece_pos[1]+i)]):
                available_pos += [(selected_piece_pos[0]-i, selected_piece_pos[1]+i)]
            break
        available_pos += [(selected_piece_pos[0]-i, selected_piece_pos[1]+i)]
    # Up & right diagonal
    for i in range(1,8):
        if (selected_piece_pos[0]+i, selected_piece_pos[1]-i) in pieces:
            if is_white(pieces[selected_piece_pos]) ^ is_white(pieces[(selected_piece_pos[0]+i, selected_piece_pos[1]-i)]):
                available_pos += [(selected_piece_pos[0]+i, selected_piece_pos[1]-i)]
            break
        available_pos += [(selected_piece_pos[0]+i, selected_piece_pos[1]-i)]
    # Down & right diagonal
    for i in range(1,8):
        if (selected_piece_pos[0]+i, selected_piece_pos[1]+i) in pieces:
            if is_white(pieces[selected_piece_pos]) ^ is_white(pieces[(selected_piece_pos[0]+i, selected_piece_pos[1]+i)]):
                available_pos += [(selected_piece_pos[0]+i, selected_piece_pos[1]+i)]
            break
        available_pos += [(selected_piece_pos[0]+i, selected_piece_pos[1]+i)]
    return available_pos

# Queen
def queen_movement(selected_piece_pos, pieces):
    available_pos = []
    ### Up, down, left, right
    # Check right for pieces and break once hit a piece
    for i in range(1,8):
        if (selected_piece_pos[0]+i, selected_piece_pos[1]) in pieces:
            if is_white(pieces[selected_piece_pos]) ^ is_white(pieces[(selected_piece_pos[0]+i, selected_piece_pos[1])]):
                available_pos += [(selected_piece_pos[0]+i, selected_piece_pos[1])]
            break
        available_pos += [(selected_piece_pos[0]+i, selected_piece_pos[1])]
    # Check down for pieces and break once hit a piece
    for i in range(1,8):
        if (selected_piece_pos[0], selected_piece_pos[1]+i) in pieces:
            if is_white(pieces[selected_piece_pos]) ^ is_white(pieces[(selected_piece_pos[0], selected_piece_pos[1]+i)]):
                available_pos += [(selected_piece_pos[0], selected_piece_pos[1]+i)]
            break
        available_pos += [(selected_piece_pos[0], selected_piece_pos[1]+i)]
    # Check left for pieces and break once hit a piece
    for i in range(1,8):
        if (selected_piece_pos[0]-i, selected_piece_pos[1]) in pieces:
            if is_white(pieces[selected_piece_pos]) ^ is_white(pieces[(selected_piece_pos[0]-i, selected_piece_pos[1])]):
                available_pos += [(selected_piece_pos[0]-i, selected_piece_pos[1])]
            break
        available_pos += [(selected_piece_pos[0]-i, selected_piece_pos[1])]
    # Check up for pieces and break once hit a piece
    for i in range(1,8):
        if (selected_piece_pos[0], selected_piece_pos[1]-i) in pieces:
            if is_white(pieces[selected_piece_pos]) ^ is_white(pieces[(selected_piece_pos[0], selected_piece_pos[1]-i)]):
                available_pos += [(selected_piece_pos[0], selected_piece_pos[1]-i)]
            break
        available_pos += [(selected_piece_pos[0], selected_piece_pos[1]-i)]
    ### Diagonals ###
    # Up & left diagonal
    for i in range(1,8):
        if (selected_piece_pos[0]-i, selected_piece_pos[1]-i) in pieces:
            if is_white(pieces[selected_piece_pos]) ^ is_white(pieces[(selected_piece_pos[0]-i, selected_piece_pos[1]-i)]):
                available_pos += [(selected_piece_pos[0]-i, selected_piece_pos[1]-i)]
            break
        available_pos += [(selected_piece_pos[0]-i, selected_piece_pos[1]-i)]
    # Down & left diagonal
    for i in range(1,8):
        if (selected_piece_pos[0]-i, selected_piece_pos[1]+i) in pieces:
            if is_white(pieces[selected_piece_pos]) ^ is_white(pieces[(selected_piece_pos[0]-i, selected_piece_pos[1]+i)]):
                available_pos += [(selected_piece_pos[0]-i, selected_piece_pos[1]+i)]
            break
        available_pos += [(selected_piece_pos[0]-i, selected_piece_pos[1]+i)]
    # Up & right diagonal
    for i in range(1,8):
        if (selected_piece_pos[0]+i, selected_piece_pos[1]-i) in pieces:
            if is_white(pieces[selected_piece_pos]) ^ is_white(pieces[(selected_piece_pos[0]+i, selected_piece_pos[1]-i)]):
                available_pos += [(selected_piece_pos[0]+i, selected_piece_pos[1]-i)]
            break
        available_pos += [(selected_piece_pos[0]+i, selected_piece_pos[1]-i)]
    # Down & right diagonal
    for i in range(1,8):
        if (selected_piece_pos[0]+i, selected_piece_pos[1]+i) in pieces:
            if is_white(pieces[selected_piece_pos]) ^ is_white(pieces[(selected_piece_pos[0]+i, selected_piece_pos[1]+i)]):
                available_pos += [(selected_piece_pos[0]+i, selected_piece_pos[1]+i)]
            break
        available_pos += [(selected_piece_pos[0]+i, selected_piece_pos[1]+i)]
    return available_pos

# King 
def king_movement(selected_piece_pos, pieces):
    available_pos = []
    for i in range(-1,2):
        for j in range(-1,2):
            available_pos += [(selected_piece_pos[0]+i, selected_piece_pos[1]+j)]
    available_pos.remove((selected_piece_pos[0],selected_piece_pos[1]))
    for loc in available_pos:
        if loc in pieces and not (is_white(pieces[selected_piece_pos])^is_white(pieces[loc])):
            print(is_white(pieces[selected_piece_pos]), is_white(pieces[loc]))
            available_pos.remove(loc)
    return available_pos

# =============================================================================
    # Setup board and
# =============================================================================

def initial_board(root):
    cell_size = board_size // 8 # size of one square on the chess board
    colour = ["#FFCE9E", "#D18B47"] # colour of the light and dark squares
    
    canvas = tk.Canvas(root,width = board_size, height = board_size)
    canvas.pack()
    
    selected_piece_id = None
    selected_piece_pos = None
    whites_turn = True
    pieces = {}
    
    def move_piece(event):
        nonlocal selected_piece_id, selected_piece_pos, whites_turn
        cell_x = event.x // cell_size
        cell_y = event.y // cell_size
        if selected_piece_id:
            if (is_white(selected_piece_id) ^ whites_turn):
                selected_piece_id = None
                selected_piece_pos = None
                return None
            # Check pawn movement
            if selected_piece_id % 4 == 2:
                available_pos = black_pawn_movement(selected_piece_pos, pieces)
            elif selected_piece_id % 2 == 0:
                available_pos = white_pawn_movement(selected_piece_pos, pieces)
            # Check rook movement
            elif selected_piece_id in [65,67,93,95]:
                available_pos = rook_movement(selected_piece_pos, pieces)
            # Check knight movement
            elif selected_piece_id in [69,71,89,91]:
                available_pos = knight_movement(selected_piece_pos, pieces)
            # Check bishop movement
            elif selected_piece_id in [73,75,85,87]:
                available_pos = bishop_movement(selected_piece_pos, pieces)
            # Check queen movement
            elif selected_piece_id in [77, 79]:
                available_pos = queen_movement(selected_piece_pos, pieces)
            # Check king movement
            elif selected_piece_id in [81, 83]:
                available_pos = king_movement(selected_piece_pos, pieces)
            if ((cell_x, cell_y)) not in available_pos:
                selected_piece_id = None
                selected_piece_pos = None
                return None
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
            whites_turn = not whites_turn
            print(pieces)
        elif (cell_x, cell_y) in pieces:
            # Select piece
            selected_piece_id = pieces[(cell_x, cell_y)]
            selected_piece_pos = (cell_x, cell_y)
            
    canvas.bind("<Button-1>", move_piece)
    
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
        # Create white pieces
        piece_id = canvas.create_text(100*i + 50, 750, text=piece_placement[1][i], font=("Arial", 48))
        pieces[(i, 7)] = piece_id  # Add the piece to the pieces dictionary
        # Create white pawns
        piece_id = canvas.create_text(100*i + 50, 650, text=w_pawn, font=("Arial", 48))
        pieces[(i, 6)] = piece_id  # Add the piece to the pieces dictionary
        

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