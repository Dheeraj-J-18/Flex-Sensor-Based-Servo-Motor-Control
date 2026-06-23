from machine import ADC, Pin, PWM, I2C
import time

# -------- FLEX SENSOR --------
flex = ADC(26)

# -------- SERVO --------
servo = PWM(Pin(15))
servo.freq(50)

def set_angle(angle):
    duty = int(1638 + (angle / 180) * (8192 - 1638))
    servo.duty_u16(duty)

# -------- I2C LCD --------
i2c = I2C(0, scl=Pin(5), sda=Pin(4), freq=400000)

# LCD address (usually 0x27 or 0x3F)
LCD_ADDR = 0x27

# Simple LCD functions
def lcd_cmd(cmd):
    i2c.writeto(LCD_ADDR, bytearray([0x80, cmd]))

def lcd_data(data):
    i2c.writeto(LCD_ADDR, bytearray([0x40, data]))

def lcd_init():
    time.sleep(0.1)
    lcd_cmd(0x38)
    lcd_cmd(0x0C)
    lcd_cmd(0x01)
    time.sleep(0.05)

def lcd_string(msg):
    for char in msg:
        lcd_data(ord(char))

lcd_init()

# -------- CALIBRATION --------
min_val = 10000   # change after testing
max_val = 50000

while True:
    flex_value = flex.read_u16()

    # Map to angle
    angle = (flex_value - min_val) * 180 / (max_val - min_val)
    angle = max(0, min(180, angle))

    set_angle(angle)

    # Decide bend level
    if flex_value < (min_val + 5000):
        status = "STRAIGHT"
    elif flex_value < (min_val + 20000):
        status = "SLIGHT BEND"
    else:
        status = "FULL BEND"

    # Display on LCD
    lcd_cmd(0x01)
    lcd_string("Angle: {}".format(int(angle)))
    
    lcd_cmd(0xC0)
    lcd_string(status)

    print(flex_value)

    time.sleep(0.3)