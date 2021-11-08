from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
import numpy as np

Ma = 28.971
Mh = 4
R = 8.314
M = 5

Screen_helper = """
#: import SlideTransition kivy.uix.screenmanager.SlideTransition

Screen:
    NavigationLayout:
        
        
        
        ScreenManager:
            id:Sc_MG
            Screen:
                name:'login_screen'
                MDCard:
                    size_hint:None,None
                    size:300, 400
                    pos_hint:{'center_x':0.5,'center_y':0.5}
                    orientation:'vertical'
                    MDLabel:
                        id:welcome
                        text:'Test'
                        halign:'center'
                        height:self.texture_size[1]
                    Widget:
                    MDTextField:
                        id:user
                        hint_text:"Username"
                        icon_right:'account'
                        pos_hint:{'center_x':0.5,'center_y':0.5}
                        width:200
                        size_hint_x:None
                    MDTextField:
                        id:user
                        hint_text:"Password"
                        icon_right:'eye-off'
                        pos_hint:{'center_x':0.5,'center_y':0.5}
                        width:200
                        size_hint_x:None
                        password:True
                    
                    MDRoundFlatButton:
                        text: "LOG IN"
                        font_size: 12
                        pos_hint: {"center_x": 0.5,"center_y":0.6}
                        on_press:Sc_MG.current='s1'
                        spacing:0
            
                    MDRoundFlatButton:
                        text: "CLEAR"
                        font_size: 12
                        pos_hint: {"center_x": 0.5,"center_y":1} 
                       
                                    
                    Widget:
                        size_hint_y: None
                        height: 10

            
            
            
            Screen:
                name:'s1'
                BoxLayout:
                    orientation:'vertical'
                    MDToolbar:
                        title: 'Home'
                        left_action_items: [["menu",lambda x:nav_drawer.toggle_nav_drawer()]]
                                    
                        elevation:"10"
                        MDLabel:
                            halign:'center'
                    
                    
                    GridLayout:
                        rows:2
                        
                        
                            
                                
                            
                    Widget:
            Screen:
                name:'s2'
                BoxLayout:
                    orientation:'vertical'
                    MDToolbar:
                        title:'Calculator'
                        left_action_items:[["menu",lambda x:nav_drawer.toggle_nav_drawer()]]
                    Widget:
                MDLabel:
                    text:"FOR CALCULATING STUFFS"
                    halign:'center'
                    pos_hint:{'center_y':0.85}
                    font_size:'20'
                    theme_text_color:"Primary"
                MDTextField:
                    id:Input_1
                    hint_text:'Enter Temperature'
                    pos_hint:{'center_x':0.5,'center_y':0.7}
                    size_hint_x:None
                    width:200
                MDTextField:
                    id:Input_2
                    hint_text:'Enter Pressure'
                    pos_hint:{'center_x':0.5,'center_y':0.6}
                    size_hint_x:None
                    width:200
                MDIconButton:
                    icon: "airballoon"
                    pos_hint: {"center_x": .5, "center_y": .5}
                    on_release:app.calculation()
                    
            Screen:
                name:"s3"
                BoxLayout:
                    orientation:'vertical'
                    MDToolbar:
                        title:"Feed"
                        left_action_items:[["menu",lambda x:nav_drawer.toggle_nav_drawer()]]
                    
                    Widget:  
                        
                    
            Screen:
                name:'s4'
                BoxLayout:
                    orientation:'vertical'
                    
                    MDToolbar:
                        title:'??'
                    GridLayout:
                        MDTextField:
                            text:'asjkjkljl'
                                                
                                
                            
                            
                        
                    
                
        MDNavigationDrawer:
            id:nav_drawer
            BoxLayout:
                orientation:'vertical'
                MDToolbar:
                    title:'About us'
                
                    
                ScrollView:
                    MDList:
                        OneLineListItem:
                            text:"Home"
                            on_release:
                                Sc_MG.transition = SlideTransition(direction="left")
                                Sc_MG.current="s1"
                                nav_drawer.toggle_nav_drawer()
                               
                        OneLineListItem:
                            text:"Calculator"
                            on_release:
                                Sc_MG.transition = SlideTransition(direction="right")
                                Sc_MG.current="s2"
                                nav_drawer.toggle_nav_drawer()

                               
                        OneLineListItem:
                            text:"Feed"
                            on_release:
                                Sc_MG.transition = SlideTransition(direction="right")
                                Sc_MG.current="s3"
                                nav_drawer.toggle_nav_drawer()
                                
                        OneLineListItem:
                            text:'Exp'
                            on_release:
                                Sc_MG.current="s4"
    
               

"""


class HAB(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Red'
        screen = Builder.load_string(Screen_helper)

        return screen

    def calculation(self):
        p = (self.root.ids.Input_1.text)
        t = (self.root.ids.Input_2.text)
        P = float(p)
        T = float(t)
        Ma = 0.028971
        Mh = 0.004
        R = 8.314
        M = 1.455989
        L1 = (M*R*T)
        L2 = P*(Ma-Mh)
        V = (L1/L2)
        print(V)


HAB().run()
