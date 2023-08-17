# prigram to read, write and display the contents of a csv file and text file using pandas and csv libraries

#using csv libraries

# import csv

# with open("dataset/demo.csv", 'w') as file1:
#     csvwriter = csv.writer(file1)
#     for i in range(2):
#         name = input("Enter the name: ")
#         age = int(input("Enter the age: "))
#         csvwriter.writerow([name, age])
    
# with open("dataset/demo.csv", 'r') as file2 :
#     csvreader = csv.reader(file2)
#     for i in csvreader :
#         print(i)
        

# using the pandas

import pandas as pd

def write_to_csv(filename, data):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"Data written to {filename} successfully")
    
def read_and_display_csv(filename):
    df = pd.read_csv(filename)
    print("content of the csv file is : \n", df)

def write_to_text(filename, data):
    with open(filename, 'w') as file:
        for line in data:
            file.write(line + '\n')
    print(f"Data written to {filename} successfully")
    
def read_and_display_text(filename):
    with open (filename, 'r') as file:
        content = file.read()
        print("content of text file: ")
        print(content)
        
#sample data for csv and text file

csv_data = [
    ["Name", "Age", "City"],
    ["Alice", 25, "New York"],
    ["Bob", 30, "Los Angeles"],
    ["Charlie", 28, "Chicago"]
]

text_data = [
    "This is a sample text file.",
    "It contains multiple lines of text.",
    "Each line is written as a separate element in the list.",
    "You can write more lines here."
]

#file path
csv_filename = 'dataset/demo.csv'
text_filename = 'dataset/demo.txt'

# write_to_csv(csv_filename, csv_data)
# write_to_text(text_filename, text_data)


read_and_display_csv(csv_filename)
# read_and_display_text(text_filename)





import csv

# with open("dataset/demo.csv", 'w') as file1 :
#     csvwriter = csv.writer(file1)
#     for i in range(2):
#         name = input("enter the name: ")
#         age = int(input("enter the age: "))
#         csvwriter.writerow([name, age])
        
# with open('dataset/demo.csv', 'r') as file2:
#     csvreader = csv.reader(file2)
#     for i in csvreader:
#         print(i)










