
import math

def left_top(matrix):
    for x in range(6):#top
        matrix[0][x] = 1  
    for x in range(6):#left
        matrix[x][0] = 1 # 0,0 , 1,0 , 2,0 , 3,0  , 4,0 , 5, 0 

    for x in range(7):#bot
        matrix[6][x] = 1 # with 6,6 as well
    for x in range(6):#right
        matrix[x][6] = 1 

    for x in range(2,5):#inside top
        matrix[2][x] = 1
     
    for x in range(2,5):#inside left
        matrix[x][2] = 1

    for x in range(2,5):#inside bot
        matrix[4][x] = 1 
    
    for x in range(2,5):#inside right
        matrix[x][4] = 1 

        matrix[3][3] = 1 #mid 
 
def top_right(matrix):
    for x in range(14,21):#top
       matrix[0][x] = 1 
    for x in range(7):#left
        matrix[x][14] = 1 

    for x in range(14,21):#bot
        matrix[6][x] = 1 
    for x in range (6):#right
        matrix[x][20] = 1 
    for x in range(16,19):#top-mid
        matrix [2][x] = 1     
    for x in range (16,19):#mid-mid
        matrix [3][x] = 1
    for x in range (16,19):#bot
        matrix [4][x] = 1

def bot_left(matrix):
    for x in range(7):#top
        matrix[14][x] = 1

    for x in range(14,21):#left
        matrix[x][0] = 1

    for x in range(7):#bot
        matrix[20][x] = 1
    
    for x in range(14,21):#right
        matrix[x][6] = 1


    for x in range(2,5):#mid-top
        matrix[16][x] = 1

    for x in range(2,5):#mid-mid
        matrix[17][x] = 1
                
    for x in range(2,5):#mid-bottom
        matrix[18][x] = 1

def print_matrix(matrix):
    for row in matrix:
        print(row) 

def timing_stretcher(matrix):
    # between  bot-left & top left
    matrix[8][6] = 1 
    matrix[10][6] = 1 
    matrix[12][6] = 1 
    # between  both of top
    matrix[6][8] = 1 
    matrix[6][10] = 1 
    matrix[6][12] = 1 
    
def level_q(matrix):
    matrix[20][8] = 1 
    matrix[19][8] = 1 

    matrix[8][0] = 1 
    matrix[8][1] = 1 

def make_mask(matrix):
    #1,0,1 one option ((i+j)%2==0) 
            #1
            #0
            #1  
    # bottom
    matrix [16][8] = 1
    matrix [18][8] = 1
    #top
    matrix [8][2] = 1
    matrix [8][4] = 1

# def error_correction():
    #get 5 place to change.
    
def text_binary(string):
    size =  len(string)


def toBinary(a):
  l,m=[],[]
  for i in a:
    l.append(ord(i))
  for i in l:
    m.append(int(bin(i)[2:]))
  return m

def pair_binary_number(fires_char,second_char):
     
     firest = toBinary(fires_char)
     second = toBinary(second_char)
     print ("line 120: \n ",firest,second)

def send_pair(qr_string):
    for i in range(len(qr_string)):
        if (i % 2 != 0):
            pair_binary_number(qr_string[i-1],qr_string[i])  
        if ( i == len(qr_string)-1 and i %2 == 0):
            # do somting on the last char ,we
            print("do somting on the last char 129")
        
def mask(matrix_mask):
    for i in range(21):
        for j in range(21):
            if ((i+j)% 3==0):
                matrix_mask [i][j] = 1                 

def main():
    qr_string = input("enter a string :\n")
    count_string = len(qr_string)
    print("count_string :",count_string)
    print ("answer:",qr_string)
    toBinary(qr_string)
    print(toBinary(qr_string))
    send_pair(qr_string)
    # print("string in Binary",toBinary(count_string))
    toBinary(str(count_string))

    print("")
    matrix = [[0 for i in range(21)] for j in range(21)]
    matrix_mask = [[0 for i in range(21)] for j in range(21)] 
    matrix[0][0] = 1
    matrix[19][20] = 1
    left_top(matrix)
    top_right(matrix)
    bot_left(matrix)
    timing_stretcher(matrix)
    level_q(matrix)
    make_mask(matrix)
    print_matrix(matrix) # output matrix.

    print("")
    # mask(matrix_mask)
    # print_matrix(matrix_mask) # output matrix _ mask.
    
if __name__=='__main__':
    main()

    # test(matrix  ,top_left=(0,0) ,top_right=(6,0) ,bot_left=(0,6), bot_right=(6,6))