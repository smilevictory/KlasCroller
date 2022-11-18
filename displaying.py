from tkinter import *
from tkinter import ttk
import os
import sys
from functools import partial
import tkinter.font
import math
from math import pi
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
matplotlib.rcParams['font.family']='Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] = False

# 상대 경로 -> 절대 경로
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class WindowManager():
    def __init__(self, user_info = {}):
        self.id = ''
        self.pw = ''
        
        self.category = ['의지력', '지능' , '생존력' , '근명성' , '가성비']
        # 유저 정보 ( 의지력 , 지능 , 생존력 , 근명성 , 가성비)
        self.user_info = user_info
        # 전체(완료+현재) 학기 이름 (ex) 2022년 1학기)
        self.seme_list = list(user_info.keys())
        # 전체(완료+현재) 학기 수
        self.cnt_seme = len(user_info)
    
    def __del__(self):
        print()

    # 로그인 용 Window 열기
    def OpenWindow_Login(self):
        # 창 설정
        self.win_lo = Tk()
        self.win_lo.title("Klas Log-in")
        self.win_lo.geometry("400x500")
        font=tkinter.font.Font(family="맑은 고딕 25", size=10, weight="bold")
        
        canvas = Canvas(self.win_lo, width=400, height=500, background='#7C1B0F')
        canvas.pack(padx=0, pady=0)
        canvas.place(x=0, y=0)

        can = Canvas(self.win_lo, width=300, height=85, background='#7C1B0F')
        can.pack(padx=0, pady=0)
        can.place(x=50, y=55)

        file_img1 = resource_path("KlasCroller\\img\\back.png")
        img1 = PhotoImage(file=file_img1)
        canvas.create_image(200, 250, image=img1)

        file_img2 = resource_path("KlasCroller\\img\\campus_logo.png")
        img2 = PhotoImage(file=file_img2)
        can.create_image(157, 45, image=img2)

        # id 입력창
        self.ent1 = Entry(self.win_lo, relief="groove")
        self.ent1.insert(0, "ID : 학번을 입력하세요")
        def clear(event):
            # 좌클릭 했을 때 입력창의 내용 다 지우기
            if self.ent1.get() == "ID : 학번을 입력하세요":
                self.ent1.delete(0, len(self.ent1.get()))
        self.ent1.bind("<Button-1>", clear)
        self.ent1.place(x=50,y=200,width=300,height=35)

        # pw 입력창
        self.ent2 = Entry(self.win_lo)
        self.ent2.config(show="*")
        self.ent2.place(x=50,y=270,width=300,height=35)
        
        btn = Button(self.win_lo, font=font, bg="white", fg="black")
        btn.config(text = "로그인")
        btn.place(x=150,y=350,width=100,height=40)
        btn.config(command=self.EventHandler_Login)
        
        self.win_lo.mainloop()

    def GetIdPw(self):
        self.OpenWindow_Login()
        return self.id,self.pw

    # 로그인 이벤트 핸들러
    def EventHandler_Login(self):
        self.id = self.ent1.get()
        self.pw = self.ent2.get()
        self.win_lo.destroy()
        
    # 메인메뉴 창 열기
    def OpenWindow_MainMenu(self):
        # 창 설정
        win_main = Tk()
        win_main.title("Main Menu")
        win_main.geometry("500x560") # 가로 세로
        win_main.resizable(True, True)
        
        # 폰트들 설정
        font=tkinter.font.Font(family="맑은 고딕 25", size=10, weight="bold")
        font1=tkinter.font.Font(family="휴먼둥근헤드라인", size=30)#, weight="bold")
        font2=tkinter.font.Font(family="휴먼둥근헤드라인", size=17)
        
        can = Canvas(win_main, width=500, height=230,background='red')
        can.pack(padx=0, pady=0)
        can.place(x=0, y=0)
        
        # 바탕 광운대 사진 삽입
        file_back = resource_path("KlasCroller\\img\\back.png")
        back = PhotoImage(file=file_back)
        can.create_image(0,0,image=back)

        # 각 기능 버튼에 해당하는 이미지들
        file_img1 = resource_path("KlasCroller\img\img1.png")
        img1 = PhotoImage(file=file_img1)

        file_img2 = resource_path("KlasCroller\img\img2.png")
        img2 = PhotoImage(file=file_img2)

        file_img3 = resource_path("KlasCroller\img\img3.png")
        img3 = PhotoImage(file=file_img3)

        file_img4 = resource_path("KlasCroller\img\img4.png")
        img4 = PhotoImage(file=file_img4)

        lab1 = Label(win_main)
        lab1.config(text = "기능선택", font=font1, foreground='white', background='#7C1B0F')
        lab1.place(x=25,y=25)

        # 사용자 이름(사용자 이름 크롤링 활용해야해요!)
        lab2 = Label(win_main)
        lab2.config(text = "2020603033" + " " + "한수민" + " " + "님", font=font2, foreground='white', background='#7C1B0F')
        lab2.place(x=25,y=170)

        b1 = Button(win_main, text = "완료 학기\n 분석",font=font, bg="white", fg="black",image=img1, compound="left",command=self.OpenWindow_SelectOne)
        b2 = Button(win_main, text = "학기 간 \n비교 분석", font=font, bg="white", fg="black",image=img2, compound="left")
        b3 = Button(win_main, text = "SF\nMBTI", font=font, bg="white", fg="black",image=img3, compound="left")
        b4 = Button(win_main, text = "취업정보 확인", font=font, bg="white", fg="black",image=img4, compound="left")
        b1.place(x=0,y=220,width=250, height=170)
        b2.place(x=250,y=220,width=250, height=170)
        b3.place(x=0,y=390,width=250, height=170)
        b4.place(x=250,y=390,width=250, height=170);
        win_main.mainloop()
    
    # 학기선택 창 설정
    def OpenWindow_SelectOne(self):
        # 창 설정
        win_select_one = Tk()
        win_select_one.title("학기 선택창")
        win_select_one.geometry("650x400")
        win_select_one.resizable(width = FALSE, height = FALSE)

        # 하위 컴포넌트 선언
        # Button : 1
        # Combobox : 2
        button_select_1 = Button(win_select_one)
        self.combobox_1 = ttk.Combobox(win_select_one)
        
        #비교 학기 선택창에 콤보박스 생성
        self.combobox_1.config(height = 20)
        self.combobox_1.config(value = self.seme_list)
        self.combobox_1.current(0)
        
        button_select_1.config(command = self.OpenWindow_OneSemesterAnalysis)
        
        #출력
        self.combobox_1.pack()
        button_select_1.pack()
        
        win_select_one.mainloop()
    def OpenWindow_OneSemesterAnalysis(self):
        title = self.combobox_1.get()
        data_list = self.user_info[title]
        data_list += data_list[:1]
        
        angles = [n/float(5) * 2 *pi for n in range(5)]
        angles += angles[:1]
        
        fig,ax = plt.subplots(1,1,figsize=(3,5),subplot_kw=dict(polar=True))
        ax.patch.set_facecolor('#7C1B0F')
        fig.patch.set_facecolor('#7C1B0F')
        ax.set_theta_offset(pi / 2) ## 시작점
        ax.set_theta_direction(-1) ## 그려지는 방향 시계방향
        plt.title(title, size=15, color='white')
        
        plt.xticks(angles[:-1],self.category,color='white',size=10)
        ax.tick_params(axis='x', which='major', pad=5)
        plt.yticks([20,40,60,80],['20','40','60','80'],color='white',size=10)
        plt.ylim(0,100)
        ax.set_rlabel_position(100)
        
        ax.plot(angles,data_list,linewidth=3,linestyle='solid',color='#FFFF00')
        ax.fill(angles,data_list,'#FFFF00',alpha=0.5) 
        
        window = Tk()
        window.config(bg='#7C1B0F')
        window.title(str(title)+" 학기 분석")
        window.geometry("650x400")
        window.resizable(width = FALSE, height = FALSE)
        
        canvas = FigureCanvasTkAgg(fig, master=window)
        canvas.get_tk_widget().pack()



    
    # 두번째 기능 선택 이벤트 핸들러
    def OpenWindow_SelectTwo(self):
        # 창 설정
        win_select_two = Tk()
        win_select_two.title("비교 학기 선택창")
        win_select_two.geometry("650x400")
        win_select_two.resizable(width = FALSE, height = FALSE)

        # 하위 컴포넌트 선언
        # Button : 1
        # Combobox : 2
        button_select_two = Button(win_select_two)
        self.combobox_1 = ttk.Combobox(win_select_two)
        self.combobox_2 = ttk.Combobox(win_select_two)
        
        #비교 학기 선택창에 콤보박스 생성
        self.combobox_1.config(height = 20)
        self.combobox_1.config(value = self.seme_list)
        self.combobox_1.current(0)

        self.combobox_2.config(height = 20)
        self.combobox_2.config(value = self.seme_list)
        self.combobox_2.current(0)
        button_select_two.config(command = self.OpenWindow_TwoSemesterCompare)
        
        
        #출력
        self.combobox_1.pack()
        self.combobox_2.pack()
        button_select_two.pack()
        
        win_select_two.mainloop()
        
    def OpenWindow_TwoSemesterCompare(self):
        list_1 = self.user_info[self.combobox_1.get()]
        list_2 = self.user_info[self.combobox_2.get()]
        
        print(list_1)
        print(list_2)
        print()
        
    # 세번째 기능 선택 이벤트 핸들러
    def FuncEventHandler3(self):
        self.win_sem3 = Tk()
        self.win_sem3.title("Klas semester3")
        self.win_sem3.geometry("400x300")
        self.win_sem3.option_add("*Font", "맑은고딕 25")
        idx = len(self.sem_list)-1
        self.label1 = Label(self.win_sem3, text = self.sem_list[idx] + "학기 학점 결과보기")
        self.label1.pack()
        
class SubBoxManager():
    def __init__(self):
        print()
    def __del__(self):
        print()
    def MessageBox(self,string):
        self.win_message = Tk()
        self.win_message.title("Message")
        self.win_message.geometry("384x128")
        self.win_message.option_add("*Font", "맑은고딕 12")
        
        label_message = Label(master=self.win_message)
        button_message = Button(master=self.win_message)
        
        label_message.config(text = string,justify= CENTER, wraplength= 300)
        button_message.config(text="확인",command=self.Check_Ok)
        
        label_message.pack(expand=True, fill="both")
        button_message.pack(side="bottom", anchor="s",pady=10)
        self.win_message.mainloop()
    
    def LoadingBox(self):
        self.win_loading = Tk()
        self.win_loading.title("Loading")
        self.win_loading.geometry("384x128")
        self.win_loading.option_add("*Font", "맑은고딕 12")
        
        Label(self.win_loading,text="Klas에서 정보를 가져오고 있습니다..").pack(fill="both",pady=10)
        Label(self.win_loading,text="( 최대 소요시간: 5분 )").pack(fill="both")
        
        progress = ttk.Progressbar(self.win_loading,orient=HORIZONTAL,length=300,mode='determinate')
        progress.pack(pady=10)
        progress.start(10)
        self.win_loading.mainloop()
        
    def Check_Ok(self):
        self.win_message.destroy()