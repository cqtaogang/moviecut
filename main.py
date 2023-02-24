from moviepy.editor import VideoFileClip, concatenate_videoclips


start1 = 1
start2 = 2
start3 = 10
end1 = 5
end2 = 2
end3 = 10
start = start1 * 60 * 60 + start2 * 60 + start3
end = end1 * 60 * 60 + end2 * 60 + end3

clip1 = VideoFileClip(r"d:\test2.mp4").subclip(start, end)
# clip2 = VideoFileClip("myvideo2.mp4").subclip(50, 60)
# clip3 = VideoFileClip("myvideo3.mp4")

finalclip = concatenate_videoclips([clip1])
finalclip.write_videofile(r"d:\ttt.mp4")
