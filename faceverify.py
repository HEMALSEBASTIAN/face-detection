from deepface import DeepFace
verification=DeepFace.verify(img1_path="faces\\MEH.JPG",
img2_path="faces\\m1.JPG")
print(verification)