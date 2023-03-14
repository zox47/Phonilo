from kivy.config import Config
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from kivy.properties import StringProperty, BooleanProperty, ObjectProperty
import threading
from kivy.clock import mainthread, Clock
import pause
from kivymd.uix.list import  ThreeLineAvatarIconListItem
from kivymd.uix.bottomsheet import MDCustomBottomSheet
from kivy.factory import Factory
from kivy.core.window import Window
from kivymd.toast import toast
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.boxlayout import MDBoxLayout
import requests
from kivymd.uix.spinner import MDSpinner
import json
import os
from bs4 import BeautifulSoup
from requests import get
from fake_headers import Headers
import random
from kivy.core.clipboard import Clipboard
from kivmob import KivMob, TestIds
from functools import partial
from kivymd.uix.dialog import MDDialog
from kvdroid.tools.audio import Player
from kivy.config import Config
from kivymd.uix.button import MDFlatButton
from plyer import notification
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.list import OneLineAvatarIconListItem
from kivy.metrics import dp
from kivymd.utils.set_bars_colors import set_bars_colors
from kivy.utils import get_color_from_hex
from kivy.core.window import Window


player = Player()
Config.set('kivy', 'exit_on_escape', '0')
Config.set('kivy','pause_on_minimize', 1)
os.environ["KIVY_AUDIO"] = "ffpyplayer"
#from kivymd.uix.bottomsheet import MDCustomBottomSheet
Window.keyboard_anim_args = {'d': .1, 't': 'in_out_expo'}
Window.softinput_mode = "below_target"

lists = []
listss = []
menu_items = []

KV = '''
#:import get_color_from_hex kivy.utils.get_color_from_hex
#:import NoTransition  kivy.uix.screenmanager.NoTransition 
#:import Clock kivy.clock.Clock
#:import Clipboard kivy.core.clipboard.Clipboard
#:import SlideTransition kivy.uix.screenmanager.SlideTransition


        
<Item>
    IconLeftWidget:
        icon: root.left_icon
        
        

    
        
        
<Content> 
    orientation: "vertical"
    spacing: "0dp"
    size_hint_y: None
#    width_offset: "30sp"
    height: "35dp"
    MDBoxLayout:
        MDLabel:           
            text: "Please Wait 1 min for SMS."
            font_style: "Caption"
            font_size: "15sp"
            
        MDSpinner:
            size_hint: None, None
            size: dp(30), dp(30)
            pos_hint: {'center_x': .5, 'center_y': .5}
           # determinate: True
            color: get_color_from_hex("#14cdc7")
            
<CustomOneLineIconListItems>:

    id: root.id
    text: root.text
   # font_style: "Caption"

    secondary_text: root.second 
    secondary_font_style: "Caption"
    tertiary_font_style: "Caption"
    tertiary_text: root.three
    on_press: 
        app.getphone(root.text,root.three,root.id)
        
   # divider_color: app.theme_cls.bg_dark

    IconLeftWidget:
        id: yup
        icon: root.icon
        
                   

  #  IconRightWidget:
#        id: yup
#        icon: "content-copy"
#        on_press: app.ok(root.id)
#        
<CustomOneLineIconListItem>:

    id: root.id
    text: root.text
   # font_style: "Caption"

    secondary_text: root.second 
    secondary_font_style: "Caption"
    tertiary_font_style: "Caption"
    tertiary_text: root.three
    on_press:    	
    	app.showt(root.text, root.three)
   # divider_color: app.theme_cls.bg_dark

    IconLeftWidget:
        id: yup
        icon: root.icon
                   

    IconRightWidget:
        id: yup
        icon: "content-copy"
        on_press: app.ok(root.id)

ScreenManager:
    transition: SlideTransition()
    Welcome:
    Home:
    History:

<Welcome>:
    name: "welcome"              
    on_enter: 
        app.splits()

    MDFloatLayout:
            
        FitImage:
            source: "/storage/emulated/0/projet/logo.png"
            size_hint: None, None
            size: dp(100), dp(100)
            pos_hint: {'center_x': .5, 'center_y': .76}
    
        MDLabel:
            text: "App #1 To Get free phone number to receive messages"
            halign: "center"
        #    font_style: "Caption"
            pos_hint: {"center_x": .5 ,"center_y": .6} 

            font_size: "17sp"
        
        MDLabel:
            halign: "center"
            text: "Phonelo"
            pos_hint: {"center_x": .5, "center_y": .65} 

            bold: True
            fonr_name: "bb.ttf"
            font_size: "35sp"

    MDSpinner:
        size_hint: None, None
        size: dp(45), dp(45)
        pos_hint: {'center_x': .5, 'center_y': .15}
        determinate: True
        color: get_color_from_hex("#14cdc8")

    MDLabel:
        halign: "center"
        text: "V 1.0"
        font_style: "Caption"
        pos_hint: {"center_x": .5, "center_y": .05} 

        bold: True

        font_size: "17sp"    
        
                                
<History>:
    name: "history"  
    on_enter:
        Clock.schedule_once(root.set_list_md_icons, 0.5)
    
    
        
        
        
                
    #MDIconButton:
#        icon: "chevron-left"
#        pos_hint: {"center_x": .1,  "center_y": .95}         
        
    MDCard:
        
        elevation: 0
        size_hint_y: 1
        radius: [0,0,0,0]

        MDBoxLayout:
            pos_hint: {"center_x": .5,  "center_y": .95}         
            padding: "15dp", "10dp", "10dp", "15dp"
            MDIconButton:
                icon: "chevron-left"
                pos_hint: {"center_x": .1,  "center_y": .5} 
                on_release: root.manager.current = "home"        
            MDLabel:
                text: "Recent Numbers"
                bold: True
                font_size: "20sp"
            MDFloatLayout:
                size_hint: .7, .05
                radius: [20]
                md_bg_color: app.theme_cls.bg_dark
                pos_hint: {"center_x": .1, "center_y": .5}
                                
                TextInput:
                    id: username
                    foreground_color: get_color_from_hex("#ffffff") \
                    if app.theme_cls.theme_style == "Dark" else get_color_from_hex("#000000")
                    size_hint_x: .9
                    on_text: 
                        root.set_list_md_icons(self.text, True)
                    size_hint_y: .7
                    hint_text: "Search"
                    pos_hint: {"center_x": .5, "center_y": .5}
                    background_color: 0,0,0,0
                    cursor_width: "2sp"
                    cursor_color: get_color_from_hex("#ffffff") \
                        if app.theme_cls.theme_style == "Dark" else get_color_from_hex("#000000")

                MDIconButton:
                    icon: "magnify"
                    pos_hint: {"center_x": .9, "center_y": .5}
                       
    FitImage:
        opacity:  "1.0" \
                                    if len(rvs.data) == 0 else "0.01"

        source:  "/storage/emulated/0/projet/empty.png" \
                                    if len(rvs.data) == 0 else "/storage/emulated/0/projet/empty.png"
        size_hint: None,None
        size: dp(100), dp(100)
        pos_hint: {"center_x": .5 ,"center_y": .5}       
        
    MDBoxLayout:
        adaptive_height: True
        size_hint: 1,.9
        pos_hint: {"center_x": .5,  "center_y": .8}                        
        RecycleView:
            id: rvs
            key_viewclass: 'viewclass'
            key_size: 'height'
            pos_hint: {"center_x": .5,  "center_y": .1}         
            RecycleBoxLayout:
                padding: dp(1)
                default_size: None, dp(75)
                default_size_hint: 1, None
                size_hint_y: None
                height: self.minimum_height
                orientation: 'vertical'                            
                           
                
                    
                    
        
    
                   
                                    
                                
    MDIconButton:
        icon: "history" 
        md_bg_color: get_color_from_hex("#161616")
        pos_hint: {"center_x": .5,  "center_y": .1}     
        theme_icon_color: "Custom"
        icon_color: get_color_from_hex("#FFFFFF")            
        icon_size: "30sp"         
        #rounded_button: False
        on_press: 
            root.set_list_md_icons()
            
        
            
                                               
<Home>:
    name: "home"
    on_enter: 
        Clock.schedule_once(app.play, 0.5)
        Clock.schedule_once(app.allnumber, 0.5)
        Clock.schedule_interval(app.play, 60)
        
        
        
        
    
                 
    MDNavigationLayout:

        ScreenManager:
            id: screen_manager

            MDScreen:  
                               
                MDCard:
                    elevation: 0

                    size_hint_y: .4
                    pos_hint: {'top': 1}
                    md_bg_color: get_color_from_hex("#161616")
                                
                MDCard:
                    elevation: 0

                    size_hint: .2, .9

                    pos_hint: {"center_x": .9,  "center_y": .5}
                
                MDCard:
                    id: link
                    links: ""
                    elevation: 0
                    size_hint_y: .35
                    pos_hint: {'top': 1}
                    md_bg_color: get_color_from_hex("#161616")
                    radius: [0,0,100,0]                     

                    RelativeLayout:                 
                        MDIconButton:
                            id: player
                            #icon: "play-outline"        
                            user_font_size: "45sp"      
                            pos_hint: {"center_x": .5, "center_y": .257}
                            theme_text_color: "Custom"
                           # text_color: get_color_from_hex("#eff0f5")
                            line_width: 2
                            line_color: get_color_from_hex("#eff0f5")
                            icon_size: "60sp"
                        FitImage:
                            id: back
                            source: ""
                           

                            radius: [0,0,100,0]                

                            id: progress
                            pos_hint: {"center_x": .5,  "center_y": 1}

                            running_duration: 1
                            catching_duration: 1.5     
                        
                        MDIconButton:
                            id: button
                            icon: "earth-plus"     
                            pos_hint: {"center_x": .9,  "center_y": .1}
                            theme_text_color: "Custom"
                            text_color: get_color_from_hex("#eff0f5")             
                            on_press: 
                            	Clock.schedule_once(app.listcountry, 0.1)
                            	Clock.schedule_once(app.showlistcountry, 0.5)
                            	
                            
                        MDBoxLayout:
                            orientation: "vertical"
                            spacing: 15
                            padding: "10dp"
                            
                                
                            MDIconButton:
                                id: rep
                                icon: "refresh"
                                md_bg_color: get_color_from_hex("#eff0f5")   
                                theme_text_color: "Custom"
                                text_color: get_color_from_hex("#000000")
                                on_press: 
                                    Clock.schedule_once(app.play, 0.5)
                                    Clock.schedule_once(root.set_list_md_icons, 2)

                            MDIconButton:
                                id: rep
                                icon: "delete"
                                md_bg_color: get_color_from_hex("#eff0f5")   
                                theme_text_color: "Custom"
                                text_color: get_color_from_hex("#000000")
                                on_press: 
                                    Clock.schedule_once(app.playss, 0.5)                        
                                    Clock.schedule_once(app.play, 0.8)

                            MDIconButton:
                                icon: "content-copy"    
                                md_bg_color: get_color_from_hex("#eff0f5")   
                                theme_text_color: "Custom"
                                text_color: get_color_from_hex("#000000")
                                
                                on_press: 
                                 #   Clock.schedule_once(partial(copyphone, root.ids.title.text))
                                    app.copyphone(root.ids.title.text)
                                    

                MDBoxLayout:
                    spacing: 5
                    padding: 10
                    orientation: "vertical"
                    pos_hint: {"center_x": .5, "center_y": .95}

                    MDLabel:
                        id: top
                        text: "----"            
                        bold: True
                        font_style: "Caption"
                        font_size: "25sp"
                        halign: "center"
                        theme_text_color: "Custom"
                        text_color: get_color_from_hex("#eff0f5")

                FitImage:
                    id: logos
                    size_hint: None,None
                    size: dp(80), dp(80)

                    source: "us.png"
                    pos_hint: {"center_x": .5, "center_y": .74}

                MDBoxLayout:

                    adaptive_height: True

                    pos_hint: {"center_x": .5, "center_y": .85}

                    Label:
                        id: title

                        size: self.texture_size

                        shorten: True
                        shorten_from: "right"
                        text: "-------"            
                        bold: True
                        font_style: "Caption"
                        font_size: "25sp"
                    #    font_name: f"/storage/emulated/0/projet/bb.ttf"
                        halign: "center"

                        theme_text_color: "Custom"
                        text_color: get_color_from_hex("#eff0f5")    

                MDCard:
                    elevation: 0
                    size_hint_y: .65
                    
                    shadow_softness: 8
                    shadow_offset: (-2, 2)
                    radius: [70,0,0,0]

                    MDBoxLayout:

                        pos_hint: {"center_x": .5,  "center_y": .92}         

                        padding: "15dp", "10dp", "10dp", "15dp"

                        MDLabel:
                            text: "Recent Messages"

                            bold: True
                            font_size: "20sp"

                        MDFloatLayout:
                            size_hint: .7, .08
                            radius: [20]
                            md_bg_color: app.theme_cls.bg_dark
                            pos_hint: {"center_x": .1, "center_y": .5}

                            TextInput:
                                id: username
                                foreground_color: get_color_from_hex("#ffffff") \
                                    if app.theme_cls.theme_style == "Dark" else get_color_from_hex("#000000")

                                size_hint_x: .9
                                on_text: 

                                    root.set_list_md_icons(self.text, True)
                                size_hint_y: .7
                                hint_text: "Search"
                                pos_hint: {"center_x": .5, "center_y": .5}
                                background_color: 0,0,0,0

                                cursor_width: "2sp"
                                cursor_color: get_color_from_hex("#ffffff") \
                                    if app.theme_cls.theme_style == "Dark" else get_color_from_hex("#000000")

                            MDIconButton:
                                icon: "magnify"
                                pos_hint: {"center_x": .9, "center_y": .5}
                                        
                FitImage:
                    id: bok
                    opacity:  "1.0" \
                                    if len(rv.data) == 0 else "0.01"

                    source:  "/storage/emulated/0/projet/empty.png" \
                                    if len(rv.data) == 0 else "/storage/emulated/0/projet/empty.png"
                    size_hint: None,None
                    size: dp(100), dp(100)
                    pos_hint: {"center_x": .5 ,"center_y": .3}   

                MDBoxLayout:

                    adaptive_height: True
                    size_hint: 1,.55
                    pos_hint: {"center_x": .5,  "center_y": .5}                        

                    RecycleView:
                        id: rv
                        effect_cls: "ScrollEffect"
                        scroll_type: ['content']
                        do_scroll_x: False
                		do_scroll_y: True

                        key_viewclass: 'viewclass'
                        key_size: 'height'
                  #      scroll_distance: 200
                        
                        pos_hint: {"center_x": .1,  "center_y": .1}         
                        RecycleBoxLayout:
                            padding: dp(1)
                            default_size: None, dp(75)
                            default_size_hint: 1, None
                            size_hint_y: None
                            height: self.minimum_height
                            orientation: 'vertical'         
                MDIconButton:
                    icon: "history" 
                  #  size_hint: .5, .2
                    md_bg_color: get_color_from_hex("#161616")
         #           line_color: 0, 0, 1, 1
                    pos_hint: {"center_x": .1,  "center_y": .1}     
                    theme_icon_color: "Custom"
                    icon_color: get_color_from_hex("#FFFFFF")            
                    icon_size: "30sp"         
                    rounded_button: True                           
                    on_press: 
                    	root.change()            
                    	app.set_bars_colors("#FFFFFF")
                
'''
mulist =[]
listsallnum= []

class Welcome(Screen):
    pass
#class YourContainer(IRightBodyTouch, MDBoxLayout):
#    adaptive_width = True
    
class Content(MDBoxLayout):
    pass

class CustomOneLineIconListItems(ThreeLineAvatarIconListItem):
    icon = StringProperty()
    second = StringProperty()
    text = StringProperty()
    id = StringProperty()
    three = StringProperty()
    
class CustomOneLineIconListItem(ThreeLineAvatarIconListItem):
    icon = StringProperty()
    second = StringProperty()
    text = StringProperty()
    id = StringProperty()
    three = StringProperty()

    def split(self, pro, title):
        pass

    @mainthread
    def toast(self, on):
        toast(on)
        
class Content(MDBoxLayout):
    pass
    
class History(Screen):
    
        
    #@mainthread
    def set_list_md_icons(self, text="", search=False):
       
        def add_icon_item(country, number, id):
            

            self.ids.rvs.data.append(
                {
                    "viewclass": "CustomOneLineIconListItems",
                    "icon": "/storage/emulated/0/projet/backup.png",
                    "second": "Now",
                    "text": country,
                    "three": str(number),
                    "id": id,

                }
            )

        self.ids.rvs.data = []
        
        for name_icon in listss:

            h= name_icon.split("|", 3)
        #    print (h[1])
     #       print (h[2])

            if search:
                if text in name_icon:
                    add_icon_item(h[0], h[1] , h[2]) 

            else:
                add_icon_item(h[0], h[1] , h[2]) 

                pause.seconds(0.01)
#class Show(Screen):
#    text = StringProperty()
    
class Home(Screen):
    

    @mainthread        
    def ony(self, x):
        self.set_list_md_icons()
        
    def change(self):
        self.manager.current = "history"        
        

    def on_searche(self, text="",  search=False):
        threading.Thread(target=self.set_list_md_icon, args=(text, search)).start()

   # @mainthread        
    def set_list_md_icons(self, text="", search=False):

        def add_icon_item(company, timeago, msgs, new):

            self.ids.rv.data.append(
                {
                    "viewclass": "CustomOneLineIconListItem",
                    "icon": "/storage/emulated/0/projet/check.png",
                    "second": timeago,
                    "text": company,
                    "three": str(msgs),
                    "id": new,

                }
            )

        self.ids.rv.data = []

        for name_icon in lists:

            h= name_icon.split("--", 3)

            if search:
                if text in name_icon:
                    add_icon_item(h[0], h[1] , h[2], h[3]) 

            else:
                add_icon_item(h[0], h[1] , h[2], h[3]) 

                pause.seconds(0.01)
                
class Item(OneLineAvatarIconListItem):
    left_icon = StringProperty()
    right_icon = StringProperty()
    right_text = StringProperty()


class TestNavigationDrawer(MDApp):
    dialog = None
    menu = None
    snackbar = None
    
        
    @mainthread            
    def allnumber(self, dt):
        threading.Thread(target=self.showallnumber).start()
        
        
        
    def showallnumber(self):
        listsallnum.clear()
        headers = Headers(os="win", headers=True).generate()
        lno = "https://www.receivesms.co/active-numbers/"
        
        f = get(lno, headers=headers).content
		
        if len(f) > 100000:
            soup = BeautifulSoup(f, 'html.parser')

            for tr in soup.find_all('tr'):
                data = tr.find_all('td')
                data=[x.text.strip() for x in data]
                for link in tr.find_all('a', href=True):
                    if link['href'] is None:
                        continue
                    indo = str(link['href'])+":"+(data[2])
                   # print(indo)
               	 
                    if "-phone-number/" in indo:
                 	   linkos = indo.partition(":")[0]
                 	   
                 	   #print (linkos)
                 	   if "us" in linkos:
                 	   	tops = "us"
                 	   	country = "United State"
                 	   	flag = "/storage/emulated/0/projet/uss.png:/storage/emulated/0/projet/us.png"
                 	   elif "finnish" in linkos:
                 	   	tops = "fi"
                 	   	country = "firland"
                 	   	flag = "/storage/emulated/0/projet/fis.png:/storage/emulated/0/projet/fi.png"
                 	   elif "fr" in linkos:
                 	   	tops = "fr"
                 	   	country = "France"
                 	   	flag = "/storage/emulated/0/projet/frs.png:/storage/emulated/0/projet/fr.png"
                 	   elif "swedish" in linkos:
                 	   	tops = "sw"
                 	   	country = "Swedish"
                 	   	flag = "/storage/emulated/0/projet/ses.png:/storage/emulated/0/projet/se.png"
                 	   elif "belgium" in linkos:
                 	   	tops = "be"
                 	   	country = "Belgium"
                 	   	flag = "/storage/emulated/0/projet/bes.png:/storage/emulated/0/projet/be.png"
                 	   elif "denmark" in linkos:
                 	   	tops = "dk"
                 	   	country = "Denmark"
                 	   	flag = "/storage/emulated/0/projet/dks.png:/storage/emulated/0/projet/dk.png"
                 	   elif "uk" in linkos:
                 	   	tops = "uk"
                 	   	country = "United Kingdom"
                 	   	flag = "/storage/emulated/0/projet/gbs.png:/storage/emulated/0/projet/gb.png"
                 	   elif "dutch" in linkos:
                 	   	tops = "du"
                 	   	country = "Dutch"
                 	   	flag = "/storage/emulated/0/projet/nls.png:/storage/emulated/0/projet/nl.png"
                 	   numberso = indo.partition(":")[2]
                 	   #vb = flag.partition(":")[0]
                 	   top = "{} - {} Phone Number".format(tops,country)
                 	   som = linkos+":"+numberso+":"+flag+":"+top
                 	   listsallnum.append(som)
        else:
        	Clock.schedule_once(self.allnumber, 1)
		            
        
    @mainthread
    def listcountry(self, dt):
    	threading.Thread(target=self.listcountrys).start()
    	
    def showlistcountry(self, dt):
            
            self.menu = MDDropdownMenu(
	            caller=self.root.get_screen("home").ids.button,
	            items=menu_items,
	            max_height=dp(224),
	            hor_growth="left",
	            
	            elevation=4,
	            opening_time=0,
	            width_mult=5,
        ).open()
        
        		   		   
    def listcountrys(self):
        
        
        for x in listsallnum:
        	
        	hl= x.split(":", 3)
        	hl3 = ("https://www.receivesms.co"+hl[0])
        	menu_items.append({
                "text": hl[1],
                "id": hl3,
               # "right_text": f"+448292929",
                #"right_icon": "",
                "left_icon": hl[2].partition(":")[0],                
                "viewclass": "Item",
                "on_release": lambda x=hl[1], logo=hl[2],ids=hl3,top=hl[3]: self.top(x,logo,ids,top),
                "height": dp(40),})
		      
       
        
        
    def top(self,ok,logo,ids,top):
       logos = top.partition(":")[0]
       print(logos)
       
       top = top.partition(":")[2]
       #logos = top.partition(":")[0]
       
       
      
       self.root.get_screen("home").ids.top.text = str(top)
       self.root.get_screen("home").ids.title.text = str(ok)
       self.root.get_screen("home").ids.logos.source = (logos)
       linkforphone = self.root.get_screen("home").ids.link.links = (ids)
       
       Clock.schedule_once(self.play, 0.5)
       Clock.schedule_once(self.set_list_md_icons, 3)
       
       #his = "{} - {} Phone Number|{}|{}".format(number,links,phoness,linkforphone)
       
    def showt(self, text, second):
       	Clock.schedule_once(partial(self.showts,text,second),0.01)
	   
    def showts(self,text, second, dt):
       self.dialog = MDDialog(
            title=text,
            text=second,
            
        ).open()
          
                
    @mainthread            
    def notify(self,company,msgs):
        #
        player.play("/storage/emulated/0/projet/notify.mp3")
    #    plyer.notification.notify(message="Your code is 71818",timeout=10)
        notification.notify(
            title = company,
            message=msgs,
            app_name="Phonilo",
            app_icon="/storage/emulated/0/projet/logo.png",
            timeout=2
)

      
    def ony(self, dt):
        self.set_list_md_icons()
    #@mainthread            
#    def thony(self, dt):
#        threading.Thread(target=self.ony).start()
            
    #@mainthread        
    def set_list_md_icons(self, text="", search=False):

        def add_icon_item(company, timeago, msgs, new):

            self.root.get_screen("home").ids.rv.data.append(
                {
                    "viewclass": "CustomOneLineIconListItem",
                    "icon": "/storage/emulated/0/projet/check.png",
                    "second": timeago,
                    "text": company,
                    "three": str(msgs),
                    "id": new,

                }
            )

        self.root.get_screen("home").ids.rv.data = []
        
        for name_icon in lists:

            h= name_icon.split("--", 3)

            if search:
                if text in name_icon:
                    add_icon_item(h[0], h[1] , h[2], h[3]) 

            else:
                add_icon_item(h[0], h[1] , h[2], h[3]) 

                #pause.seconds(0.01)
                
    
    def show(self, dt):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Refreshing",
                type="custom",
                content_cls=Content())
        self.dialog.open()
                
    @mainthread            
    def getphone(self, text, number, id):
         jk = text.partition(" -")[0]
         self.root.get_screen("home").ids.top.text = str(text)
         
         
         self.root.get_screen("home").ids.title.text = str(number)
          #  toast("Generate Successful with: "+links+" Number")
        
         self.root.get_screen("home").ids.logos.source = ("/storage/emulated/0/projet/"+jk+".png")
         linkforphone = self.root.get_screen("home").ids.link.links = (id)
         toast("Update To "+ number)
         pause.seconds(1)
         kv.current = "home"
         
    #def ok(self, text):

#        Clipboard.copy(text)
#        toast(text+" Copied!")
        
    def copyphone(self, text):

        Clipboard.copy(text)
        toast(text+" Copied!")
        

    @mainthread            
    def play(self, dt):
        threading.Thread(target=self.music).start()
    #@mainthread            
#    def plays(self, dt):
#        threading.Thread(target=self.musics).start()
    @mainthread            
    def playss(self, dt):
        threading.Thread(target=self.ia).start()        
        
    @mainthread            
    def on_start(self):       
        threading.Thread(target=self.ia).start()
     
                            
    def music(self):
                
        try:
            self.ads.request_interstitial()
            lists.clear()
            Clock.schedule_once(self.show, 2)
            pause.seconds(2)
            
    
            headers = Headers(os="win", headers=True).generate()
            #toast(self.root.get_screen("home").ids.link.links)
            lik = self.root.get_screen("home").ids.link.links
    
            f = requests.get(lik, headers=headers).content
            if len(f) > 100000:
    
                soup = BeautifulSoup(f, 'html.parser')
                
                for link in soup.find_all('div', {"class": "row border-bottom table-hover"}):
                    company = (link.find('div', {"class": "mobile_hide"}).get_text())
                    timeago = (link.find('div', {"class": "col-xs-0 col-md-2 mobile_hide"}).get_text())
                    
                    new = (link.find('div', {"class": "col-xs-12 col-md-8"}).get_text())
    
                    if "ADS" in company or "Google Ads" in company:
                        pass
    
                    else:
                        msg = (link.find('span', {"class": "btn1"}))
                        kek = str(msg)
                        msj = kek.partition("<b>")[2]
                        msgs = msj.partition("</b></span>")[0]
                        text = str(link)
                        textnow = text.partition("</b></span>")[2]
                        textmsg = textnow.partition("</div")[0]                       
              #          print (msgs+ "|" + new)
                       # if ":" in str(msgs):
#                            msgs = msgs.partition(":")[2]
#                        else:
#                            pass
                        
                        lists.append(company+"--"+timeago+"--"+new+"--"+msgs)
                        if "sec ago" in timeago:
                            self.notify(company,msgs)
                                                            
                if len(lists)>0:
                    try: 
                        self.dialog.dismiss()
                        self.root.get_screen("home").ids.rv.refresh_from_data()
                        Clock.schedule_once(self.ony)
                    #    self.ads.show_interstitial()
                    except:
                        pass
                    
                    #aa = Home()
                   # self.ony()
                
                            
            else:
          #      toast("Refreshing Please Wait 1 min for SMS")
                #pause.seconds(5)    
                Clock.schedule_once(self.play, 0.5)
        except:
#              toast("Try Again")
           #   self.dialog.dismiss(force=True)
              pass    
        
    def ia(self):
        self.ads.request_interstitial()
        player.play("/storage/emulated/0/projet/rcli.mp3")
        listsphone = []
        listsphone.clear()

        headers = Headers(os="win", headers=True).generate()
        red = ["finnish:fi","swedish:se","french:fr", "belgium:be", "denmark:dk", "us:us", "uk:gb", "dutch:nl"]
        linkk = random.choice(red)
        links= linkk.partition(":")[0]
        number = linkk.partition(":")[2]
        lno = 'https://www.receivesms.co/{}-phone-numbers/{}/'.format(links,number)
        
        f = get(lno, headers=headers).content

        if len(f) > 100000:
            soup = BeautifulSoup(f, 'html.parser')

            for tr in soup.find_all('tr'):
                data = tr.find_all('td')
                data=[x.text.strip() for x in data]
                for link in tr.find_all('a', href=True):
                    if link['href'] is None or link['href'] == "/{}-phone-numbers/{}/".format(links,number):
                        continue
                    indo = str(link['href'])+":"+(data[2])
                    listsphone.append(indo)
            finumber = random.choice(listsphone)
            if "https://www.receivesms.org/" in str(finumber):

                ok = finumber.partition("https://www.receivesms.org")[2]
                linkos = ok.partition(":")[0]
                phoness =  ok.partition(":")[2]
          #      print (ok)
            else:     
                linkos = finumber.partition(":")[0]
                phoness =  finumber.partition(":")[2]

            self.root.get_screen("home").ids.title.text = str(phoness)
           # toast("Generate Successful with: "+links+" Number")

            self.root.get_screen("home").ids.top.text = str("{} - {} Phone Number".format(number,links))

            self.root.get_screen("home").ids.logos.source = ("/storage/emulated/0/projet/"+number+".png")

            linkforphone = self.root.get_screen("home").ids.link.links = ("https://www.receivesms.co"+linkos)
            #toast(self.root.get_screen("home").ids.link.links)
            his = "{} - {} Phone Number|{}|{}".format(number,links,phoness,linkforphone)
            
            listss.append(his)
            
            
            

        else:
       #     toast("Generate New Number Please Wait •••") 
            self.on_start()
            pause.seconds(2)

    def ok(self, text):  
        #self.ads.request_interstitial()
      #  self.ads.show_interstitial()
        Clipboard.copy(text)
        toast(text+" Copied!")

    def wel(self, ok):
        kv.current = "home"
    
        
    def build(self):
        global kv
        from kivy.core.window import Window
        self.theme_cls.theme_style = "Dark"
        self.set_bars_colors("#161616")
        Window.bind(on_keyboard=self.Android_back_click)

        Clock.schedule_once(self.wel, 5)
      
        self.ads = KivMob("ca-app-pub-3202390806346245~4632644573")
#        self.ads.new_banner("ca-app-pub-3202390806346245/9579944104", False)
#        self.ads.request_banner()
        self.ads.new_interstitial("ca-app-pub-3202390806346245/8099108686")
#        self.ads.request_interstitial()
#        self.ads.show_interstitial()
#        self.ads.show_banner()

        
       # self.theme_cls.material_style = "M3"
        kv = Builder.load_string(KV)

        return kv
    def set_bars_colors(self, color):
        set_bars_colors(
            get_color_from_hex(color),  # status bar color
            get_color_from_hex("#FFFFFF"),
            "Light",                      
        )
                
    def Android_back_click(self,window,key,*largs):
            if key == 27:
                Clock.schedule_once(self.wel)
               
   
    def on_pause(self):
      #  self.ads.request_interstitial()
        return True
    def on_resume(self):
      #  self.ads.request_interstitial()
        pass
    #def on_start(self):
#        return kv

#    #def on_stop(self):
#        return True
#        
#    def on_pause(self):
#        return True
        
#self.profile.dump_stats('myapp.profile')        
TestNavigationDrawer().run()
