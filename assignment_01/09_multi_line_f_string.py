# Example of a multi-line f-string with math and variables

name = "Nancy"
age = 18
age_in_5_years = age + 5
test_score1 = 92
test_score2 = 88
average_score = (test_score1 + test_score2) / 2

fstring = f'''
Hello! My name is {name}.
I am currently {age} years old,
and in five years I will be {age_in_5_years}.

Here are my test scores: {test_score1} and {test_score2}.
My average score is {average_score}.
'''

print(fstring)

