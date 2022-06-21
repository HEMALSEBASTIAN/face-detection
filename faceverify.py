from deepface import DeepFace
models = ["VGG-Face", "Facenet", "Facenet512", "OpenFace", "DeepFace", "DeepID", "ArcFace", "Dlib", "SFace"]
detectors = ["opencv", "ssd", "mtcnn", "dlib", "retinaface"]
metrics = ["cosine", "euclidean", "euclidean_l2"]
verification=DeepFace.verify(
img1_path="faces\\ddd.jpg",
img2_path="faces\\MEH.jpg",
model_name = models[1], distance_metric = metrics[2],
detector_backend = detectors[0])
print(verification)