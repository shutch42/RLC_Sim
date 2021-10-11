from pylab import *

goldenratio = .5*(1+sqrt(5))
fsx = 7
fsy = fsx/goldenratio

def rlc(voltage = 100, inductance = .05, resistance = 20, capacitance = .0001, charge = 0, current = 0, dt = .0001, simLength = .05):
    numIterations = int(simLength/dt)
    change_in_current = (voltage - resistance * current - charge / capacitance)/inductance
    t = 0
    timeLst = [t]
    chargeLst = [charge]
    currentLst = [current]

    for i in range(1,numIterations):
        t = i * dt
        timeLst.append(t)
        current = current + change_in_current*dt
        currentLst.append(current)
        charge = charge + current*dt
        chargeLst.append(charge)
        change_in_current = (voltage - resistance * current - charge / capacitance)/inductance
    return chargeLst, currentLst, timeLst

qLst, iLst, tLst = rlc()

figure(figsize = (fsx, fsy))
plot(tLst, qLst, 'k-')
xlabel('Time')
ylabel('Charge')
title('Charge vs. Time')
show()

figure(figsize=(fsx, fsy))
plot(tLst, iLst, 'k-')
xlabel('Time')
ylabel('Current')
title('Current vs. Time')
show()
