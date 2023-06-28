
####YOLOv8
1. `git clone https://github.com/ultralytics/ultralytics`
2. `pip install ultralytics`
3. Inference: `yolo task=detect mode=predict model=./ultralytics/best3.pt conf=0.5 source=./scr12.png project=/Users/muqsitamir/PycharmProjects/RidaBackend/processed_images`
4. The weights are best2.pt, best3.pt and best_last.pt stored in ultralytics subdirectory with mAP of 0.94, 0.91 and 0.75 respectively.
5. These weights have been trained on increasingly difficult and larger datasets and the best_last.pt was trained only for 100 epochs on augmented dataset of 1.4k images so there is a lot of room for improvement in it.
6. Google Colab notebook used for training with the roboflow dataset link attached (It's a private notebook and you will need to request access). https://colab.research.google.com/drive/17t2B_z2YBvCPizkbGWLR6PHfT4ZaKLyy?usp=sharing

####FaceNet
1. `git clone https://github.com/arsfutura/face-recognition.git`
2. `cd face-recognition`
3. `pip install -r requirements.txt`
4. Arrange the data in the face-recognition/images folder in the following manner:
   - images 
   - person1
       - person1_1.png
       - person1_2.png
       ...
       - person1_n.png
   - person2
       ...
   - personN
5. To train FaceNet, run `./tasks/train.sh path/to/folder/with/images`
6. I have trained the FaceNet model on miniscule images so there's a huge room for improvement with this one.
7. Run inference using the trained weights and embeddings `python -m inference.classifier -h --image-path /path/to/img --save-dir /path/to/dir`
8. The code to draw bounding boxes for all predictions is commented out and only bboxes with rida will be clear in new added code.

####Flask
1. `pip install flask`
2. `pip install --upgrade flask`
3. `flask --app flask_app run`

####Hosting
1. Using Pktriot and Ngrok for free self-hosting HTTP tunnels.
2. Run `./ngrok http 5000` and any app you run on 5000 port will be tunneled to the new domain provided by ngrok to you.
3. Use `ngrok-skip-browser-warning` header with any value to bypass browser warning.


####Notes
1. Processed and Posted Images directories are not added to git so you will have to create them yourself.


In case, anyone wants to implement this for themselves and needs help, you can email me at `islammuqsit7@gmail.com`