## Mengchen Xu
## this is the module that deal with the game logic
## it is almost the same as the last project,
## but I modified the user_interface from last project
## and add it here as another class called Run



from random import randrange

class Game:


# the function that creat a new game board, take the use's input as parameters
    def new_creat_board(self,row:int, column:int)-> [[]]:
        '''creat a new, empty game board'''
        board = []
        for col in range(int(column)*3):
            board.append([])
            for ro in range(int(row)+2):
                board[-1].append(0)
        return board

# function that change the string input into list, easier to handle list than string
    def str_to_list(self,example:str)->list:
        '''function that change the user input(str) into list'''
        result = []
        for i in example:
            result.append(i)
        return result
        
    def translate(self,str_list:[str])->list:
        '''translate the input letters into numbers that represent them'''
        num_list = []
        table = str.maketrans("MSTVWXYZ_|","0123456789")
        for j in str_list:
            c = j.translate(table)
            num_list.append(c)
        return num_list


    def add_side(self,board:[[]])->[[]]:
        '''add the sides of the game board to the 2D list'''
        side = "|"
        board1 = self.copy_game_board(board)
        for i in range(len(board1)):
            sides = side * len(board1[i])
        side_list_1 = self.str_to_list(sides)
        side_list = self.translate(side_list_1)
        board1.insert(0,side_list)
        board1.append(side_list)
        for j in range(len(board1)-1):
            board1[j].append(0)        
        for i in range(1,len(board1)-1):
            board1[i][-1]=8    
        return board1


    def copy_game_board(self,board: [[]]) -> [[]]:
        '''Copies the given game board'''
        jr = len(board[0]) - 2
        ic = len(board)//3
        board_copy = self.new_creat_board(jr,ic)
        for col in range(len(board)):
            for row in range(len(board[col])):
                board_copy[col][row] = board[col][row]
        return board_copy


    def print_board(self,board:[[]])->None:
        '''print the game board with all the sides added on the 2D list'''
        board1 = self.add_side(board)
        point = ""
        column = len(board1)
        row = len(board1[1])    
        for i in range(2,row):
            for j in range(column):
                if int(board1[j][i]) == 0:
                    point = " "
                elif int(board1[j][i]) == 1:
                    point = "S"
                elif int(board1[j][i]) == 2:
                    point = "T"
                elif int(board1[j][i]) == 3:
                    point = "V"
                elif int(board1[j][i]) == 4:
                    point = "W"
                elif int(board1[j][i]) == 5:
                    point = "X"
                elif int(board1[j][i]) == 6:
                    point = "Y"
                elif int(board1[j][i]) == 7:
                    point = "Z"
                elif int(board1[j][i]) == 8:
                    point = "-"
                elif int(board1[j][i]) == 9:
                    point = "|"
                elif int(board1[j][i]) == 10:
                    point = "["
                elif int(board1[j][i]) == 11:
                    point = "]"
                elif int(board1[j][i]) == 12:
                    point = "*" 
                else:
                    point = board1[j][i]
                print(point,end = "")   
            print()
# the function that change a list of list to a list of string,or list of number
    def move_extra_list(self,result:[[str]])->[str]:
        '''function that remove extra list in a list'''
        r_list = []
        for i in result:
            for j in i:
                r_list.append(j)
        return r_list

    def find_bottom_empty_row(self,board: [[]], raw:int,column_number: int) -> int:
        '''find the bottom empty row of the specific column,return the bottom row number'''
        for i in range(int(raw) - 1 +2, 1, -1):
            if int(board[int(column_number)][i]) == 0:
                return i
#       if there are no bottom empty row, return -1
        return -1

    def convert_color_to_number(self,result:list)->list:
        '''function that convert color to numbers'''
        result_list = []
        num_list = []
        table = str.maketrans("MSTVWXYZ-","012345678")
        for i in result:
            s = i.replace(" ","M")
            k = self.str_to_list(s)
            num_list = self.translate(k)
            result_list.append(num_list)
        return result_list  

    def creat_content_board(self,raw:int,column:int,content_list:list)-> list:
        '''the function that create a board with contents when initialize the contents'''
        board_list=[]
        board = self.new_creat_board(raw,column)  
        for i in range(len(content_list)-1,-1,-1):
            for j in range(len(content_list[i])):
                col = (j+1)*3-2
                raw1 = self.find_bottom_empty_row(board,raw,col)
                board[col][raw1] = content_list[i][j]            
        board_list.append(board)
        board_list.append(raw)
        board_list.append(column)
        return board_list
    
    def three_str_in_column(self,three_str_list:list,result_list:list,column:int)->list:
        '''function that creat a list of the positions of the three jews form the command input'''
        board = result_list[0]
        board_list = []
        r_list = []
        command_list = self.convert_color_to_number(three_str_list)
        command_list = self.move_extra_list(command_list)
        col = int(column)*3 - 2
        co_row = 2
        jew_list = []
        row = self.find_bottom_empty_row(board,result_list[1],col)
        for i in command_list:
            board[col-1][co_row] = "10"
            board[col+1][co_row] = "11"        
            board[col][co_row] = i
            jew_list.append((col,co_row))
            co_row -= 1
        board_list.append(board)
        board_list.append(result_list[1])
        board_list.append(column)
        board_list.extend(jew_list)
        return board_list
            
    def command_to_three_str_list(self,command:list)->list:
        '''reverse the three jews order in the command list'''
        three_str_list = []
        for i in range(len(command)-1,1,-1):
            three_str_list.append(command[i])
        return three_str_list


# the function that put the three jews in the board,
# and with only the bottom one showing in the board
    def falling(self,result_list:list,command:list)->list:
        '''the function that put the three jews in the board'''
        three_str_list = self.command_to_three_str_list(command)
        board_list = self.three_str_in_column(three_str_list,result_list,command[1])
        return board_list

# get the position and the color of the three jewels
    def get_col_row(self,result_list:list,board:list)->["col","firstRow","secondRow","thirdRow","first","second","third"]:
        '''function that only return the column and row list, no game board included'''
        a_list = []
        col = result_list[3][0]
        first_row = result_list[3][1]
        second_row = result_list[4][1]
        third_row = result_list[5][1]
        first = board[col][first_row]
        second = board[col][second_row]
        third = board[col][third_row]
        a_list.append(col)
        a_list.append(first_row)
        a_list.append(second_row)
        a_list.append(third_row)
        a_list.append(first)
        a_list.append(second)
        a_list.append(third)
        return a_list
   
    def fall_one(self,result_list:list)-> list:
        '''the function that falls the three jews one row down'''    
        r_list = []
        board = result_list[0]
        a = self.get_col_row(result_list,board)
        board[a[0]][a[1]] = 0
        board[a[0]][a[2]] = 0
        board[a[0]][a[3]] = 0
        board[a[0]][a[1]+1] = a[4]
        board[a[0]][a[2]+1]= a[5]
        board[a[0]][a[3]+1] = a[6]
        r_list.append(board)
        r_list.append(result_list[1])
        r_list.append(result_list[2])
        r_list.append((a[0],a[1]+1))
        r_list.append((a[0],a[2]+1))
        r_list.append((a[0],a[3]+1))
        board[a[0]-1][a[3]]=0
        board[a[0]-1][a[1]+1]=10
        board[a[0]+1][a[3]]=0
        board[a[0]+1][a[1]+1]=11
        return r_list

# function that change the game state from falling into landing
    def change_br_to_line(self,board_list:list)->list:
        '''change the brackets in the game board into lines'''
        r_list = []
        board = board_list[0]
        for i in range(len(board)):
            for j in range(len(board[i])):
                if int(board[i][j]) == 10 or int(board[i][j]) == 11:
                    board[i][j] = 9
                else:
                    None
        r_list.append(board)
        r_list.extend(board_list[1:])
        return r_list

# the function that change the game state from landing to freezing
    def frozen(self,board_list:list)->list:
        '''change the brackts to line, and remove the line from the game board'''
        board_list = self.change_br_to_line(board_list)
        r_list = []
        board = board_list[0]
        for i in range(len(board)):
            for j in range(len(board[i])):
                if int(board[i][j]) == 9:
                    board[i][j] = 0                
                else:
                    None   
        r_list.append(board)
        r_list.extend(board_list[1:])
        return r_list

# function that check the game state, if the state is falling, return True,else return Flase
    def check_br_line(self,board_list:list)->bool:
        '''check if the brackts exist in the game board'''
        board = board_list[0]
        d = False
        for i in range(1,len(board)-1):
            for j in range(len(board[i])):
                if int(board[i][j]) == 9 or int(board[i][j]) == 10 or int(board[i][j]) == 11:
                    d = True
        return d

#  function that just remove the line of the game board           
    def remove_line(self,board_list:list)->list:
        '''remove the line of the game board'''
        r_list = []
        board = board_list[0]
        for i in range(len(board)):
            for j in range(len(board[i])):
                if int(board[i][j]) == 9:
                    board[i][j] = 0                
                else:
                    None   
        r_list.append(board)
        r_list.extend(board_list[1:])
        return r_list

    def rotate_one(self,result_list:list)->list:
        '''the function that rotate the three jews'''
        board = result_list[0]
        r_list = []
        a_list = result_list[1:]
        b = self.get_col_row(result_list,board)
        board[b[0]][b[1]] = b[5]
        board[b[0]][b[2]] = b[6]
        board[b[0]][b[3]] = b[4]
        r_list.append(board)
        r_list.extend(a_list)
        return r_list

# move the three jews one column left, do nothing if the jews cannot move one step left
    def left_one(self,result_list:list)->list:
        '''move the three jews one column left'''
     
        r_list = []
        board = result_list[0]
        a = self.get_col_row(result_list,board)
        sign1 = board[a[0]-1][a[1]]
        sign2 = board[a[0]+1][a[1]]    
        if int(a[0]-1) != 0 and int(board[a[0]-3][a[1]]) == 0:
            board[a[0]-4][a[1]] = sign1
            board[a[0]-4][a[2]] = sign1
            board[a[0]-4][a[3]] = sign1
            board[a[0]-3][a[1]] = a[4]
            board[a[0]-3][a[2]] = a[5]
            board[a[0]-3][a[3]] = a[6]
            board[a[0]-2][a[1]] = sign2
            board[a[0]-2][a[2]] = sign2
            board[a[0]-2][a[3]] = sign2
            board[a[0]+1][a[1]] = 0
            board[a[0]+1][a[2]] = 0
            board[a[0]+1][a[3]] = 0
            board[a[0]][a[1]] = 0
            board[a[0]][a[2]] = 0
            board[a[0]][a[3]] = 0
            board[a[0]-1][a[1]] = 0
            board[a[0]-1][a[2]] = 0
            board[a[0]-1][a[3]] = 0
            r_list.append(board)
            r_list.append(result_list[1])
            r_list.append(result_list[2])
            r_list.append((a[0]-3,a[1]))
            r_list.append((a[0]-3,a[2]))
            r_list.append((a[0]-3,a[3]))        
            return r_list
        else:
          
            return result_list

# move the three jews one column right, do nothing if the jews cannot move one step right
    def right_one(self,result_list:list)->list:
        '''move the three jews one column left'''
        r_list = []
        board = result_list[0]
        a = self.get_col_row(result_list,board)
        sign1 = board[a[0]-1][a[1]]
        sign2 = board[a[0]+1][a[1]]
        if a[0]+3 < len(board):
            if a[0]+1 != len(board)-1 and board[a[0]+3][a[1]] == 0:
                board[a[0]+2][a[1]] = sign1
                board[a[0]+2][a[2]] = sign1
                board[a[0]+2][a[3]] = sign1
                board[a[0]+3][a[1]] = a[4]
                board[a[0]+3][a[2]] = a[5]
                board[a[0]+3][a[3]] = a[6]
                board[a[0]+4][a[1]] = sign2
                board[a[0]+4][a[2]] = sign2
                board[a[0]+4][a[3]] = sign2
                board[a[0]+1][a[1]] = 0
                board[a[0]+1][a[2]] = 0
                board[a[0]+1][a[3]] = 0
                board[a[0]][a[1]] = 0
                board[a[0]][a[2]] = 0
                board[a[0]][a[3]] = 0
                board[a[0]-1][a[1]] = 0
                board[a[0]-1][a[2]] = 0
                board[a[0]-1][a[3]] = 0
                r_list.append(board)
                r_list.append(result_list[1])
                r_list.append(result_list[2])
                r_list.append((a[0]+3,a[1]))
                r_list.append((a[0]+3,a[2]))
                r_list.append((a[0]+3,a[3]))
                return r_list
            else:
     
                return result_list
        else:
            return result_list

# find match that is in the horizontal left direction,
# and add the position of the matched jews into the result list
    def determine_match_hori_left(self,board:[[]],orow:int,ocol:int)->list:
        '''find match that is in the horizontal left direction'''
        r_list = []
        i = ocol
        j = orow
        r_list.append((ocol,orow))
        count = ocol
        for count in range((ocol+1)//3,0,-1):
            num = board[i][j]
            num1 = board[i-3][j]
            if num == num1 and num != 0 :
                r_list.append((i-3,j))
                i = i - 3
                count -= 1
        else:
            None
        return r_list
    
# find match that is in the vertical down direction,
# and add the position of the matched jews into the result list            
    def determine_match_verti_down(self,board:[[]],orow:int,ocol:int)->list:
        '''find match that is in the vertical down direction'''
        row = len(board[0])
        r_list = []
        i = ocol
        j = orow
        r_list.append((ocol,orow))
        count = orow
        for count in range(orow,row-1):
            num = board[i][j]
            num1 = board[i][j+1]
            if num == num1 and num != 0 :
                r_list.append((i,j+1))
                j = j + 1
                count += 1
            else:
                None
        return r_list

# find match that is in the diagonal left down direction,
# and add the position of the matched jews into the result list
    def determine_match_dia_left_down(self,board:[[]],orow:int,ocol:int)->list:
        '''find match that is in the diagonal left down direction'''
        row = len(board[0])
        r_list = []
        i = ocol
        j = orow
        r_list.append((ocol,orow))
        count = orow
        times = ocol
        for count in range(orow,row-1):
            for count in range((ocol+1)//3,0,-1):
                if i - 3 > 0 and j+1 <= row-1:
                    num = board[i][j]
                    num1 = board[i-3][j+1]
                    if num == num1 and num != 0 :
                        r_list.append((i-3,j+1))
                        i = i - 3
                        j = j + 1
                        count += 1
                        times -= 1
                    else:
                        None
                else:
                    None
        return r_list

# find match that is in the diagonal right down direction,
# and add the position of the matched jews into the result list    
    def determine_match_dia_right_down(self,board:[[]],orow:int,ocol:int)->list:
        '''find match that is in the diagonal right down direction'''
        row = len(board[0])
        col = len(board)
        r_list = []
        i = ocol
        j = orow
        r_list.append((ocol,orow))
        count = orow
        times = ocol
        for count in range(orow,row-1):            
            for times in range(1,(col)//3):
                if i+3 < col and j +1 <= row - 1:
                    num = board[i][j]
                    num1 = board[i+3][j+1]                    
                    if num == num1 and num != 0 :
                        r_list.append((i+3,j+1))
                        i = i + 3
                        j = j + 1
                        count += 1
                        times += 1
                    else:
                        None
                else:
                    None
        return r_list

            
    def match(self,board_list:list)->list:
        '''check the four directions of all jews, and return the list of seccessfully matched jews'''
        a_list= []
        board = board_list[0]
        a_list.extend(board_list)
        b_list = []
        for col in range(1,len(board),3):
            for row in range(2,len(board[col])):
                r1_list = self.determine_match_hori_left(board,row,col)
                r2_list = self.determine_match_verti_down(board,row,col)
                r3_list = self.determine_match_dia_left_down(board,row,col)
                r4_list = self.determine_match_dia_right_down(board,row,col)
                if len(r1_list)>= 3:
                    b_list.extend(r1_list)
                if len(r2_list)>= 3:
                    b_list.extend(r2_list)
                if len(r3_list)>= 3:
                    b_list.extend(r3_list)
                if len(r4_list)>= 3:
                    b_list.extend(r4_list)                   
                else:
                    None
        c = len(b_list)
        a_list.extend(b_list)
        a_list.append(c)
        return a_list


    def add_star(self,board_list:list)->list:
        '''add star symbol to the sides of the matched jews'''
        r_list = board_list[1:]
        board = board_list[0]
        a_list = []
        f = -1 * (board_list[-1]+1)   
        for i in board_list[f:-1]:    
            board[i[0]-1][i[1]] = 12
            board[i[0]+1][i[1]] = 12
        a_list.append(board)
        a_list.extend(r_list)
        return a_list

    def disapear(self,board_list:list)->list:
        '''make the matched jews disapear from the board(change to space)'''
        result_list = []
        print(board_list[0])
        f = -1 * (board_list[-1] + 1)
        r_list = board_list[1:f]
        board = board_list[0]    
        for i in board_list[f:-1]:
            board[i[0]][i[1]] = 0
        result_list.append(board)
        result_list.extend(r_list)
        print(result_list[0])
        return result_list

# change the stars to space after changing all the matched jews into space           
    def change_star_to_sp(self,board_list:list)->list:
        '''change the stars to space'''
        r_list = []
        board = board_list[0]
        for i in range(len(board)):
            for j in range(len(board[i])):
                if int(board[i][j]) == 12:
                    board[i][j] = 0
                else:
                    None
        r_list.append(board)
        r_list.extend(board_list[1:])
        return r_list

# check the state of the board, return True if the game state is either falling or landing
    def check_state(self,board_list:list)->bool:
        '''check the state of the board'''
        board = board_list[0]
        r_list = []
        for i in range(len(board)):
            for j in range(len(board[i])):
                if int(board[i][j]) == 9:
                    r_list.append(board[i][j])
                elif int(board[i][j]) == 10:
                    r_list.append(board[i][j])
                elif int(board[i][j]) == 11:
                    r_list.append(board[i][j])
                else:
                    None
        if len(r_list) != 0:
            return True
        else:
            return False

# check the state of the board, return True if the game state is matching   
    def check_star(self,board_list:list)->bool:
        '''check the game state'''
        board = board_list[0]
        r_list = []
        for i in range(len(board)):
            for j in range(len(board[i])):
                if int(board[i][j]) == 12:
                    r_list.append(board[i][j])
                else:
                    None
        if len(r_list) != 0:
            return True
        else:
            return False


# check the state of the board, return True if the game state is landing         
    def check_land(self,board_list:list)->bool:
        '''check the game state'''
        board = board_list[0]
        d = False
        r_list = []
        for i in range(len(board)):
            for j in range(len(board[i])):
                if int(board[i][j]) == 9:
                    r_list.append(board[i][j])
                else:
                    None
        if len(r_list) != 0:
            d = True
        return d
        

# check the state of the board, return True if the game state is falling  
    def check_falling(self,board_list:list)->bool:
        '''check the game state'''
        board = board_list[0]
        r_list = []
        d = False
        for i in range(len(board)):
            for j in range(len(board[i])):
                if int(board[i][j]) == 10 or int(board[i][j])== 11:
                    r_list.append(board[i][j])
                else:
                    None
        if len(r_list) != 0:
            d = True
        return d

        
    def fill_space(self,board_list:list)->list:
        '''fill the blank spaces after matching'''
        f = -1 * (board_list[-1]+1)
        c_points = board_list[f:-1]
        match_points = []
        for i in c_points:
            ci = i[0]
            ri = i[1]-1
            match_points.append((ci,ri))
            
        board_list = self.change_star_to_sp(board_list)
        board_list = self.disapear(board_list)
        a_list = board_list[1:]
        r_list = []
        board = board_list[0]
        raw = board_list[1]
        column = board_list[2]
        for j in match_points:
            row = self.find_bottom_empty_row(board,raw,j[0])
            board[j[0]][row] = board[j[0]][j[1]]
            board[j[0]][j[1]] = 0
        
        board = self.check_one_position_below(board)
        r_list.append(board)
        r_list.extend(a_list)
        return r_list


    def check_one_position_below(self,board:list)->list:
        '''check one row beloew, if it is balnk, replace it with the color one row above'''
        
        raw = len(board[0])-2
        for i in range(len(board)):
            for j in range(len(board[i])-1,1,-1):
                if board[i][j] != 0 and j + 1 < len(board[i]):
       
                    row = self.find_bottom_empty_row(board,raw,i)
                    if row != -1 and row != j:  
                        board[i][row] = board[i][j]
                        board[i][j] = 0
                    else:
               
                        None
                else:
                    None
        return board

    def translate_to_letter(self,str_list:[str])->list:
        '''translate the input letters into numbers that represent them'''
        num_list = []
        table = str.maketrans("0123456789","MSTVWXYZ_|")
        for j in str_list:
            c = j.translate(table)
            num_list.append(c)
        return num_list

    def random_faller(self)->[]:
        '''logic for the pygame to create random faller'''
        answer_list = []
        three_jews_list = []
        c = randrange(1,7)
        f1 = randrange(1,8)
        f2 = randrange(1,8)
        f3 = randrange(1,8)        
        three_jews_list.append(str(f1))
        three_jews_list.append(str(f2))
        three_jews_list.append(str(f3))
        three_jews_list1 = self.translate_to_letter(three_jews_list)
        three_jews_list1.insert(0,str(c))
        answer_list.append("F")
        answer_list.extend(three_jews_list1)
        return answer_list



# the class of the GameOver Error
class GameOver(Exception):
    pass




class Run:

# this is the same part as the use-interface from last project but without the
# user input part.

    def get_step_input(self,board_list:list,w)->list:
        '''the main function that handle every input except the "creat new board" command'''
    
        co = 1
        g = Game()
        f = GameOver()
        
        try:
# the line deal with the Q command            
            if len(w) != 0 and w[0] != "Q":
# the line deal with the F command                      
                if w[0] == "F":
                    board_list = g.falling(board_list,w)
                    col = board_list[3][0]
                    co += 1
# the line deal with the R command                     
                elif w[0] == "R":
                    if g.check_br_line(board_list):
                        board_list = g.rotate_one(board_list)                        
                        col = board_list[3][0]
                    else:
                        pass
# the line deal with the left command 
                elif w[0] == "<":
                    if g.check_br_line(board_list):                      
                        board_list = g.left_one(board_list)                     
                        col = board_list[3][0]
                    else:
                        pass
# the line deal with the right command                    
                elif w[0] == ">":
                    if g.check_br_line(board_list):
                        board_list = g.right_one(board_list)
                        col = board_list[3][0]
                    else:
                        pass
                else:
                    None
# the block that deal with the "" command                    
            elif len(w) == 0:         
                col = board_list[3][0]
                if g.check_state(board_list):                    
                    row = g.find_bottom_empty_row(board_list[0],board_list[1],col)
                    row1 = board_list[3][1] + 1
                    df = row - row1                                   
                    if row != -1:                     
                        if df >= 1:                          
                            board_list = g.fall_one(board_list)
                        elif df == 0:                            
                            board_list = g.fall_one(board_list)
                            g.change_br_to_line(board_list)
                        else:
                            board_list = g.match(board_list)
                            board_list = g.add_star(board_list)
                            board_list = g.remove_line(board_list)
                            if g.check_star(board_list):
                                board = board_list[0]
                                board_list = g.fill_space(board_list)
                            else:
                                board_list = g.frozen(board_list)
                                if board_list[5][1] <3:
                                    raise GameOver()
                    elif row == -1:                      
                        if co == 0:
                            board_list = g.change_br_to_line(board_list)
                            co += 1
                        else:
                            board_list = g.frozen(board_list)
                            board_list = g.match(board_list)
                            board_list = g.add_star(board_list)
                            if g.check_star(board_list):
                                board = board_list[0]
                                board_list = g.fill_space(board_list)
                            else:
                                if board_list[5][1] < 3:                                    
                                    raise GameOver()
                else:                   
                    if co == 0:                        
                        board_list = g.fill_space(board_list)
                        board_list = g.match(board_list)
                        board_list = g.add_star(board_list)
                        if g.check_star(board_list):
                            pass
                        else:
                            pass
                    else:
                        board_list = g.match(board_list)
                        board_list = g.add_star(board_list)
                        if g.check_star(board_list):
                            board = board_list[0]
                            board_list = g.fill_space(board_list)
                        else:
                            pass
# if the game ends, the return -1, so it is easier to determine the type
            elif len(w) != 0 and w[0] == "Q":
                return -1
            else:
                pass
        except GameOver:
            return -1
# return the game list if nothing happended.
        return board_list
                              
        

