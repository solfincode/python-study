scores = [35,62,75,100,45,10,83,98,64,23,23,4,46,70]

total=0
number_of_item=len(scores)

for score in scores:
    total+=score

avg = total / number_of_item

print("total grades is ", total)
print("average is ", avg)