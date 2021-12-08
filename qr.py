import math
import re

def top_left(matrix):
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
            # do somting on the last char ,
            print("do somting on the last char 129")
        
def mask(matrix_mask):
    #creat mask
    for i in range(21):
        for j in range(21):
            if ((i+j)% 3==0):
                matrix_mask [i][j] = 1                 

def get_ascii_value(qr_string):
    list_ascii = []
    string = qr_string
    # string with encoding 'utf-8'
    arr = bytes(string, 'utf-8')
    arr2 = bytes(string, 'ascii')

    print(arr,'\n')
    # actual bytes in the the string
    for byte in arr:
        print(byte, end=' ')
        # print(byte," :146")
        list_ascii.append(byte) 
    print("\n")
    return list_ascii
    #ascii value

def ascii_to_alphanumeric(list_ascii):
    #get ascii list and make it to alphanumeric.
    #action for letters between A-Z 
    for i in range(len(list_ascii)):
        
        list_ascii[i] = list_ascii[i]-55
        print("list_ascii",list_ascii[i])
    #need to do action for spectioal caractor. 
    # $ 37 ,% 38 ,* 39 ,+ 40 , - 41 ect.
    # . 42
    # / 43
    # : 44  
    return list_ascii

def pair_to_calculat(value_to_calculat):
    for i in range(len(value_to_calculat)):
        if (i % 2 != 0):
            firest = value_to_calculat[i-1]
            second = value_to_calculat[i]
            sum = (firest * 45)+ second
            return sum

def get_input_to_binary():
    qr_string = input("enter a string in upper case only :\n")
    # while not (qr_string.isupper()):
    pattern = '^[A-Z0-9]*$'  
    while not(re.search(pattern,qr_string)):
        qr_string = input("enter a string in upper case only :\n")


    count_string = len(qr_string)
    print("count_string :",count_string)
    print ("answer:",qr_string)
    print("174",toBinary(qr_string))
    send_pair(qr_string)

    print ("use of send pair line 177" , send_pair(qr_string))
    toBinary(str(count_string))
    ascii_list= get_ascii_value(qr_string)
    print(ascii_list,"x:\n")

    value_to_calculat  = ascii_to_alphanumeric(ascii_list)
    # print("177 :",ascii_to_alphanumeric(ascii_list))
    print("value is list :",value_to_calculat)
    sum = pair_to_calculat(value_to_calculat)
    print("sum :",sum)
    
    sum_in_binary = toBinary(str(sum))
    print("sum in binary:",sum_in_binary)

def main():
    get_input_to_binary()
    
    matrix = [[0 for i in range(21)] for j in range(21)]
    matrix_mask = [[0 for i in range(21)] for j in range(21)] 
    matrix[0][0] = 1
    matrix[19][20] = 1
    top_left(matrix)
    top_right(matrix)
    bot_left(matrix)
    timing_stretcher(matrix)
    level_q(matrix)
    make_mask(matrix)  
    # print_matrix(matrix) # output matrix.

    print("")
    # mask(matrix_mask)
    # print_matrix(matrix_mask) # output matrix _ mask.
    
if __name__=='__main__':
    main()
    # test(matrix  ,top_left=(0,0) ,top_right=(6,0) ,bot_left=(0,6), bot_right=(6,6))