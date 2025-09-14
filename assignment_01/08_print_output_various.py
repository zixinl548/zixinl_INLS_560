# Demonstrating escapes, concatenation, and format

# Escape characters
print("Don't fear!")            
print('I\'m here!')             
print("He said, \"Hello!\"")    
print("Line1\nLine2")           
print("Column1\tColumn2")       
print("A backslash: \\")        

# Concatenation
greeting = "Hello, "
name = "Nancy"
print(greeting + name)          

# Number formatting
number = 1234.56789
print(format(number, "12,.3f"))  

# More Example
print("Nancy\'s hometown is \"Hangzhou\".\nIt\'s famous for West Lake.")
print("UNC" + " " + "Chapel Hill")  
print("Formatted GPA:", format(3.61, ".2f"))
