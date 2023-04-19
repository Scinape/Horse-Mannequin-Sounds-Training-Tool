import sys
import time
import pygame
import glob
import os
import sys
os.add_dll_directory(r'C:\Program Files\VideoLAN\VLC')
import vlc
# ---------------------------------------------------------
class Color:
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)


class Text:
    def __init__(self, text: str, text_color: Color, font_type: str, font_size: int):
        """
        text: 文本内容，注意是字符串形式
        text_color: 字体颜色，如Color.WHITE、COLOR.BLACK
        font_type: 字体文件(.ttc)，如'msyh.ttc'，注意是字符串形式
        font_size: 字体大小，如20、10
        """
        self.text = text
        self.text_color = text_color
        self.font_type = font_type
        self.font_size = font_size

        font = pygame.font.Font(os.path.join('font', (self.font_type)), self.font_size)
        self.text_image = font.render(self.text, True, self.text_color).convert_alpha()

        self.text_width = self.text_image.get_width()
        self.text_height = self.text_image.get_height()

    def draw(self, surface: pygame.Surface, center_x, center_y):
        """
        surface: 文本放置的表面
        center_x, center_y: 文本放置在表面的<中心坐标>
        """
        upperleft_x = center_x - self.text_width / 2
        upperleft_y = center_y - self.text_height / 2
        surface.blit(self.text_image, (upperleft_x, upperleft_y))


class Image:
    def __init__(self, img_name: str, ratio=0.4):
        """
        img_name: 图片文件名，如'background.jpg'、'ink.png',注意为字符串
        ratio: 图片缩放比例，与主屏幕相适应，默认值为0.4
        """
        self.img_name = img_name
        self.ratio = ratio

        self.image_1080x1920 = pygame.image.load(os.path.join('image', self.img_name)).convert_alpha()
        self.img_width = self.image_1080x1920.get_width()
        self.img_height = self.image_1080x1920.get_height()

        self.size_scaled = self.img_width * self.ratio, self.img_height * self.ratio

        self.image_scaled = pygame.transform.smoothscale(self.image_1080x1920, self.size_scaled)
        self.img_width_scaled = self.image_scaled.get_width()
        self.img_height_scaled = self.image_scaled.get_height()

    def draw(self, surface: pygame.Surface, center_x, center_y):
        """
        surface: 图片放置的表面
        center_x, center_y: 图片放置在表面的<中心坐标>
        """
        upperleft_x = center_x - self.img_width_scaled / 2
        upperleft_y = center_y - self.img_height_scaled / 2
        surface.blit(self.image_scaled, (upperleft_x, upperleft_y))


class ColorSurface:
    def __init__(self, color, width, height):
        self.color = color
        self.width = width
        self.height = height

        self.color_image = pygame.Surface((self.width, self.height)).convert_alpha()
        self.color_image.fill(self.color)

    def draw(self, surface: pygame.Surface, center_x, center_y):
        upperleft_x = center_x - self.width / 2
        upperleft_y = center_y - self.height / 2
        surface.blit(self.color_image, (upperleft_x, upperleft_y))


class ButtonText(Text):
    def __init__(self, text: str, text_color: Color, font_type: str, font_size: int):
        super().__init__(text, text_color, font_type, font_size)
        self.rect = self.text_image.get_rect()

    def draw(self, surface: pygame.Surface, center_x, center_y):
        super().draw(surface, center_x, center_y)
        self.rect.center = center_x, center_y

    def handle_event(self, command, *args):
        self.hovered = self.rect.collidepoint(pygame.mouse.get_pos())
        if self.hovered:
            command(*args)


class ButtonImage(Image):
    def __init__(self, img_name: str, ratio=0.4):
        super().__init__(img_name, ratio)
        self.rect = self.image_scaled.get_rect()

    def draw(self, surface: pygame.Surface, center_x, center_y):
        super().draw(surface, center_x, center_y)
        self.rect.center = center_x, center_y

    def handle_event(self, command, *args):
        self.hovered = self.rect.collidepoint(pygame.mouse.get_pos())
        if self.hovered:
            command(*args)


class ButtonColorSurface(ColorSurface):
    def __init__(self, color, width, height):
        super().__init__(color, width, height)
        self.rect = self.color_image.get_rect()

    def draw(self, surface: pygame.Surface, center_x, center_y):
        super().draw(surface, center_x, center_y)
        self.rect.center = center_x, center_y

    def handle_event(self, command, *args):
        self.hovered = self.rect.collidepoint(pygame.mouse.get_pos())
        if self.hovered:
            command(*args)


class InterFace():

    def __init__(self):  # 初始化
        pygame.init()

    def quit(self):  # 退出程序的函数（未来替换为关机）
        pygame.quit()
        sys.exit()

    def stop(self):
        p1.stop()
        p2.stop()
        p3.stop()
        p4.stop()



    def initialize(self, set):

        global p1, p2, p3, p4, horsenum

        if set == 1:
            print(set)
            horsenum = 1
            p1 = vlc.MediaPlayer("horse1\heart-L-R.mp3")
            p2 = vlc.MediaPlayer("horse1\lung-L-R.mp3")
            p3 = vlc.MediaPlayer("horse1\stomach-UL-UR.mp3")
            p4 = vlc.MediaPlayer("horse1\stomach-LL-LR.mp3")
            
        if set == 2:
            print(set)
            horsenum = 2
            p1 = vlc.MediaPlayer("horse2\heart-L-R.mp3")
            p2 = vlc.MediaPlayer("horse2\lung-L-R.mp3")
            p3 = vlc.MediaPlayer("horse2\stomach-UL-UR.mp3")
            p4 = vlc.MediaPlayer("horse2\stomach-LL-LR.mp3")
            
        if set == 3:
            print(set)
            horsenum = 3
            p1 = vlc.MediaPlayer("horse3\heart-L-R.mp3")
            p2 = vlc.MediaPlayer("horse3\lung-L-R.mp3")
            p3 = vlc.MediaPlayer("horse3\stomach-UL-UR.mp3")
            p4 = vlc.MediaPlayer("horse3\stomach-LL-LR.mp3")
            
        if set == 4:
            print(set)
            horsenum = 4
            p1 = vlc.MediaPlayer("horse4\heart-L-R.mp3")
            p2 = vlc.MediaPlayer("horse4\lung-L-R.mp3")
            p3 = vlc.MediaPlayer("horse4\stomach-UL-UR.mp3")
            p4 = vlc.MediaPlayer("horse4\stomach-LL-LR.mp3")
            
        if set == 5:
            print(set)
            horsenum = 5
            p1 = vlc.MediaPlayer("horse5\heart-L-R.mp3")
            p2 = vlc.MediaPlayer("horse5\lung-L-R.mp3")
            p3 = vlc.MediaPlayer("horse5\stomach-UL-UR.mp3")
            p4 = vlc.MediaPlayer("horse5\stomach-LL-LR.mp3")
            
        if set == 6:
            print(set)
            horsenum = 6
            p1 = vlc.MediaPlayer("horse6\heart-L-R.mp3")
            p2 = vlc.MediaPlayer("horse6\lung-L-R.mp3")
            p3 = vlc.MediaPlayer("horse6\stomach-UL-UR.mp3")
            p4 = vlc.MediaPlayer("horse6\stomach-LL-LR.mp3")
            
        if set == 7:
            print(set)
            horsenum = 7
            p1 = vlc.MediaPlayer("horse7\heart-L-R.mp3")
            p2 = vlc.MediaPlayer("horse7\lung-L-R.mp3")
            p3 = vlc.MediaPlayer("horse7\stomach-UL-UR.mp3")
            p4 = vlc.MediaPlayer("horse7\stomach-LL-LR.mp3")
            
        if set == 8:
            print(set)
            horsenum = 8
            p1 = vlc.MediaPlayer("horse8\heart-L-R.mp3")
            p2 = vlc.MediaPlayer("horse8\lung-L-R.mp3")
            p3 = vlc.MediaPlayer("horse8\stomach-UL-UR.mp3")
            p4 = vlc.MediaPlayer("horse8\stomach-LL-LR.mp3")
            
        if set == 9:
            print(set)
            horsenum = 9
            p1 = vlc.MediaPlayer("horse9\heart-L-R.mp3")
            p2 = vlc.MediaPlayer("horse9\lung-L-R.mp3")
            p3 = vlc.MediaPlayer("horse9\stomach-UL-UR.mp3")
            p4 = vlc.MediaPlayer("horse9\stomach-LL-LR.mp3")
            
        if set == 10:
            print(set)
            horsenum = 10
            p1 = vlc.MediaPlayer("horse10\heart-L-R.mp3")
            p2 = vlc.MediaPlayer("horse10\lung-L-R.mp3")
            p3 = vlc.MediaPlayer("horse10\stomach-UL-UR.mp3")
            p4 = vlc.MediaPlayer("horse10\stomach-LL-LR.mp3")
            
        if set == 11:
            print(set)
            horsenum = 11
            p1 = vlc.MediaPlayer("horse11\heart-L-R.mp3")
            p2 = vlc.MediaPlayer("horse11\lung-L-R.mp3")
            p3 = vlc.MediaPlayer("horse11\stomach-UL-UR.mp3")
            p4 = vlc.MediaPlayer("horse11\stomach-LL-LR.mp3")
            
        if set == 12:
            print(set)
            horsenum = 12
            p1 = vlc.MediaPlayer("horse12\heart-L-R.mp3")
            p2 = vlc.MediaPlayer("horse12\lung-L-R.mp3")
            p3 = vlc.MediaPlayer("horse12\stomach-UL-UR.mp3")
            p4 = vlc.MediaPlayer("horse12\stomach-LL-LR.mp3")



    def basic_background(self):
        """
        <基本背景><basic_background>\n
        返回值为背景尺寸和背景表面
        """
        # 设置logo和界面标题
        # game_icon = pygame.image.load(os.path.join('image', 'horse_icon.jpg'))
        game_caption = 'Auscultation Training'
        # pygame.display.set_icon(game_icon)
        pygame.display.set_caption(game_caption)

        # 设置开始界面
        show_ratio = 1
        size = width, height = 1920 * show_ratio, 1080 * show_ratio
        screen = pygame.display.set_mode(size)

        # 设置背景贴图
        Image('background.png').draw(screen, width / 2, height / 2)

        return size, screen

    def start_interface(self):
        """
        <开始界面><start_interface>
        """
        # 设置<基本背景>
        size, screen = self.basic_background()
        width, height = size

        Image('mainpage2.png', ratio=1).draw(screen, width * 0.5, height * 0.5)
        Image('debug.png', ratio=1).draw(screen, width * 0.2, height * 0.79)
        Text('Welcome to Auscultation Training!', Color.BLACK, 'msyh.ttc', 40).draw(screen, width / 2, height * 1 / 3.3)
        Text('Interface Version: 0.8b', Color.BLACK, 'msyh.ttc', 20).draw(screen, width * 0.82, height * 0.85)
        button_start = ButtonText('                     ', Color.WHITE, 'msyh.ttc', 80)  # 开始按钮
        button_start.draw(screen, width / 2, height * 2 / 3.25)
        button_quit = ButtonText('                                               ', Color.WHITE, 'msyh.ttc', 35)  # 关闭
        button_quit.draw(screen, width / 2, height * 2 / 2.55)
        button_modify = ButtonText('Modify', Color.BLACK, 'msyh.ttc', 35)
        button_modify.draw(screen, width * 0.2, height * 0.79)
        clock = pygame.time.Clock()
        # 设置<开始界面>文字和贴图

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # ！此处为界面切换的关键，即进入另一死循环
                if event.type == pygame.FINGERDOWN:
                    button_start.handle_event(self.choose_interface)
                if event.type == pygame.FINGERDOWN:
                    button_modify.handle_event(self.modify_interface)
                if event.type == pygame.FINGERDOWN:
                    button_quit.handle_event(self.quit)

            pygame.display.update()

    def modify_interface(self):

        size, screen = self.basic_background()
        width, height = size

        Image('modify.png', ratio=0.8).draw(screen, width * 0.5, height * 0.5)
        button_back = ButtonText('  ', Color.BLACK, 'msyh.ttc', 130)  # 开始按钮
        button_back.draw(screen, width * 0.135, height * 0.17)
        button_qr = ButtonText('                                            ', Color.BLACK, 'msyh.ttc', 160)  # 开始按钮
        button_qr.draw(screen, width * 0.5, height * 0.5)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # ！此处为界面切换的关键，即进入另一死循环
                if event.type == pygame.FINGERDOWN:
                    button_back.handle_event(self.start_interface)
                if event.type == pygame.FINGERDOWN:
                    button_qr.handle_event(self.panel_interface)

            pygame.display.update()

    def panel_interface(self):

        size, screen = self.basic_background()
        width, height = size

        Image('panel page.png', ratio=0.8).draw(screen, width * 0.5, height * 0.5)
        button_back = ButtonText('  ', Color.BLACK, 'msyh.ttc', 130)  # 开始按钮
        button_back.draw(screen, width * 0.135, height * 0.17)
        Image('control panel.png', ratio=0.4).draw(screen, width * 0.5, height * 0.5)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # ！此处为界面切换的关键，即进入另一死循环
                if event.type == pygame.FINGERDOWN:
                    button_back.handle_event(self.modify_interface)

            pygame.display.update()

    def choose_interface(self):
        """
        <选择界面><choose_interface>
        """
        # 设置基本背景
        size, screen = self.basic_background()
        width, height = size

        # 定义各种按钮
        choose1 = ButtonText('    Horse#1', Color.BLACK, 'msyh.ttc', 35)
        choose2 = ButtonText('    Horse#2', Color.BLACK, 'msyh.ttc', 35)
        choose3 = ButtonText('    Horse#3', Color.BLACK, 'msyh.ttc', 35)
        choose4 = ButtonText('    Horse#4', Color.BLACK, 'msyh.ttc', 35)
        choose5 = ButtonText('    Horse#5', Color.BLACK, 'msyh.ttc', 35)
        choose6 = ButtonText('    Horse#6', Color.BLACK, 'msyh.ttc', 35)
        choose7 = ButtonText('    Horse#7', Color.BLACK, 'msyh.ttc', 35)
        choose8 = ButtonText('    Horse#8', Color.BLACK, 'msyh.ttc', 35)
        choose9 = ButtonText('    Horse#9', Color.BLACK, 'msyh.ttc', 35)
        choose10 = ButtonText('    Horse#10', Color.BLACK, 'msyh.ttc', 35)
        choose11 = ButtonText('    Horse#11', Color.BLACK, 'msyh.ttc', 35)
        choose12 = ButtonText('    Horse#12', Color.BLACK, 'msyh.ttc', 35)
        button_back = ButtonText('          ', Color.BLACK, 'msyh.ttc', 80)

        Image('choose1.png', ratio=0.8).draw(screen, width * 0.5, height * 0.5)
        button_back.draw(screen, width * 0.2, height * 0.8)

        Image('choosebutton.png', ratio=0.25).draw(screen, width * 0.4, height * 0.25)
        choose1.draw(screen, width * 0.4, height * 0.25)

        Image('choosebutton.png', ratio=0.25).draw(screen, width * 0.6, height * 0.25)
        choose2.draw(screen, width * 0.6, height * 0.25)

        Image('choosebutton.png', ratio=0.25).draw(screen, width * 0.8, height * 0.25)
        choose3.draw(screen, width * 0.8, height * 0.25)

        Image('choosebutton.png', ratio=0.25).draw(screen, width * 0.4, height * 0.35)
        choose4.draw(screen, width * 0.4, height * 0.35)

        Image('choosebutton.png', ratio=0.25).draw(screen, width * 0.6, height * 0.35)
        choose5.draw(screen, width * 0.6, height * 0.35)

        Image('choosebutton.png', ratio=0.25).draw(screen, width * 0.8, height * 0.35)
        choose6.draw(screen, width * 0.8, height * 0.35)

        Image('choosebutton.png', ratio=0.25).draw(screen, width * 0.4, height * 0.45)
        choose7.draw(screen, width * 0.4, height * 0.45)

        Image('choosebutton.png', ratio=0.25).draw(screen, width * 0.6, height * 0.45)
        choose8.draw(screen, width * 0.6, height * 0.45)

        Image('choosebutton.png', ratio=0.25).draw(screen, width * 0.8, height * 0.45)
        choose9.draw(screen, width * 0.8, height * 0.45)

        Image('choosebutton.png', ratio=0.25).draw(screen, width * 0.4, height * 0.55)
        choose10.draw(screen, width * 0.4, height * 0.55)

        Image('choosebutton.png', ratio=0.25).draw(screen, width * 0.6, height * 0.55)
        choose11.draw(screen, width * 0.6, height * 0.55)

        Image('choosebutton.png', ratio=0.25).draw(screen, width * 0.8, height * 0.55)
        choose12.draw(screen, width * 0.8, height * 0.55)
        clock = pygame.time.Clock
        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # ！此处为界面切换的关键，即进入另一死循环
                if event.type == pygame.FINGERDOWN:
                    button_back.handle_event(self.start_interface)
                if event.type == pygame.FINGERDOWN:
                    choose1.handle_event(self.initialize, 1)
                    choose1.handle_event(self.play_interface)
                if event.type == pygame.FINGERDOWN:
                    choose2.handle_event(self.initialize, 2)
                    choose2.handle_event(self.play_interface)
                if event.type == pygame.FINGERDOWN:
                    choose3.handle_event(self.initialize, 3)
                    choose3.handle_event(self.play_interface)
                if event.type == pygame.FINGERDOWN:
                    choose4.handle_event(self.initialize, 4)
                    choose4.handle_event(self.play_interface)
                if event.type == pygame.FINGERDOWN:
                    choose5.handle_event(self.initialize, 5)
                    choose5.handle_event(self.play_interface)
                if event.type == pygame.FINGERDOWN:
                    choose6.handle_event(self.initialize, 6)
                    choose6.handle_event(self.play_interface)
                if event.type == pygame.FINGERDOWN:
                    choose7.handle_event(self.initialize, 7)
                    choose7.handle_event(self.play_interface)
                if event.type == pygame.FINGERDOWN:
                    choose8.handle_event(self.initialize, 8)
                    choose8.handle_event(self.play_interface)
                if event.type == pygame.FINGERDOWN:
                    choose9.handle_event(self.initialize, 9)
                    choose9.handle_event(self.play_interface)
                if event.type == pygame.FINGERDOWN:
                    choose10.handle_event(self.initialize, 10)
                    choose10.handle_event(self.play_interface)
                if event.type == pygame.FINGERDOWN:
                    choose11.handle_event(self.initialize, 11)
                    choose11.handle_event(self.play_interface)
                if event.type == pygame.FINGERDOWN:
                    choose12.handle_event(self.initialize, 12)
                    choose12.handle_event(self.play_interface)

            pygame.display.update()


    def play_interface(self):

        device1 = p1.audio_output_device_enum()
        device = device1
        device2 = device1.contents.next
        device3 = device2.contents.next
        device4 = device3.contents.next
        device5 = device4.contents.next

        print("playing on...")
        dev_list = [device1, device2, device3, device4, device5]
        for i in range(len(dev_list)):
            print("Device " + str(i) + " :")
            print(dev_list[i].contents.device)
            print(dev_list[i].contents.description)

            p1.audio_output_device_set(None, b'alsa_output.usb - C - Media_Electronics_Inc._USB_Audio_Device - 00.analog - stereo.1')
            p2.audio_output_device_set(None, b'alsa_output.usb - C - Media_Electronics_Inc._USB_Audio_Device - 00.analog - stereo.2')
            p3.audio_output_device_set(None, b'alsa_output.usb - C - Media_Electronics_Inc._USB_Audio_Device - 00.analog - stereo.3')


        p1.play()
        p2.play()
        p3.play()
        # 播放器界面
        size, screen = self.basic_background()
        width, height = size
        fps = 20
        clock = pygame.time.Clock()
        volume_heart = 60
        volume_lung = 60
        volume_abdomen = 60
        p1.audio_set_volume(volume_heart)
        p2.audio_set_volume(volume_lung)
        p3.audio_set_volume(volume_abdomen)

        Image('play.png', ratio=0.195).draw(screen, width * 0.5, height * 0.5)
        Image('detail.png', ratio=0.84).draw(screen, width * 0.725, height * 0.41)

        back_button = pygame.image.load("image/backbutton.png")
        back_button = pygame.transform.scale(back_button, (140, 140))
        screen.blit(back_button, (width * 0.12, height * 0.14))
        back = ButtonText('    ', Color.BLACK, 'msyh.ttc', 160)
        back.draw(screen, width * 0.12, height * 0.14)

        pause_button = pygame.image.load("image/pausebutton.png")
        pause_button = pygame.transform.scale(pause_button, (120, 120))
        screen.blit(pause_button, (width * 0.45, height * 0.72))

        play_button = pygame.image.load("image/playbutton.png")
        play_button = pygame.transform.scale(play_button, (120, 120))


        stop = pygame.image.load("image/stopbutton.png")
        stop = pygame.transform.scale(stop, (120, 120))
        screen.blit(stop, (width * 0.55, height * 0.72))

        forward_button = pygame.image.load("image/forward.png")
        forward_button = pygame.transform.scale(forward_button, (120, 120))
        screen.blit(forward_button, (width * 0.75, height * 0.72))

        backwards_button = pygame.image.load("image/backward.png")
        backwards_button = pygame.transform.scale(backwards_button, (120, 120))
        screen.blit(backwards_button, (width * 0.65, height * 0.72))

        volup_button = pygame.image.load("image/volup.png")
        volup_button = pygame.transform.scale(volup_button, (60, 60))
        screen.blit(volup_button, (width * 0.38, height * 0.75))

        voldown_button = pygame.image.load("image/voldown.png")
        voldown_button = pygame.transform.scale(voldown_button, (60, 60))
        screen.blit(voldown_button, (width * 0.28, height * 0.75))

        sound = pygame.image.load("image/sound.png")
        sound = pygame.transform.scale(sound, (90, 90))
        screen.blit(sound, (width * 0.2, height * 0.73))
        #---
        heart_down = pygame.image.load("image/voldown.png")
        heart_down = pygame.transform.scale(heart_down, (60, 60))
        screen.blit(heart_down, (width * 0.64, height * 0.3))
        Text('Heart:' + str(volume_heart), Color.BLACK, 'msyh.ttc', 25).draw(screen, width * 0.73, height * 0.32)
        heart_up = pygame.image.load("image/volup.png")
        heart_up = pygame.transform.scale(heart_up, (60, 60))
        screen.blit(heart_up, (width * 0.78, height * 0.3))
        # ---
        lung_down = pygame.image.load("image/voldown.png")
        lung_down = pygame.transform.scale(lung_down, (60, 60))
        screen.blit(lung_down, (width * 0.64, height * 0.45))
        Text('Lung' + str(volume_lung), Color.BLACK, 'msyh.ttc', 25).draw(screen, width * 0.73, height * 0.47)
        lung_up = pygame.image.load("image/volup.png")
        lung_up = pygame.transform.scale(lung_up, (60, 60))
        screen.blit(lung_up, (width * 0.78, height * 0.45))
        #---
        abdomen_down = pygame.image.load("image/voldown.png")
        abdomen_down = pygame.transform.scale(abdomen_down, (60, 60))
        screen.blit(abdomen_down, (width * 0.64, height * 0.6))
        Text('Abdomen' + str(volume_abdomen), Color.BLACK, 'msyh.ttc', 25).draw(screen, width * 0.73, height * 0.62)
        abdomen_up = pygame.image.load("image/volup.png")
        abdomen_up = pygame.transform.scale(abdomen_up, (60, 60))
        screen.blit(abdomen_up, (width * 0.78, height * 0.6))
        #---
        default = pygame.image.load("image/default.png")
        default = pygame.transform.scale(default, (320,140))
        screen.blit(default, (width * 0.64, height * 0.18))
        Text('Default', Color.BLACK, 'msyh.ttc', 30).draw(screen, width * 0.725, height * 0.245)

        Text('Partial Volume', Color.BLACK, 'msyh.ttc', 30).draw(screen, width * 0.725, height * 0.18)
        show = pygame.image.load("image/show.png")
        show = pygame.transform.scale(show, (600, 120))
        screen.blit(show, (width * 0.3, height * 0.14))

        Text('Now simulating: Horse#'+ str(horsenum), Color.BLACK, 'msyh.ttc', 30).draw(screen, width * 0.45, height * 0.2)
        Image('scan.png', ratio=0.3).draw(screen, width * 0.45, height * 0.48)
        '''
        pause_button = ButtonImage('pausebutton.png', ratio=0.8)
        pause_button.draw(screen, width * 0.5, height * 0.85)
        stop_button = ButtonImage('stopbutton.png', ratio=0.8)
        stop_button.draw(screen, width * 0.6, height * 0.85)
        forward_button = ButtonImage('forward.png', ratio=0.8)
        forward_button.draw(screen, width * 0.8, height * 0.85)
        backward_button = ButtonImage('backward.png', ratio=0.8)
        backward_button.draw(screen, width * 0.7, height * 0.85)
        volup_button = ButtonImage('volup.png', ratio=0.8)
        volup_button.draw(screen, width * 0.4, height * 0.85)
        voldown_button = ButtonImage('voldown.png', ratio=0.8)
        voldown_button.draw(screen, width * 0.25, height * 0.85)
        sound = ButtonImage('sound.png', ratio=0.5)
        sound.draw(screen, width * 0.13, height * 0.85)
        # mute = ButtonImage('mute.png', ratio=0.5)
        '''
        while True:
            clock.tick(fps)
            progress = p1.get_time()

            volshow = pygame.image.load("image/volshow.png")
            volshow = pygame.transform.scale(volshow, (90, 60))
            screen.blit(volshow, (width * 0.323, height * 0.75))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.FINGERUP:
                    x, y = pygame.mouse.get.pos()
                    print(pygame.mouse.get.pos())
                    '''暂停和播放'''
                    if (width * 0.45 < x < width * 0.45 + 120) & (height * 0.72 < y < height * 0.78 + 68):
                        print('clicked on pause/play')
                        check = p1.is_playing()
                        if check == 1:
                            p1.pause()
                            p2.pause()
                            p3.pause()
                            screen.blit(play_button, (width * 0.45, height * 0.72))
                        elif check == 0:
                            p1.play()
                            p2.play()
                            p3.play()
                            screen.blit(pause_button, (width * 0.45, height * 0.72))

                    '''停止'''
                    if (width * 0.55 < x < width * 0.55 + 120) & (height * 0.72 < y < height * 0.78 + 68):
                        print('clicked on STOP')
                        p1.stop()
                        p2.stop()
                        p3.stop()

                    '''回退4秒'''
                    if (width * 0.65 < x < width * 0.65 + 120) & (height * 0.72 < y < height * 0.78 + 68):
                        print('clicked on backwards')
                        p1.set_time(progress - 4000)
                        p2.set_time(progress - 4000)
                        p3.set_time(progress - 4000)

                    '''快进4秒'''
                    if (width * 0.755 < x < width * 0.75 + 120) & (height * 0.72 < y < height * 0.78 + 68):
                        print('clicked on forward')
                        p1.set_time(progress + 4000)
                        p2.set_time(progress + 4000)
                        p3.set_time(progress + 4000)

                    '''音量+'''
                    if (width * 0.38 < x < width * 0.38 + 60) & (height * 0.73 < y < height * 0.81 + 40):
                        print('clicked on volup')
                        volume_heart = p1.audio_get_volume()
                        volume_heart = volume_heart + 20
                        if volume_heart > 100:
                            volume_heart = 100

                        volume_lung = p2.audio_get_volume()
                        volume_lung = volume_lung + 20
                        if volume_lung > 100:
                            volume_lung = 100

                        volume_abdomen = p3.audio_get_volume()
                        volume_abdomen = volume_abdomen + 20
                        if volume_abdomen > 100:
                            volume_abdomen = 100

                        p1.audio_set_volume(volume_heart)
                        p2.audio_set_volume(volume_lung)
                        p3.audio_set_volume(volume_abdomen)

                    '''音量-'''
                    if (width * 0.28 < x < width * 0.28 + 60) & (height * 0.73 < y < height * 0.81 + 40):
                        print('clicked on voldown')
                        volume_heart = p1.audio_get_volume()
                        volume_heart = volume_heart - 20
                        if volume_heart < 0:
                            volume_heart = 0

                        volume_lung = p2.audio_get_volume()
                        volume_lung = volume_lung - 20
                        if volume_lung < 0:
                            volume_lung = 0

                        volume_abdomen = p3.audio_get_volume()
                        volume_abdomen = volume_abdomen - 20
                        if volume_abdomen < 00:
                            volume_abdomen = 0

                        p1.audio_set_volume(volume_heart)
                        p2.audio_set_volume(volume_lung)
                        p3.audio_set_volume(volume_abdomen)

                    if (width * 0.64 < x < width * 0.64 + 60) & (height * 0.3 < y < height * 0.3 + 60):
                        print('clicked on heart down')
                        volume_heart = p1.audio_get_volume()
                        volume_heart = volume_heart - 20
                        if volume_heart < 0:
                            volume_heart = 0
                        p1.audio_set_volume(volume_heart)

                    if (width * 0.78 < x < width * 0.78 + 60) & (height * 0.3 < y < height * 0.3 + 60):
                        print('clicked on heart up')
                        volume_heart = p1.audio_get_volume()
                        volume_heart = volume_heart + 20
                        if volume_heart < 0:
                            volume_heart = 0
                        p1.audio_set_volume(volume_heart)
                    
                    if (width * 0.64 < x < width * 0.64 + 60) & (height * 0.45 < y < height * 0.45 + 60):
                        print('clicked on lung down')
                        volume_lung = p2.audio_get_volume()
                        volume_lung = volume_lung - 20
                        if volume_lung < 0:
                            volume_lung = 0
                        p2.audio_set_volume(volume_lung)
                        
                    if (width * 0.78 < x < width * 0.78 + 60) & (height * 0.45 < y < height * 0.45 + 60):
                        print('clicked on lung up')
                        volume_lung = p2.audio_get_volume()
                        volume_lung = volume_lung + 20
                        if volume_lung < 0:
                            volume_lung = 0
                        p2.audio_set_volume(volume_lung)
                        
                    if (width * 0.64 < x < width * 0.64 + 60) & (height * 0.6 < y < height * 0.6 + 60):
                        print('clicked on abdomen down')
                        volume_abdomen = p3.audio_get_volume()
                        volume_abdomen = volume_abdomen - 20
                        if volume_abdomen < 0:
                            volume_abdomen = 0
                        p3.audio_set_volume(volume_abdomen)

                    if (width * 0.78 < x < width * 0.78 + 60) & (height * 0.6 < y < height * 0.6 + 60):
                        print('clicked on abdomen up')
                        volume_abdomen = p3.audio_get_volume()
                        volume_abdomen = volume_abdomen + 20
                        if volume_abdomen < 0:
                            volume_abdomen = 0
                        p3.audio_set_volume(volume_abdomen)

                    if (width * 0.64 < x < width * 0.64 + 320) & (height * 0.18 < y < height * 0.18 + 140):
                        print('clicked on default')
                        volume_heart = 60
                        volume_lung = 60
                        volume_abdomen = 60
                        p1.audio_set_volume(volume_heart)
                        p2.audio_set_volume(volume_lung)
                        p3.audio_set_volume(volume_abdomen)

                if event.type == pygame.FINGERDOWN:
                    back.handle_event(self.stop)
                    back.handle_event(self.choose_interface)

            pygame.display.update()


if __name__ == '__main__':
    scene = InterFace()
    # 开始时选定start_interface
    scene.start_interface()
