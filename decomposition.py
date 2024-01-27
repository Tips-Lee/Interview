from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.decomposition import TruncatedSVD, NMF, LatentDirichletAllocation, PCA
from sklearn.decomposition import nmf
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from scipy import sparse
import numpy as np
from sklearn.model_selection import GridSearchCV

corpus = [
    'This is the first document.',
    'This document is the second document.',
    'And this is the third one.',
    'Is this the first document?']
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(corpus)
print(vectorizer.get_feature_names())
# print(X.shape)
# print(vectorizer.vocabulary_)
# print(vectorizer.norm)
# print(vectorizer)
# print(X.todense())
X = X.toarray()
print(X)

countvectorizer = CountVectorizer()
C_ = countvectorizer.fit_transform(corpus)
print(C_.toarray())

GridSearchCV(estimator=estimator, param_grid={}, scoring='f1')
exit()

decompose = TruncatedSVD(n_components=2)
feature = decompose.fit_transform(X)
print(feature)
print('++'*30)

decompose = NMF(n_components=2)
feature = decompose.fit_transform(X)
print(feature)
print('++'*30)

decompose = LatentDirichletAllocation(n_components=2)
feature = decompose.fit_transform(X)
print(feature)
print('++'*30)

decompose = PCA(n_components=2)
feature = decompose.fit_transform(X)
print(feature)
print('++'*30)

decompose = LinearDiscriminantAnalysis()
feature = decompose.fit_transform(X, [0, 1, 1, 0])
print(feature)
print('++'*30)
# data = np.array([1, 2, 3, 4, 5, 6])
# row = np.array([0, 0, 1, 2, 2, 2])
# col = np.array([0, 2, 2, 0, 1, 2])
# csr_ = sparse.csr_matrix((data, (row, col)), shape=(3, 3))
# print(csr_.toarray())
# print(csr_.todense())
# print(csr_)

# data = np.array([1, 2, 3, 4, 5, 6])
# indptr = np.array([0, 2, 3, 6])
# indices = np.array([0, 2, 2, 0, 1, 2])
# csr_ = sparse.csr_matrix((data, indices, indptr), shape=(3, 3))
# print(csr_.toarray())
# print(csr_.todense())
# print(csr_)

# docs = [["hello", "world", "hello"], ["goodbye", "cruel", "world"]]
# indptr = [0]
# indices = []
# data = []
# vocabulary = {}
# for d in docs:
#     for term in d:
#         index = vocabulary.setdefault(term, len(vocabulary))
#         indices.append(index)
#         data.append(1)
#     indptr.append(len(indices))
# csr_ = sparse.csr_matrix((data, indices, indptr), dtype=int)
# print(csr_.shape)
# print(csr_.todense())
# print(csr_)
from sklearn.svm import SVC, OneClassSVM, SVR, NuSVR, NuSVC, LinearSVR, LinearSVC