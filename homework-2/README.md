# Режимы доступа. Домашнее задание

## Описание задачи
Модифицируйте конструктор `Channel`, чтобы после инициализации экземпляр имел следующие атрибуты, заполненные реальными данными канала:
- id канала
- название канала
- описание канала
- ссылка на канал
- количество подписчиков
- количество видео
- общее количество просмотров

Добавьте в класс `Channel` следующие методы:
- класс-метод `get_service()`, возвращающий объект для работы с YouTube API
- метод `to_json()`, сохраняющий в файл значения атрибутов экземпляра `Channel`

## Ожидаемое поведение
- Код в файле `main.py` должен выдавать ожидаемые значения




    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        channel = youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        info_channel = json.dumps(channel, indent=2, ensure_ascii=False)
        info_channel_json = json.loads(info_channel)
        self.title = info_channel_json['items'][0]['snippet']['title']
        self.description = info_channel_json['items'][0]['snippet']['description']
        self.url = 'https://www.youtube.com/channel/' + self.__channel_id
        self.subs_count = info_channel_json['items'][0]['statistics']['subscriberCount']
        self.video_count = info_channel_json['items'][0]['statistics']['videoCount']
        self.view_count = info_channel_json['items'][0]['statistics']['viewCount']