from dotenv import load_dotenv
from os import environ
from showcase_bot.client import Client


def main():
    load_dotenv()
    client = Client(environ)
    client.run()


if __name__ == "__main__":
    main()
