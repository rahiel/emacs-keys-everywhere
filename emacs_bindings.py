# emacs-keys-everywhere - Enable Emacs key bindings on the desktop
# Copyright (C) 2017  Rahiel Kasim
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
import argparse
import subprocess
from configparser import ConfigParser
from os import makedirs
from os.path import exists, expanduser
try:
    from subprocess import run
except ImportError:             # Python < 3.5
    from subprocess import call as run

__version__ = "0.2"


def enable_gtk3():
    gtk3_dir = expanduser("~/.config/gtk-3.0/")
    gtk3 = gtk3_dir + "settings.ini"
    makedirs(gtk3_dir, exist_ok=True)
    config = ConfigParser()
    config.read(gtk3)
    if "Settings" not in config:
        config["Settings"] = {}
    config["Settings"]["gtk-key-theme-name"] = "Emacs"
    with open(gtk3, "w") as f:
        config.write(f)

def enable_gtk2():
    gtk2 = expanduser("~/.gtkrc-2.0")
    if exists(gtk2):
        with open(gtk2) as f:
            conf = f.read()
    else:
        conf = ""

    setting = 'gtk-key-theme-name = "Emacs"\n'
    if setting not in conf:
        if conf and conf[-1] != "\n":
            setting = "\n" + setting
        with open(gtk2, "w") as f:
            f.write(conf + setting)

def run_anyway(*args, **kwargs):
    try:
        run(*args, **kwargs, stderr=subprocess.DEVNULL)
    except FileNotFoundError:
        pass

def main():
    parser = argparse.ArgumentParser(description="Enable Emacs style key bindings for all GTK+ programs.",
                                     epilog="Homepage: https://github.com/rahiel/emacs-keys-everywhere")
    parser.add_argument("--version", action="version", version="%(prog)s {}".format(__version__))
    args = parser.parse_args()

    run_anyway("xfconf-query -c xsettings -p /Gtk/KeyThemeName -s Emacs".split())
    run_anyway('gsettings set org.gnome.desktop.interface gtk-key-theme "Emacs"'.split())
    run_anyway('gsettings set org.cinnamon.desktop.interface gtk-key-theme "Emacs"'.split())
    run_anyway("gconftool-2 --type=string --set /desktop/gnome/interface/gtk_key_theme Emacs".split())
    run_anyway("mateconftool-2 -s /desktop/mate/interface/gtk_key_theme -t string Emacs".split())
    enable_gtk3()
    enable_gtk2()


if __name__ == "__main__":
    main()
