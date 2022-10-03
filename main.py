from PIL import Image
import os
import shutil

downloadFolder = "/Users/maino/Downloads/"
picturesFolder = "/Users/maino/Downloads/Pictures/"

videosFolder = "/Users/maino/Downloads/videos/"

if __name__ == "__main__":
    for filename in os.listdir(downloadFolder):
        name, extension = os.path.splitext(downloadFolder + filename)

        if extension in [".jpg", ".jpeg", ".png"]:
            picture = Image.open(downloadFolder + filename)
            picture.save(downloadFolder + filename, optimize=True,quality=60)
            os.remove(downloadFolder + filename)

        if extension in [".mp3"]:
            musicFolder = "/Users/maino/Downloads/Music/"
            os.rename(downloadFolder+ filename, musicFolder+ filename)
        
        if extension in [".mp4"]:
            videosFolder = "/Users/maino/Downloads/Videos/"
            os.rename(downloadFolder+ filename, videosFolder+ filename)


        
        # if extension in [".mp4"]:
        #     os.rename(downloadFolder + filename, videosFolder + filename)
