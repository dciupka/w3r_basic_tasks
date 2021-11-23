""" Write a Python program to print the following string in a specific format (see the output). Go to the editor
Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high,
Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are" Output :

Twinkle, twinkle, little star,
	    How I wonder what you are!
		        Up above the world so high,
		        Like a diamond in the sky.
Twinkle, twinkle, little star,
	    How I wonder what you are
"""
# first solution
print("Twinkle, twinkle, little star,")
print("     How I wonder what you are!")
print("		        Up above the world so high,")
print("		        Like a diamond in the sky.")
print("Twinkle, twinkle, little star,")
print("		How I wonder what you are!")

print(10*'-',"SECOND SOLUTION",10*'-')

# second solution
print("Twinkle, twinkle, little star,\n\t\tHow I wonder what you are!\n\t\t\t\tUp above the world so high,\n\t\t\t\tLike a diamond in the sky.\nTwinkle, twinkle, little star,\n\t\tHow I wonder what you are!")