import pickle
import cv2
import mediapipe as mp
import numpy as np
from flask import Flask, render_template, Response, request, redirect, url_for, session, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import time

# Load the trained model
model_dict = pickle.load(open('./model.p', 'rb'))
model = model_dict['model']

# Initialize MediaPipe hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5, min_tracking_confidence=0.5)

# Labels dictionary
labels_dict = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y'}

# Function to pad sequence
def pad_sequence(seq, max_length):
    return seq + [0] * (max_length - len(seq))

# Determine the maximum length from the training data
max_length = 84  # This should match the number of features used during training

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for users
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)

current_letter = None
recognized_word = []
last_recorded_time = 0
recording_interval = 7  # Time interval in seconds
probabilities = {}

@app.route('/')
def index():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            session['username'] = user.username
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = generate_password_hash(password)  # Use default method
        new_user = User(username=username, password=hashed_password)
        try:
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('login'))
        except:
            flash('Username already exists')
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

def generate():
    global current_letter, recognized_word, last_recorded_time, probabilities
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  # Set desired width, adjust as needed
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)  # Set desired height, adjust as needed

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        data_aux = []
        x_ = []
        y_ = []

        H, W, _ = frame.shape
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(frame_rgb)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                for i in range(len(hand_landmarks.landmark)):
                    x = hand_landmarks.landmark[i].x
                    y = hand_landmarks.landmark[i].y
                    x_.append(x)
                    y_.append(y)
                for i in range(len(hand_landmarks.landmark)):
                    x = hand_landmarks.landmark[i].x
                    y = hand_landmarks.landmark[i].y
                    data_aux.append(x - min(x_))
                    data_aux.append(y - min(y_))

            data_aux_padded = pad_sequence(data_aux, max_length)
            prediction = model.predict([np.asarray(data_aux_padded)])
            predicted_character = labels_dict[int(prediction[0])]

            # Get probabilities
            probas = model.predict_proba([np.asarray(data_aux_padded)])[0]
            probabilities = {labels_dict[i]: float(probas[i]) for i in range(len(labels_dict))}

            current_letter = predicted_character

            current_time = time.time()
            if current_time - last_recorded_time > recording_interval:
                recognized_word.append(predicted_character)
                last_recorded_time = current_time

            x1 = int(min(x_) * W) - 40
            y1 = int(min(y_) * H) - 40
            x2 = int(max(x_) * W) + 40
            y2 = int(max(y_) * H) + 40

            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 0), 4)
            cv2.putText(frame, predicted_character, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 0, 0), 3, cv2.LINE_AA)

        _, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    cap.release()

@app.route('/video_feed')
def video_feed():
    return Response(generate(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/current_letter')
def get_current_letter():
    global probabilities
    return jsonify(letter=current_letter, probabilities=probabilities)

@app.route('/recognized_word')
def get_recognized_word():
    global recognized_word
    return jsonify(word=''.join(recognized_word))

@app.route('/reset_word', methods=['POST'])
def reset_word():
    global recognized_word
    recognized_word = []
    return jsonify(status="success")

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
