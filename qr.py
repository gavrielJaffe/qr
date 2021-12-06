
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
    

def mask(matrix_mask):
    for i in range(21):
        for j in range(21):
            if ((i+j)%2==0):
            # if(((i*j)%3 +i +j) %2 == 0):
                matrix_mask [i][j] = 1 
                # print ("hi is working")


def main():
    qr_string = input("enter a string :\n")
    print ("answer:",qr_string)

    string = qr_string
    # string with encoding 'utf-8'
    arr = bytes(string, 'utf-8')
    arr2 = bytes(string, 'ascii')

    print(arr,'\n')
    # actual bytes in the the string
    for byte in arr:
        print(byte, end=' ')
    print("\n")
    for byte in arr2:
        print(byte, end=' ')

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


    mask(matrix_mask)
    print_matrix(matrix_mask) # output matrix _ mask.



    
if __name__=='__main__':
    main()

    # test(matrix  ,top_left=(0,0) ,top_right=(6,0) ,bot_left=(0,6), bot_right=(6,6))