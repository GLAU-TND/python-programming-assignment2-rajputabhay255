c = int(input('Enter the no : '))
n = bin(c) #converts input into binary
n = n[2:] #remove first 2 character of output binary (0b.... as return of binary)
b = n.split('0')
# splits all substrings of consecutives 1's
# seperated by 0's .... output be like [1,1111,11,1]
a = max(map(len,b))
# len fun on each substrings of consecutive 1's
# max() returns max. element from list
print('Max no of 1's is : ',a)
 #finaloutput       
