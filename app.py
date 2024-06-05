from flask import Flask, request, jsonify
import numpy as np
import tensorflow as tf
from flask_cors import CORS
import base64
from io import BytesIO
from PIL import Image

app = Flask(__name__)
CORS(app)

model = tf.keras.models.load_model('mymodel.keras')


@app.route('/classifica_lixo', methods=['POST'])
def classificador_lixo():
    request_data = request.get_json()
    imagem_base64 = request_data['imagem']
    imagem_bytes = base64.b64decode(imagem_base64)
    imagem = Image.open(BytesIO(imagem_bytes))
    imagem = imagem.resize((224, 224))
    img_array = np.array(imagem) / 255.0
    img_array = img_array.reshape(1, 224, 224, 3)

    p = model.predict(img_array)
    predicted_class = np.argmax(p[0])
    tipo_lixo = {0: "Papelão", 1: "Vidro", 2: "Metal",
                 3: "Papel", 4: "Plástico", 5: "Lixo"}

    response = {

        'categoria': tipo_lixo[predicted_class]
    }

    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
