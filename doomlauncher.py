import sys
import gi
import os
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw


class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_default_size(400, 350)
        self.set_title("Linux Doom Launcher")
        self.box1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        self.box2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        self.box3 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        self.box4 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
        self.box5 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        self.set_child(self.box1)
        self.box1.append(self.box2) 
        self.box1.append(self.box3)  
        self.box1.append(self.box4)
        self.box1.append(self.box5)
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

        self.open_button2 = Gtk.Button(label="Open PK3 #3")
        self.box3.append(self.open_button2)
        self.open_dialog2 = Gtk.FileChooserNative.new(title="Choose a PK3/PWAD", 
                                                     parent=self, action=Gtk.FileChooserAction.OPEN)
        
        self.open_dialog2.connect("response", self.open_response2)
        self.open_button2.connect("clicked", self.show_open_dialog2)
        
        self.display = Gtk.Entry()
        self.display.set_placeholder_text("Display ie: 0,1,2")
        self.box3.append(self.display)

        self.display1 = Gtk.Entry()
        self.display1.set_placeholder_text("Width")
        self.box4.append(self.display1)
        
        self.display2 = Gtk.Entry()
        self.display2.set_placeholder_text("Height")
        self.box4.append(self.display2)


        self.button = Gtk.Button(label="Lift Off!")
        self.box5.append(self.button)
        self.button.connect('clicked', self.gzdoom)

    def show_open_dialog(self, button):
        self.open_dialog.show()
    
    def open_response(self, dialog, response):
        if response == Gtk.ResponseType.ACCEPT:
            file = dialog.get_file()
            global pk3
            pk3 = file.get_path()
    
    def show_open_dialog1(self, button):
        self.open_dialog1.show()
    
    def open_response1(self, dialog, response):
        if response == Gtk.ResponseType.ACCEPT:
            file = dialog.get_file()
            global pk32
            pk32 = file.get_path()
    
    def show_open_dialog2(self, button):
        self.open_dialog2.show()
    
    def open_response2(self, dialog, response):
        if response == Gtk.ResponseType.ACCEPT:
            file = dialog.get_file()
            global pk33
            pk33 = file.get_path()

    
    def gzdoom(self, button):
        s = ' '
        f = "-file"
        gzdoom = "gzdoom -file"
        m = self.display.get_text()
        v = "-vid_adapter"
        if 'pk3' in globals():
            if 'pk32' in globals():
                if 'pk33' in globals():
                    os.system(gzdoom + s + pk3 + s + f + s + pk32 + s + f + s + pk33 + s + v + s + m + s +'&')
                    quit()
                else:
                    os.system(gzdoom + s + pk3 + s + f + s + pk32 + s + v + s + m + s + '&')
                    quit()
            else:
                os.system(gzdoom + s + pk3 + s + v + s + m + s + '&')
                quit()
        else:
            os.system('gzdoom' + s + v + s + m + s + '&')
            quit()
        
        

class MyApp(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate', self.on_activate)

    def on_activate(self, app):
        self.win = MainWindow(application=app)
        self.win.present()

app = MyApp(application_id="org.gtk.linuxdoomlauncher")
app.run(sys.argv)