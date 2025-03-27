from manim import *

from core.manim_builder import ManimBuilder

class PasswordSpraying(ManimBuilder):
    def construct(self):
        # set background and title
        self.set_background()
        title, underline_title = self.create_title('Password Spraying')
        
        # create main items
        hacker: Text = self.create_text(self.ICONS['hacker'], color='red')
        password: Text = self.create_text(self.ICONS['password'], color='green')
        document: Text = self.create_text(self.ICONS['document'], color='blue')
        server: Text = self.create_text(
            self.ICONS['server'],
            color='purple',
            font_size=135
        )

        hacker.move_to(LEFT * 2.5 + UP * 0.5)
        arrow_password = Arrow(
            start=hacker.get_bottom(),
            end=hacker.get_bottom() + DOWN * 2,
            color=self.COLORS['grey'],
            stroke_width=5
        )
        arrow_users = Arrow(
            start=hacker.get_right(),
            end=hacker.get_right() + RIGHT * 3,
            color=self.COLORS['grey'],
            stroke_width=5
        )
        self.play(FadeIn(hacker))
        self.play(Create(arrow_password), run_time=2)
        password.next_to(arrow_password, DOWN)
        self.play(FadeIn(password))
        self.play(Create(arrow_users), run_time=1.5)
        
        rectangle_users = Rectangle(
            width=2.75,
            height=4,
            color=self.COLORS['grey']
        ).next_to(arrow_users, RIGHT)
        self.play(Create(rectangle_users.shift(DOWN * 0.5)))
        icon_user1, icon_user2, icon_user3 = self.create_text(
            self.ICONS['user'],
            color='blue',
            quantity=3
        )
        text_user1, text_user2, text_user3 = self.create_text(
            text=['jhon', 'emily', 'david'],
            color='blue',
            font_size=30
        )
        user1 = VGroup(icon_user1, text_user1).arrange(RIGHT, buff=0.3)
        user2 = VGroup(icon_user2, text_user2).arrange(RIGHT, buff=0.3)
        user3 = VGroup(icon_user3, text_user3).arrange(RIGHT, buff=0.3)
        users = VGroup(
            user1, user2, user3
        ).arrange(DOWN, aligned_edge=LEFT).move_to(rectangle_users)
        
        users.align_to(rectangle_users.get_left(), LEFT)
        users.shift(RIGHT * 0.2)
        document.next_to(arrow_users.get_right(), RIGHT)
        self.play(Write(users))
        self.play(FadeOut(rectangle_users))
        self.play(Transform(users, document, replace_mobject_with_target_in_scene=True))

        self.play(FadeOut(arrow_users, arrow_password, run_time=0.5))
        future_cord_password = password.get_center() + LEFT * 0.6 + ((0.0, 1.65, 0.0))
        self.play(
            password.animate.move_to(future_cord_password),
            document.animate.next_to(future_cord_password, RIGHT, buff=0.8)
        )
        hacker_group = VGroup(hacker, password, document)
        self.play(hacker_group.animate.move_to(LEFT * 4.5 + DOWN * 1.10))

        server_cord = hacker.get_center() + RIGHT * 4.5
        icon_user4, icon_user5, icon_user6 = self.create_text(
            self.ICONS['user'],
            color='blue',
            quantity=3
        )
        self.play(
            FadeIn(server.move_to(server_cord)),
            FadeIn(icon_user4.next_to(server, RIGHT * 1, buff=3)),
            FadeIn(icon_user5.next_to(icon_user4, UP, buff=0.8)),
            FadeIn(icon_user6.next_to(icon_user4, DOWN, buff=0.8))
        )
        
        text_packet1, text_packet2, text_packet3 = self.create_text(
            ['jhon:P4$$w0rd', 'emily:P4$$w0rd', 'david:P4$$w0rd'],
            color='grey',
            font_size=30
        )
        packet1, packet2, packet3 = self.create_text(
            self.ICONS['packet'],
            color='yellow',
            quantity=3,
            font_size=80
        )
        text_failed1, text_failed2 = self.create_text(
            'failed',
            color='red',
            font_size=30,
            quantity=2
        )
        text_pwned = self.create_text(
            'pwn3d!',
            color='green',
            font_size=30
        )
        packet1.next_to(hacker, RIGHT, buff=0.1)
        packet2.next_to(hacker, RIGHT, buff=0.1)
        packet3.next_to(hacker, RIGHT, buff=0.1)

        self.play(
            Write(text_packet1.next_to(hacker_group, DOWN, buff=0.3)),
            run_time=1.25
        )
        self.wait(0.25)
        self.play(Transform(
            text_packet1, packet1,
            replace_mobject_with_target_in_scene=True,
            run_time=1.25
        ))
        self.play(packet1.animate.move_to(server.get_center()), run_time=1)
        self.play(packet1.animate.move_to(icon_user5.get_left() + LEFT / 2), run_time=1)
        self.play(
            icon_user5.animate.set_color(self.COLORS['red']),
            packet1.animate.scale(0.000000001),
            Write(text_failed1.next_to(icon_user5)),
            run_time=1.25
        )
        self.play(
            FadeOut(packet1),
            Write(text_packet2.next_to(hacker_group, DOWN, buff=0.3)),
            run_time=1.25
        )
        self.wait(0.25)
        self.play(Transform(
            text_packet2, packet2,
            replace_mobject_with_target_in_scene=True,
            run_time=1.25
        ))
        self.play(packet2.animate.move_to(server.get_center()), run_time=1)
        self.play(packet2.animate.move_to(icon_user4.get_left() + LEFT / 2), run_time=1)
        self.play(
            icon_user4.animate.set_color(self.COLORS['red']),
            packet2.animate.scale(0.000000001),
            Write(text_failed2.next_to(icon_user4)),
            run_time=1.25
        )
        self.play(
            FadeOut(packet2),
            Write(text_packet3.next_to(hacker_group, DOWN, buff=0.3))
        )
        self.wait(0.25)
        self.play(Transform(
            text_packet3, packet3,
            replace_mobject_with_target_in_scene=True,
            run_time=1.25
        ))
        self.play(packet3.animate.move_to(server.get_center()), run_time=1)
        self.play(packet3.animate.move_to(icon_user6.get_left() + LEFT / 2), run_time=1)
        self.play(
            icon_user6.animate.set_color(self.COLORS['green']),
            packet3.animate.scale(0.000000001),
            Write(text_pwned.next_to(icon_user6)),
            run_time=1.5
        )
        self.wait(2)
