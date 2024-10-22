import logging


class FileManager():
    def __init__(self, filename, filemode):
        self.filename = filename
        self.filemode = filemode
        self.file = None
        logging.basicConfig(filename="file_errors.log", level=logging.INFO)

    def __enter__(self):
        try:
            self.file = open(self.filename, self.filemode)
            logging.info("Файл открыт в режиме %s", self.filemode)
            return self.file
        except Exception as e:
            logging.info("Произошла ошибка при открытии файла %s : %s",self.filename ,e)
            raise e

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            if self.file:
                self.file.close()
                logging.info("Файл %s закрыт", self.filename)
            if exc_type:
                logging.error("Ошибка %s", exc_type)
        except Exception as e:
            logging.info("Произошла ошибка при закрытии файла %s : %s", self.filename, e)
            raise e

with FileManager("my_file.txt", "w") as file:
    file.write("ABRAKADABRA")









