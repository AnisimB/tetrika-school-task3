

class Sudoku:
    def __init__(self):
        self.sudoku = [] # здесь будет сама судоку
                         # маска для определения номера маленького квадрата
        self.square_mask = [[1,1,1,2,2,2,3,3,3],[1,1,1,2,2,2,3,3,3],[1,1,1,2,2,2,3,3,3],[4,4,4,5,5,5,6,6,6],[4,4,4,5,5,5,6,6,6],[4,4,4,5,5,5,6,6,6],[7,7,7,8,8,8,9,9,9],[7,7,7,8,8,8,9,9,9],[7,7,7,8,8,8,9,9,9]]

    def addLine(self):
        self.sudoku.append([])
        
    def solveSudoku(self):
        max_iterations = 20 # максимальное число итераций - для защиты от нерешаемых судоку
        iterations = 0
        stop_iterations_flag = True
        while (iterations < max_iterations):
            stop_iterations_flag = True # в начале каждой итерации ставим флаг остановки
            for i in range(len(sudoku.sudoku)): # проходим по всем ячейкам судоку и подбираем значения, для каждой ячейки
                for j in range(len(sudoku.sudoku[i])):
                     if sudoku.solveCell(i, j) == True: # если за итерацию было хотя бы одно присвоение
                         stop_iterations_flag = False # то не нужно останавливать итерации, нужно продолжать
            iterations += 1
            if stop_iterations_flag == True: # если флаг так и остался - нужно остановить итерации
                break
            
        print("The sudoku is solved in " + str(iterations) + " iterations")
            
    def solveCell(self, cell_i, cell_j): # Подбор значений одной ячейки
        result_flag = False # флаг для определения момента остановки итераций
        if self.sudoku[cell_i][cell_j] == 0:
            self.candidates = [1,2,3,4,5,6,7,8,9] # изначальный список цифр - рандидатов для каждой ячейки
            for i in range(9): # перебираем значения столбца и исключаем кандидатов
                if i != cell_i:
                    if self.sudoku[i][cell_j] != 0:
                        result = self.removeFromCandidates(self.sudoku[i][cell_j])
                        if result != -1:
                            self.sudoku[cell_i][cell_j] = result
                            result_flag = True
            for j in range(9): # перебираем значения строки и исключаем кандидатов
                if j != cell_j:
                    if self.sudoku[cell_i][j] != 0:
                        result = self.removeFromCandidates(self.sudoku[cell_i][j])
                        if result != -1:
                            self.sudoku[cell_i][cell_j] = result
                            result_flag = True
                            
            small_square_index = self.square_mask[cell_i][cell_j]
            for i in range(9):# перебираем значения маленького квадрата и исключаем кандидатов
                for j in range(9):
                    if self.square_mask[i][j] == small_square_index:
                        if self.sudoku[i][j] != 0:
                            result = self.removeFromCandidates(self.sudoku[i][j])
                            if result != -1:
                                self.sudoku[cell_i][cell_j] = result
                                result_flag = True
        return result_flag

    def removeFromCandidates(self, value):  # перебирает все числа-кандидаты, сравнивая с value
        for i in range(len(self.candidates)):
            if self.candidates[i] == value:
                self.candidates.pop(i)
                if len(self.candidates) == 1: # если остаётся один кандидат
                    return self.candidates[0] # возвращаем его значение
                else:
                    return -1 # в противном случае - возвращаем -1
        return -1    


    def printSudoku(self):
        for i in range(len(sudoku.sudoku)):
            if i == 3 or i == 6:
                print(" ")
            for j in range(len(sudoku.sudoku[i])):
                if j == 3 or j == 6:
                    print(" ", end = '')
                print(" "+str(sudoku.sudoku[i][j])+str(" "), end='')
            print(" ")

    def fromFile(self, filename):
        lines = []
        self.sudoku = []
        with open(filename, "r") as file:
            line = file.readline()
            while line:
                lines.append(line)
                line = file.readline()
        print("From " + filename + " loaded sudoku:")
        for i in range(len(lines)):
            sudoku.addLine()
            for char in lines[i]:
                if char.isdigit():
                    sudoku.sudoku[i].append(int(char))
        sudoku.printSudoku()
        print(" ")
            
sudoku = Sudoku()
sudoku.fromFile("input_sudoku.txt")
sudoku.solveSudoku()
print("Solved sudoku:")
sudoku.printSudoku()
