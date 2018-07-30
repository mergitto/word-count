##########################################################
#
# 分かち書きされたテキストの語彙数や単語数をカウントする
#
##########################################################

import pandas as pd
import sys
from collections import Counter

FILENAME = sys.argv[1]

df = pd.read_csv(FILENAME, header=None)

documents = list(df[0])
documents = [text.strip().split(' ') for text in documents]

words = []
words = [word for text in documents for word in text if word != ""]

print(FILENAME + "のテキスト情報を解析します")
print("単語数:" + str(len(words)))
print("語彙数:" + str(len(set(words))))

counter_words = Counter(words)
print(counter_words.most_common(10))



