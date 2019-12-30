# string method
#1.split
sentence = "This is beautiful iphone ever we made"
#split with every white space from string
split_sentence = sentence.split()
# split 3 element from string
split_sentense_two=sentence.split(" ",2)

print("splited :",split_sentence)
print("splited with 3 element:",split_sentense_two)

#2.join sentence
joined=" ".join(split_sentence)
print("this is joined : ", joined)