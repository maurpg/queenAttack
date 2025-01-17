from collections import Counter

def create_board(n):
    board= [0] * n
    for i in range(n):
        board[i] = [0] * n
    return board

def out_of_range(board,row, column,):
    global out_range
    if row>=len(board) or column>=len(board) or row<0 or column<0:
        return True
    else:
        return False

def queen_position(board,row, column):
    if out_of_range(board,row - 1, column - 1):
        print("queen can't be out of board...")
    else:
        board[row - 1][column - 1]=2
        r_row= row - 1
        r_column= column - 1
        return [r_row,r_column]

def busy(board,row, column):
    if board[row][column]==0:
        return False
    else:
        return True

def obstacle_position(board,row, column):
    if busy(board,row - 1, column - 1):
        print("an obstacle can't be where there is another object")
        quit()
    else:
        if out_of_range(board,row - 1, column - 1):
            print("an obstacle can't be out of the board...")
            quit()
        else:
            board[row - 1][column - 1] = 1

def movements(board,row, column , vector ):
    """this function printed movements of queen in the board"""
    new_x = row + vector[0]
    new_y = column + vector[1]
    count_movements = 0
    if  out_of_range(board,new_x, new_y) == False and board[new_x][new_y] == 0:
        board[new_x][new_y] = 5
        count_movements = count_movements + 1
        movements(board , new_x , new_y , vector)
        return board
    else:
        return board


def solver():
    vectors = [[-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0]]
    p_queen_col=0
    p_queen_row=0
    size=0
    num_obs=0
    file_data=''
    total_movement = 0
    #reading file
    try:
     file_data=open('tt.txt', 'r')
    except:
       print("error opening file...")
       exit()
    #passing file_data to vector and oreganize
    data=file_data.readlines()
    for i in range(0, len(data)):
     data[i]=data[i].split()
    #operating file_data
    try:
        size=int(data[0][0])
        num_obs = int(data[0][1])
        p_queen_row=int(data[1][0])
        p_queen_col=int(data[1][1])

    except:
        print("document dosen't have correct format")
        exit()
    total=0
    board=create_board(size)
    queen=queen_position(board,p_queen_row, p_queen_col)
    # checking there aren't obstacles
    if num_obs>=1 or num_obs==0:
      for i in range(2, len(data)):
          total+=1
      if num_obs==total:
            try :
                for i in range(2, len(data)):
                     cont=0
                     fil=int(data[i][cont])
                     cont+=1
                     col=int(data[i][cont])
                     obstacle_position(board,fil, col)
            except:
              print("document dosen't have correct format")
              exit()
            # checking queen movements
            for vector in vectors:
                table  = movements(board,queen[0], queen[1] , vector)


      else:
          print("there are more or less obstacles than the document has")
          exit()


    return table

table = solver()

def counter_movements(board):
    """this function count all the movement of queen """
    total = 0
    for column in board:
        print(column)
        t = Counter(column).get(5)
        try:
            total = total + t
        except:
            pass
    print(total)


counter_movements(table)

'''
mov=0
    vectors=[[-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0]]
    #movements
    for i in range(0, len(vectors)):
        t_row = row
        t_col = column
        go_ahead=True
        while go_ahead==True:
            count = 0
            t_row+=vectors[i][count]
            count+=1
            t_col+=vectors[i][count]
            if out_of_range(board,t_row, t_col):
                go_ahead = False
            else:
                if busy(board,t_row, t_col):
                    go_ahead = False
                else:
                    mov+=1
    return "movements that queen can do: "+str(mov)
'''