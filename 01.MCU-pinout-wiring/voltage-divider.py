resistorValues = [10,12,15,18,22,27,33,39,47,56,68,82]
adcVoltage = 3.3

for i in range(0,len(resistorValues)):
    for j in range(0,len(resistorValues)):
        rate = 1/(resistorValues[i] / (resistorValues[i] + resistorValues[j]))
        print(resistorValues[i],"\t",resistorValues[j],"\t",rate,"\t\t\t\t",adcVoltage*rate)


# R1       R2      Rate                            Max
# 10       33      4.3                             14.19
# 12       39      4.25                            14.024999999999999
# 10       47      5.7                             18.81
# 10       56      6.6                             21.779999999999998
# 10       10      2.0                             6.6
# 10       12      2.2                             7.26
# 10       15      2.5                             8.25
# 12       12      2.0                             6.6
# 12       15      2.25                            7.425
# 12       18      2.5                             8.25