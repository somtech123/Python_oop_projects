class LoggerMixin:
    def log(self, message: str):

        print(f'[LOG]: {message}')