with open('cities.txt','r') as file:
    texts = file.readlines()

cleaned_cities = [text.strip() for text in texts]
cleaned_cities.sort()

print(cleaned_cities)

with open('updated_cities','w') as f1:
    for city in cleaned_cities:
        f1.write(city+'\n')
