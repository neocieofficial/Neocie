import os
# सर्वर की RAM (Memory) को क्रैश होने से बचाने के लिए सेटिंग्स
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["NUMEXPR_MAX_THREADS"] = "1"

from flask import Flask, request, send_file
from rembg import remove
from PIL import Image
import io

app = Flask(__name__)

@app.route("/")
def home():
    # HTML फाइल का सही रास्ता (Path) ढूंढने के लिए सुरक्षित तरीका
    base_dir = os.path.dirname(os.path.abspath(__file__))
    html_path = os.path.join(base_dir, "index.html")
    return open(html_path).read()

@app.route("/remove", methods=["POST"])
def bg_remove():
    try:
        if "image" not in request.files:
            return "No image uploaded", 400
            
        file = request.files["image"]
        input_image = Image.open(file.stream)

        # बैकग्राउंड हटाने की प्रोसेसिंग
        output = remove(input_image)

        img = io.BytesIO()
        output.save(img, format="PNG")
        img.seek(0)

        return send_file(img, mimetype="image/png")
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        return "Processing failed due to memory limit", 500

if __name__ == "__main__":
    # Render पर लाइव चलाने के लिए पोर्ट सेटिंग्स
    app.run(host="0.0.0.0", port=10000)