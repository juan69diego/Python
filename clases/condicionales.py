import math



def is_criticality_balanced(temperature, neutrons_emitted):
    if temperature * neutrons_emitted < 500000:
        plus = True
    else:plus = False
    
    if temperature < 800:
        temperature = True
    else:temperature = False
    
    if neutrons_emitted > 500:
        neutrons_emitted = True 
    else:neutrons_emitted = False
    
    if temperature == False:
        return False
    elif neutrons_emitted == False:
        return False
    elif plus == False:
        return False
    
    else:
        return True

print(is_criticality_balanced(500.01,999.99))


def reactor_efficiency(voltage, current, theoretical_max_power):
    MaxPower = voltage * current
    Power = (MaxPower/theoretical_max_power)*100
    print(Power)
    if Power > 80:
        return ('green')
    elif Power < 80 and Power > 60:
        return ('orange')
    elif Power < 60 and Power > 30:
        return ('red')
    elif Power < 30:
        return ('black')
    
print(reactor_efficiency(10,0,10000))



def fail_safe(temperature, neutrons_produced_per_second, threshold):
    
    a = temperature * neutrons_produced_per_second
    print(a)
    if a < (0.9 *threshold):
        return 'low'
    elif a >= ((0.1*threshold)-threshold) and a <= ((0.1*threshold)+threshold):
        return 'normal'
    else:
        return 'danger'
    
    
    



print(fail_safe(10,11.1,100))