from pylab import *

goldenratio = .5*(1+sqrt(5))
fsx = 7
fsy = fsx/goldenratio

def rlc(voltage = 120, frequency = pi*120, inductance = .2, resistance = 50, capacitance = .00001, charge = 10e-6, current = 0, dt = .0001, simLength = .25):
    numIterations = int(simLength/dt)
    #if(inductance == 0):
    #    current = (voltage + charge/capacitance)/resistance
    #    change_in_current = 0;
    #else:
    #change_in_charge = (voltage - charge/capacitance - inductance*change_in_current)/resistance
    t = 0
    timeLst = [t]
    chargeLst = [charge]
    currentLst = [current]
    E = voltage*cos(frequency*t)
    change_in_current = (E - resistance*current - charge/capacitance)/inductance

    for i in range(1,numIterations):
        t = i * dt
        timeLst.append(t)
        current = current + change_in_current*dt
        currentLst.append(current)
        charge = charge + current*dt
        chargeLst.append(charge)
        #if(inductance == 0):
        #current = (voltage + charge/capacitance)/resistance
        #else:
        E = voltage*cos(frequency*t)
        change_in_current = (E - resistance*current - charge/capacitance)/inductance
        #change_in_charge = (voltage - charge/capacitance - inductance*change_in_current)/resistance
    return chargeLst, currentLst, timeLst

qLst, iLst, tLst = rlc()

figure(figsize = (fsx, fsy))
plot(tLst, qLst, 'k-')
xlabel('Time')
ylabel('Charge')
title('Charge vs. Time (DC Source)')
show()

figure(figsize=(fsx, fsy))
plot(tLst, iLst, 'k-')
xlabel('Time')
ylabel('Current')
title('Current vs. Time (DC Source)')
show()

figure(figsize=(fsx, fsy))
plot(tLst, iLst*50, 'k-')
xlabel('Time')
ylabel('Current')
title('Current vs. Time (DC Source)')
show()

print("All done!")
