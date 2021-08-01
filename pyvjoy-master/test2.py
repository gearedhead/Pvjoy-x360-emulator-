import pyvjoy

#Pythonic API, item-at-a-time

j = pyvjoy.VJoyDevice(1)

#turn button number 15 on

 # buttons number 1,2 and 5 (1+2+16)
j.data.wAxisX = 0x4000
j.data.wAxisY= 0x4000
j.data.wAxisZRot=0x7000

#send data to vJoy device
j.update()


#Lower-level API just wraps the functions in the DLL as thinly as possible, with some attempt to raise exceptions instead of return codes.
