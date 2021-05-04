import os

files=os.listdir()

#If folder don't exist then create folder
def CreateIfNotExist(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

# for creating folder
CreateIfNotExist('Images')
CreateIfNotExist('Documents')
CreateIfNotExist('Media')

#Image file transfer to Images folder
imageExtensions=[".png",".jpg",".jpeg"]
images=[file for file in files if os.path.splitext(file)[1].lower() in imageExtensions]
print(images)

#Documents files transfer to Documents folder
DocumentExtensions=[".txt",'.docx','.doc','.pdf']
documents=[file for file in files if os.path.splitext(file)[1].lower() in DocumentExtensions]
print(documents)

#Video files transfer to Media folder
MediaExtensions=['.mp4','.mp3','.flv']
MediaFiles=[file for file in files if os.path.splitext(file)[1].lower() in MediaExtensions]
print(MediaFiles)

#Move files to appropriate folders
for image in images:
    os.replace(image,f"Images/{image}")

for document in documents:
    os.replace(document,f"Documents/{document}")

for video in MediaFiles:
    os.replace(video,f"Media/{video}")
