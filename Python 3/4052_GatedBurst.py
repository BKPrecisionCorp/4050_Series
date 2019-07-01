import time
import visa
rm=visa.ResourceManager()
li=rm.list_resources()
for index in range(len(li)):
    print(str(index)+" - "+li[index])
choice = input("Which device?: ")
vi=rm.open_resource(li[int(choice)])

print(vi.query("*idn?"))

print("Configuring C2")
vi.write("c2:bswv frq,1")
vi.write("c2:bswv wvtp,square") #set before the duty cycle
vi.write("c2:bswv duty,75")

print("Configure C1")
#The basic waveform parameters need to be set before the burst parameters
#Reason not clear to me.
vi.write("c1:bswv frq,1250000")
#set the amplitude, offset etc... here

vi.write("c1:btwv state,on") #enable Burst mode
vi.write("c1:btwv trsr,ext") #trigger source
vi.write("c1:btwv gate_ncyc,gate") #set the burst cycles to be gated by the trigger
vi.write("c2:output on")
for index in range(0,5):
    vi.write("c1:output on")
    print("Output on")
    time.sleep(3)
    vi.write("c1:output off")
    print("Output off")
    time.sleep(3)

