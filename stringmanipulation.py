
#STRING MANIPULATION
string="GIT HUB"
print(string)
#index srarts with Zer0
print(string[0:2])    #prints value from 0 to 1 0r n-1 values because zero is inclusive and 2 is exclusive 
print(string[:5])     #prints characters before five(index 0 to 4)
print(string[1:])     #prints all characters except first character 
print(string[-1])     #print characters from reverse index
print(string[-2:-1])  #print the inclusive index (which is -2) character
print(string[:-1])    #print except the last character
print(string[::-1])   #used to print the string in reverse

'''
GIT HUB
GI
GIT H
IT HUB
B
U
GIT HU
BUH TIG
'''
