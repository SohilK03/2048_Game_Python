import random
def start_game():
    mat=[[0 for i in range(4)] for j in range(4)]
    return mat

def add_new_2(mat):
    r=random.randint(0,3)
    c=random.randint(0,3)
    while mat[r][c]!=0:
        r=random.randint(0,3)
        c=random.randint(0,3)
    mat[r][c]=2


def compress(mat):
    new_mat=[[0 for j in range(4)] for i in range(4)]
    chan=False
    for i in range(4):
        pos=0
        for j in range(4):
            if mat[i][j]!=0:
                new_mat[i][pos]=mat[i][j]
                if pos!=j:
                    chan=True
                pos+=1
                
    return new_mat,chan

def merge(mat):
    chan=False
    for i in range(4):
        for j in range(3):
            if mat[i][j]==mat[i][j+1] and mat[i][j] !=0:
                mat[i][j]*=2
                mat[i][j+1]=0
                chan=True
    return mat,chan

def reverse(mat):
    new_mat=[[0 for j in range(4)] for i in range(4)]
    for i in range(4):
        for j in range(4):
            new_mat[i][j]=mat[i][4-j-1]

    return new_mat

def transpose(mat):
    new_mat=[[0 for j in range(4)] for i in range(4)]
    for i in range(4):
        for j in range(4):
            new_mat[i][j]=mat[j][i]
    return new_mat

def move_up(grid):
    #Implement This Function
    ans1=transpose(grid)
    ans2,changed1=compress(ans1)
    ans3,changed2=merge(ans2)
    changed=changed1 or changed2
    ans4=compress(ans3)
    ans5=transpose(ans4)
    for i in range(4):
        for j in range(4):
            grid[i][j]=ans5[i][j]
    return grid,changed
    

def move_down(grid):
    
    ans1=transpose(grid)
    ans2=reverse(ans1)
    ans3,changed1=compress(ans2)
    ans4,changed2=merge(ans3)
    changed=changed1 or changed2
    ans5=compress(ans4)
    ans6=reverse(ans5)
    ans7=transpose(ans6)
    for i in range(4):
        for j in range(4):
            grid[i][j]=ans7[i][j]
            
    return grid,changed
    
    

def move_right(grid):
    #Implement This Function
    ans1=reverse(grid)
    ans2,changed1=compress(ans1)
    ans3,changed2=merge(ans2)
    changed=changed1 or changed2
    ans4=compress(ans3)
    ans5=reverse(ans4)
    
    for i in range(4):
        for j in range(4):
            grid[i][j]=ans5[i][j]
            
    return grid,changed
    
    

    

def move_left(grid):
    
    ans2,changed1=compress(grid)
    ans3,changed2=merge(ans2)
    changed=changed1 or changed2

    ans4,temp=compress(ans3)

    
    for i in range(4):
        for j in range(4):
            grid[i][j]=ans4[i][j]
            
    return grid,changed
    

def get_current_state(mat):
    empty=0
    adjSame=0
    for i in range(4):
        for j in range(4):
            if i+1<3 and j+1<3 and (mat[i][j]==mat[i+1][j] or mat[i][j]==mat[i][j+1]):
                adjSame=1
            if mat[i][j]==0:
                empty=1
            if mat[i][j]==2048:
                return 'WON'
    if empty:
        return 'GAME NOT OVER'
    if adjSame:
        return 'GAME NOT OVER'

    return 'GAME OVER'
    

    