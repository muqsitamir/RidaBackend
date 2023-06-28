import os
import subprocess

from flask import Flask, request, jsonify, send_file

app = Flask(__name__)


@app.route('/image/<filename>')
def serve_image(filename):
    if request.args['model'] == "YOLOv8":
        file_path = f'processed_images/predict/{filename}'  # Replace with the actual path to the saved file
    else:
        file_path = f'processed_images/{filename}'  # Replace with the actual path to the saved file
    return send_file(file_path, mimetype='image/jpeg')


@app.route('/', methods=['GET', 'POST'])
def process():
    if request.method == 'GET':
        return 'Test is working!'
    elif request.method == 'POST':
        if 'file' not in request.files:
            error_response = jsonify({"file": ["This field is required"]})
            error_response.status_code = 400
            return error_response
        path = "/Users/muqsitamir/PycharmProjects/RidaBackend/"
        file = request.files['file']
        name = file.filename.replace(" ", '').replace(".", "", file.filename.count(".") - 1)
        file_path = os.path.join(f"{path}posted_images", name)
        if os.path.exists(file_path):
            name = str(len(os.listdir(path + "posted_images")) + 1) + "_" + name
            file_path = os.path.join(f"{path}posted_images", name)
        file.save(file_path)

        if request.args['model'] == "FaceNet":
            destination_directory = "/Users/muqsitamir/PycharmProjects/RidaBackend/face-recognition"
            if not os.path.isdir(destination_directory):
                return 'Destination directory does not exist', 500
            os.chdir(destination_directory)
            command = f"python -m inference.classifier --image-path {file_path} --save-dir {path}processed_images/"
            saved_location = name
        else:
            command = f"yolo task=detect mode=predict model=/Users/muqsitamir/PycharmProjects/RidaBackend/ultralytics/best3.pt conf=0.5 source={file_path} project=/Users/muqsitamir/PycharmProjects/RidaBackend/processed_images save"
            saved_location = "predict/" + name

        subprocess.run(command, shell=True, capture_output=True, text=True)

        return f'{saved_location}', 200
