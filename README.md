<h1> DocumentParser </h1>
This repo contains the files for a text document parser. Use it to prepare your text files for machine learning. It will read in lines and split these into cleaned sentences by ending punctuation or words. The outputs include sentences, words, vocabulary, encoded vectors and decoded matches.
<br>
<h2> Local import </h2>
<br>
1. Download the files, taking care to maintain the folder structure that's in place<br>
2. Using the terminal open your working environment with the command: source bin/activate<br>
3. Move into the package folder with command: cd /YourFilepath/DocumentParser/src/document_parser<br>
4. Startup and run python3<br>
<br>

<h2> Usage </h2>
<br>
`from document_parser import Parser`<br>
<br>
`folder_path = "/filepath/filename.txt"<br>  
par = Parser(folder_path)<br>
lines = par.read_in_lines()<br>
sentences = par.sentence_parse()<br>
words = par.word_parse()<br>
vocab = par.vocab()<br>
encoded_vector = par.encode()<br>
decode = par.decode()`<br>  
<br>
 
<h2> Example Output at the Sentence Level </h2>
<br>
`par = Parser(folder_path)<br>
lines = par.read_in_lines()<br>
sentences = par.sentence_parse()<br>
dictionary = par.sentence_dict()`<br>    
<br>
{0: 'before we start fitting regression models we begin the model building process by performing an exploratory data analysis eda',<br>    
 1: 'given that we have a response variable y and four predictor variables x1 x2 x3 and x4 how do we perform an eda for a simple linear regression model',<br>  
 2: 'suppose that x1 and x2 are continuous and that x3 and x4 are categorical'}<br>  
<br>

<h2> Example Output at the Word Level </h2>
<br>
`lines = par.read_in_lines()<br>
sentences = par.sentence_parse()<br>
words = par.word_parse()`<br>
<br>
['I', 'was', 'taught', 'it', 'in', 'childhood', 'and', 'throughout', 'my', 'boyhood', 'and', 'youth', '.', 'But', 'when', 'I', 'abandoned', 'the', 'second', 'course', 'of', 'the', 'university', 'at', 'the', 'age', 'of', 'eighteen', 'I', 'no']<br>
<br>

<h2> Troubleshooting </h2>
<br>
To view the intermediary state of the data<br>
par.lines<br>
par.sentence_list<br>
par.text<br>

