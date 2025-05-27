from flask import Flask, request, render_template, jsonify
from my_utils.db_utils import is_plate_allowed, add_plate, create_table
import cv2
from flask import Response
from my_utils.detector import detect_plate
from my_utils.ocr_reader import read_plate_text
from my_utils.db_utils import is_plate_allowed
from my_utils.truck_detector import is_truck_present

app = Flask(__name__)

create_table()
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return "No file uploaded", 400

    image = request.files['image']
    image_path = 'temp.jpg'
    image.save(image_path)

    if not is_truck_present(image_path):
        return jsonify({'status': 'denied', 'message': 'Araç tipi uygun değil: Erişim reddedildi'})

    plate_img = detect_plate(image_path)
    if plate_img is None:
        return jsonify({'status': 'error', 'message': 'Plaka tespit edilemedi'})

    # OCR ile plaka metnini oku
    plate_text = read_plate_text(plate_img)

    if is_plate_allowed(plate_text):
        return jsonify({'status': 'success', 'message': f'{plate_text}: Kapı açılıyor'})
    else:
        return jsonify({'status': 'denied', 'message': f'{plate_text}: Erişim reddedildi'})

@app.route('/add_plate', methods=['POST'])
def add_plate_route():
    plate = request.form.get('plate')
    if not plate:
        return jsonify({'status': 'error', 'message': 'Plaka bilgisi eksik'})

    add_plate(plate)
    return jsonify({'status': 'success', 'message': f'{plate} başarıyla eklendi'})

camera = cv2.VideoCapture(2)

def generate_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break

        plate_img, conf = detect_plate(frame)
        plate_text = read_plate_text(plate_img) if plate_img is not None else None

        if plate_text:
            allowed = is_plate_allowed(plate_text)
            color = (0, 255, 0) if allowed else (0, 0, 255)
            label = "Kapı Açılıyor" if allowed else "Erişim Reddedildi"
            cv2.putText(frame, f"{label}: {plate_text}", (30, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

        ret, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)