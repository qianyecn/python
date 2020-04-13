#coding=utf-8
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
my_in = 16
my_out = 12
GPIO.setwarnings(False)
now_time=time.strftime("%H:%M", time.localtime())
GPIO.setup(my_in,GPIO.IN)
GPIO.setup(my_out,GPIO.OUT)
# 按钮接通为17:00，不接通为17:30响铃
sum_win_flag=GPIO.input(my_in)
def open():
	print("now time is "+now_time+"  stats is "+str(sum_win_flag))
	GPIO.output(my_out,GPIO.HIGH)
        time.sleep(5)
        GPIO.output(my_out,GPIO.LOW)
		#GPIO.cleanup()
def panduan():
	if now_time=="12:00":
	# if now_time=="12:00":
		open()
	elif now_time=="17:00":
		if sum_win_flag==1:
			open()

	elif now_time=="17:30":
		if sum_win_flag==0:
			open()
	else:
		print("time wrong")
try:
	panduan()
except KeyboardInterrupt:
	GPIO.output(my_out,GPIO.LOW)
	GPIO.cleanup()
exit()
