import pystray
from PIL import Image
import subprocess, os

title = "Nordlayer"

countries = {
    "Portugal": "pt",
    "Spain": "es",
    "France": "fr",
    "United Kingdom": "uk",
    "Ireland": "ie",
    "Italy": "it",
    "Belgium": "be",
    "Switzerland": "ch",
    "Germany": "de",
    "Netherlands": "nl",
    "Austria": "at",
    "Croatia": "hr",
    "Czech Republic": "cz",
    "Slovakia": "sk",
    "Denmark": "dk",
    "Hungary": "hu",
    "Serbia": "rs",
    "Bulgaria": "bg",
    "Norway": "no",
    "Poland": "pl",
    "Romania": "ro",
    "Sweden": "se",
    "Turkey": "tr",
    "Finland": "fi",
    "Israel": "il",
    "Canada": "ca",
    "United States": "us",
    "United Arab Emirates": "ae",
    "Mexico": "mx",
    "Hong Kong": "hk",
    "Japan": "jp",
    "Singapore": "sg",
    "Australia": "au"
}

dir = os.path.dirname(os.path.abspath(__file__))

def get_key_by_value(dict, value):
    for key in dict:
        if dict[key] == value:
            return key
        
def get_value_by_key(dict, key):
    if key in dict:
        return dict[key]

def on_exit(app):
    app.stop()

def disconnect(app):
   subprocess.run(["nordlayer", "disconnect"])
   app.notify("Disconnected", title)


def restart(app):
    subprocess.run([
        "systemctl", "restart", "nordlayer.service",
        "systemctl", "restart", "nordlayer.socket"
    ])
    app.notify("Restarted", title)

def status(app):
    cmd = subprocess.run(["nordlayer", "status", "--silent"], stdout=subprocess.PIPE, text=True)
    if cmd.returncode == 0:
        app.notify(cmd.stdout, title)


def gateway(app, item):
    id = get_value_by_key(countries, str(item))
    cmd = subprocess.run(["nordlayer", "connect", str(id)])
    if cmd.returncode == 0:
        app.notify("Connected in " + str(item), title)
        

def main():

    app_menu = [
        pystray.Menu.SEPARATOR,
        pystray.MenuItem(text='Status', action=status),
        pystray.MenuItem(text='Disconnect', action=disconnect),
        pystray.MenuItem(text='Restart', action=restart),
        pystray.Menu.SEPARATOR,
        pystray.MenuItem(text='Exit', action=on_exit)
    ]

    list_ids = []
    with open(dir + '/ids', 'r') as ids:
        for id in ids:
            list_ids.append(pystray.MenuItem(text=get_key_by_value(countries, id.strip()), action=gateway))

    icon = Image.open(dir + '/ico.png')

    app = pystray.Icon(name="Nordlayer", icon=icon, title="Nordlayer", menu=list_ids + app_menu)

    app.run()

if __name__ == "__main__":
    main()
