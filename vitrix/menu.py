import os
import ursina
import platform
import threading


def buildexec(modulename,dir_path):
    try:
        if modulename == "mp":
            os.system("python " + dir_path + "/multiplayer.py")
        elif modulename =="sp":
            os.system("python " + dir_path + "/singleplayer.py")
        else:
            pass
    except:
        pass # throws error: something wrong with os.system or the path


def start_multiplayer():
    app.destroy()
    if built:
        if platform.system() == "Linux":
            os.system("sh multiplayer.sh")
        if platform.system() == "Windows":
            os.system("multiplayer.bat")
    else:
        buildexec("mp",dir_path)
    os._exit(0)

def start_singleplayer():
    app.destroy()
    if built:
        if platform.system() == "Linux":
            os.system("sh singleplayer.sh")
        if platform.system() == "Windows":
            os.system("singleplayer.bat")
    else:
        buildexec("sp",dir_path)
    os._exit(0)


def playBackgroundMusic():
    global bgmusic
    bgmusic = ursina.Audio("background-music")
    bgmusic.loop = True
    bgmusic.play()


class LoadingWheel(ursina.Entity):
    def __init__(self, **kwargs):
        super().__init__()
        self.parent = ursina.camera.ui
        self.point = ursina.Entity(parent=self, model=ursina.Circle(24, mode='point', thickness=.03), color=ursina.color.light_gray, y=.75, scale=2, texture='circle')
        self.point2 = ursina.Entity(parent=self, model=ursina.Circle(12, mode='point', thickness=.03), color=ursina.color.light_gray, y=.75, scale=1, texture='circle')

        self.scale = .025
        self.text_entity = ursina.Text(world_parent=self, text='loading...', origin=(0,1.5), color=ursina.color.light_gray)
        self.y = -.25

        self.bg = ursina.Entity(parent=self, model='quad', scale_x=ursina.camera.aspect_ratio, color=ursina.color.black, z=1)
        self.bg.scale *= 400

        for key, value in kwargs.items():
            setattr(self, key ,value)


    def update(self):
        self.point.rotation_y += 5
        self.point2.rotation_y += 3


class MenuButton(ursina.Button):
    def __init__(self, text='', **kwargs):
        super().__init__(text, scale=(.25, .075), highlight_color=ursina.color.gray, **kwargs)

        for key, value in kwargs.items():
            setattr(self, key ,value)


def load_menu():
    button_spacing = .075 * 1.25
    menu_parent = ursina.Entity(parent=ursina.camera.ui, y=.15)
    main_menu = ursina.Entity(parent=menu_parent)
    load_menu = ursina.Entity(parent=menu_parent)
    options_menu = ursina.Entity(parent=menu_parent)


    state_handler = ursina.Animator({
        'main_menu' : main_menu,
        'load_menu' : load_menu,
        'options_menu' : options_menu,
        }
    )


    main_menu.buttons = [
        MenuButton('Start', on_click=ursina.Func(setattr, state_handler, 'state', 'load_menu')),
        MenuButton('Options', on_click=ursina.Func(setattr, state_handler, 'state', 'options_menu')),
        MenuButton('Quit', on_click=ursina.Sequence(ursina.Wait(.01), ursina.Func(ursina.sys.exit))),
    ]
    for i, e in enumerate(main_menu.buttons):
        e.parent = main_menu
        e.y = (-i-2) * button_spacing
        e.enabled = False
    

    singleplayer_btn = MenuButton(parent=load_menu, text="Singleplayer", 
                                  on_click=ursina.Func(start_singleplayer), y=(i*button_spacing))
    
    multiplayer_btn = MenuButton(parent=load_menu, text="Multiplayer", 
                                  on_click=ursina.Func(start_multiplayer), y=((i-1)*button_spacing))

    load_menu.back_button = MenuButton(parent=load_menu, text='back', 
                                       y=((-i-2)*button_spacing), 
                                    on_click=ursina.Func(setattr, state_handler, 
                                                  'state', 'main_menu'))


    preview_text = ursina.Text(parent=options_menu, x=.275, y=.25, text='Preview text', 
                       origin=(-.5,0))
    for t in [e for e in ursina.scene.entities if isinstance(e, ursina.Text)]:
        t.original_scale = t.scale

    text_scale_slider = ursina.Slider(0, 2, default=1, step=.1, dynamic=True, text='Text Size:', 
                            parent=options_menu, x=-.25)
    def set_text_scale():
        for t in [e for e in ursina.scene.entities if isinstance(e, ursina.Text) and hasattr(e, 'original_scale')]:
            t.scale = t.original_scale * text_scale_slider.value
    text_scale_slider.on_value_changed = set_text_scale


    # fov_slider = Slider(20, 130, default=80, step=1 , dynamic=True, text='FOV:',)

    # def set_fov():
    #     pass
    # fov_slider.on_value_changed = set_fov

    options_back = MenuButton(parent=options_menu, text='Back', x=-.25, origin_x=-.5, 
                            on_click=ursina.Func(setattr, state_handler, 'state', 'main_menu'))

    for i, e in enumerate((text_scale_slider, options_back)):
        e.y = -i * button_spacing



    for menu in (main_menu, load_menu, options_menu):
        def animate_in_menu(menu=menu):
            for i, e in enumerate(menu.children):
                e.original_x = e.x
                e.x += .1
                e.animate_x(e.original_x, delay=i*.05, duration=.1, 
                            curve=curve.out_quad) # type: ignore

                e.alpha = 0
                e.animate('alpha', .7, delay=i*.05, duration=.1, 
                        curve=curve.out_quad) # type: ignore

                if hasattr(e, 'text_entity'):
                    e.text_entity.alpha = 0
                    e.text_entity.animate('alpha', 1, delay=i*.05, duration=.1)

        menu.on_enable = animate_in_menu


    background = ursina.Entity(model='quad', texture='background', parent=ursina.camera.ui, 
                        scale=(ursina.camera.aspect_ratio), color=ursina.color.white, z=1)


    playBackgroundMusic()
    print('Loaded Menu')
    loading_screen.enabled = False
    for i, e in enumerate(main_menu.buttons):
        e.enabled = True


app = ursina.Ursina()
loading_screen = LoadingWheel(enabled=False)
ursina.window.show_ursina_splash = False
ursina.window.exit_button.visible = False
ursina.window.title = "Vitrix"
ursina.window.borderless = False
default_width = 600  # would be migrated to settings.json
default_height = 600
ursina.window.size = (default_width, default_height)
ursina.window.fullscreen = True

loading_screen.enabled = True
threading.Thread(target=load_menu).start()


dir_path = os.path.dirname(os.path.realpath(__file__))
if os.path.exists(dir_path + "/.unbuilt"):
    built = False
else:
    built = True


if __name__ == "__main__":
    app.run(info=False)