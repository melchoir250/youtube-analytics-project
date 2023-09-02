class Video:
    def __init__(self, video_id:int, video_tite:str, video_link:str,
                video_view:int, video_like:int) -> None:
        self.video_id = video_id
        self.video_tite = video_tite
        self.video_link = video_link
        self.video_view = video_view
        self.video_like = video_like
    
    #def __str__(self):
    #    return f"Video: {self.video_tite} ({self.video_link}, {self.video_view}, {self.quantity_like})"


class PLVideo(Video):
    
    def __init__(self, video_id, video_tite, video_link,
                video_view, video_like, playlist_id:int) -> None:
        super().__init__(video_id, video_tite, video_link, video_view, video_like)
        self.playlist_id = playlist_id
    
    #def __str__(self):
    #    super().__str__() + f"{self.playlist_id}"
