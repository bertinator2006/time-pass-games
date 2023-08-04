import time
# import pygame


dimensional_board = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,1,0,1,0,0,0,0,0],
    [0,0,0,1,1,0,0,0,0,0],
    [0,0,0,1,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0]
]
board_width = len(dimensional_board[0])
board_height = len(dimensional_board)

board = []
for i in dimensional_board:
    for x in i:
        board.append(x)

cells_to_flip = []



# position relatives
TOP_LEFT = -board_width-1
TOP_CENTER = -board_width
TOP_RIGHT = -board_width+1
MID_LEFT = -1
MID_RIGHT = 1
BOT_LEFT = board_width-1
BOT_CENTER = board_width
BOT_RIGHT = board_width+1


def PrintBoard():
    
    global board_width
    board_line = "|"
    counter = 0
    for i in board:
        if counter == 0:
            print("__" * board_width)
        if counter % board_width == 9:
            print(board_line + "|")
            board_line = "|"
        else:
            if i == 1:
                board_line += "[]"
            elif i == 0:
                board_line += "  "
        counter += 1
    print("__" * board_width)
def CheckCellRelative(cell_index, relative_position):
    return board[cell_index + relative_position]

def CellNeighbourCount():
    global board_width, board_height
    respective_neighbour_count = []
    for cell_index, cell in enumerate(board):
        neighbour_count = 0
        
        is_right = cell_index % board_width == 9
        is_left = cell_index % board_width == 0
        is_top = cell_index % board_width == cell_index
        is_bot = cell_index + board_width > board_width * board_height - 1      

        #checking right
        if not is_right:
            neighbour_count += CheckCellRelative(cell_index, MID_RIGHT)
        if not is_left:
            neighbour_count += CheckCellRelative(cell_index, MID_LEFT)
            
        if not is_top:
            if not is_right:
                neighbour_count += CheckCellRelative(cell_index, TOP_RIGHT)
            if not is_left:
                neighbour_count += CheckCellRelative(cell_index, TOP_LEFT)
            neighbour_count += CheckCellRelative(cell_index, TOP_CENTER)
        
        if not is_bot:
            if not is_right:
                neighbour_count += CheckCellRelative(cell_index, BOT_RIGHT)
            if not is_left:
                neighbour_count += CheckCellRelative(cell_index, BOT_LEFT)
            neighbour_count += CheckCellRelative(cell_index, BOT_CENTER)
        respective_neighbour_count.append(neighbour_count)
    return respective_neighbour_count

def PrintCellNeighbour(neighbours_list):
    global board_width
    neighbours_list
    board_line = ""
    counter = 0
    for i in neighbours_list:
        if counter == board_width-1: 
            counter = 0 
            print(board_line)
            board_line = ""
        else:
            board_line += str(i)
            board_line += str(i)
            counter += 1

def FindFlippingCells(neighbours_list):
    
    cell_to_flip = []
    for index, neighbour_count in enumerate(neighbours_list):
        if board[index] == 0:
            if neighbour_count == 3:
                cell_to_flip.append(index)
        elif board[index] == 1:
            if neighbour_count < 2:
                cell_to_flip.append(index)
            elif neighbour_count > 3:
                cell_to_flip.append(index)
    
    return cell_to_flip
    
def FlipCells(list_to_flip):
    for index in list_to_flip:
        if board[index] == 1:
            board[index] = 0
        elif board[index] == 0:
            board[index] = 1
        # board[index] = -boarwd[index] + 1


#main loop time
PrintBoard()

for i in range(100):
    neighbour_counts = CellNeighbourCount()
    cells_to_flip = FindFlippingCells(neighbour_counts) #it stops working here
    FlipCells(cells_to_flip) 
    PrintBoard()
    time.sleep(0.5)

# pygame.init()
# window = pygame.display.set_mode((500,500))
# clock = pygame.Clock()

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             quit()
#     window.fill((255,255,255))
#     pygame.display.update()
#     clock.tick(60)


