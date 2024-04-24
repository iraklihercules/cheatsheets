# The Adapter Pattern is a structural design pattern that allows objects with incompatible interfaces to work together.
# It acts as a bridge between two incompatible interfaces, converting the interface of one class into another interface
# that a client expects. This pattern allows existing classes to be reused without modifying their code.

# MediaPlayer: Represents the target interface that the client expects. It defines a method play() to play audio files.
# AdvancedMediaPlayer: Represents the source interface with advanced features. It defines methods play_mp4() and
# play_vlc() to play MP4 and VLC files, respectively.
# Mp4Player and VlcPlayer: Concrete implementations of the AdvancedMediaPlayer interface for playing MP4 and VLC files.
# MediaAdapter: Acts as an adapter between the MediaPlayer and AdvancedMediaPlayer interfaces. It adapts the play()
# method of MediaPlayer to call the appropriate methods of AdvancedMediaPlayer based on the audio type.
# AudioPlayer: Represents the client that uses the MediaPlayer interface. It plays MP3 files directly and uses the
# MediaAdapter to play MP4 and VLC files.

# In this example, the AudioPlayer class represents the client code that expects to play audio files using the
# MediaPlayer interface. When the AudioPlayer receives requests to play MP4 or VLC files, it delegates the task to the
# MediaAdapter, which acts as an adapter to the AdvancedMediaPlayer interface and plays the files using the appropriate
# methods. This way, the AudioPlayer can work with both MP3 and advanced audio formats without directly depending on
# their implementations.

class MediaPlayer:
    def play(self, audio_type, filename):
        pass


class AdvancedMediaPlayer:
    def play_mp4(self, filename):
        pass

    def play_vlc(self, filename):
        pass


class Mp4Player(AdvancedMediaPlayer):
    def play_mp4(self, filename):
        print("Playing MP4 file:", filename)


class VlcPlayer(AdvancedMediaPlayer):
    def play_vlc(self, filename):
        print("Playing VLC file:", filename)


class MediaAdapter(MediaPlayer):
    def __init__(self, audio_type):
        if audio_type == "mp4":
            self.advanced_player = Mp4Player()
        elif audio_type == "vlc":
            self.advanced_player = VlcPlayer()

    def play(self, audio_type, filename):
        if audio_type == "mp4":
            self.advanced_player.play_mp4(filename)
        elif audio_type == "vlc":
            self.advanced_player.play_vlc(filename)


class AudioPlayer(MediaPlayer):
    def play(self, audio_type, filename):
        if audio_type == "mp3":
            print("Playing MP3 file:", filename)
        elif audio_type == "mp4" or audio_type == "vlc":
            media_adapter = MediaAdapter(audio_type)
            media_adapter.play(audio_type, filename)
        else:
            print("Unsupported audio format:", audio_type)


# Client code
if __name__ == "__main__":
    audio_player = AudioPlayer()

    audio_player.play("mp3", "song.mp3")  # Output: Playing MP3 file: song.mp3
    audio_player.play("mp4", "video.mp4")  # Output: Playing MP4 file: video.mp4
    audio_player.play("vlc", "video.vlc")  # Output: Playing VLC file: video.vlc
    audio_player.play("avi", "video.avi")  # Output: Unsupported audio format: avi
