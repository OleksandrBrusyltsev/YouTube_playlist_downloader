import asyncio
import os
from pathlib import Path


async def download_playlist(url: str, folder: str = "downloads") -> None:
    Path(folder).mkdir(parents=True, exist_ok=True)

    command = [
        "yt-dlp",
        "-f", "bestvideo+bestaudio/best",
        "-o", f"{folder}/Tutorial %(playlist_index)s - %(title)s.%(ext)s",
        "--yes-playlist",
        "--progress",
        url,
    ]

    print(f"\n🎬 Downloading playlist: {url}\n📂 Saving to folder: {folder}\n")

    process = await asyncio.create_subprocess_exec(
        *command,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.STDOUT,
    )

    while True:
        line = await process.stdout.readline()
        if not line:
            break
        print(line.decode("utf-8").rstrip())

    await process.wait()
    print("\n✅ Download completed.")