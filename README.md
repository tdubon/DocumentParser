# DocumentParser
This repo contains the files for a text document parser. Use it to prepare your text files for machine learning. It will read in lines and split these into cleaned sentences by ending punctuation or words. The outputs include sentences, words, vocabulary, encoded vectors and decoded matches.

## Local import
1. Download the files, taking care to maintain the folder structure that's in place
2. Using the terminal open your working environment with the command: source bin/activate
3. Move into the package folder with command: cd /YourFilepath/DocumentParser/src/document_parser
4. Startup and run python3 

## Usage
from document_parser import Parser

folder_path = "/filepath/filename.txt"  
par = Parser(folder_path)
lines = par.read_in_lines()
sentences = par.sentence_parse()
words = par.word_parse()
vocab = par.vocab()
encoded_vector = par.encode()
decode = par.decode()  

## Example Output at the Sentence Level
par = Parser(folder_path)
lines = par.read_in_lines()
sentences = par.sentence_parse()
dictionary = par.sentence_dict()    

{0: 'before we start fitting regression models we begin the model building process by performing an exploratory data analysis eda',    
 1: 'given that we have a response variable y and four predictor variables x1 x2 x3 and x4 how do we perform an eda for a simple linear regression model',  
 2: 'suppose that x1 and x2 are continuous and that x3 and x4 are categorical'}  

## Example Output at the Word Level
lines = par.read_in_lines()
sentences = par.sentence_parse()
words = par.word_parse()

['I', 'was', 'taught', 'it', 'in', 'childhood', 'and', 'throughout', 'my', 'boyhood', 'and', 'youth', '.', 'But', 'when', 'I', 'abandoned', 'the', 'second', 'course', 'of', 'the', 'university', 'at', 'the', 'age', 'of', 'eighteen', 'I', 'no']

## Troubleshooting
To view the intermediary state of the data
par.lines
par.sentence_list
par.text

