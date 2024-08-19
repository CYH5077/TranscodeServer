from config.Config import TranscodeServerConfig
from celery import Celery
from pytube import YouTube

# Server Info Print
print()
print("#" * 52)
print("#" + " " * 50 + "#")
print("#" + "Transcode Server".center(50) + "#")
print("#" + " " * 50 + "#")
print("#" * 52)

# 설정 load
try:
    transcode_server_config = TranscodeServerConfig()
    transcode_server_config.load_config()
    print(f"Redis url: {transcode_server_config.get_redis_url()}")
except Exception as e:
    print(e)
    exit(-1)

CELERY_BROKER = transcode_server_config.get_redis_url() + "/0"
app = Celery(__name__, broker=CELERY_BROKER)
app.conf.task_always_eager = True

@app.task
def youtube_video_info(url: str):
    yt = YouTube(url)
    print(f"title: {yt.title}")
    print(f"조회수: {yt.views}")

    print(f"사용 가능한 스트림 정보:")
    for stream in yt.streams:
        print(stream)
