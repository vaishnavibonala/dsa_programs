list =["a", "hi", "on", "bye", "bag", 
"pen","man", "book","girl"]
#empty list 
grouped_list = {}
#loop through the list
for l in list :
    #get the length of the list
    length =len(l)
    print(length)
    if length not in grouped_list:
        grouped_list[length] = []
        print(grouped_list)
    grouped_list[length].append(l)
print(grouped_list)