import face_recognition
import numpy as np
import os


def encodeDir(path):
    encodding = []
    names = []

    for file in os.listdir(path)[:5]:
        if file.endswith(".jpg") or file.endswith(".JPG"):
            print("Tring To Encode : {}".format(file))
            try:
                img = face_recognition.load_image_file("{}/{}".format(path, file))
                face_encoding = face_recognition.face_encodings(img)[0]
                encodding.append(face_encoding)
                names.append(file.rsplit(".", 1)[0])
                print("Done...")
            except:
                print("Err...")

    return encodding, names
            




class faceRec():

    def __init__(self):
        self.encodings = []
        self.labels = []



    def addFace(self, img, name):
        self.encodings.append( face_recognition.face_encodings(img)[0] )
        self.labels.append(name)


    def rec(self,img):
        new_encodings = face_recognition.face_encodings(img)[0]
        matches = face_recognition.compare_faces(self.encodings, new_encodings)
        distances = face_recognition.face_distance(self.encodings, new_encodings)
        best_match_index = np.argmin(distances)
        name = "Unknown"
        confd = distances[best_match_index]
        if matches[best_match_index]:
            name = self.labels[best_match_index]

            
        return name, confd




if __name__ == "__main__":

    fr = faceRec()
    enc, names = encodeDir("IMG")
    fr.encodings += enc
    fr.labels += names

    import sys


    try:
        new = sys.argv[1]
    except:
        new = "m.jpg"

    print(fr.rec(face_recognition.load_image_file(new)))
    




