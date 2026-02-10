#Input of the person
filename = input("File name: ").strip().lower()
if filename.endswith(".gif"):
    print("image/gif")
elif filename.endswith(".jpeg"):
    print('image/jpeg')
elif filename.endswith(".jpg"):
    print('image/jpg')
elif filename.endswith(".png"):
    print('image/png')
elif filename.endswith(".pdf"):
    print('application/pdf')
elif filename.endswith(".txt"):
    print('text/txt')
elif filename.endswith(".zip"):
    print('archive/zip')
else:
    print("application/octet-stream")
