
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

 
# def top_left(matrix):
#     for x in range (14,20):
#         matrix [x][0] = 1 

def print_matrix(matrix):
    for row in matrix:
        print(row) 

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
    matrix[0][0] = 1
    matrix[19][20] = 1
    left_top(matrix)
    print_matrix(matrix) # output matrix.
    
if __name__=='__main__':
    main()

    # test(matrix  ,top_left=(0,0) ,top_right=(6,0) ,bot_left=(0,6), bot_right=(6,6))