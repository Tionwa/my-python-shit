import re

pattern = r'\d+\s*?[+\-\*\/]\s*?\d+'
equation = input()

if re.match(pattern, equation):
    print(equation)
else:
    print("not even an equation bluddy")