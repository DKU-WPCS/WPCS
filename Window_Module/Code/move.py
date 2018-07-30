import motor,encoder from motor.py
import sensing from sensing.py

run =True
OPEN=True
CLOSE=False
# 구동을 위한 Bool 형 run,OPNE,CLOSE
encoder=encoder()
motor=motor()
sensor=sensing()
#인스턴스 선언
speed=0
# 모터 스피드
input_result=CLOSE
motor_con=CLOSE
#입력을 통한 input result의 변화
#motor_con의 상태를 확인

#BW를 닫는 방향
#FW를 여는 방향으로 설정

def con_change(codition):
    if condition ==CLOSE:
        while sensor.compare_processing==CLOSE:
            motor.MotorControl('A','BW',speed)
            if sensor.compare_processing == -1:
                run ==False
    if codition == OPEN:
        while sensor.compare_processing==OPEN:
            motor.MotorControl('A','FW',speed)
            if sensor.compare_processing == -1:
                run ==False
    # Master 서버에 락을 푸는 신호를 전송

# 상태를 변경하기 위한 함수, condition애 따라 일때 샅애 변화떄 까지 
# 코드를 반복


con_change(CLOSE)
# 초기 닫침상태로 변경


while run:
    encoder.encoder_run()
    #엔코더 값을 항상 검사

    #
    # 소켓을 통한 입력을 받고 그 CLOSE, OPEN 상태를 input_result에 저장
    #

    if input_result==OPEN && motor_con==CLOSE:
       con_change(CLOSE)
    elif input_result==CLOSE && motor_con==OPEN:
       con_change(OPEN)
    else:
        pass
        

    

