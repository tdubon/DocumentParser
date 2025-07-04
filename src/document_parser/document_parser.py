import csv
import re

# for documents in .docx or .doc: create a command to open file and save as copy in plain text
"""Parser currently setup to be used with .txt files only"""
class Parser:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.lines = []
        self.long_string = ""
        self.sentence_list = []
        self.text = []

    def read_in_lines(self):
        with open(self.folder_path, "r", newline="", encoding="utf-8") as f:
            self.lines = f.readlines()
            return self.lines
    
    def sentence_parse(self):
        # attach each line and save as a long string
        for i in self.lines:
            self.long_string = self.long_string + " " + i.strip()

        #split string by punctuation
        pattern = r'[.!?]\s+|\s{2}|#'  #match by punctuation
        self.sentence_list = re.split(pattern, self.long_string.strip())
        return self.sentence_list
        
    def word_parse(self):
            self.text = re.split(r'([,.:;?_!"+/()*#=<>]+|-|--|[\]]+|[\[]+|\s|[\n]+)', self.long_string)
            self.text = [item.strip() for item in self.text if item.strip()]
            return self.text

    #requires output from word_parse
    def vocab(self):
            self.vocab = {token:integer for integer, token in enumerate(self.text)}
            return(self.vocab)
    
    # use to convert text into json format where every sentence is indexed
    def sentence_dict(self):
        self.data_dict = {idx: value for idx, value in enumerate(self.sentence_list)}
        return self.data_dict
    
    def encode(self):
        self.str_to_int = self.vocab
        self.int_to_str = {i:s for s,i in self.vocab.items()}
        preprocessed = [item if item in self.str_to_int else "<|unk|>" for item in self.text]
        self.ids = [self.str_to_int[s] for s in preprocessed]
        return self.ids  

    def decode(self):
        self.decoded_text = " ".join([self.int_to_str[i] for i in self.ids])
        self.decoded_text = re.sub(r'\s+([,.?!"()\'])', r'\1', self.decoded_text) #removes space before these punctuations
        return self.decoded_text 

class CSV_reader:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.records = {}

    # read in csv with column names as first row and save as dictionary: each column is a key, the values are a list for each 
    def csv_read_in(self, sep = ","):
        self.sep = sep
        self.data = []
        self.items = []

        with open(self.folder_path, 'r', newline="") as csvfile:
            reader = csv.reader(csvfile, delimiter = self.sep)
            for row in reader:
                self.data.append(row)

        count = 0
        for c in range(len(self.data[0])):
            for i in range(len(self.data)): 
                if i != 0 & i < len(self.data): #bounds 1 to second to last
                    self.items.append(self.data[i][c])
                    self.records[self.data[0][c]] = self.items
                    if len(self.items) < len(self.data)-1: #bounds length of list appended to key, minus row with column names
                        count +=1
                    elif len(self.items) == len(self.data)-1:
                        count = 0
                        self.items = []
        return self.records

    def csv_inspect(self):
        #print column count and names
        print(f"count: {len(self.records.keys())}, cols: {self.records.keys()}")

        #check length of each element by dictionary key
        for i in self.records.keys():
            print(f"col: {i}, len: {len(self.records[i])}")

    def column_type(self, dataframe, column, new_type):
        #types: int, float, string, list, dict
        self.data = dataframe
        self.column = str(column)
        self.type = str(new_type)

        if "int" in self.type:
            self.data[self.column] = [int(self.data[self.column][i]) for i in range(len(self.data[self.column]))]

        elif "float" in self.type:
            self.data[self.column] = [float(self.data[self.column][i]) for i in range(len(self.data[self.column]))]

        elif "string" in self.type:
            self.data[self.column] = [str(self.data[self.column][i]) for i in range(len(self.data[self.column]))]

        else:
            assert TypeError

        return self.data[self.column]
           
