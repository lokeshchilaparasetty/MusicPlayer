from tkinter import *
from tkinter import filedialog
from pygame import mixer
class MusicPlayer:
    def __init__(self, window):
        self.window = window
        self.window.configure(bg='#fcfcec')
        self.window.geometry("470x150")
        self.window.title('Universal Music Player')
        self.window.resizable(0, 0)

        # Initialize mixer
        mixer.init()

        # Create and place buttons
        self.Load = Button(window, text='Load', width=10, command=self.load, bg='#4b7fa4', fg="#fcfcec", font=("times", 20))
        self.Play = Button(window, text='Play', width=10, command=self.play, bg='#4b7fa4', fg="#fcfcec", font=("times", 20))
        self.Pause = Button(window, text='Pause', width=10, command=self.pause, bg='#4b7fa4', fg="#fcfcec", font=("times", 20))
        self.Stop = Button(window, text='Stop', width=10, command=self.stop, bg='#cb464e', fg="#fcfcec", font=("times", 20))
        self.Close = Button(window, text='Close', width=10, command=self.close, bg='#cb464e', fg="#fcfcec", font=("times", 20))

        self.Load.place(x=10, y=20)
        self.Play.place(x=120, y=20)
        self.Pause.place(x=230, y=20)
        self.Stop.place(x=340, y=20)
        self.Close.place(x=150, y=75)

        self.music_file = None
        self.playing_state = False

    def load(self):
        self.music_file = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3 *.wav")])

    def play(self):
        if self.music_file:
            mixer.music.load(self.music_file)
            mixer.music.play()

    def pause(self):
        if not self.playing_state:
            mixer.music.pause()
            self.playing_state = True
        else:
            mixer.music.unpause()
            self.playing_state = False

    def stop(self):
        mixer.music.stop()
        self.playing_state = False

    def close(self):
        mixer.music.stop()
        self.window.destroy()

root = Tk()
app = MusicPlayer(root)
root.mainloop()
