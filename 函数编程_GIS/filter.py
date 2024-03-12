def judge(num):
    return num%2==0

numbers=[1,2,3,4,5]
even_numbers=filter(judge,numbers)
print(list(even_numbers))

words = ['apple', 'banana', 'cherry', 'date', 'elderberry']
long_words = filter(lambda word: len(word) > 5, words)
print(list(long_words))  # 输出：['banana', 'elderberry']