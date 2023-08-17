import threading 


def process_file(filename, outputfile, char_type) :
    with open(filename, 'r') as file:
        characters = file.read()
        with open(outputfile, 'w') as output :
            for char in characters:
                if char_type(char) :
                    output.write(char)
                    
                   
filename = "dataset/t.csv"
output1 = "dataset/output1.csv"
output2 = "dataset/output2.csv"
output3 = "dataset/output3.csv"

if __name__ == "__main__" :
    t1 = threading.Thread(target=process_file, args=(filename, output1, str.isalpha))
    t2 = threading.Thread(target=process_file, args=(filename, output2, str.isdigit))
    t3 = threading.Thread(target=process_file, args=(filename, output3, lambda char: not char.isalnum()))
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()