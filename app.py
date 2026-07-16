import gradio as gr
from rembg import remove
from PIL import Image

def remove_background(input_img):
    if input_img is None:
        return None
    # यह सिर्फ एक लाइन में बैकग्राउंड साफ़ कर देगा
    return remove(input_img)

# एक सुंदर और आसान इंटरफ़ेस बनाना
demo = gr.Interface(
    fn=remove_background,
    inputs=gr.Image(type="pil", label="अपनी इमेज अपलोड करें"),
    outputs=gr.Image(type="pil", label="बिना बैकग्राउंड वाली इमेज"),
    title="AI Background Remover",
    description="अपनी इमेज अपलोड करें और तुरंत बैकग्राउंड हटाएं। (Powered by Hugging Face)"
)

if __name__ == "__main__":
    demo.launch()