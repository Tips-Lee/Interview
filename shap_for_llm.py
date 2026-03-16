import transformers
import shap
import matplotlib
import matplotlib.pyplot as plt

# load a transformers pipeline model
model = transformers.pipeline('sentiment-analysis', return_all_scores=True)

# explain the model on multiple sample inputs
explainer = shap.Explainer(model)
texts = [
    "What a great movie! ...if you have no taste.",
    "This film is absolutely fantastic and amazing!",
    "Terrible movie, waste of time.",
    "Not bad, but could be better."
]
shap_values = explainer(texts)

# 1. Text plot - visualize the first prediction's explanation for the POSITIVE output class
print("Generating text plot...")
text_plot_html = shap.plots.text(shap_values[0, :, "POSITIVE"], display=False)
with open('shap_text_plot.html', 'w', encoding='utf-8') as f:
    f.write(text_plot_html)
print("Text plot saved to shap_text_plot.html")

# # 2. Waterfall plot - shows how each word contributes to the prediction
# print("Generating waterfall plot...")
# shap.plots.waterfall(shap_values[0, :, "POSITIVE"])
# plt.savefig('shap_text_waterfall.png', dpi=300, bbox_inches='tight')
# print("Waterfall plot saved to shap_text_waterfall.png")
# plt.close()
#
# # 3. Bar plot - shows average feature importance across all samples
# print("Generating bar plot...")
# shap.plots.bar(shap_values[:, :, "POSITIVE"])
# plt.savefig('shap_text_bar.png', dpi=300, bbox_inches='tight')
# print("Bar plot saved to shap_text_bar.png")
# plt.close()
#
# # 4. Beeswarm plot - shows feature importance across multiple predictions
# print("Generating beeswarm plot...")
# shap.plots.beeswarm(shap_values[:, :, "POSITIVE"])
# plt.savefig('shap_text_beeswarm.png', dpi=300, bbox_inches='tight')
# print("Beeswarm plot saved to shap_text_beeswarm.png")
# plt.close()

# 5. Force plot - interactive HTML visualization
# print("Generating force plot...")
# force_plot = shap.plots.force(shap_values[0, :, "POSITIVE"], show=False)
# shap.save_html('shap_text_force.html', force_plot)
# print("Interactive force plot saved to shap_text_force.html")

# # 6. Heatmap - visualize multiple predictions at once
# print("Generating heatmap...")
# shap.plots.heatmap(shap_values[:, :, "POSITIVE"])
# plt.savefig('shap_text_heatmap.png', dpi=300, bbox_inches='tight')
# print("Heatmap saved to shap_text_heatmap.png")
# plt.close()

print("\nAll visualizations completed!")
