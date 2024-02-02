words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]
from collections import Counter
a = Counter(words)
# 出现频率最高的3个单词
top_three = a.most_common(3)
print(top_three)


a.update(words)
b=Counter(words)
print(a-b)
print(a+b)
a.clear()

