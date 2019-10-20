# DirFaceSearch
Search Face in Local Dir. Or Recognize Face To Dir.


## Dependency :
+ face_recognition  : pip install face_recognition
+ Numpy             : pip install numpy





### Easy To Use Api.

> #Create A Object Of FaceRec(diractory_name)
> rec = FaceRec("Dir_Path");
> fr = faceRec()
> enc, names = encodeDir("IMG")
> fr.encodings += enc
> fr.labels += names
>
> import sys
>
>
> try:
>   img_path = sys.argv[1]
> except:
>   img_path = "manual_Path.jpg"
>
> print(fr.rec(face_recognition.load_image_file(img_path)))
