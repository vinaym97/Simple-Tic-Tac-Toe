"""Create a list of words from the text below that are shorter than or equal to the input value. Print the new list.

"""


text = [["Glitch", "is", "a", "minor", "problem", "that", "causes", "a", "temporary", "setback"],
        ["Ephemeral", "lasts", "one", "day", "only"],
        ["Accolade", "is", "an", "expression", "of", "praise"]]
n = int(input())
new_list = [word for words in text for word in words if len(word) <= n]
print(new_list)