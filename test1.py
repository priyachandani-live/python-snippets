"""
Given : Staircase detail

This is a staircase of size :

   #
  ##
 ###
####
Its base and height are both equal to n. It is drawn using # symbols and spaces. The last line is not preceded by any spaces.
     #
    ##
   ###
  ####
 #####
######
"""
n = 4
string = " "
for i in range(1, n+1):
    print(((n-i)*string) + "#"*i)