
#definition => myset={} 
myset={"apple","watermelon","peach"}

print(myset)   #unordered => printing this will have some elements in a
            # place other than the one it was defined


#unchangeble=> once created its items can't be changed but can be removed or new items added
# since it is also unindexed => we can not access items at specific positions

myset.add("I_was_added")
print(myset)

myset.remove("apple")
print(myset)

#it also does not allow duplicates
duplicateSet={"apple","apple","papaya"}
print(duplicateSet)  #will only print the duplicated element once

#it takes boolean, int and String data types only and like lists and tuples items can be of different data types

#sets have a constructor set() to create a set as follows

consSet=set(("mango","banana"))
print(consSet)

