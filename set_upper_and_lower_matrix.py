import copy

example = [[1,2,3,4],[5,6,8,8],[9,10,11,21],[13,14,15,16]]
#input = copy.deepcopy(example)

# cheaking is matrix square or not
def is_square(self):
    rowcount = len(self)
    for row in self:
        if len(row) != rowcount:
            return False
    return True

# defining upper 3angle matrix
def upper3(self):
    if is_square(self) == True:
        input = copy.deepcopy(self)
        for i in range(len(input)):
            for j in range(len(input)):
                if j>i:
                   input[i][j] = 0
            print(input[i])
    else:
        print("Matrix is not square, please enter a square matrix")

# defining lower 3angle matrix
def lower3(self):
    if is_square(self) == True:
        input = copy.deepcopy(self)         # deepcopy is needed, because without it when we run two functions
        for i in range(len(input)):          # together, the second function will use the result of first function
            for j in range(len(input)):
                if j<i:
                   input[i][j] = 0
            print(input[i])
    else: print("Matrix is not square, please enter a square matrix")

upper3(example)
#lower3(example)