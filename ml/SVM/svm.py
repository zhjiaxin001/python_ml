# coding=utf-8
from sklearn import svm

X = [[2, 0], [1, 1], [2, 3]] # 特征向量值
y = [0, 0, 1] # 特征向量值对应标记的三个点的分类
clf = svm.SVC(kernel='linear')
clf.fit(X, y)
print clf
print clf.support_vectors_
print clf.support_
print clf.n_support_