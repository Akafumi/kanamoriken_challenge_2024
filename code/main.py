from machine import Pin, UART

uart = UART(0, 9600)
MotorPhase = Pin(13, Pin.OUT)
MotorEnbl = Pin(18, Pin.OUT)

def go():
    MotorPhase.value(1)
    MotorEnbl.value(1)
    print('Go LED is OFF \n')
    uart.write('Go LED is OFF \n')

def back():
    MotorPhase.value(0)
    MotorEnbl.value(1)
    print('Back LED is ON \n')
    uart.write('Back LED is ON \n')

def stop():
    MotorEnbl.value(0)
    print('Stop LED is OFF \n')
    uart.write('Stop LED is OFF \n')

def not_found():
    print('Command is not found \n')
    uart.write('Command is not found\n')

commands = {
    'go': go,
    'back': back,
    'stop': stop
}

while True:
    if uart.any() > 0:
        data = uart.read().decode('utf-8').strip()
        print(data)
        command = commands.get(data, not_found)
        command()