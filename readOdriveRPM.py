import odrive
import time

cpr = 258  # count per round of this small wheels

def cpsTOrpm(cps):
	return (cps/cpr)*60.0


print("Finding ODrive...")
odrv0 = odrive.find_any()

while True:
	startTime = time.time()
	cps0 = odrv0.axis0.encoder.vel_estimate
	cps1 = odrv0.axis1.encoder.vel_estimate
	rpm0 = cpsTOrpm(cps0)
	rpm1 = cpsTOrpm(cps1)
	period = time.time() - startTime
	print("rpm0: "+"{:.2f}".format(rpm0)+\
		"  rpm1: "+"{:.2f}".format(rpm1)+\
		"  period [sec]: "+"{:.6f}".format(period))
	# this loop took 0.5ms, faster than UART.