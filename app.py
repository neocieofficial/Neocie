import os
import gradio as gr
from rembg import remove

def remove_background(input_img):
    if input_img is None:
        return None
    return remove(input_img)

# एक साधारण इंटरफ़ेस जो कम मेमोरी में काम करेगा
demo = gr.Interface(
    fn=remove_background,
    inputs=gr.Image(type="pil", label="अपनी इमेज अपलोड करें"),
    outputs=gr.Image(type="pil", label="बिना बैकग्राउंड वाली इमेज"),
    title="AI Background Remover"
)

if __name__ == "__main__":
    # Koyeb के लिए पोर्ट सेटिंग्स
    port = int(os.environ.get("PORT", 8000))
    demo.launch(server_name="0.0.0.0", server_port=port)