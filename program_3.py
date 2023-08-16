# a) sorting a csv file with multiple fields

import pandas as pd

def sorting_csvfile(filename) : 
    df = pd.read_csv(filename, sep=" ")
    df = df.sort_values(by=["age"], ascending=True)
    print(f"sorted value is \n{df}")
    
csv_filename = "dataset/student.csv"

sorting_csvfile(csv_filename)
    
# b) analysing and printing the results of a csv file based on different criteria

import pandas as pd

def res_criteria(filename):
    df = pd.read_csv(filename, sep=" ")
    df1 = df[df['age'] > 21]
    print(f"data which have age greater than 12 is \n {df1}")

    
filename = "dataset/student.csv"

res_criteria(filename)


# c) perform mergin of csv files, appending a new field to an existing csv file,
# retrieving certain fields and saving as new csv file

import pandas as pd

def merge_csv(filename1, filename2) :
    df1 = pd.read_csv(filename1)
    df2 = pd.read_csv(filename2)
    df = pd.merge(df1, df2, left_index=True, right_index=True)
    print(f"merged file is \n{df}")
    
def append_newfield(filename, field_name, field_data):
    df = pd.read_csv(filename, sep=" ")
    df[field_name] = field_data
    df.to_csv(filename, index=False)
    print(df)
    
def retriving_and_saving(filename, output_filename, selected_fields) :
    df = pd.read_csv(filename, sep=" ")
    selected_df = df[selected_fields]
    selected_df.to_csv(output_filename, sep=" ", index=False)
    
    
    
csv_filename1 = "dataset/a.csv"
csv_filename2 = "dataset/b.csv"
csv_student = "dataset/student.csv"
new_csv = "dataset/new.csv"

new_field_data = [1, 2, 3, 4]  # Example data for the new field
new_field_name = "new_field"
selected_fields = ["name", "age"]

merge_csv(csv_filename1, csv_filename2)
append_newfield(csv_student,new_field_name, new_field_data )
retriving_and_saving(csv_student, new_csv, selected_fields )


