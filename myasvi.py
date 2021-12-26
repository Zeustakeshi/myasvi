
import audioop
from os import name, scandir
import os
from typing import Text
import speech_recognition as sr
from random import randint
import pyttsx3
import datetime
from time import strftime
import time
import webbrowser as wb
import wikipedia

engine =pyttsx3.init()
language = 'vi'
# chuyển text qua giọng nói 
def speak(Ai_brain):
    voi= engine.getProperty('voices')
    engine.setProperty('voice', voi[1].id)
    engine.say(Ai_brain)
    engine.runAndWait()
 # chuyển nói thành text 
def Ai_ear(): 
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Bạn: ", end='')
        audio = r.listen(source, phrase_time_limit=3)

        try:
            text = r.recognize_google(audio, language="vi-VN")
            print(text)
            
        except sr.UnknownValueError:
            print("...")
            speak('Tôi chưa hiểu ý bạn. bạn có thể vui lòng nói lại. tôi sẽ nghe kĩ hơn')
            print("Bạn: ", end='')
            audio = r.listen(source, phrase_time_limit=3)
            try:
                text = r.recognize_google(audio, language="vi-VN")
                print(text)
            except sr.UnknownValueError:
                print("...")
                speak('Tôi vẫn chưa hiểu ý bạn. vui lòng nhập vào phần ghi chú')  
                print('Ai: bạn muốn tôi làm gì?')
                speak (' yêu cầu của bạn là')  
                text= str(input('Yêu cầu của bạn là: '))
        return text    
    return text 


# ngày giờ                 
def time():
    now = datetime.datetime.now()
    hour= datetime.datetime.now().hour
    if "giờ" in text or "time" in text:
        speak('Bây giờ là %d giờ %d phút ' % (now.hour, now.minute))
        if 6<= hour<=10: speak("Bạn đã ăn sáng chưa")
        elif 11<= hour<=14: speak('Tôi nghĩ cũng trễ rồi,Bạn thấy đói chưa đi ăn thôi')
        elif 18<= hour<=20: speak('Đã đến giờ ăn tối rồi đấy. Bạn đã ăn tối chưa')
        elif 22<= hour<=24: speak('Cũng khuya rồi đấy,tôi nghĩ bạn nên ngủ sớm đi. công việc mai làm cũng được mà phải không?')

    elif "ngày" in text or "day" in text:
        speak("Hôm nay là ngày %d tháng %d năm %d .và Hôm nay tôi cảm thấy rất vui,chúc bạn có một ngày vui vẻ" %
              (now.day, now.month, now.year))
def remind(name):
    hour= datetime.datetime.now().hour   
    if 6<= hour<=10: speak("Bạn đã ăn sáng chưa {}".format(name))
    elif 11<= hour<=14: speak('Bạn đã ăn trưa chưa{}'.format(name))  
    elif 18<= hour<=20: speak('Bạn đã ăn tối chưa{}'.format(name)) 
    elif 22<= hour<=24: speak('tôi nghĩ bạn nên ngủ sớm đi {}. công việc mai làm cũng được mà'.format(name))  
# hàm xin chào    
def welcome():
    print("""╔══════════════════════╗
║╔════════════════════╗╚╗
║║██░░░░░░░░░░░░░░░░░░╚╗╚╗
║║██░░░░░Battery Low ░░░░░ ─║║║
║║██░░░░░░░░░░░░░░░░░░╔╝╔╝
║╚════════════════════╝╔╝
╚══════════════════════╝
            """)
    speak('xin chào. tôi có thể gọi  bạn bằng gì?')
    print("""╲╲╲╲╲┏━━━┓╱╱╱╱╱
╲┏━━━┻━━━┻━━━┓╱
╲┃╭━╮┏━━━┓╭━╮┃╱
╱┃┃╳┃┣◯━◯┫┃╳┃┃╲
╱┃╰━╯┣━━━┫╰━╯┃╲
╱┃┈▊▊▊▊┈▂▃▅▇┈┃╲
╱┗━━━━━━━━━━━┛╲""")
    print('[0__0]: Tôi có thể gọi bạn là gì ?')
    name =Ai_ear().lower()
    hour= datetime.datetime.now().hour
    if 6<=hour<12:
     speak("chào buổi sáng .Chúc bạn một ngày thành công nha {} ".format(name))
     remind(name)
    elif 12<=hour <18 : 
        speak('chào buổi trưa . chúc bạn có một bữa trưa vui vẻ nha {}'.format(name))
        remind(name)
    elif 18<= hour < 24: 
        speak('chào buổi tối {}'.format(name))
        remind(name)
    speak('tôi có thể giúp gì cho bạn ')  
   # tra trên wiki: 
def tell_me_about():
    try:
        speak("có vẻ như bạn đang muốn biết thứ gì đó.Nói lại thêm lần nữa tôi sẽ nói cho bẹn biết")
        text = Ai_ear().lower()
        wikipedia.set_lang("vi")
        contents = wikipedia.summary(text).split('\n')
        print(contents[0])
        speak(contents[0])
        for content in contents[1:]:
            speak("Bạn muốn nghe thêm không")
            ans = Ai_ear().lower()
            if "có" not in ans:
                break    
            print(content)
            speak(content)

        speak('Cảm ơn bạn đã lắng nghe!!!')
    except:
        speak("tôi chưa định nghĩa được thuật ngữ của bạn. Xin mời bạn nói lại")    
if __name__== "__main__":
    welcome()
    while True:
        text = Ai_ear().lower()
        print(text)
        time()
        if 'ok google' in text:
            print("""                      [0__0] 
                    <=I___I=>
                      1   1
            ohhhh.NO !!!!!!!!!!! 
             i am not google assistant 
             you can call me is MINH HIẾU assistant
             """)
            speak("""ôi không.
            tôi không phải trợ lí ảo của google.
            bạn có thể gọi tôi là trợ lí ảo của MINH Hiếu""")
#tìm kiếm trên google
        elif 'google' in text or 'tìm kiếm'in text:
            speak('ok. bạn muốn tôi tìm gì trên google')
            search=Ai_ear().lower()
            url= f"https://www.google.com/search?q={search}"
            wb.get().open(url)
            speak(f'kết quả tìm kiếm {search} của bạn trên google')
#tìm kiếm trên youtube            
        elif 'youtube' in text:
            speak('tôi có thể tìm gì trên du túp giúp bạn')
            search=Ai_ear().lower()
            url= f"https://www.youtube.com/search?q={search}"
            wb.get().open(url)
            speak(f'kết quả tìm kiếm {search} của bạn trên du túp')
#mở zalo            
        elif 'zalo' in text:
            speak('ok. tôi sẽ mở da lô trên web cho bạn') 
            url= f"https://chat.zalo.me/?null" 
            wb.get().open(url)
#mở facebook            
        elif 'facebook' in text:
            speak(' ok. tôi sẽ mở phây búc trên quép cho bạn') 
            url= f"https://www.facebook.com/"   
            wb.get().open(url)    
#mở trang chủ DHTDM            
        elif 'thời khóa biểu' in text or 'lịch thi'in text or'timetable' in text:
            speak('tôi sẽ mở trang chủ của trường cho bạn') 
            url= f"https://dkmh.tdmu.edu.vn/Default.aspx?page=thoikhoabieu"   
            wb.get().open(url)  
#mở web xem thời gian             
              
#kết thúc chương trình                
        elif "turn off" in text or 'tắt' in text or 'see you again' in text or 'goodbye'in text or 'off'in text or 'bye' in text:
            speak('Tạm biệt bạn. rất vui được giúp đỡ bạn') 
            quit()     
#mở ảnh QR            
        elif 'info' in text :
            speak('ok.tôi sẽ mở mã qui rờ cho bạn')
            QR=r"C:\Users\Admin\Downloads\myqr.png"
            os.startfile(QR)
#trả lời tên            
        elif 'what\'s your name' in text or 'name' in text or 'bạn tên gì' in text :
            speak('Tôi chưa được MInh Hiếu đặt tên. ')    
            print("""                  [0__0] 
                <=I___I=>                                             
                  1   1
        Tôi chưa được đặt tên :(  
          bạn có thể gọi tôi là trợ lí của MINH HIẾU
            """)
            speak('Bạn có thể tạm gọi tôi là trợ lí ảo của Minh Hiếu')
#giúp đỡ, hiển thị tính năng             
        elif 'help' in text or 'bạn có thể làm gì' in text:
            speak('hiện tại Tôi có thể làm một số việc như sau')
            print("""Tôi có thể giúp bạn:
            - tìm kiếm trên google
            - tìm kiếm trên youtube
            - mở mã qr lưu thông tin của bạn
            - cho bạn biết thời gian hiện tại
            - cho bạn xem thời khóa biểu
            - mở zalo và facebook
            -cùng vài chức năng khác tôi đang được hoàn thiện
            """)
            speak(""" tìm kiếm trên google
            - tìm kiếm trên you túp
            - mở mã qui rờ lưu thông tin của bạn
            - cho bạn biết thời gian hiện tại
            - cho bạn xem thời khóa biểu
            - mở da lô và phây búc
            -cùng vài chức năng khác tôi đang được hoàn thiện
            """)
        #wikipedia    
        elif'là gì'in text or 'định nghĩa' in text or 'nói tôi biết' in text:
            tell_me_about()  

