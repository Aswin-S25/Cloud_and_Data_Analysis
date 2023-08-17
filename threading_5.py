import pandas as pd
import threading
iris_df = pd.read_csv('dataset/Iris1.csv')

largest_lock = threading.Lock()
smallest_lock = threading.Lock()

output1 = "dataset/largest.csv"
output2 = "dataset/smallest.csv"

def write_largest_flowers():
    largest_lock.acquire()
    
    with open(output1, 'a') as f:
        largest_flowers = iris_df.groupby('Species').apply(lambda x: x.nlargest(1, 'PetalLengthCm')).reset_index(drop=True)
        f.write(largest_flowers.to_string(index = False))
   
        
    largest_lock.release()
    
def write_smallest_flowers():
    smallest_lock.acquire()
    
    with open(output2, 'a') as f:
        smallest_flower = iris_df.groupby('Species').apply(lambda x: x.nsmallest(1, 'PetalLengthCm')).reset_index(drop=True)
        f.write(smallest_flower.to_string(index=False))
        f.write("\n\n")
    
    smallest_lock.release()
    

if __name__ == "__main__":
    t1 = threading.Thread(target=write_largest_flowers)
    t2 = threading.Thread(target=write_smallest_flowers)
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
