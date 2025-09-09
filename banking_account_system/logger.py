
class LoggerMixin:
    def log(self, message: str, type: str = 'LOG'):

        print(f'[{type}]: {message}')