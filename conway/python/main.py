import time
import pygame

#board initialisation
dimensional_board = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,1,0,1,0,0,0,0,0],
    [0,0,0,1,1,0,0,0,0,0],
    [0,0,0,1,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,1,0,0,0,0,0,0,0,0],
    [0,1,0,0,0,0,0,0,0,0],
    [0,1,0,0,0,0,0,0,0,0]
]
board_width = len(dimensional_board[0])
board_height = len(dimensional_board)
board = []
cells_to_flip = []

# CONSTANTS
TOP_LEFT = -board_width-1
TOP_CENTER = -board_width
TOP_RIGHT = -board_width+1
MID_LEFT = -1
MID_RIGHT = 1
BOT_LEFT = board_width-1
BOT_CENTER = board_width
BOT_RIGHT = board_width+1
TILE_SIZE = 30
FPS = 5

#setting the 1D array for board
for i in dimensional_board:
    for x in i:
        board.append(x)

pygame.init()
window = pygame.display.set_mode((TILE_SIZE * board_width,TILE_SIZE * board_height))
clock = pygame.time.Clock()

cells_to_flip = []
is_first = True


def UpdateDisplay():
    global board_width
    window.fill((0,0,0))
    for index_tile, tile in enumerate(board):
        if tile == 1:
            tile_rect = pygame.Rect((index_tile % board_width) * TILE_SIZE, (index_tile // board_width) * TILE_SIZE, TILE_SIZE, TILE_SIZE)
            pygame.draw.rect(window,  (255,255,255), tile_rect)

    if is_first:
        return 1

    rects_to_update = []
    for cell in cells_to_flip:
        rects_to_update.append(pygame.Rect((cell % board_width) * TILE_SIZE, (cell // board_width) * TILE_SIZE, TILE_SIZE, TILE_SIZE))
    pygame.display.update(rects_to_update)
    return 0

def CheckCellRelative(cell_index, relative_position):
    return board[cell_index + relative_position]

def CellNeighbourCount():
    global board_width, board_height
    respective_neighbour_count = []
    for cell_index, cell in enumerate(board):
        neighbour_count = 0
        
        is_right = cell_index % board_width == board_width - 1
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
        
    cell_to_flip = []
    for index, neighbour_count in enumerate(respective_neighbour_count):
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


# main program
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_SPACE:
                pass
                # cells_to_flip = CellNeighbourCount()
                # FlipCells(cells_to_flip)
    
    if UpdateDisplay():
        pygame.display.update()
        is_first = False
    
    clock.tick(FPS)
    cells_to_flip = CellNeighbourCount()
    FlipCells(cells_to_flip)
    
    

pygame.quit()

