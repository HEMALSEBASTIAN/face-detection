from deepface import DeepFace
models = ["VGG-Face", "Facenet", "Facenet512", "OpenFace", "DeepFace", "DeepID", "ArcFace", "Dlib", "SFace"]
detectors = ["opencv", "ssd", "mtcnn", "dlib", "retinaface"]
metrics = ["cosine", "euclidean", "euclidean_l2"]
verification=DeepFace.verify(img1_path="faces\\MEH.JPG",
img2_path="faces\\m1.JPG",
model_name = models[1], distance_metric = metrics[1],
detector_backend = detectors[0])
print(verification)