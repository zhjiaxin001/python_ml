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

print("Fitting the classifier to the training set")
t0 = time()
param_grid = {'C': [1e3, 5e3, 1e4, 5e4, 1e5],
              'gamma': [0.0001, 0.0005, 0.001, 0.005, 0.01, 0.1]}# 尝试不同的值,，C:对于错误的部分进行惩罚,gamma:
clf = GridSearchCV(SVC(kernel='rbf'),param_grid)
clf = clf.fit(x_train_pca,y_train)
print("done in %0.3fs"%(time()-t0))
print("Best estimator found by grid search:")
print(clf.best_estimator_)

#
print("predicting peoples's banes ib tge test set")
t0 = time()
y_pred = clf.predict(x_test_pca)
print("done in %0.3fs"%(time()-t0))

print(classification_report(y_test, y_pred, target_names=target_names)) # 预估精确率分析
print(confusion_matrix(y_test, y_pred, labels=range(n_classes)))  # 对角线的值相对越大，越准确

def  plot_gallery(images, titles, h, w, n_row =3, n_col=4):
    plt.figure(figsize=(1.8*n_col, 2.4*n_row))
    plt.subplots_adjust(bottom=0, left=.01, right=.99, top=.99, hspace=.35)
    for i in range(n_row*n_col):
        plt.subplot(n_row, n_col, i+1)
        plt.imshow(images[i].reshape((h, w)),cmap=plt.cm.gray)
        plt.title(titles[i], size=12)
        plt.xticks(())
        plt.yticks(())

# plot the result of the prediction on a portion of the test set

def title(y_pred, y_test, target_names,i):
    pred_name = target_names[y_pred[i]].rsplit(' ',1 )[-1]
    true_name = target_names[y_test[i]].rsplit(' ',1 )[-1]
    return "predicted:%s\ntrue ;    %s"% (pred_name,true_name)
prediction_titles = [title(y_pred, y_test, target_names, i)
                     for i in range(y_pred.shape[0])]
plot_gallery(x_test, prediction_titles, h, w)

# plot the gallery of the most significative eigenfaces
eigenfaces_titles = ["eigenface %d"% i for i in range(eigenfaces.shape[0])]
plot_gallery(eigenfaces, eigenfaces_titles, h, w)
plt.show()


