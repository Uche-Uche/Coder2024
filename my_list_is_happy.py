def my_List():
    #create an empty list called my_list
    my_list=[]
    #append elements to my_list
    elements=[10, 20, 30, 40]
    #loop through the each element and append to the list
    for each_number in elements:
        my_list.append(each_number)
    #insert the value 15 to the second position in the list
    my_list.insert(1, 15)
    #extend the list
    my_list.extend([50, 60, 70])
    #remove last element from the list
    my_list.pop()
    #sort the list in ascending order
    my_list.sort()
    #print the index of the value 30
    index=my_list.index(30)
    print(f"the index of 30 is {index}")
    print(f"my_list is= {my_list}")
my_List()
