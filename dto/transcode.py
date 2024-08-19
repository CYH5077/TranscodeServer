from dataclasses import dataclass

@dataclass
class YoutubeRequest:
    url: str

@dataclass
class YoutubeDownloadResponse:
    url: str
    title: str

    video_codec: str
    video_resolution: str
    video_extension: str
    video_bitrate: str
    video_fps: str

    audio_codec: str
    audio_bitrate: str

    media_file_size: int