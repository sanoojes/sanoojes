#!/usr/bin/env python3
import urllib.request
from pathlib import Path
from config import SKILLS, SOCIALS, CUSTOM_ICONS

BASE_URL = "https://raw.githubusercontent.com/tandpfun/skill-icons/main/icons"
ROOT_DIR = Path(__file__).resolve().parent.parent
DEST_DIR = ROOT_DIR / "assets" / "icons"


def get_all_items():
    items = []
    for cat in SKILLS:
        items.extend(cat["items"])
    items.extend(SOCIALS)
    items.extend(CUSTOM_ICONS)
    return items


def download_icon(item):
    file_path = DEST_DIR / item["icon"]
    if file_path.exists():
        return False

    source = item.get("source", "skillicons")
    if source == "local":
        return False
    elif source == "url":
        url = item["remote"]
    else:
        url = f"{BASE_URL}/{item['remote']}"

    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req) as resp, open(file_path, "wb") as f:
        f.write(resp.read())
    return True


def main():
    DEST_DIR.mkdir(parents=True, exist_ok=True)
    items = get_all_items()

    print(f"Syncing icons to {DEST_DIR.relative_to(ROOT_DIR)}/")

    downloaded = 0
    for item in items:
        if download_icon(item):
            print(f"Downloaded {item['icon']}")
            downloaded += 1

    if downloaded:
        print(f"Downloaded {downloaded} new icon(s)")
    else:
        print("All icons already present")


if __name__ == "__main__":
    main()