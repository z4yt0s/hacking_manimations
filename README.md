# hacking_manimations

**hacking_manimations** is a project that contains the source code to create educational and visual animations about hacking using Manim. You can use this repository to create, modify, and share your own animations, as long as you give credit to the original author!

## Requirements && Installation

To run this proyect, it is recommended to use a Python 3.11+ virtual enviroment.

- **0xProtoNerdFonts** for render icons
- **Python 3.11** or higher
- **Manim**

```bash
pip install -r requirements.txt
```

## Rendering Animations

To render an animation with manim in this proyect, you need to run a specific command in the terminal. This command will execute the Manim script and generate the animation.

```bash
python3 -m manim <quality> <script_in_animation_directory>
```

After running this command, Manim will process the scene and create a video file. The rendered video will be stored in a directory (media/) that Manim automatically creates within the project folder.

### Render Quality Options

| Option  | Quality Description        | Resolution  | Frame Rate  |
|---------|----------------------------|-------------|-------------|
| `-ql`   | Low quality                | 854x480     | 15 FPS      |
| `-qm`   | Medium quality             | 1280x720    | 30 FPS      |
| `-qh`   | High quality               | 1920x1080   | 60 FPS      |
| `-qp`   | 2K quality                 | 2560x1440   | 60 FPS      |
| `-qk`   | 4K quality                 | 3840x2160   | 60 FPS      |


### Example
```bash
python3.11 -m manim -qk animations/password_spraying.py
```

## Animations samples

**These animations its rendered in low quality**.

### Password Spraying
<video controls>
    <source src='samples/PasswordSpraying.mp4' type='video/mp4'>
</video>