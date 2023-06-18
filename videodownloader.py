from pytube import YouTube
link=str(input("Enter your Video Link : "))
yt=YouTube(link)
stream=yt.streams.get_highest_resolution()
print("Download Commencing........");
stream.download()
print("Download Completed!!")
