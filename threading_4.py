# min and max pool

import threading

inp = [
    [5, 3, 8, 2],
    [1, 9, 4, 7],
    [6, 2, 0, 5],
    [8, 2, 5, 4],
]


matrix = []
def read_csv():
    
    for i in range(4):
        row = []
        for j in range(4):
            a = int(input(""))
            row.append(a)
        matrix.append(row)
    
    print(matrix)

min_lock = threading.Lock()
max_lock = threading.Lock()

min_value = float('inf')
max_value = -10000

def min_pooling(matrix):
    global min_value
    with min_lock:
        for row in range(0, 4, 2):
            for col in range(0, 4, 2):
                min_val = min(matrix[row][col], matrix[row][col+1], matrix[row+1][col], matrix[row+1][col+1])
                min_value = min(min_value, min_val)

def max_pooling(matrix):
    global max_value
    with max_lock:
        for row in range(0, 4, 2):
            for col in range(0, 4, 2):
                max_val = max(matrix[row][col], matrix[row][col+1], matrix[row+1][col], matrix[row+1][col+1])
                max_value = max(max_value, max_val)
                               
if __name__ == "__main__":
    
    read_csv()
    
    t1 = threading.Thread(target=min_pooling, args=(inp, ))
    t2 = threading.Thread(target=max_pooling, args=(inp, ))
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    
    print(f"min value is {min_value}")
    print(f"max value is {max_value}")