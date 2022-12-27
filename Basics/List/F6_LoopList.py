# it will loop thorugh the list elements
thislist = ["Python","Javascript","Java","C","C++","Php"]
for i in thislist:
    print(i, end=" ")
# result will be  Python Javascript Java C C++ Php

# It is shortest syntax for looping list using Comprehension
[print(x) for x in thislist]
# result will be 
# Javascript
# Java
# C
# C++
# Php
