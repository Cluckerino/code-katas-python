"""
Use regex to find if the given binary number is divisible by 5.
Yep, use REGEX.
https://www.codewars.com/kata/regular-expression-for-binary-numbers-divisible-by-5/python
The div by 5 regex can be represented by the following finite state machine:
http://aswitalski.github.io/img/FSM-binary-divisible-by-five.png
"""

# After reducing the graph, my unoptimized result:
# 0+1[{10+(0+11)(01*01)*01*00}*(0+11)(01*01)*1]

PATTERN = r'(0|1((10|(0|11)(01*01)*01*00)*(0|11)(01*01)*)1)+$'
