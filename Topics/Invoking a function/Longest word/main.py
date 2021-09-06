word1 = input()
word2 = input()

word1_len = len(word1)
word2_len = len(word2)
print(word1_len if word1_len > word2_len else word2_len)
