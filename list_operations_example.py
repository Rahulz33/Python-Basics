a=[10,20,30,40,50,60,70,80,90,100]
a.append(110) #adds 110 at the end of the list
a.insert(2, 25)  #adds 25 at index 2 and shifts the rest of the elements to the right
a.pop() #removes the last element of the list and returns it
a.pop(3) #removes the element at index 3 and returns it
a.clear() #removes all the elements from the list, leaving it empty
print(a)