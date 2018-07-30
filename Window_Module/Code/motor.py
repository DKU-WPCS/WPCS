import RPI.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

class motor:
    def __init__(self):
        self.IN1=0
        self.IN2=0
        self.IN3=0
        self.IN4=0
        # 선 배선 확인
        # ENA, ENB 에 PWM 신호
        self.ENA=0
        self.ENB=0

        self.pwn_A=setPin_A
        self.pwm_B=setPin_B

    def setPin_A(self):
        GPIO.setup(self.IN1,OUT)
        GPIO.setup(self.IN2,OUT)
        GPIO.setup(self.ENA,OUT)
        pwm=GPIO.PWM(ENA,100)

        pwm.start(0)
        return pwm
        # PWM 핸들 반환

    def setPin_B(self):
        GPIO.setup(self.IN3,OUT)
        GPIO.setup(self.IN4,OUT)
        GPIO.setup(self.ENB,OUT)
        pwm=GPIO.PWM(ENA,100)

        pwm.start(0)
        return pwm
        # PWM 핸들 반환

    # 모터의 기초적인 Initialize를 진행한다.
    def MotorControl(self,motor_num='A',way='FW',speed=0):
        if motor_num =='A':
            self.pwm_A.ChangeDutyCycle(speed)
            if way=="FW":
                #앞으로 이동
                GPIO.output(self.IN1,HIGH)
                GPIO.output(self.IN2,LOW)
            if way=="BW":
                #앞으로 이동
                GPIO.output(self.IN1,LOW)
                GPIO.output(self.IN2,HIGH)
        if motor_num =='B':
            self.pwm_B.ChangeDutyCycle(speed)
            if way=="FW":
                #앞으로 이동
                GPIO.output(self.IN3,HIGH)
                GPIO.output(self.IN4,LOW)
            if way=="BW":
                #앞으로 이동
                GPIO.output(self.IN3,LOW)
                GPIO.output(self.IN4,HIGH)
# speed= DutyCycle을 입력, way 앞 뒤 방향 =(FW,BW) motor_num =(A, B) 중 선택


class encoder:

    def __init__(self):
        self.encoder_pinA=0
        self.encodef_pinB=0
        self.encoder_pos=0
        # 핀 설정
        self.set_encoder
        # 핀 initialize
    def set_encoder(self):
        GPIO.setmode(self.encoder_pinA,GPIO.IN,GPIO.PUD_UP)
        GPIO.setmode(self.encoder_pinB,GPIO.IN,GPIO.PUD_UP)
    def encoder_A(self,channel):
        #pos edge의 경우
        if GPIO.input(self.encoder_pinA)==GPIO.input(self.encoder_pinB):
            self.encoder_pos+=1
        else:
            self.encoder_pos-=1
    def encoder_B(self,channel):
        #neg edge의 경우
        if GPIO.input(self.encoder_pinA)==GPIO.input(self.encoder_pinB):
            self.encoder_pos-=1
        else:
            self.encoder_pos+=1
    def encoder_run(self):
        GPIO.add_event_detect(self.encoder_pinA, GPIO.BOTH, callback=self.encoder_A)
        GPIO.add_event_detect(self.encodef_pinB, GPIO.BOTH, callback=self.encoder_B)


            




