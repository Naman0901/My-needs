from pytube import YouTube

try:
    youtube_video_url=input()
    yt_obj = YouTube(youtube_video_url) 
    stream=yt_obj.streams.filter(type="audio")
    for i in range(len(stream)):
        print(i ,stream[i])
    n=int(input("Enter The Corresponding Number You Want To Download(-1 To Exit):"))
    stream[0].download(output_path='D:/NAMAN/Satsang/ભક્તચિંતામણિ', filename=yt_obj.title)
    print('Video Downloaded Successfully')
except Exception as e:
    print(e)
    
