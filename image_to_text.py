import PIL
import pytesseract
from PIL import Image
from io import BytesIO
import numpy as np
from flask import Flask, request, jsonify

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False


@app.route("/ping")
def ping():
    return "Hello, I am alive"


def read_file_as_image(data) -> np.ndarray:
    image = np.array(PIL.Image.open(BytesIO(data)))
    return image


@app.route("/predict", methods=['POST'])
def predict():
    try:
        file = request.files.get('file')
        image = read_file_as_image(file.read())

        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        text = pytesseract.image_to_string(image, lang='eng')

        return jsonify(
            Text=text,
        )


    except Exception as e:
        error = "Please Use Another Image"
        return jsonify(response=error)


if __name__ == "__main__":
    app.debug = True
    app.run()
