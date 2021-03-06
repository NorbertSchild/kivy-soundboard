from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.core.audio import SoundLoader,Sound
from kivy.uix.togglebutton import ToggleButton

class SoundBoard(Screen):
    playing = []

    # Filename is pushed from the kivy file
    def plays(self, id3):
        nummer=id3
        nummer2="Sounds//"+ nummer
        Asong = SoundLoader.load(nummer2)
        
        #Could be improved by correctly grouping the togglebuttons
        if Asong.state == 'stop':
            for f in SoundBoard.playing:
                f.stop()
            SoundBoard.playing.append(Asong)
            Asong.play()
        elif  Asong.state == 'play':
            SoundBoard.playing.append(Asong)
            for f in SoundBoard.playing:
                f.stop()
            Asong.stop()


buildKV = Builder.load_file("LayOut.kv")
#Added the screenmanager for future imporvements and multiple screen
sm = ScreenManager()
sm.add_widget(SoundBoard(name='soundboard'))

class StartApp(App):

    def build(self):
        return sm

if __name__ == '__main__':
    StartApp().run()
