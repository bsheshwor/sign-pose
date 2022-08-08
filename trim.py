from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import glob2
import os

SOURCE_PATH = "data"
TARGET_PATH = "trim_data"
start_time = 0.6
end_time = 3

def read_vidnames():
    vid_path = glob2.glob(f'{SOURCE_PATH}/*.*')
    return vid_path

def trim_video():
    target_path = []
    vid_path = read_vidnames()

    if (os.path.exists(TARGET_PATH)):
        print("Success")
    else:
        os.mkdir(TARGET_PATH)

    for i,vid in enumerate(vid_path):
        target_path = vid.split("/")[1]
        ffmpeg_extract_subclip(vid, start_time, end_time, targetname=f"{TARGET_PATH}/{target_path}")

trim_video()