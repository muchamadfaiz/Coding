letters = ["a", "b", "c"]

# Add
letters.append("d") #Adding after last item
print(letters)
letters.insert(0,"-") #Adding on specific 
print(letters)

# Remove
letters.pop(0) # we know the index, only delete 1 item
print(letters)

letters.remove("a")  # we dont know the index, only delete 1 item
print(letters)

del letters[0:2] #using delete statement, can remove a range of items
print(letters)

letters.clear()
print(letters)



