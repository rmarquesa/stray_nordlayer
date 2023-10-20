## How to use

1. **IDs**: add your ids in `ids.json` file

2. **Desktop Shortcut**: If you want create a shortcut in your machine

Create a file stray_nordlayer.desktop in `/usr/share/applications` - Replace `your_path` please

```bash
[Desktop Entry]
Version=1.0
Name=Nordlayer System Tray
Comment=Nordlayer System Tray for Linux
Exec=nohup python3 your_path/stray_nordlayer.py > /tmp/stray_nordlayer.log 2>&1 &
Icon=your_path/ico.png
Terminal=false
Type=Application
Categories=Applications;
```

## Python Environment Setup for pystray Code

1. **Python**: Make sure you have Python installed. You can download Python from the [official website](https://www.python.org/downloads/).

2. **Required Python Libraries**:
    - **pystray**: This library is for creating system tray icons and menus. You can install it using `pip`:

      ```bash
      pip install pystray
      ```

    - **PIL (Pillow)**: This library is used for image processing. Install it with:

      ```bash
      pip install Pillow
      ```

3. **Pillow Image Dependencies**: Pillow relies on external libraries for image format support. Install them based on your operating system:
    - **Debian-based Linux**:

      ```bash
      sudo apt-get install libjpeg-dev libfreetype6-dev zlib1g-dev
      ```

    - **macOS** (using Homebrew):

      ```bash
      brew install libjpeg libpng
      ```

4. **System Commands**: The code uses system commands through the `subprocess` library. Ensure that the commands used in your code (`subprocess`) are available in your system.

5. **Images**: Have the images ready for the system tray icon. The code expects an image file. Replace `"path_to_your_image.png"` with the actual image path when running the code.

After setting up the required dependencies and ensuring you have the image file, you can run the provided Python code. Don't forget to replace `"path_to_your_image.png"` with the actual path to your image when executing the code.

# Next steps

1. Create a .deb to build a single package

2. Publish in Ubuntu Store