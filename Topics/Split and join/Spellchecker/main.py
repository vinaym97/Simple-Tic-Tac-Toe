"""Write a spellchecker that tells you which words in the sentence are spelled incorrectly. Use the dictionary in the code below.

The input format: A sentence. All words are in the lowercase.

The output format: All incorrectly spelled words in the order of their appearance in the sentence. If all words are spelled correctly, print OK.

Sample Input: srutinize is to examene closely and minutely

Sample Output:
srutinize
examene

Sample Input: all correct

Sample Output: OK"""


dictionary = ['all', 'an', 'and', 'as', 'closely', 'correct', 'equivocal',
              'examine', 'indication', 'is', 'means', 'minutely', 'or', 'scrutinize',
              'sign', 'the', 'to', 'uncertain']
sentence = input().split()
wrong_word = []
for i in sentence:
    if i not in dictionary:
        wrong_word.append(i)
if len(wrong_word) == 0:
    print("OK")
else:
    for word in wrong_word:
        print(word)