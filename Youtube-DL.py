import requests, json

def ytSearch(search):
    result = json.loads(requests.get("https://api.boteater.us/ytdl?search="+search).text)
    print("Title: "+result["result"]["title"])
    print("Artist: "+result["result"]["artist"])
    print("Thumbnail: "+result["result"]["thumbnail"])
    print("Video Download: "+result["result"]["video_url"])
    print("Audio Download: "+result["result"]["audio_url"])

def ytLink(link):
    result = json.loads(requests.get("https://api.boteater.us/ytdl?url="+link).text)
    print("Title: "+result["result"]["title"])
    print("Artist: "+result["result"]["artist"])
    print("Thumbnail: "+result["result"]["thumbnail"])
    print("Video Download: "+result["result"]["video_url"])
    print("Audio Download: "+result["result"]["audio_url"])
