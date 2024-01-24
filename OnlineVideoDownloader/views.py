from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

from pytube import YouTube #for downloading videos
import validators #for validating if the input is an URL

def home(request):
    url = error = channel = title = duration = thumbnail = ""
    context = {
        'url' : url,
        'error' : error,
        'channel' : channel,
        'title' : title,
        'duration' : duration,
        'thumbnail' : thumbnail,
    }
    try:
        if request.method == "POST":
            url = request.POST['url']
            context['url'] = url
            try:
                validate = validators.url(url)
                if validate is True:
                    if "playlist?list=" in url:
                        error = "Playlists can't be downloaded for now"
                        context['error'] = error
                        print(error)
                        return redirect('home', context)
                    elif "youtube.com" in url:
                        try:
                            yt = YouTube(url)
                            channel = yt.author
                            title = yt.title
                            duration = yt.length
                            thumbnail = yt.thumbnail_url
                            # description = yt.description

                            if title == "" and thumbnail == "":
                                error = "some error occurred"
                                print(error)
                                context['error'] = error
                                return redirect ('home', context)
                            else:
                                context['channel'] = channel
                                context['title'] = title
                                context['duration'] = duration
                                context['thumbnail'] = thumbnail
                                return redirect('home', context)
                            
                        except VideoUnavailable:
                            error = "this video is unavailable"
                            print(error)
                            context['error'] = error
                            return redirect ('home', context)
                        except LiveStreamError:
                            error = "live stream video can't be downloaded"
                            print(error)
                            context['error'] = error
                            return redirect ('home', context)
                        except MembersOnly:
                            error = "this video can only be downloaded and viewed by members of the channel"
                            print(error)
                            context['error'] = error
                            return redirect ('home', context)
                        except VideoPrivate:
                            error = "this video is private"
                            print(error)
                            context['error'] = error
                            return redirect ('home', context)
                        except AgeRestrictedError:
                            error = "this video is age restricted"
                            print(error)
                            context['error'] = error
                            return redirect ('home', context)
                        except VideoRegionBlocked:
                            error = "this video is blocked in your region"
                            print(error)
                            context['error'] = error
                            return redirect ('home', context)
                        except:
                            error = "some error occurred"
                            print(error)
                            context['error'] = error
                            return redirect ('home', context)
                    else:
                        error = "some error occurred. url may be invalid"
                        print(error)
                        context['error'] = error
                        return redirect ('home', context)
                else:
                    error = "invalid url"
                    print(error)
                    context['error'] = error
                    return redirect ('home', context)
            except:
                pass
    except:
        pass
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')



#functions for downloading

#yt video download
def ytDownload(request):
    try:
        if request.method == "POST":
            videoURL = request.POST['videoURL']
            videoType = request.POST['videoType']
            yt = YouTube(videoURL)
            if videoType == 'audio':
                audio = yt.streams.filter(only_audio=True)
                itag = audio[0].itag
                yt.streams.get_by_itag(itag).download()
            else:
                video = yt.streams.filter(file_extension='mp4')
                itag = video[0].itag
                yt.streams.get_by_itag(itag).download()

            messages.success(request, "Video Downloaded Successfully" )
            return redirect('home')
        else:
            return HttpResponse("Something went wrong. Invalid request")
    except:
        pass