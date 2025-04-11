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

## Example Output
>>> data_dict  
{0: 'before we start fitting regression models we begin the model building process by performing an exploratory data analysis eda',
 1: 'given that we have a response variable y and four predictor variables x1 x2 x3 and x4 how do we perform an eda for a simple linear regression model',
 2: 'suppose that x1 and x2 are continuous and that x3 and x4 are categorical',
 3: 'does your approach to eda for x1 and x2 differ from x3 and x4',
 4: 'if we want to fit a multiple regression model does our eda change',
 5: 'when we validate a statistical model should we only consider the traditional goodness-of-fit measures',
 6: 'are there other ways in which the model should be validated'}

## Troubleshooting
To view the intermediary state of the data
parser.clean_lines
parser.sentence_holder_clean
