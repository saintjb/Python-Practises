import requests
from bs4 import BeautifulSoup
import json
from collections import deque



channels = ["UC9MK8SybZcrHR3CUV4NMy2g", "AlexeySuprun", "UCqGjCzCi5zG3RjJUA-ZDBkQ"]
last_videos = {
    "UC9MK8SybZcrHR3CUV4NMy2g": ['' for i in range(10)],
    "AlexeySuprun": ['' for i in range(10)],
    "UCqGjCzCi5zG3RjJUA-ZDBkQ": ['' for i in range(10)]
}

with open('file.json', 'r') as file:
    last_videos = json.load(file)

for channel in channels:
    r = requests.get(f'https://www.youtube.com/channel/{channel}/videos')
    soup = BeautifulSoup(r.text, 'lxml')
    videos = soup.find_all('a', class_="yt-uix-sessionlink yt-uix-tile-link spf-link yt-ui-ellipsis yt-ui-ellipsis-2")
    d = deque(last_videos[channel], 10)
    j = 0

    for i in range(min(len(d), len(videos))):
        if videos[i]['href'].split('=')[1] != d[0]:
            j += 1
        else:
             break
    for video in reversed(videos[:j+1]):
        d.appendleft(video['href'].split('=')[1])
        print(video.text, '  |  ',
              f'https://www.youtube.com/watch?v={video["href"].split("=")[1]}')
    last_videos[channel] = list(d)
    print('_________________________________________________________________________________________________________')


with open('file.json', 'w') as file:
    json.dump(last_videos, file, indent=2)




