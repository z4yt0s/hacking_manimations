# hacking_manimations

**hacking_manimations** es un proyecto que contiene el código fuente para crear animaciones educativas y visuales sobre hacking utilizando Manim. Puedes utilizar este repositorio para crear, modificar y compartir tus propias animaciones, ¡siempre que des crédito al autor original!

## Requirements && Installation

To run this proyect, it is recommended to use a Python 3.11+ virtual enviroment.

- **Python 3.11** or higher
- **Manim**

```bash
pip install -r requirements.txt
```

## Rendering Animations

To render an animation with manim in this proyect, you need to run a specific command in the terminal. This command will execute the Manim script and generate the animation.

```bash
python3 -m manim --resolution <custom_resolution> --frame_rate <custom_framerate> <script_in_animation_directory> <mp4_filename>
```

After running this command, Manim will process the scene and create a video file. The rendered video will be stored in a directory (media/) that Manim automatically creates within the project folder.

**Example**
```bash
python3.11 -m manim --resolution 1920x1080 --frame_rate 60 animations/password_spraying.py PasswordSpraying
```
