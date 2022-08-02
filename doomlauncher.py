import gi
import os

gi.require_version("Gtk", "4.0")

from gi.repository import Gtk

def on_activate(app):
    win = Gtk.ApplicationWindow(application=app)
    btn = Gtk.Button(label="Lift Off!")
    btn.connect('clicked', lambda x: os.system("gzdoom"))
    win.set_child(btn)
    win.present()


app = Gtk.Application(application_id='org.gtk.linuxdoomlauncher')
app.connect('activate', on_activate)
app.run(None)