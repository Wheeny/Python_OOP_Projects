import unittest
from src.video.video import Video

class TestVideo(unittest.TestCase):

    def test_that_the_video_plays(self):
        video = Video("Python Masterclass", 12, 0)
        self.assertEqual(video.title, "Python Masterclass")
        self.assertEqual(video.play(), "The video Python Masterclass is now playing")


    def test_that_the_video_has_been_fast_forwarded_by_the_number_of_given_minutes(self):
        video = Video("Python Masterclass", 12, 6)
        video.advance(5)
        self.assertEqual(video.current_playback_position, 11)


    def test_that_the_video_has_been_fast_forwarded_by_the_number_of_given_minutes_and_stops_at_max_duration(self):
            video = Video("Python Masterclass", 12, 10)
            video.advance(5)
            self.assertEqual(video.current_playback_position, 12)


    def test_that_the_video_is_finished(self):
        video = Video("Python Masterclass", 10, 10)
        self.assertTrue(video.is_finished())


    def test_that_the_video_was_restarted(self):
        video = Video("Python Masterclass", 10, 5)
        video.restart()
        self.assertEqual(video.current_playback_position, 0)

    def test_for_the_time_remaining(self):
        video = Video("Python Masterclass", 12, 4)
        self.assertEqual(video.time_remaining(), 8)

