import kivy
#kivy.require('1.10.0')
import faceload as fc
from kivy.app import App
from kivy.uix.button import Label
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout

class FileChooseWidget(GridLayout):

    def selected(GridLayout, filename):
        try:
            self.ids.image.source = filename[0]
        except:
            pass

class FileChooseButton(Widget):

    def __init__(self, **kwargs):
        super(FileChooseButton, self).__init__(**kwargs)
        file_choose_btn = Button(text = "Choose a File Manually")
        file_choose_btn.bind(on_press=self._on_button_press)
        self.add_widget(file_choose_btn)

    def _on_button_press(x, y):
        return FileChooseWidget()
    

class Gui(App):

    def build(self):
        layout = FloatLayout()
        
        file_choose_btn = FileChooseButton()

        layout.add_widget(file_choose_btn)
        
        #layout.add_widget(Label())

        Window.bind(on_drop_file=self._on_file_drop)


        #Window.bind(on_press=self._button_press)
        
        return layout
        
        #return Label(text = "Drag and Drop File here")
        #return file_choose_btn
    
    def _on_file_drop(self, window, file_path, x, y):
        print(file_path)
        return fc.load_faces(str(file_path)[2:len(str(file_path))-1])


def main():
    loadfile = Gui()
    loadfile.run()

if __name__ == "__main__":
    main()
