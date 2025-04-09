import os
import json
import pandas as pd
import re

# for documents in .docx or .doc: create a command to open file and save as copy in plain text
"""Parser currently setup to be used with .txt files only"""
class Parser:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.sentence_holder = []
        self.sentence_holder_clean = []
    
    def parse_txt(self):
        self.clean_lines = []
        self.long_string = ""
        
        with open(self.folder_path, "r", newline="") as f:
            lines = f.readlines()
        
        for line in lines:
            self.clean_lines.append(line.strip())
        
        # attach each line and save as a long string
        for i in range(len(self.clean_lines)):
            self.long_string = self.long_string + " " + self.clean_lines[i]
        
        #split string by punctuation
        pattern = r'[.!?]\s+'  #match by punctuation 
        pattern2 = r'[A-Za-zd]+.\s' #match alphabets and digits
        self.sentence_holder = re.split(pattern, self.long_string) 
        
        # remove white spaces, meta characters, puctuation and lowercase
        pattern = r'[^\w]+[\s]|(\\t)|[()?!.,:;]' #\w match word characters, \s match whitespace characters, meta characters
        for i in self.sentence_holder:
            self.sentence_holder_clean.append(re.sub(pattern, "", i).lower())
    
    def convert_to_json(self):
        self.data_dict = {}
        for idx, value in enumerate(self.sentence_holder_clean):
            self.data_dict[idx] = value.strip()
            if self.data_dict[idx] == "":
                del(self.data_dict[idx])
        return self.data_dict
           
