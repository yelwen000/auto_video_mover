# 视频下载
def download_video(video_id, output_dir="downloads"):
    print(f"[downloader] Downloading video {video_id} to {output_dir}")
    return f"{output_dir}/{video_id}.mp4"
