from PIL import Image
import os

downloadFolder = "C:/Users/maino/Downloads/"
picturesFolder = "E:/Downloads/Pictures/"
musicFolder = "E:/Downloads/Music/"
videosFolder = "E:/Downloads/videos/"

if __name__ == "__main__":
    for filename in os.listdir(downloadFolder):
        name, extension = os.path.splitext(downloadFolder + filename)

        if extension in [".jpg", ".jpeg", ".png"]:
            picture = Image.open(downloadFolder + filename)
            picture.save(downloadFolder + filename, optimize=True,quality=60)
            os.remove(downloadFolder + filename)
            print(name + ": " + extension)
        
        if extension in [".mp3"]:
            os.rename(downloadFolder + filename, musicFolder + filename)
        
        if extension in [".mp4"]:
            os.rename(downloadFolder + filename, videosFolder + filename)
