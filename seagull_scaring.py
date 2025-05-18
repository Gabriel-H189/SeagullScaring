from configparser import ConfigParser
from datetime import datetime
from random import randint, seed
from threading import Thread
from time import sleep
from zipfile import ZipFile

from playsound import playsound
from pyttsx3 import Engine, init  # type: ignore


class Scarer:
    """Seagull scarer."""

    def __init__(
        self,
        sound: str,
        timer: int,
        min_time: int,
        max_time: int,
        config_file: str,
        log_file: str,
    ) -> None:

        self.sound: str = sound
        self.min_time: int = min_time
        self.max_time: int = max_time
        self.config_file: str = config_file
        self.log_file: str = log_file
        self.timer: int = timer
        self.seagulls_scared: int = 0
        self.log_data: str = ""
        self.FMT: str = "%d.%m.%y %H:%M:%S"

        self.parser: ConfigParser = ConfigParser()
        self.parser.read(self.config_file)

        self.config: list[str] = self.parser.sections()

    def scare_thread(self) -> None:
        """Scares seagulls in a thread."""

        seed()

        # Scare seagulls in a loop until timer reaches 0
        while self.timer > 0:

            pause: int = randint(a=self.min_time, b=self.max_time)
            playsound(self.sound)
            self.log_data += f"A seagull was scared on {datetime.now():{self.FMT}}.\n"
            self.seagulls_scared += 1
            sleep(pause)
            self.timer -= pause

    def start(self) -> None:
        """Start seagull scaring."""

        thread: Thread = Thread(target=self.scare_thread)
        thread.start()

    def save_log(self) -> None:
        """Saves text file to log."""

        with open(file=self.log_file, mode="a", encoding="utf-8") as file:
            file.write(self.log_data)

    def send_announcement(self, text: str) -> None:
        """Sends announcement."""

        engine: Engine = init()  # type: ignore

        for _ in range(2):
            playsound(r"alarm_seagull.wav")

        engine.say("This is a Seagull Wars public service announcement.")  # type: ignore
        engine.say(text)  # type: ignore
        engine.runAndWait()  # type: ignore

        for _ in range(2):
            playsound(r"alarm_seagull.wav")

    def extract(self) -> None:
        """Sound effect autoextractor method."""

        file_path: str = r"media.zip"
        with ZipFile(file=file_path, mode="r") as zip_file:

            zip_file.extractall("media")
