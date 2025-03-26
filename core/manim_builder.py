from typing import Tuple, List, Union

from manim import *

class ManimBuilder(Scene):
    DEF_FONT: str = '0xProto Nerd Font Mono'
    ICONS = {
        'hacker': '',
        'user': '',
        'password': '󰟵',
        'document': '󰧮',
        'server': '',
        'packet': '',
        'packet_open': ''
    }
    COLORS = {
        'background': '0x1a1b26',
        'foreground': '0xa9b1d6',
        'green': '#00b44e',
        'blue': '#0063e2',
        'purple': '#7f00df',
        'pink': '#ba1d67',
        'red': '#bc2920',
        'orange': '#cd620e',
        'yellow': '#cac20d',
        'grey': '#505050',
        'dark_green': '#227547',
        'dark_blue': '#2b5893',
        'dark_purple': '#542d98',
        'dark_pink': '#792f57',
        'dark_red': '#712823',
        'dark_orange': '#8a5429',
        'dark_yellow': '#858125',
    }

    def set_background(
        self,
        opacity: Tuple[float, float]=(0.3, 0.4),
        background_color: str=COLORS['background'],
        border_color: str=COLORS['foreground']
    ) -> None:
        background = FullScreenRectangle()
        background.set_fill(background_color, opacity=opacity[0])
        background.set_stroke(border_color, width=6, opacity=opacity[1])
        self.add(background)

    def create_title(
        self,
        title: str,
        font: str=DEF_FONT,
        font_size: int=45,
        color: str=COLORS['pink']
    ) -> Tuple[Text, Line]:
        """
        Creates an animated title with an underline effect.

        This method generates a `Text` object as a title, animates its appearance 
        and movement, and then creates an underline (`Line`) beneath it. 
        The animation sequence includes:
        - Fading in the title.
        - Moving the title upwards.
        - Creating an underline below the title.

        Args:
            title (str): The title text to be displayed.
            font (str, optional): The font used for the title. Defaults to `DEF_FONT`.
            font_size (int, optional): The font size of the title. Defaults to 45.
            color (str, optional): The color of both the title and the underline. 
                Defaults to `COLORS['pink']`.

        Returns:
            Tuple[Text, Line]: A tuple containing:
                - The `Text` object representing the title.
                - The `Line` object representing the underline.

        Example:
            >>> obj = MyClass()
            >>> title_text, underline = obj.create_title("Welcome")
            >>> print(title_text.text, underline.color)
            'Welcome' 'pink'
        """
        animated_title = Text(
            title,
            font=font,
            font_size=font_size,
            color=color
        )
        self.add(animated_title)
        self.play(FadeIn(animated_title))
        self.play(animated_title.animate.move_to(UP * 3.25), run_time=1.5)
        underline_title = Line(
            start=animated_title.get_left() + DOWN * 0.4,
            end=animated_title.get_right() + DOWN * 0.4,
            color=color,
            stroke_width=5
        )
        self.play(Create(underline_title, run_time=1.5))
        return (animated_title, underline_title)

    def create_text(
        self,
        text: str,      #Union[str, List[str]],
        color: str,
        quantity: int=1,
        font: str=DEF_FONT,
        font_size: int=100,
    ) -> Text:#Union[Text, Tuple[Text, ...]]:
        """
        Creates one or multiple `Text` elements.

        This method allows generating `Text` objects in three different ways:
    
        1. If a single `str` is provided and `quantity == 1`, it returns a
        single `Text` object.

        2. If a single `str` is provided and `quantity > 1`, it returns a tuple
        of `Text` objects with identical content.

        3. If a `List[str]` is provided, it creates a `Text` object for each
        string in the list and returns them as a tuple.

        Args:
            text (Union[str, List[str]]): 
                - A `str` to create one or multiple identical `Text` elements.
                - A `List[str]` to create a `Text` object for each element in the list.
            color (str): The color of the text.
            quantity (int, optional): 
                - The number of `Text` objects to create if `text` is a `str`. Defaults to 1.
                - Ignored if `text` is a `List[str]`.
            font (str, optional): The font used for the text. Defaults to `DEF_FONT`.
            font_size (int, optional): The font size of the text. Defaults to 100.

        Returns:
            Union[Text, Tuple[Text, ...]]: 
                - A single `Text` object if `quantity == 1` and `text` is a `str`.
                - A tuple of `Text` objects if multiple are created.

        Example:
            >>> obj = MyClass()

            ## Create a single text object
            >>> text1 = obj.create_text("Hello", "red")
            >>> print(text1.text, text1.color)
            'Hello' 'red'

            ## Create multiple identical text objects
            >>> text_multiple = obj.create_text("Hello", "blue", quantity=3)
            >>> print(len(text_multiple))
            3

            ## Create multiple text objects from a list of different texts
            >>> text_list = obj.create_text(["Hi", "Welcome", "Goodbye"], "green")
            >>> print(len(text_list))
            3
            >>> print(text_list[0].text, text_list[1].text, text_list[2].text)
            'Hi' 'Welcome' 'Goodbye'
        """
        # Case 1: Single Text, single quantity
        if isinstance(text, str) and quantity == 1:
            return Text(text=text, font=font, font_size=font_size, color=self.COLORS[color])

        # Case 2: List of texts (create one Text object per item)
        if isinstance(text, list):
            text_list: List[Text] = [
                Text(text=texts, font=font, font_size=font_size, color=self.COLORS[color])
                for texts in text
            ]
            return tuple(text_list)

        # Case 3: Single text, multiple quantity
        text_list: List[Text] = [
            Text(text=text, font=font, font_size=font_size, color=self.COLORS[color])
            for _ in range(quantity)
        ]
        return tuple(text_list)
