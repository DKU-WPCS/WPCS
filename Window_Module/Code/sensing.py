import RPI.GPIO as GPIO

OPEN=True
CLOSE=False

GPIO.setmode(GPIO.BCM)
# comparater 사용을 상정
# 버튼 OR 적외선 센서를 사용

class sensing:
    def __init__(self):
        self.pinA=0
        self.pinB=0
        # 선 배선 확인
        #    - - - - - - - - - - -
        #   |   @@@              |
        #   | A @@@            B | 
        #    - - - - - - - - - - - 
        # A가 눌리면 열림 
        # B가 눌리면 닫침
        GPIO.setup(self.pinA,GPIO.IN)
        GPIO.setup(self.pinB,GPIO.IN)
        #초기 설정
        self.A_stat=True
        self.B_stat=False
        self.checking()
        # 초기 상태 확인
        #PULL_DOWN을 상정 HIGH=True LOW= False

    def checking(self):
        self.A_stat=GPIO.input(self.pinA)
        self.B_stat=GPIO.input(self.pinB)
    def compare_processing(self):
        self.checking()
        if self.A_stat==True and self.B_stat ==False:
            # A에 닿아 있는 상태(CLOSE)
            return CLOSE
        elif self.A_stat==False and self.B_stat ==True:
            # B에 닿아 있는 상태(CLOSE)
            return OPEN
        elif self.A_stat==False and self.B_stat ==False:
            # 두 부분 다 닿아있지 않은 상태(FLOAT)
            return 1
        else:
            # 두 부분 다 닿아있는 상황(ERROR)
            return -1

        