# 主入口，自动化流程调度
from pipeline.fetch_trending import fetch_trending
from pipeline.downloader import download_video
from pipeline.subtitle import generate_subtitles
from pipeline.editor import edit_video
from pipeline.uploader import upload_video
from pipeline.utils import log

def main():
    log("Starting pipeline...")
    videos = fetch_trending("music")
    for v in videos:
        video_id = v["id"]
        path = download_video(video_id)
        subs = generate_subtitles(path)
        edited = edit_video(path)
        upload_video(edited, platform="YouTube")

if __name__ == "__main__":
    main()
