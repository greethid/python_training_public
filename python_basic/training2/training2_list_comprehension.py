fruits = ['cherry', 'apple', 'melon', 'grape', 'pomelo', 'strawberry']
countries = ['vietnam', 'poland', 'sweden', 'india', 'canada', 'finland', 'denmark']

result = [country for country in countries for fruit in fruits if country[0] == fruit[0]]
print(result)          
