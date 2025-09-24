# PyIL
Python Interlinearizer

PyIL adds spaces to create an aligned interlinear. 
Make sure to use a fixed width font.

Usage:
python pyil.py INPUT_FILE --max-length NUMBER --lines-per-block NUMBER TEXT_FILE

Example:
python pyil.py --max-length 50 --lines-per-block 2 Test.txt

Test.txt
He likes eating pizza.
他 喜欢 吃 比萨并。

Output:
He likes eating pizza.
他 喜欢   吃     比萨并。
