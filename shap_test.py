import tensorflow as tf
import matplotlib
import matplotlib.pyplot as plt
import shap
import numpy as np
matplotlib.use("Agg")

model = tf.keras.models.load_model(model_path)
e = shap.DeepExplainer(model, background)

# e = shap.DeepExplainer((model.layers[0].input, model.layers[-1].output), background)
shap_values = e.shap_values(x_test[1:5])

# plot the feature attributions
shap.image_plot(shap_values, -x_test[1:5])
plt.savefig('shap_image_plot.png', dpi=300, bbox_inches='tight')
print("Plot saved to shap_image_plot.png")
