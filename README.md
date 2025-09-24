# PyIL
Python Interlinearizer   
   
PyIL adds spaces to create an aligned interlinear.    
Make sure to use a fixed width font.  
   
Usage:   
python pyil.py INPUT_FILE --max-length NUMBER --lines-per-block NUMBER TEXT_FILE   
   
Example:
python pyil.py --max-length 50 --lines-per-block 2 My_interlin.txt   
   
The text file should have matching lines with equal number of words/spaces. You can have 2 or 3 or more lines per block, but each block needs to be separated by a blank line.   
   
Example file, My_interlin.txt   
He likes eating pizza.   
他 喜欢 吃 比萨并。   

He eats pizza every day.   
他 吃 比萨并 每 天。   

