import os

file_path = r'd:\Projects\masterclass.org\index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Provide exact address link
content = content.replace(
    'href="https://go.2gis.com/j4q49"',
    'href="https://2gis.kg/bishkek/search/%D1%83%D0%BB.%20%D0%9C%D0%BE%D1%81%D0%BA%D0%BE%D0%B2%D1%81%D0%BA%D0%B0%D1%8F,%2054"'
)

# 2. Text align justify for reviews
content = content.replace(
    'style="color:var(--c-dark-text); font-size:14px; line-height:1.5;"',
    'style="color:var(--c-dark-text); font-size:14px; line-height:1.5; text-align:justify;"'
)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Update successful")
