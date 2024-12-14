#Task
#Write a program that accepts user input to create two sets of integers. Then, create a new set that contains only the elements that are common to both sets.

def get_integer_set(prompt):
    return set(map(int, input("Enter numbers you wish to include in the set separated with a space: ").split()))

#Get two sets of integers from the user
set1 = get_integer_set("Enter the 1st set of the numbers: ")
set2 = get_integer_set("Enter the 2nd set of the numbers: ")

#Finding the intersection of the 2 sets
common_integers= set1.intersection(set2)

#Displaying the common integers 
print("\nThe common integers in both sets are: ", common_integers)