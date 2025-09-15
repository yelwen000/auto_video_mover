# fetcher.py
import yt_dlp
import json
import os

DB_FILE = "db.json"

def load_db():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r", encoding="utf-8") as f:
            return set(json.load(f))
    return set()

def save_db(video_ids):
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(list(video_ids), f, ensure_ascii=False, indent=2)

CATEGORY_URLS = {
    "all": "https://www.youtube.com/feed/trending",
    "music": "https://www.youtube.com/feed/trending?bp=6gQJRkVleHBsb3Jl",
    "gaming": "https://www.youtube.com/feed/trending?bp=6gQJRkVleHBsb3JlfGdhbWVz",
    "movies": "https://www.youtube.com/feed/trending?bp=6gQJRkVleHBsb3JlfG1vdmllcw%3D%3D",
    "technology": "https://www.youtube.com/results?search_query=technology&sp=CAI%253D"
}

def fetch_category_videos(category="all", max_results=5):
    """抓取YouTube分类热榜"""
    url = CATEGORY_URLS.get(category, CATEGORY_URLS["all"])
    ydl_opts = {
        'quiet': True,
        'extract_flat': True,
        'skip_download': True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        entries = info.get('entries', [])
        return [f"https://www.youtube.com/watch?v={e['id']}" for e in entries[:max_results]]

def get_new_videos(category="all", max_results=5):
    """获取分类热榜的新视频"""
    seen = load_db()
    videos = fetch_category_videos(category, max_results)
    new_videos = [v for v in videos if v not in seen]
    for v in new_videos:
        seen.add(v)
    save_db(seen)
    return new_videos
