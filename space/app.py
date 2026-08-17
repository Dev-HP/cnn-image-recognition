#!/usr/bin/env python3
"""Interface Gradio para classificação de imagens com MobileNetV2."""

import os

import gradio as gr
import numpy as np
from PIL import Image
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import decode_predictions, preprocess_input


print("Carregando modelo MobileNetV2...")
model = MobileNetV2(weights="imagenet")
print("Modelo carregado.")


def predict_image(image):
    """Classifica uma imagem e retorna um resumo Markdown legível."""
    if image is None:
        return "Envie uma imagem para iniciar a classificação."

    if isinstance(image, Image.Image):
        pil_image = image.convert("RGB")
    else:
        pil_image = Image.fromarray(np.asarray(image).astype("uint8")).convert("RGB")

    image_array = np.asarray(pil_image.resize((224, 224)), dtype=np.float32)
    batch = preprocess_input(np.expand_dims(image_array, axis=0))
    predictions = model.predict(batch, verbose=0)

    results = decode_predictions(predictions, top=5)[0]
    lines = ["### Principais previsões", ""]
    for position, (_, name, confidence) in enumerate(results, start=1):
        label = name.replace("_", " ").title()
        lines.append(f"{position}. **{label}** — {confidence:.2%}")
    return "\n".join(lines)


demo = gr.Interface(
    fn=predict_image,
    inputs=gr.Image(type="numpy", label="Envie uma imagem"),
    outputs=gr.Markdown(label="Previsões"),
    title="CNN Image Recognition",
    description="Classificação educacional de imagens usando MobileNetV2 treinada no ImageNet.",
    examples=[],
    theme=gr.themes.Soft(),
    css="""
    .gradio-container {
        max-width: 960px !important;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }
    """,
)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", "7860"))
    demo.launch(
        server_name="0.0.0.0",
        server_port=port,
        show_error=True,
    )
