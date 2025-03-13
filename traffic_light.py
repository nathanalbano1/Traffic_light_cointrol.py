from giozero
import LED
import time

red_LED = LED(3)

def stop_light(led_status):
    print(led_status)
    red, yellow, green = led_status
    if (led_status[red]):
        red_LED.on()
    else :
        red_LED.off()
def main():
    traffic_light_status = {"red_LED" : 1, "yellow_LED" : 1, "green_LED" : 1}

    while(True):
        print("led off = 0")
        print("led on = 1" )
        traffic_light_status["red_LED"] = int(input("Led on or off?"))
        stop_light(traffic_light_status)

main()