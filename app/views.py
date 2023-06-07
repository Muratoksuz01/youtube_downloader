from django.shortcuts import render
from pytube import YouTube
from pytube import Playlist
# Create your views here.
def index(request):
    form_type = request.POST.get('form_type')
    if form_type == 'form1':
        print("form1 gonderildi")
        kalite,videolar,temp=set(),{},{}
        context={}
        link=request.POST.get("arama")
        print(link)
        if "playlist" in link:
            print("playlist gönderdi")
            
            p=Playlist(link)
            for video in p.videos:
                y=YouTube(video.watch_url)
                for i in y.streams.filter(mime_type="video/mp4"):
                   kalite.add(str(i.resolution))

                liste=sorted(kalite) 
                temp["resim_url"]=str(video.thumbnail_url)
                temp["title"]=video.title
                temp["kaliteler"]=liste

                videolar[video.title]=temp
            context={
                "videolar":videolar
            }




        else:# play list degilse tamam
            try:
                y=YouTube(link)
                for i in y.streams.filter(mime_type="video/mp4"):
                    print(y.title +"  kalite " + str(i.resolution))
                    kalite.add(str(i.resolution))

                liste=sorted(kalite)
                temp["resim_url"]=y.thumbnail_url
                temp["title"]=y.title
                temp["kaliteler"]=liste
                videolar[y.title]=temp
                context={
                    "videolar":videolar
                }
            except:
                print("hata var url yanlış")
            
        return render(request, 'index.html',context)





    elif form_type == 'form2':
        pass
    else:
        return render(request, 'index.html')



# videolar{
#     "film1":{
#         "resim":vfsdvsd,
#         "title":"vfdvsd",
#         "kalite":{53453453}
#     }

# }