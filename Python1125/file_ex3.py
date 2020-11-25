cities = [{"index": 1, "name": "Tokyo", "population": 927},
          {"index": 2, "name": "London", "population":  898},
          {"index": 3, "name": "New York", "population": 834}]


file = "cities.csv"

f = open(file, "w")
for city in cities:
   f.write(str(city["index"]) + "," + city["name"]  + "," + str(city["population"]) + "\n")

f.close()