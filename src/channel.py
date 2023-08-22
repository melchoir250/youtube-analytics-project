import os
from googleapiclient.discovery import build
import json


api_key: str = os.getenv('YT_API_KEY')
#youtube = build('youtube', 'v3', developerKey='AIzaSyAa9bdrXR0NRQX4X4TI6zKdfhWGHwISbCA')


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        self.youtube = self.get_service()
        
        channel = self.youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        info_channel = json.dumps(channel, indent=2, ensure_ascii=False)
        info_channel_json = json.loads(info_channel)
        self.title = info_channel_json['items'][0]['snippet']['title']
        self.description = info_channel_json['items'][0]['snippet']['description']
        self.url = 'https://www.youtube.com/channel/' + self.__channel_id
        self.subs_count = info_channel_json['items'][0]['statistics']['subscriberCount']
        self.video_count = info_channel_json['items'][0]['statistics']['videoCount']
        self.view_count = info_channel_json['items'][0]['statistics']['viewCount']

    @classmethod
    def get_service(cls):
        return build('youtube', 'v3', developerKey=api_key)

    def to_json(self, file_name):
        channel = self.youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        with open(os.path.join(file_name), 'w') as file:
            file.write(json.dumps(channel, indent=2, ensure_ascii=False))
        # print(name_file)

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        youtube = self.get_service()
        channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        print(channel)

