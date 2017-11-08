f = open('crime_rates.csv','r')
data = f.read()
#print(data)
rows = data.split('\n')
#print(rows)
final_list = []

for i in rows:
    split_list = i.split(',')
    final_list.append(split_list)
    
# print(final_list)
# print (len(rows))
# print (len(final_list))

five_elements = final_list[0:5]
#print (five_elements)

cities = []
crime_rates = []

for i in five_elements:
    cities.append(i[0])
    crime_rates.append(i[1])


print (cities)
print (crime_rates)