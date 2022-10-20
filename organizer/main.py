import os
import shutil
from time import time, sleep
import patoolib

directory = os.fsencode("F:\Downloads")

while True:
    for filename in os.listdir("F:\Downloads"):
        # Photos
        if filename.endswith(".jfif") or filename.endswith(".png"):
            File_Path = os.path.join("F:\Downloads", filename)
            New_Directory = (os.path.join("F:\Photos", filename))
            shutil.move(File_Path, New_Directory)
        # Videos
        elif filename.endswith(".mp4") or filename.endswith(".avi") or filename.endswith(".mkv"):
            File_Path = os.path.join("F:\Downloads", filename)
            File_size = os.path.getsize(File_Path)
            if File_size <= 2147483648:
                New_Directory = (os.path.join("F:\Videos", filename))
                shutil.move(File_Path, New_Directory)
            else:
                New_Directory = (os.path.join("F:\Movies", filename))
                shutil.move(File_Path, New_Directory)
        # Music
        elif filename.endswith(".mp3") or filename.endswith(".m4a") or filename.endswith(".wav"):
            File_Path = os.path.join("F:\Downloads", filename)
            New_Directory = (os.path.join("F:\Music", filename))
            shutil.move(File_Path, New_Directory)
        # Executable
        elif filename.endswith(".exe"):
            File_Path = os.path.join("F:\Downloads", filename)
            os.startfile(File_Path)
            while filename in os.listdir("F:\Downloads"):
                try:
                    os.chmod(File_Path, 0o777)
                    os.remove(File_Path)
                except PermissionError:
                    print("Gulu")
                    sleep(60 - time() % 60)
        #Rar
        elif filename.endswith(".rar") or filename.endswith(".7zip") or filename.endswith(".zip"):
            File_Path = os.path.join(r"F:\Downloads", filename)
            patoolib.extract_archive(File_Path,outdir="F:\Rar")
            os.remove(File_Path)
        #PDF
        elif filename.endswith(".pdf"):
            File_Path = os.path.join("F:\Downloads", filename)
            New_Directory = (os.path.join("F:\Pdf", filename))
            shutil.move(File_Path, New_Directory)