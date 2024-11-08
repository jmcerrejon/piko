import os


class DotenvLoader:
    """
    A class to load environment variables from a .env file.

    Methods:
        load(file_path: str):
            Loads the environment variables from the .env file into the os.environ dictionary.

    Usage:
        # Accessing an environment variable
        DotenvLoader.load(".env")
        value = os.environ.get('VARIABLE_NAME')
    """

    @staticmethod
    def load(file_path: str) -> None:
        with open(file_path) as f:
            for line in f:
                if line.strip() and not line.startswith("#"):
                    key, value = line.strip().split("=", 1)
                    os.environ[key] = value
