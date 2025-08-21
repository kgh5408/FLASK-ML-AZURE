# REST API - https://www.youtube.com/watch?v=fB3MB8TXNXM
# 빌트인
import logging

# 서드파티
import numpy as np
import tensorflow as tf
from flask import Flask, request, jsonify


logging.basicConfig(level=logging.DEBUG)
app = Flask(__name__)


def preprocessing(json_payload):
    sentences = json_payload['message']
    tensor = tf.constant([[sentence] for sentence in sentences])
    return tensor


def postprocessing(json_payload, prediction_dict):
    prediction = prediction_dict['dense_36'].numpy()
    sentences = json_payload['message']
    response = {}
    d = {}
    for idx, sentence in enumerate(sentences):
        pred_idx = np.argmax(prediction[idx])
        d[sentence] = 'ham' if pred_idx == 1 else 'spam'
    response['request'] = sentences
    response['response'] = d
    return response


@app.route("/")
def home():
    html = "<h3>애저 파이프라인을 이용한 지속적 배포</h3>"
    return html.format(format)


# POST 메소드로 예측 요청을 처리하는 엔드포인트
@app.route("/predict", methods=['POST'])
def predict():
    # Keras 3에서 TensorFlow SavedModel을 로딩하는 방법
    model = tf.keras.layers.TFSMLayer('./saved_model', call_endpoint='serving_default')
    app.logger.info(f"Model loaded.")
    
    json_payload = request.json # POST 요청으로 전달된 JSON 데이터를 읽음
    app.logger.info(f"JSON payload: {json_payload}")

    preprocessed_payload = preprocessing(json_payload)
    # TFSMLayer는 직접 텐서를 받음
    prediction = model(preprocessed_payload)
    app.logger.info(f"Prediction: {prediction}")

    response = postprocessing(json_payload, prediction)
    return jsonify(response) # Flask서버에서 Python객체를 JSON 형태로 변환하고 HTTP 응답(Response) 객체로 만들어주고, 클라이언트에 반환


if __name__ == "__main__":
    '''
    Flask 애플리케이션을 실행
    host='0.0.0.0': 모든 IP 주소에서 접근 가능하도록 설정
    port=5000: Flask 서버가 5000번 포트에서 실행되도록 설정
    '''
    app.run(host='0.0.0.0', port=5000)
