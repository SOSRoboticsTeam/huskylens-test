import smbus2
import time

HUSKYLENS_I2C_ADDRESS = 0x32

bus = smbus2.SMBus(1)  

def huskylens_write(command):
    """ Küld egy parancsot a HuskyLensnek I2C-n keresztül """
    bus.write_i2c_block_data(HUSKYLENS_I2C_ADDRESS, 0, command)

def huskylens_read():
    """ Olvas adatokat a HuskyLensből """
    try:
        data = bus.read_i2c_block_data(HUSKYLENS_I2C_ADDRESS, 0, 16) 
        return data
    except OSError:
        print("Hiba: Nem sikerült adatot olvasni a HuskyLensből!")
        return None

def huskylens_request_blocks():
    """ Kérést küld a HuskyLens-nek a blokkok (QR-kódok vagy színdetekció) lekérésére """
    command = [0x55, 0xAA, 0x11, 0x00, 0x2A]  
    huskylens_write(command)

def parse_huskylens_data(data):
    """ Egyszerű adatfeldolgozás: visszaadja a QR-kód vagy színérzékelés adatait """
    if data and len(data) > 5:
        object_type = data[5]  
        x = data[6]  
        y = data[7]  
        width = data[8]  
        height = data[9]  
        return {"type": object_type, "x": x, "y": y, "width": width, "height": height}
    return None


while True:
    huskylens_request_blocks()  
    time.sleep(0.
