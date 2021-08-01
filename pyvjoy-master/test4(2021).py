import pyvjoy

#Pythonic API, item-at-a-time

j = pyvjoy.VJoyDevice(1)

#turn button number 15 on

 # buttons number 1,2 and 5 (1+2+16)
s=32895
j.data.wAxisZRot=s

#send data to vJoy device
j.update()


#Lower-level API just wraps the functions in the DLL as thinly as possible, with some attempt to raise exceptions instead of return codes.
