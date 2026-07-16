from flask import Flask, request, send_file
from rembg import remove
from PIL import Image
import io

app = Flask(__name__)

@app.route("/")
def home():
    return open("index.html").read()

@app.route("/remove", methods=["POST"])
def bg_remove():
    file = request.files["image"]
    input_image = Image.open(file.stream)

    output = remove(input_image)

    img = io.BytesIO()
    output.save(img, format="PNG")
    img.seek(0)

    return send_file(img, mimetype="image/png")

if __name__ == "__main__":
    app.run(debug=True)
