color, vars, vowels, sentence = "\033[93m","\033[0m",['a','e','ı','i','o','ö','u','ü'], list(input("Enter the sentence : "))
a = 0
for i in vowels:
    a += sentence.count(i)
print(color + "Vowels in the sentence : ",str(a) + vars)
print(color + "Vowels : ",end="")
for i in vowels:
    if i in sentence:
        print(color + i,end=" " + vars)