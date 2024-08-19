from task import app, youtube_video_info

task = youtube_video_info.delay("https://www.youtube.com/watch?v=D-_MPGVveMk")
print(task.status)
print(task.result)