import kivy
#kivy.require('1.10.0')
from kivy.app import App
from kivy.uix.button import Label
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup

class FileChooseWidget(GridLayout):

    def selected(GridLayout, filename):
        try:
            self.ids.image.source = filename[0]
        except:
            pass

class FileChooser(Widget):

    def __init__(self, **kwargs):
        super(FileChooser, self).__init__(**kwargs)
        file_choose_btn = Button(text = "Choose a File Manually")
        file_choose_btn.bind(on_press=self._on_button_press)
        self.add_widget(file_choose_btn)

    def _on_button_press(x, y):

        layout = GridLayout(cols = 1, padding = 10)
        layout.add_widget(FileChooseWidget())
        
        label = Label(text = "Drop A File Here")
        layout.add_widget(label)

        closeButton = Button(text = "Done")
        layout.add_widget(closeButton)
        

        popup = Popup(title = "Drag and Drop",
                          content=layout,
                          size_hint=(None, None), size=(400,400)
            )
        popup.open()

        Window.bind(on_drop_file=FileChooser._on_file_drop)

        closeButton.bind(on_press = popup.dismiss)
        #return FileChooseWidget()
    def _on_file_drop(self, file_path, x, y):
        print(file_path)



class Gui(App):

    def build(self):
        layout = BoxLayout()

        chooser_button = FileChooser()

        layout.add_widget(chooser_button)


        return layout
    

def main():
    loadfile = Gui()
    loadfile.run()

if __name__ == "__main__":
    main()
