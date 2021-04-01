from pytube import YouTube

link = input("enter url :")



#print(f"The video title is:\n{video.title} \n----------------------------")
#print(f"The video views is : \n{video.views}\n----------------------------")
#print(f"The video is : \n {video.length/60}m \n----------------------------")
#print(f"The video retng : \n {video.rating}\n------------------------------")
#for straem in video.streams:
#    print(straem)
video.streams.get_lowest_resolution().download(output_path="C:/video")

def complet():
    print("download doen")
video.register_on_complete_callback(complet())
