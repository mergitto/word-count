##########################################################
#
# 分かち書きされたテキストの語彙数や単語数をカウントする
#
##########################################################

import pandas as pd
import sys

FILENAME = sys.argv[1]

df = pd.read_csv(FILENAME, header=None)

documents = list(df[0])
documents = [text.split(' ') for text in documents]
words = []

for text in documents:
    for word in text:
        words.append(word)

print(FILENAME + "のテキスト情報を解析します")
print("単語数:" + str(len(words)))
print("語彙数:" + str(len(set(words))))



