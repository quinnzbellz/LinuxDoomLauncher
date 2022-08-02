import sys
import gi
import os
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw


class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_default_size(640, 480)
        self.set_title("Linux Doom Launcher")
        self.box1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.box2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.box3 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.box4 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.box5 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.set_child(self.box1)
        self.box1.append(self.box2) 
        self.box1.append(self.box3)  
        self.open_button = Gtk.Button(label="Open PK3 #1")
        self.box3.append(self.open_button)
        self.open_dialog = Gtk.FileChooserNative.new(title="Choose a PK3/PWAD", 
                                                     parent=self, action=Gtk.FileChooserAction.OPEN)
        
        self.open_dialog.connect("response", self.open_response)
        self.open_button.connect("clicked", self.show_open_dialog)

        self.open_button1 = Gtk.Button(label="Open PK3 #2")
        self.box3.append(self.open_button1)
        self.open_dialog1 = Gtk.FileChooserNative.new(title="Choose a PK3/PWAD", 
                                                     parent=self, action=Gtk.FileChooserAction.OPEN)
        
        self.open_dialog1.connect("response", self.open_response1)
        self.open_button1.connect("clicked", self.show_open_dialog1)


        self.button = Gtk.Button(label="Lift Off!")
        self.box2.append(self.button)
        self.button.connect('clicked', self.gzdoom)

    def show_open_dialog(self, button):
        self.open_dialog.show()
    
    def open_response(self, dialog, response):
        if response == Gtk.ResponseType.ACCEPT:
            file = dialog.get_file()
            global filename
            filename = file.get_path()
    
    def show_open_dialog1(self, button):
        self.open_dialog1.show()
    
    def open_response1(self, dialog, response):
        if response == Gtk.ResponseType.ACCEPT:
            file = dialog.get_file()
            global pk32
            pk32 = file.get_path()

    
    def gzdoom(self, button):
        try: pk32
        except NameError: os.system('gzdoom -file' + ' ' + filename)
        else:
            os.system('gzdoom -file' + ' ' + filename + ' ' + '-file' + ' ' + pk32)

    
class MyApp(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate', self.on_activate)

    def on_activate(self, app):
        self.win = MainWindow(application=app)
        self.win.present()

app = MyApp(application_id="org.gtk.linuxdoomlauncher")
app.run(sys.argv)