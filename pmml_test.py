import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from xgboost import XGBClassifier
from sklearn.linear_model import LogisticRegression
from sklearn2pmml import PMMLPipeline, sklearn2pmml
from sklearn2pmml import make_pmml_pipeline
from sklearn2pmml.preprocessing import xgboost

from pypmml import Model
from nyoka import xgboost_to_pmml
from sklearn_pandas import DataFrameMapper
import os
from sklearn.datasets import load_iris, load_boston,load_breast_cancer

data = load_breast_cancer(return_X_y=False)
X, y = pd.DataFrame(data.data, columns=data.feature_names), pd.Series(data.target, name='has_cancer')

"""
pipeline = PMMLPipeline([("tips_classifier", LogisticRegression(max_iter=1000, multi_class='ovr'))])
pipeline.fit(X, y)
print(pipeline.predict(X))
sklearn2pmml(pipeline, "demo.pmml", with_repr=True)

pipeline1 = Model.load("demo.pmml")
print(np.asarray(pipeline1.predict(X)).argmax(axis=1))
"""

lr = LogisticRegression(max_iter=10000, multi_class='ovr')
lr.fit(X, y)
print(lr.predict(X))

# pipeline2 = PMMLPipeline([("tips_classifier", lr)])
pipeline2 = make_pmml_pipeline(lr, active_fields=X.columns, target_fields=['has_cancer'])
# pipeline2 = make_pmml_pipeline(lr, active_fields=data.feature_names)
print(pipeline2.predict(X.values))
sklearn2pmml(pipeline2, "demo.pmml", with_repr=True, debug=True)

pipeline3 = Model.load("demo.pmml")
print(pipeline3.predict(X.values))
print(np.asarray(pipeline3.predict(X.values)).argmax(axis=1))


'''
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn2pmml import sklearn2pmml, PMMLPipeline
import pandas as pd
from xgboost import XGBClassifier

seed = 123

iris = datasets.load_iris()
target = 'Species'
features = iris.feature_names
iris_df = pd.DataFrame(iris.data, columns=features)
iris_df[target] = iris.target

X, y = iris_df[features], iris_df[target]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=seed)

pipeline = PMMLPipeline([
    ('xgb', XGBClassifier(n_estimators=5, seed=seed))
])

pipeline.fit(X_train, y_train)
y_pred = pipeline.predict(X_test)
print(y_pred)
# y_pred_proba = pipeline.predict_proba(X_test)

from nyoka import xgboost_to_pmml

# xgboost_to_pmml(pipeline, features, target, "xgb-iris.pmml")
sklearn2pmml(pipeline, "demo.pmml", with_repr=True, debug=False)


from pypmml import Model

model = Model.load("demo.pmml")
print(model.predict(X_test))
'''
