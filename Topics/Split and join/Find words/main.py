""" Find all words that end in "s" and print them together separated by an underscore.

After such words there will be no punctuation marks, you do not need to worry about that.


Sample Input:
First ladies rule the State and state the rule: ladies first

Sample Output:
ladies_ladies"""
sentence = input().split()
ending_with_s = [words for words in sentence if words.endswith("s")]
print("_".join(ending_with_s))