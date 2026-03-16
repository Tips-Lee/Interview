# https://github.com/Tips-Lee/shap?tab=readme-ov-file

import matplotlib
import matplotlib.pyplot as plt
import xgboost
import shap
# train an XGBoost model
X, y = shap.datasets.california()
model = xgboost.XGBRegressor().fit(X, y)
# matplotlib.use("Agg")
# explain the model's predictions using SHAP
# (same syntax works for LightGBM, CatBoost, scikit-learn, transformers, Spark, etc.)
explainer = shap.Explainer(model)
shap_values = explainer(X)

# summarize the effects of all the features

# shap.plots.waterfall(shap_values[0])
# plt.savefig('shap_waterfall.png', dpi=300, bbox_inches='tight')
# print("Plot saved to shap_waterfall.png")

# shap.plots.beeswarm(shap_values)
# plt.savefig('shap_beeswarm.png', dpi=300, bbox_inches='tight')
# print("Plot saved to shap_beeswarm.png")

# shap.plots.scatter(shap_values[:, "Latitude"], color=shap_values)
# plt.savefig('shap_scatter.png', dpi=300, bbox_inches='tight')
# print("Plot saved to shapscatter.png")

# shap.plots.bar(shap_values)
# plt.savefig('shap_bar.png', dpi=300, bbox_inches='tight')
# print("Plot saved to shap_bar.png")


# Force plot generates interactive HTML visualization
force_plot = shap.plots.force(shap_values[:500], show=False)
# force_plot = shap.plots.force(shap_values[0])
shap.save_html('shap_force.html', force_plot)
print("Interactive force plot saved to shap_force.html")
