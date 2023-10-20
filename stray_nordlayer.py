import pystray
from PIL import Image
import subprocess, os, json

title = "Nordlayer"

basedir = os.path.dirname(os.path.abspath(__file__))

def get_id(dict, key):
    with open(dict, 'r') as file:
        data = json.load(file)

    for k, v in data.items():
        if k == key:
            return v

def on_exit(app):
    app.stop()

def disconnect(app):
    cmd = subprocess.run(["nordlayer", "disconnect"])
    if cmd.returncode == 0:
        app.notify("Disconnected", title)
    else:
        app.notify("Failed to try disconnect", title)

def restart(app):
    cmd = subprocess.run([
        "systemctl", "restart", "nordlayer.service",
        "systemctl", "restart", "nordlayer.socket"
    ])
    if cmd.returncode == 0:
        app.notify("Restarted", title)
    else:
        app.notify("Failed to try restart", title)

def status(app):
    cmd = subprocess.run(["nordlayer", "status", "--silent"], stdout=subprocess.PIPE, text=True)
    if cmd.returncode == 0:
        app.notify(cmd.stdout, title)
    else:
        app.notify("Failed to get status", title)

def gateway(app, item):
    id = get_id(basedir + '/ids.json', str(item))
    cmd = subprocess.run(["nordlayer", "connect", str(id)])
    if cmd.returncode == 0:
        app.notify("Connected in " + str(item), title)
    else:
        app.notify("Failed to try connect", title)
        
def main():

    app_menu = [
        pystray.Menu.SEPARATOR,
        pystray.MenuItem(text='Status', action=status),
        pystray.MenuItem(text='Disconnect', action=disconnect),
        pystray.MenuItem(text='Restart', action=restart),
        pystray.Menu.SEPARATOR,
        pystray.MenuItem(text='Exit', action=on_exit)
    ]

    with open(basedir + '/ids.json', 'r') as ids_file:
        ids = json.load(ids_file)

    list_ids = []
    for name, id in ids.items():
        list_ids.append(pystray.MenuItem(text=f"{name}", action=gateway))

    icon = Image.open(basedir + '/ico.png')

    app = pystray.Icon(name="Nordlayer", icon=icon, title="Nordlayer", menu=list_ids + app_menu)

    app.run()

if __name__ == "__main__":
    main()
