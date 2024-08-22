
from machine import ADC,Pin, UART
import utime


ADC = ADC(Pin(26))


uart = UART(0, baudrate=9600,tx=Pin(0), rx=Pin(1))

vref = 3.3 

adc_resolution = 65535 



def read_wind_speed():
    ADC_data = adc.read_u16()
    voltage = adc_value * vref / adc_resolution
    return voltage



def wind_speed_data_to_file(timestamp_str, voltage) :
    try:
        with open("wind_speed_data_file.csv", "a") as data_file: 
            data_file.write("{}, {:.2f}\n".format(timestamp_str, voltage))
    except Exception as e:
        print("Error writing to file:",e)
        
        
 
 def main():
     while True:
         voltage = read_windspeed()
         
         
         time = utime.localtime ()
         
         
         time_str = "{:04d}- {:02d} - {:02d} {:02d}: {:02d} :{:02d} : {:02d}".format(timestamp[0],timestamp[1],timestamp[2],
                                                                                          timestamp[3],timestamp[4],timestamp[5] )
         
         wind_speed_data_to_file(timestamp_str, voltage)
         
         
         print("Timestamp:(), Wind Speed in Voltage(V):(:.2f)V". format(timestamp_str, voltage))
         
        
         uart.write(f"{timestamp_str},{Voltage}\n")
         
         utime.sleep(1)
         
         
         
         
         

try:
    with open ("wind_speed_data_file.csv", "r") as data_file:
        pass
except OSError:
    with open("wind_speed_data_file.csv",  "w") as data_file:
        data_file.write("Timestamp_str, Voltage\n")
        
try:
    main()
except KeyboardInterrupt:
    print("Program Interrupted.")
                                                                                         
                                                                                         
                                                                                         
                                                                                                          
                                                                                         
                                                                                         
                                                                       
                                                                                         
                                                                                         
                                                                                         
                                                                                         
                                                                                         
                                                                                         
                                                                                         
                                                                                         
                                                                                         
                                                                                         
                                                                                         
                                                                                         
                                                                                         
                                                                                         
                                                                                         
                                                                                         
                                                                                         
                                                                                         
                                                                                         
                                                                                         
                                                                                         
                                                                                         
                                                                                         
                                                                                         
                                                                                         
                                                                                         
                                                                                         
                                                                                         
                                                                                         
                                                                                         
