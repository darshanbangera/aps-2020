import functools 
import operator 

lis = [1,4,62,6,16,4,6,7] 

# Sum
print (functools.reduce(operator.add,lis)) 

# Product
print (functools.reduce(operator.mul,lis)) 

# String Concat
print (functools.reduce(operator.add,["hello","world"])) 
