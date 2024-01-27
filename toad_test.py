from sklearn.datasets import load_breast_cancer
from bwfintech.feature import FeatureSelection
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import get_scorer, accuracy_score,f1_score, auc, roc_auc_score
from lightgbm.sklearn import LGBMClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, AdaBoostClassifier
from xgboost.sklearn import XGBClassifier
from toad.merge import merge, ChiMerge, DTMerge, KMeansMerge, QuantileMerge, StepMerge
from toad.selection import select, stepwise
from bwfintech.modeling import LogisticRegressionTrainer
from toad.metrics import KS, PSI, KS_bucket
from toad.transform import WOETransformer
import matplotlib.pyplot as plt
from toad.plot import bin_plot
from toad import ScoreCard
from toad.transform import Combiner
import pandas as pd
import pandas_profiling as pd_pro
import numpy as np
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression


data = load_breast_cancer()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.Series(data.target, name='target')
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=10)
print(X.columns)
# data_train = x_train.join(y_train)
# toad.detect(x_train)
# print(x_train.join(y_train))
# print(toad.quality(x_train, target=y_train, iv_only=False))
# print(data_train.columns)
# print(toad.IV(data_train['mean smoothness'], data_train['target'], return_sub=True))
# selected_data, dropped1 = toad.selection.select(x_train, target=y_train, empty=0.5, iv=0.2, corr=0.8,
#                                                 return_drop=True)
# # print(selected_data)
# # print(dropped1)
#
c = Combiner()
c.fit(x_train, y=y_train, method='chi', empty_separate=True, min_samples=0.05)
# print(c.export())
# print(len(c), c['mean smoothness'], 'mean smoothness' in c)
x_train_bins = c.transform(x_train, labels=False)
# print(xx)
# bin_plot(xx, x='mean radius', target='target')
# plt.show()
woe = WOETransformer()
woe.fit(x_train_bins, y_train)

x_train_woe = woe.transform(x_train_bins)
# print(woe.export())
x_test_bins = c.transform(x_test[x_train_woe.columns], labels=False)
x_test_woe = woe.transform(x_test_bins)
# psi, frame = PSI(x_train, x_test, combiner=c, return_frame=True)
# print('PSI: \n', psi)
# print('Frame: \n', frame)

final_data, dropped2 = stepwise(x_train_woe, target=y_train, estimator='ols', direction='backward',
                                               criterion='ks', return_drop=True)
# print(final_data)
# print(dropped2)

card = ScoreCard(pdo=60, rate=2, base_odds=35, base_score=750,
                      combiner=c, transer=woe, class_weight='balanced',
                      C=0.1)
card.fit(final_data, y_train)
y_pred = card.predict(x_train)
print(y_pred)
print(card.export())
print(card.predict(x_train))

# print(pd.concat([pd.Series(v, name=k).reset_index() for k, v in bb.items()]))
lr = LogisticRegression(max_iter=10000)
lr.fit(x_train, y_train)
y_pred = lr.predict(x_test)
y_proba = lr.predict_proba(x_test)
# print(y_pred.shape, y_test.shape)
# agg = toad.metrics.KS_bucket(y_proba[:,1], y_test, bucket=20)
# print(agg)
# print(agg.columns)
