import math
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer, TfidfTransformer


def tf_idf(docs):
    vocab = set()
    for doc in docs:
        vocab.update(doc)
    vocab = sorted(vocab)

    idf_result = []
    for doc in docs:
        tf_ = tf(doc, vocab)
        idf_ = idf(docs, vocab)
        tf_idf_ = [tf_[word] * (math.log(idf_[word])) for word in vocab]
        idf_result.append(tf_idf_)
    return idf_result, vocab


def tf(doc, vocab):
    d = {k: 0 for k in vocab}
    for word in doc:
        if word in d:
            d[word] += 1
        # else:
        #     d[word] = 1
    return d


def idf(docs, vocab):
    d = {word: 0 for word in vocab}
    n = len(docs)
    for i in range(n):
        for word in vocab:
            if word in docs[i]:
                d[word] += 1
    d = {word: (n+1)/(d[word]+1) for word in d}
    # d = {word: (n)/(d[word]) for word in d}
    return d


if __name__ == '__main__':
    # docs = [['this', 'is', 'a', 'dog'], ['that', 'is', 'a', 'cat']]
    docs = [['this', 'is', 'dog'], ['that', 'is', 'cat']]
    tfidf, vocab = tf_idf(docs)
    print(tfidf)
    print(vocab)
    docs = ['this is a dog', 'that is a cat']
    # docs = [['this', 'is', 'a', 'dog'], ['that', 'is', 'a', 'cat']]

    vectorizer = TfidfVectorizer()
    print(vectorizer.fit_transform(docs).toarray())
    print(vectorizer.idf_)
    print(vectorizer.get_feature_names())

    cntvec = CountVectorizer()
    bow = cntvec.fit_transform(docs).toarray()
    print(cntvec.get_feature_names())


    trans = TfidfTransformer()
    print(trans.fit_transform(bow).toarray())










