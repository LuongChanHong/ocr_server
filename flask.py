from flask import Flask, request, jsonify
import cv2
import numpy as np

app = Flask(__name__)

@app.route('/process_image', methods=['POST'])
def process_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file'}), 400

    image_file = request.files['image']
    image = np.frombuffer(image_file.read(), np.uint8)
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)

    # Xử lý hình ảnh (ví dụ: chuyển sang grayscale)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, buffer = cv2.imencode('.jpg', gray_image)

    response = {
        'processed_image': buffer.tobytes()
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)