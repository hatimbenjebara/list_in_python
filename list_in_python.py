#list 
list = [] #empty list
list = [1,2,3,4]
print("this is the first value in list :".capitalize(), list[0]) #print first value in list
list = ["a", "b", "c", "e"]
list.insert(3,"d") # add value in position 3 
print(list)
list.append("f") # add at the end of list
print(list)
list_2= ["g", "h"]
list.extend(list_2) # add another list to the end of first list
print(list)
list.remove("h") # remove value from a list
print(list)
list.pop(-1) # remove value from list using index item
print(list)
del list[-1] # remove value from list using index item
print(list)
del list # remove all list
print(list)
list = ["a", "b", "c", "e"]
#loop for in list, print all element of list
for i in list: 
    print(i)
#using for in list to print all element of list, here using range and length of list to print iterm
for i in range(len(list)): #use range() and len() to create suitable iterable
    print(list[i])
#using while loop to print all element of list
i = 0
while i< len(list):
    print(list[i]) 
    i+=1
#based on a list of countries, we want to create a new list, containing only
#the countries with the letter a in the name 
#first method: without list of comprehension
countries = ["algerie".capitalize(), "Begique", "egypt", "France", "morocco".capitalize()]
new_list = []
for i in countries: 
    if "a" in i or "A" in i:
        new_list.append(i)
print(new_list)
new_list = [x for x in range(10)]
print(new_list)
#seconde method : using list of comprehension 
new_list = []
new_list = [x for x in countries if "a" in x or "A" in x]
print(new_list)
#list of comprehension is facilite code
new_list= [ x.capitalize() for x in countries]
print(new_list)
#print a list of countries without others
new_list = [x for x in countries if x not in ["Algerie", "Morocco"]]
print(new_list)
#sort list 
new_list.sort(reverse = True) # descanding 
print(new_list)
countries.sort()# sort ascanding 
print(countries)
#create own function for sorting 
def sort_distance(n):
    return abs(n-50)
list= [100, 50, 56, 65, 82, 23]
list.sort(key=sort_distance)
print(list)
list.sort(key=sort_distance, reverse=True)
print(list)
#by defaut sort() is vase sentitive, which means that uppercase letters are sorted
#before lowercase letters
countries = ["algerie", "Begique", "egypt", "France", "morocco"]
countries.sort()
print(countries) # unexpected result
countries.sort(key = str.lower)
print(countries) # the right result 
#to reverse the order, use the reverse()
countries.reverse()
print(countries)
#copy a list and keep it save from any changes 
countries_copy = countries.copy()
countries_copy.append("spain")
countries_copy.sort(key=str.lower)
print(countries)
print(countries_copy)
#join two list can do by several ways 
#first methode : using + operator 
countries_2 = ["Bresil", "Argentina", "United states of america"]
countries_all = countries + countries_2
countries_all.sort(key = str.lower)
print("Join two list using the + operator then sort it: \n ",countries_all)
#seconde methode : using the loop for 
for x in countries_2:
    countries.append(x)
countries.sort(key= str.lower)
print("Join two list using the loop for then sort it: \n",countries)\
# thirth method : use extend() method 
countries.extend(countries_2)
countries.sort(key = str.lower)
print("Join two list using the extend() method then sort it :\n", countries)
