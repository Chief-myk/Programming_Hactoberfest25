import random
import time

greetings = [
    "🔥 Hacktoberfest 2025 is Live! Time to code, contribute, and celebrate!",
    "🎉 You just made the open-source world better — one PR at a time!",
    "💜 Keep contributing, keep learning — the swag will follow!",
    "🌍 Every commit counts — your code makes an impact!",
    "🚀 From fork to PR, you’re becoming an open-source hero!",
    "⭐ Remember: quality > quantity — make your PRs meaningful!"
]

ascii_banner = r"""
 _    _            _       _            __            _       
| |  | |          | |     | |          / _|          | |      
| |__| | __ _  ___| | ____| |_   _ ___| |_ ___   ___ | |_ ___ 
|  __  |/ _` |/ __| |/ / _` | | | / __|  _/ _ \ / _ \| __/ _ \
| |  | | (_| | (__|   < (_| | |_| \__ \ || (_) | (_) | ||  __/
|_|  |_|\__,_|\___|_|\_\__,_|\__,_|___/_| \___/ \___/ \__\___|
"""

def hacktoberfest_cheer():
    print(ascii_banner)
    print("\n💻 Welcome to Hacktoberfest 2025 — Open Source Awesomeness! 💻\n")
    time.sleep(1)
    print(f"💬 {random.choice(greetings)}\n")
    print("🎯 Tip: Fork → Branch → Commit → Pull Request → Celebrate 🎊")
    print("💡 Don’t forget to sync your repo and write meaningful commit messages!\n")

if __name__ == "__main__":
    hacktoberfest_cheer()
