coordinates = (5,25)
print(coordinates)
x,y = coordinates
print(x,y)
print(coordinates[0])

set1 = {1,2,3,3,2}
print(set1)
list1=[1,2,2,3,3,4,4]
list_remove_dups=set(list1)
print(list_remove_dups)

list1 = []
for i in range(0,50):
    list1.append(i)
print(list1)

list2 = [i for i in range(0,50) if i > 40]
print(list2)

evens = [i for i in range(0,50) if i%2 == 0]
odds = [i for i in range(0,50) if i%2 == 0]

favorite_foods = {"Kathleen": "Pizza", "Steve":"burgers", "John":"chicken"}
favorite_foods["Michelle"] = "pasta"
favorite_foods["Patrick"] = "cookies"
print(favorite_foods)

for key,value in favorite_foods.items():
    print(key+"'s favorite food is "+value)

if "Mary" in favorite_foods:
    print("Mary in dictionary")
else:
    favorite_foods["Mary"] = "cake"

foods=["pizza","tikka masala","pizza","bagels","bagels","ice cream","pizza"]
food_counts = {}
for food in foods:
    if food in food_counts:
        food_counts[food] += 1
    else:
        food_counts[food] = 1

keys=["one", "two", "three"]
nums = {keys[i]: i+1 for i in range(len(keys))}
print(nums)
