import jieba

import jieba.analyse
import jieba.posseg

result = jieba.posseg.lcut('我是中国人，我爱我的祖国')
print(result)
result = jieba.lcut('我是中国人，我爱我的祖国')
print(result)
result = jieba.analyse.extract_tags('我是中国人，我爱我的祖国', topK=2)
print(result)
result = jieba.analyse.tfidf('我是中国人，我爱我的祖国', 2)
print(result)
result = jieba.lcut_for_search('我是中国人，我爱我的祖国')
print(result)
result = jieba.lcut('我是中国人，我爱我的祖国')
print(result)