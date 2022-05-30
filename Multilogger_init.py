import serial
import time
import serial.tools.list_ports
import os
import tkinter as tk
import PIL.Image
import PIL.ImageTk

List1 = []

def scan():
    ports = serial.tools.list_ports.comports()
    for port in sorted(ports):
        List1.append(port)
        #checks amount of serial devices connected
        #only proceed if number is 1
    if len(List1) > 1:
        label1 = tk.Label(root,  text = 'There are multiple serial devices connected. Please disconnect everything but the Arexx Multilogger base and try again. ', fg='red', font=('helvetica', 8, 'bold'))
        canvas1.create_window(500,300, window=label1)
    if len(List1) == 0:
        label1 = tk.Label(root, text = '                    There is no Arexx Multilogger Base connected. Please reconnect and try again.                        ', fg='red', font=('helvetica', 8, 'bold'))
        canvas1.create_window(500,300, window=label1)
    if len(List1) == 1:
        label1 = tk.Label(root, text = '                                  Succes! device is succesfully connected. Setting up multilogger base, please wait..                                ', fg='green', font=('helvetica', 8, 'bold'))
        canvas1.create_window(500,300, window=label1)
    uartwrite()    
    List1.clear()
    


def uartwrite():
    VARIABLE = serial_ports()[0] #Sets returned value from serial_ports() as the Multilogger serial port
    print(VARIABLE)
    ser = serial.Serial(VARIABLE,115200)  
    epoch_time = int(time.time())
    print(epoch_time)
    ser.write((epoch_time).to_bytes(4, byteorder='big'))      # write epoch in 4 bytes big endian to multilogger
   # for line in ser.read(20):
     #   print(str(count) + str(': ') + chr(line) )
     #   count = count+1
 #   ser.close() 
  #  ser.close()   
    #TODO: add uartread()

def serial_ports():
    ports = ['COM%s' % (i + 1) for i in range(256)]
    result = []
    #check serial port and try opening it. Format it to 'COMx' 
    #TODO: If error, write error in window for user to see
    #TODO: only open if device has CH340N UART bridge
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result

#def uartread():
#TODO: The multilogger will set the received EPOCH and write the calculated date and time back.
#User will then have to verify that the date and time received from multilogger is correct. Then the program ends.
    


root = tk.Tk()
List1 = []

#create canvas of program
canvas1 = tk.Canvas(root, width = 1000, height = 500)
canvas1.pack(fill= "both", expand = False)

#add image to window
im = PIL.Image.open("arexx_office.png")
photo = PIL.ImageTk.PhotoImage(im)
labelbg = tk.Label(root, image=photo)
labelbg.image = photo
canvas1.create_window(500, 110, window=labelbg)

#create path C:/Arexx on user PC if path is not there yet
path = 'C:/Arexx'
isExist = os.path.exists(path)
if isExist != True:
    os.makedirs(path)
    print("Done! C:/Arexx was created!")
elif isExist != False:
    print("Done! C:/Arexx already exists.")


#Add main labels and items
labelroot = tk.Label(root, text = 'AREXX Multilogger setup program',fg='black', font=('helvetica', 12, 'bold'))
canvas1.create_window(500,10, window=labelroot)
label2 = tk.Label(root,  text = 'Welcome to the Arexx multilogger program. Please disconnect all devices from your PC and connect only the Arexx Multilogger Base.', fg='black', font=('helvetica', 8, 'bold'))
canvas1.create_window(500,210, window=label2)

#This button will start the COM scanning, Serialwriting and Serialreading
button1 = tk.Button(text='Click to start!', command=scan, bg='red', fg='white')
canvas1.create_window(500,400, window=button1)



root.mainloop()
        
    