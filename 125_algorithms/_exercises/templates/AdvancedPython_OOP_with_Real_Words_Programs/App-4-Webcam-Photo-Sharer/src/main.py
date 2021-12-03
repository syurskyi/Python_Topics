____ kivy.app _____ App
____ kivy.uix.screenmanager _____ ScreenManager, Screen
____ kivy.lang _____ Builder
____ kivy.core.clipboard _____ Clipboard

_____ time
_____ webbrowser

____ filesharer _____ FileSharer

Builder.load_file('frontend.kv')

c_ CameraScreen(Screen):
    ___ start _
        """Starts camera and changes Button text"""
        ids.camera.opacity = 1
        ids.camera.play = True
        ids.camera_button.text = "Stop Camera"
        ids.camera.texture = ids.camera._camera.texture

    ___ stop _
        """Stops camera and changes Button text"""
        ids.camera.opacity = 0
        ids.camera.play = False
        ids.camera_button.text = "Start Camera"
        ids.camera.texture = None


    ___ capture _
        """Creates a filename with the current time and captures
        and saves a photo image under that filename"""
        current_time = time.strftime('%Y%m%d-%H%M%S')
        filepath = f"files/{current_time}.png"
        ids.camera.export_to_png(filepath)
        manager.current = 'image_screen'
        manager.current_screen.ids.img.source = filepath


c_ ImageScreen(Screen):
    link_message = "Create a Link First"

    ___ create_link _
        """Accesses the photo filepath, uploads it to the web,
        and inserts the link in the Label widget"""
        file_path = App.get_running_app().root.ids.camera_screen.filepath
        filesharer = FileSharer(filepath = file_path)
        url = filesharer.share()
        ids.link.text = url

    ___ copy_link _
        """Copy link to the clipboard available for pasting"""
        try:
            Clipboard.copy(url)
        except:
            ids.link.text = link_message

    ___ open_link _
        """Open link with default browser"""
        try:
            webbrowser.open(url)
        except:
            ids.link.text = link_message



c_ RootWidget(ScreenManager):
    pass

c_ MainApp(App):

    ___ build _
        r_ RootWidget()

MainApp().run()