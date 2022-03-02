## Mengchen Xu
## This is the module that draw the game praphical
## this one is for the showing of the game



import pygame
import project5_logic

FRAME_RATE = 30
INIT_WIDTH = 360
INIT_HEIGHT = 650
BACKGROUND_COLOR = pygame.Color(0,0,0)
S_PINK = pygame.Color(245,91,222)
T_BLUE = pygame.Color(144,129,240)
V_GREEN = pygame.Color(129,240,131)
W_ORANGE = pygame.Color(250,131,67)
X_RED = pygame.Color(250,2,2)
Y_YELLOW = pygame.Color(244,250,67)
Z_GREY = pygame.Color(201,201,201)
LAND_COLOR = pygame.Color(158,255,237)
WHITE = pygame.Color(225,225,225)


class GraphicalGame:

    def __init__(self):
        '''initiate a variable'''
        self._running = True


    def get_board_list(self)->list:
        '''create the 13 row, and 6 column board_list'''
        s = project5_logic.Game()
        board_list = []
        board = s.new_creat_board(13,6)
        board_list.append(board)
        board_list.append(13)
        board_list.append(6)
        return board_list


    def run_game(self)->None:
        '''the main function that display the game screen'''
        time = 0
        pygame.init()        
        clock = pygame.time.Clock()
        self.build_surface((INIT_WIDTH, INIT_HEIGHT))            
        board_list = self.get_board_list()
        try:
            while self._running:             
                k = project5_logic.Run()
                s = project5_logic.Game()
                clock.tick(FRAME_RATE)        
                board_list = self.handle_events(board_list)
                board_list = self.draw_surface(board_list)
                if time%FRAME_RATE==0:
                    board_list = self.draw_surface(board_list)       
                    if not s.check_land(board_list) and not s.check_falling(board_list) and not s.check_star(board_list):
                        w = s.random_faller()
                        board_list = k.get_step_input(board_list,w)
                    else:
                        board_list = k.get_step_input(board_list,"")
                time += 1
            pygame.quit()        
        except TypeError:            
            pygame.quit()
                                        

                
    def stop_running(self) -> None:
        '''stop running the game'''
        self._running = False
        

    def build_surface(self,size:(int,int))->None:
        '''function that build the surface'''
        self.surface = pygame.display.set_mode(size,pygame.RESIZABLE)
        self._player_image_scaled = None
                           

    def handle_events(self,board_list:list) -> list:
        '''function that handle events of quit, size,key'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.stop_running()
            if event.type == pygame.VIDEORESIZE:
                self.build_surface(event.size)
            if event.type==pygame.KEYDOWN:
                board_list = self.handle_keys(board_list)
        return board_list

    
    def handle_keys(self,board_list:list) -> list:
        '''function handle the keys when people press them'''
        keys = pygame.key.get_pressed()
        a = project5_logic.Run()

        if keys[pygame.K_LEFT]:
            board_list = a.get_step_input(board_list,"<")

        if keys[pygame.K_RIGHT]:
            board_list = a.get_step_input(board_list,">")
            
        if keys[pygame.K_SPACE]:
            board_list = a.get_step_input(board_list,"R")           
        return board_list



    def frac_x_to_pixel_x(self, frac_x: float) -> int:
        '''function that deal with resize'''
        return self.frac_to_pixel(frac_x, self._surface.get_width())


    def frac_y_to_pixel_y(self, frac_y: float) -> int:
        '''function that deal with resize'''
        return self.frac_to_pixel(frac_y, self._surface.get_height())


    def frac_to_pixel(self, frac: float, max_pixel: int) -> int:
        '''function that deal with resize'''
        return int(frac * max_pixel)


    def draw_grid(self)->None:
        '''draw the grid of the game screen'''
        w, h = pygame.display.get_surface().get_size()
        deltx = h/13
        delty = w/6
        color = (255,255,255)
        for j in range(1,13):
            stax = 0
            stay = j * deltx
            enx = w
            eny = j * deltx
            pygame.draw.line(self.surface, color,[stax,stay] , [enx,eny],1)
        for i in range(1,6):
            startx = i*delty
            starty = 0
            endx = i * delty
            endy = h 
            pygame.draw.line(self.surface, color,[startx,starty] , [endx,endy],1)
            

    def draw_surface(self,board_list:list)->list:
        '''the function that draw the game screen and the grid'''
        self.surface.fill(BACKGROUND_COLOR)
        self.draw_board(board_list)
        self.draw_grid()
        pygame.display.flip()
        return board_list


    def draw_board(self,board_list:list) -> list:
        '''the function that draw the game screen'''
        w, h = pygame.display.get_surface().get_size()
        delty = h/13
        deltx = w/6
        left_topx = 0
        left_topy = 0
        right_downx = 0
        right_downy = 0
        board = board_list[0]
        for col in range(1,len(board),3):
            for row in range(2,len(board[1])):
                left_topx = ((col - 1)//3)* deltx
                left_topy = (row - 2)* delty
                if int(board[col][row]) == 0:                    
                    pygame.draw.rect(self.surface, BACKGROUND_COLOR,[left_topx,left_topy,deltx,delty])
                if int(board[col][row]) == 1:
                    pygame.draw.rect(self.surface, S_PINK,[left_topx,left_topy,deltx,delty])
                if int(board[col][row]) == 2:
                    pygame.draw.rect(self.surface, T_BLUE,[left_topx,left_topy,deltx,delty])
                if int(board[col][row]) == 3:
                    pygame.draw.rect(self.surface, V_GREEN,[left_topx,left_topy,deltx,delty])
                if int(board[col][row]) == 4:
                    pygame.draw.rect(self.surface, W_ORANGE,[left_topx,left_topy,deltx,delty])
                if int(board[col][row]) == 5:
                    pygame.draw.rect(self.surface, X_RED,[left_topx,left_topy,deltx,delty])
                if int(board[col][row]) == 6:
                    pygame.draw.rect(self.surface, Y_YELLOW,[left_topx,left_topy,deltx,delty])
                if int(board[col][row]) == 7:
                    pygame.draw.rect(self.surface, Z_GREY,[left_topx,left_topy,deltx,delty])
                if int(board[col-1][row]) == 9:
                    pygame.draw.rect(self.surface, LAND_COLOR,[left_topx,left_topy,deltx,delty],4)
                if int(board[col-1][row]) == 12:
                    right_downx = left_topx + deltx
                    right_downy = left_topy + delty
                    pygame.draw.line(self.surface, BACKGROUND_COLOR,[left_topx,left_topy],[right_downx,right_downy],4)                                                    
        return board_list

        
if __name__ == '__main__':
    GraphicalGame().run_game()        


    
