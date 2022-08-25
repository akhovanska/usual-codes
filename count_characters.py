# count characters occurrences using Python
def count_characters(a):
    count = {}
    for i in a:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    print(count)
word=input("Enter your string:")
count_characters(word)