def prompt_user_input() -> tuple[str, str]:
    url = input("🔗 Enter the YouTube playlist URL: ").strip()
    folder = input("📁 Enter folder to save (default: downloads): ").strip() or "downloads"
    return url, folder
