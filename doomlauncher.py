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
        self.set_child(self.box1)
        self.box1.append(self.box2) 
        self.box1.append(self.box3)  
        self.button = Gtk.Button(label="Lift Off!")
        self.box2.append(self.button)
        self.button.connect('clicked', self.gzdoom)
    
    def gzdoom(self, button):
        os.system("gzdoom")

class MyApp(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate', self.on_activate)

    def on_activate(self, app):
        self.win = MainWindow(application=app)
        self.win.present()

app = MyApp(application_id="org.gtk.linuxdoomlauncher")
app.run(sys.argv)