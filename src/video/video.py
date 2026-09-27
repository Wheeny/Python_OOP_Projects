class Video:

    def __init__(self, title, duration, current_playback_position = 0 ) -> None:
        self.title = title
        self.duration = duration
        self.current_playback_position = current_playback_position



    def play(self) -> str:
        print(f"The video {self.title} is now playing")
        return f"The video {self.title} is now playing"



    def advance(self, minutes) -> int:
        if self.current_playback_position > 0:
            self.current_playback_position += minutes

            if self.current_playback_position > self.duration:
                self.current_playback_position = self.duration
        return self.current_playback_position



    def is_finished(self) -> bool:
        return self.current_playback_position >= self.duration

    def restart(self) -> None:
        self.current_playback_position = 0

    def time_remaining(self) -> int:
        remaining = self.duration - self.current_playback_position
        if remaining < 0:
            return 0

        return remaining