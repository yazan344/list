list = [54, 44, 27, 79, 91, 41]
results_list = [54, 44, 79, 27, 91, 41, 27]
element = list[2]
list.remove(element)
list.insert(4, element)
list.insert(len(list), element)

print(list)