from src.video.video import Video

video_menu_functions = """

VIDEO MENU

What do you want to do? Select an option:

1. Play
2. Advance
3. Finish
4. Restart
5. Check Time Remaining
6. Exit

"""

video_name = input("Enter Video Name: ")
video_duration = int(input("Enter Video Duration in minutes: "))
video_current_playback_position = int(input("Enter Current Playback Position in minutes: "))

video = Video(video_name, video_duration, video_current_playback_position)

while True:
    print(video_menu_functions)
    video_menu_functions_list = int(input("Select an option: "))

    match video_menu_functions_list:
        case 1:
            video.play()
        case 2:
            minutes = int(input("Enter the number of minutes you would like to fast forward the video: "))
            video.advance(minutes)
            print(f"Current position: {video.current_playback_position}")
        case 3:
            print(video.is_finished())
        case 4:
            video.restart()
        case 5:
            print(video.time_remaining())
        case 6:
            print("******Goodbye******")
            break
        case _:
            print("Invalid Input")