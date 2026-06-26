# pattern printing 
# sum 1 square box 
def squarebox(k,m):
    i=0
    for i in range(k):
        for j in range (m):
            print("*", end=" ") 
        print()
print(squarebox(5,6))
#  print("*") means:
# print *
# move to next line
        
# print("*", end=" ")

# means:

# print *
# stay on same line
# add a space