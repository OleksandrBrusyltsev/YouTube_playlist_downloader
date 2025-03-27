import asyncio
from cli import prompt_user_input
from downloader import download_playlist


def main():
    url, folder = prompt_user_input()
    asyncio.run(download_playlist(url, folder))


if __name__ == "__main__":
    main()