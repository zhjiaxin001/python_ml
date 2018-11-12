# coding=utf-8
from __future__ import print_function

from time import time
import logging
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.datasets import fetch_lfw_people
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.decomposition import PCA
from sklearn.svm import SVC


print(__doc__)

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')
lfw_people = fetch_lfw_people(min_faces_per_person=70, resize=0.4)

n_samples, h, w = lfw_people.images.shape

X = lfw_people.data
n_features = X.shape[1]

y = lfw_people.target  # 返回不同的人
target_names = lfw_people.target_names  # 返回不同的人名
n_classes = target_names.shape[0]  # 多少行就有多少人
print("Total datasets size：")
print("n_samples:%d"% n_samples)
print("n_features:%d" % n_features)
print("n_classes：%d"% n_classes)

# Split into a training set and a test set using a stratified k fold
# split into a training and test set
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

n_components = 150
print("Extracting the top %d eigenfaces from %d faces"
      %(n_components, x_train.shape[0]))
t0 = time()
pca = PCA(n_components=n_components, whiten=True).fit(x_train)  # PCA 特征模型
print("dibe ub %0.3fs"%(time()-t0))
eigenfaces = pca.components_.reshape((n_components, h, w))

print("Projectiong the input data on the eigenfaces orthonormal basis")
t0 = time()
x_train_pca = pca.transform(x_train)
x_test_pca = pca.transform(x_test)
print("done in %0.3fs"%(time()-t0))