list1 = "абввиыг9ва9абв  абвгш  фбюывщл  щиашщ  яфчсцк ф ффысцйца фысч абв фывячсммабв фывщцаб фывщвбюваю фщбывбщц"

list2 = list1.split(" ")

word = "абв"

for item in list2 :
    if item.find(word) >=0:
        list2.remove(item)

b = " ".join(list2)

print(b) 