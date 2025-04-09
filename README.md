# DocumentParser
This repo contains the files for the DocumentParser package. Use it to read in a text file, process to split document into sentences, remove whitespaces, and lower-case all words.  The output  are cleaned, indexed sentences in json format"

## Local import
1. Download the files, taking care to maintain the folder structure that's in place
2. Using the terminal open your working environment with the command: source bin/activate
3. Move into the package folder with command: cd /YourFilepath/DocumentParser/src/document_parser
4. Startup and run python3 

## Usage
from document_parser import Parser

folder = "/filepath/filename.txt"  
parser = Parser(folder)  
data = parser.parse_txt()  
data_dict = parser.convert_to_json()  

## Troubleshooting
To view the intermediary state of the data
parser.clean_lines
parser.sentence_holder_clean
