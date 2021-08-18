# Exercise 1: Reverse the list below in-place using an in-place algorithm.

words = ['this' , 'is', 'a', 'sentence', '.']

words = words[::-1]

print(words)

words1 = []

# Extra credit: reverse the strings
def revstring(alist1):
    alist = []
    for item in alist1:
        meti = item[::-1]
        alist.append(meti)
    return alist
    

print(revstring(words))



# Exercise 2: Create a function that counts how many distinct words are in the string below, 
# then outputs a dictionary with the words as the key and the value as the amount of times 
# that word appears in the string.


a_text = 'In computing, a hash table hash map is a data structure which implements an associative array abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index into an array of buckets or slots from which the desired value can be found'

def distinct_word_count(string):
    alist = list(string.lower().split())
    a_dict = {}

    for word in alist:
        if word not in a_dict:
            a_dict[word] = 1
        else:
            a_dict[word] += 1
        
    return dict(sorted(a_dict.items()))

distinct_word_count(a_text)


# Exercise 3: Write a program to implement a Linear Search Algorithm. Also in a comment, 
# write the Time Complexity of the following algorithm.
# Hint: Linear Searching will require searching a list for a given number.

def searchlist(alist, x):
    return True if x in alist else False

list1 = [1,2,3,4,5,6,7]
print(searchlist(list1, 5))

print(searchlist(list1, 8))

print(f"The Time Complexity of this algoritem is, worst case, O(n).")