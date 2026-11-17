from manim import *

# Configure vertical 9:16 resolution for YouTube Shorts / TikTok / Reels
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9.0
config.frame_height = 16.0
config.background_color = "#121212"


class RacerStickman(VGroup):
    """Compact stickman racer with optional jetpack thrusters."""
    def __init__(self, color=WHITE, label="", **kwargs):
        super().__init__(**kwargs)
        self.head = Circle(radius=0.26, color=color, stroke_width=5).move_to(UP * 0.85)
        self.body = Line(self.head.get_bottom(), DOWN * 0.15, color=color, stroke_width=5)

        shoulder = self.body.point_from_proportion(0.28)
        hip = self.body.get_end()

        self.left_arm = Line(shoulder, shoulder + LEFT * 0.35 + DOWN * 0.3, color=color, stroke_width=5)
        self.right_arm = Line(shoulder, shoulder + RIGHT * 0.4 + UP * 0.1, color=color, stroke_width=5)
        self.left_leg = Line(hip, hip + LEFT * 0.28 + DOWN * 0.75, color=color, stroke_width=5)
        self.right_leg = Line(hip, hip + RIGHT * 0.32 + DOWN * 0.75, color=color, stroke_width=5)

        # Tag above head
        self.tag = Text(label, font_size=22, color=color, weight=BOLD).next_to(self.head, UP, buff=0.14)

        # NumPy Jetpack + Flame (hidden initially)
        pack = RoundedRectangle(
            corner_radius=0.06, width=0.22, height=0.55,
            fill_color="#A9DC76", fill_opacity=1, stroke_width=0
        ).move_to(shoulder + LEFT * 0.25 + DOWN * 0.15)
        flame = Polygon(
            pack.get_left() + UP * 0.1,
            pack.get_left() + DOWN * 0.1,
            pack.get_left() + LEFT * 0.65,
            fill_color="#FFD866", fill_opacity=1, stroke_width=0
        )
        self.jetpack = VGroup(pack, flame).set_opacity(0)

        self.add(
            self.head, self.body,
            self.left_arm, self.right_arm,
            self.left_leg, self.right_leg,
            self.tag, self.jetpack
        )


class PythonVsCppEp4Short(Scene):
    def construct(self):
        # =========================================================
        # FRAME 0: SERIES BADGE + HOOK + STARTING GRID (Safe-Zone)
        # =========================================================
        ep_pill_bg = RoundedRectangle(
            corner_radius=0.14, width=3.4, height=0.42,
            fill_color="#252526", fill_opacity=1, stroke_color="#FFD866", stroke_width=1.5
        ).move_to(UP * 5.78)
        ep_pill_txt = Text("DEV PAIN • EP. 04", font_size=19, color="#FFD866", weight=BOLD).move_to(ep_pill_bg)
        ep_badge = VGroup(ep_pill_bg, ep_pill_txt)

        meme_card = RoundedRectangle(
            corner_radius=0.18, width=6.6, height=1.08,
            fill_color="#1E1E1E", fill_opacity=1, stroke_color="#78DCE8", stroke_width=3
        ).move_to(UP * 4.72)
        cap_top = Text("Python vs. C++ Speed Race", font_size=23, color="#78DCE8", weight=BOLD)
        if cap_top.width > 6.0:
            cap_top.scale_to_fit_width(6.0)
        cap_bot = Text("Task: Sum 100,000,000 numbers", font_size=18, color=WHITE)
        if cap_bot.width > 6.0:
            cap_bot.scale_to_fit_width(6.0)
        meme_header = VGroup(meme_card, VGroup(cap_top, cap_bot).arrange(DOWN, buff=0.08).move_to(meme_card))

        # Race Tracks (Lane 1: C++, Lane 2: Python) with side safe margins
        start_x = -2.55
        finish_x = 2.55

        lane1_line = Line(LEFT * 3.1 + DOWN * 0.3, RIGHT * 3.1 + DOWN * 0.3, color="#333333", stroke_width=4)
        lane2_line = Line(LEFT * 3.1 + DOWN * 2.8, RIGHT * 3.1 + DOWN * 2.8, color="#333333", stroke_width=4)

        finish_line = DashedLine(UP * 1.3 + RIGHT * finish_x, DOWN * 3.2 + RIGHT * finish_x, color="#A9DC76", stroke_width=4)
        finish_lbl = Text("FINISH", font_size=18, color="#A9DC76", weight=BOLD).next_to(finish_line, UP, buff=0.10)

        cpp_racer = RacerStickman(color="#78DCE8", label="C++").scale(0.82).move_to(RIGHT * start_x + UP * 0.45)
        py_racer = RacerStickman(color="#FFD866", label="Python").scale(0.82).move_to(RIGHT * start_x + DOWN * 2.05)

        tracks = VGroup(lane1_line, lane2_line, finish_line, finish_lbl)

        self.add(ep_badge, meme_header, tracks, cpp_racer, py_racer)
        cpp_racer.save_state()
        py_racer.save_state()

        # =========================================================
        # ACT 1: ROUND 1 — PURE PYTHON FOR-LOOP (0:01 - 0:16)
        # =========================================================
        code_r1 = Text("for i in range(100_000_000): total += i", font="Consolas", font_size=20, color="#FFD866").move_to(UP * 3.55)
        if code_r1.width > 6.4:
            code_r1.scale_to_fit_width(6.4)
        self.play(FadeIn(code_r1, shift=DOWN * 0.2), run_time=0.5)

        # Countdown: GO!
        go_txt = Text("GO!", font_size=40, color="#A9DC76", weight=BOLD).move_to(UP * 2.55)
        self.play(FadeIn(go_txt, scale=0.6), run_time=0.35)
        self.play(FadeOut(go_txt), run_time=0.25)

        # C++ rockets to finish instantly; Python crawls slowly
        cpp_time = Text("0.02s", font="Consolas", font_size=24, color="#78DCE8", weight=BOLD).move_to(UP * 1.25 + RIGHT * 1.65)
        py_slow_time = Text("12.4s (14%...)", font="Consolas", font_size=22, color="#FF6188", weight=BOLD).move_to(DOWN * 1.25 + LEFT * 0.35)

        self.play(
            cpp_racer.animate.move_to(RIGHT * finish_x + UP * 0.45),
            py_racer.animate.move_to(RIGHT * (start_x + 1.1) + DOWN * 2.05),
            run_time=0.9,
            rate_func=rush_from
        )
        self.play(FadeIn(cpp_time, scale=0.8), run_time=0.3)

        # Python struggles and overheats in red
        self.play(
            py_racer.animate.shift(RIGHT * 0.5).set_color("#FF6188"),
            FadeIn(py_slow_time),
            run_time=1.5
        )
        self.wait(1.2)

        # Reset racers to starting line for Round 2
        self.play(
            FadeOut(VGroup(code_r1, cpp_time, py_slow_time)),
            Restore(cpp_racer),
            Restore(py_racer),
            run_time=0.65
        )

        # =========================================================
        # ACT 2: ROUND 2 — PYTHON STRAPS ON NUMPY JETPACK (0:16 - 0:31)
        # =========================================================
        code_r2 = Text("import numpy as np; np.arange(10**8).sum()", font="Consolas", font_size=20, color="#A9DC76", weight=BOLD).move_to(UP * 3.55)
        if code_r2.width > 6.4:
            code_r2.scale_to_fit_width(6.4)
        self.play(FadeIn(code_r2, shift=DOWN * 0.2), run_time=0.55)

        # Equip NumPy jetpack on Python stickman
        equip_txt = Text("+ NumPy C-Backend", font="Consolas", font_size=20, color="#A9DC76", weight=BOLD).next_to(py_racer, DOWN, buff=0.22)
        self.play(
            py_racer.jetpack.animate.set_opacity(1),
            py_racer.animate.set_color("#A9DC76"),
            FadeIn(equip_txt, shift=UP * 0.2),
            run_time=0.6
        )
        self.wait(0.35)
        self.play(FadeOut(equip_txt), run_time=0.2)

        # Python blasts past C++ in 0.01s!
        py_win_time = Text("0.01s (WINNER!)", font="Consolas", font_size=23, color="#A9DC76", weight=BOLD).move_to(DOWN * 1.25 + RIGHT * 1.25)
        cpp_lose_time = Text("0.02s (WAIT WHAT?!)", font="Consolas", font_size=20, color="#78DCE8").move_to(UP * 1.25 + RIGHT * 1.10)

        self.play(
            py_racer.animate.move_to(RIGHT * (finish_x + 0.25) + DOWN * 2.05),
            cpp_racer.animate.move_to(RIGHT * (finish_x - 0.25) + UP * 0.45),
            run_time=0.65,
            rate_func=rush_into
        )
        # Shockwave knocks C++ backward slightly
        self.play(
            cpp_racer.animate.shift(LEFT * 0.4).rotate(0.25),
            FadeIn(py_win_time, scale=0.8),
            FadeIn(cpp_lose_time),
            run_time=0.45
        )
        self.wait(2.0)

        # =========================================================
        # CLEAR SCREEN END CARD: STICKMAN + FOLLOW CTA CENTERED
        # =========================================================
        cta_txt = Text("Follow for Ep. 5", font="Consolas", font_size=26, color="#78DCE8", weight=BOLD)
        cta_box = RoundedRectangle(
            corner_radius=0.22, width=cta_txt.width + 1.1, height=0.80,
            fill_color="#1E1E1E", fill_opacity=0.98, stroke_color="#78DCE8", stroke_width=2.5
        ).move_to(UP * 0.8)
        cta_txt.move_to(cta_box)
        cta_pill = VGroup(cta_box, cta_txt)

        self.play(
            FadeOut(VGroup(code_r2, py_win_time, cpp_lose_time, tracks, cpp_racer, meme_header), shift=UP * 0.3),
            py_racer.animate.move_to(DOWN * 1.2 + LEFT * 0.15),
            FadeIn(cta_pill, scale=0.9),
            run_time=0.45
        )
        self.wait(1.6)

        # =========================================================
        # SEAMLESS LOOP RESET (Matches Frame 0 Identically)
        # =========================================================
        py_racer.jetpack.set_opacity(0)
        self.play(
            FadeOut(cta_pill, scale=0.9),
            FadeIn(meme_header),
            FadeIn(tracks),
            Restore(cpp_racer),
            Restore(py_racer),
            run_time=0.55
        )
        self.wait(0.2)

        self.wait(0.2)