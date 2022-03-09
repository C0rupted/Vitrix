from ursina import *
from threading import Thread


app = Ursina()
window.show_ursina_splash = False
window.title = "Vitrix Launcher"
window.borderless = False


class MenuButton(Button):
    def __init__(self, text='', **kwargs):
        super().__init__(text, scale=(.25, .075), highlight_color=color.azure, **kwargs)

        for key, value in kwargs.items():
            setattr(self, key ,value)


button_spacing = .075 * 1.25
menu_parent = Entity(parent=camera.ui, y=.15)
main_menu = Entity(parent=menu_parent)
options_menu = Entity(parent=menu_parent)


state_handler = Animator({
    'main_menu' : main_menu,
    'options_menu' : options_menu,
    }
)


def start_game():
    menu_parent.enabled = False
    app.destroy()
    os.system("python3 game/game.py")


main_menu.buttons = [
    MenuButton('start', on_click=Func(start_game)),
    MenuButton('options', on_click=Func(setattr, state_handler, 'state', 'options_menu')),
    MenuButton('quit', on_click=Sequence(Wait(.01), Func(sys.exit))),
]
for i, e in enumerate(main_menu.buttons):
    e.parent = main_menu
    e.y = (-i-2) * button_spacing


review_text = Text(parent=options_menu, x=.275, y=.25, text='Preview text', origin=(-.5,0))
for t in [e for e in scene.entities if isinstance(e, Text)]:
    t.original_scale = t.scale

text_scale_slider = Slider(0, 2, default=1, step=.1, dynamic=True, text='Text Size:', parent=options_menu, x=-.25)
def set_text_scale():
    for t in [e for e in scene.entities if isinstance(e, Text) and hasattr(e, 'original_scale')]:
        t.scale = t.original_scale * text_scale_slider.value
text_scale_slider.on_value_changed = set_text_scale



volume_slider = Slider(0, 1, default=Audio.volume_multiplier, step=.1, text='Master Volume:', parent=options_menu, x=-.25)
def set_volume_multiplier():
    Audio.volume_multiplier = volume_slider.value
volume_slider.on_value_changed = set_volume_multiplier

options_back = MenuButton(parent=options_menu, text='Back', x=-.25, origin_x=-.5, on_click=Func(setattr, state_handler, 'state', 'main_menu'))

for i, e in enumerate((text_scale_slider, volume_slider, options_back)):
    e.y = -i * button_spacing


for menu in (main_menu, options_menu):
    def animate_in_menu(menu=menu):
        for i, e in enumerate(menu.children):
            e.original_x = e.x
            e.x += .1
            e.animate_x(e.original_x, delay=i*.05, duration=.1, curve=curve.out_quad) # type: ignore

            e.alpha = 0
            e.animate('alpha', .7, delay=i*.05, duration=.1, curve=curve.out_quad) # type: ignore

            if hasattr(e, 'text_entity'):
                e.text_entity.alpha = 0
                e.text_entity.animate('alpha', 1, delay=i*.05, duration=.1)

    menu.on_enable = animate_in_menu


background = Entity(model='quad', texture='shore', parent=camera.ui, scale=(camera.aspect_ratio,1), color=color.white, z=1)


app.run()