# RPM calc method 

## Engine specs

- 4 stroke 3 cylinders

## RPM Logic

- 4 stroke engine rotates 2 revolutions per cycle(Intake/Compression/Combustion/Exhaust)
- 3 cylinders are 120 degree out of pharse compare to each other
- In one cycle, ECU need to send ignition signal 3 times
- in Honda beat, all ignition coils get signal from the same ignition signal line via contributor.
- 39K Ohms and 22nF (about 185Hz) low-pass-RC-filter used to filter out the noise before feed it into logic IC

If we have ignition signal period <code>T(s)</code> or ignition freq <code>f(Hz)</code> signal  then <code>RPM</code> can be caculated by the following formulas.

<pre>
T = 1/f

f = RPM / 60 * 3 / 2 = RPS * 3 / 2
          ^    ^   ^
          |    |   |
       to RPS  |   |
         cylinders |
            2 revolutions per cycle

or 
RPM = 40 * f = 40 * (1/T)
</pre>

## Speed logic

- sensor signal : 4 pulses/revolution
- 637 revolution/km
- 1/637 = 0.0015698587127158557 km/revolution (or per 4 pulse)
- 1/637/4 = 0.0003924646781789639 km/pulse
- time measure between 2 pulse are in milisecond <code>Tms</code>

<pre>
speed = (1/637/4) * (60*60*1000) / Tms = 1412.87284144427 / Tms

@   1km/h Tms = 1412.87284144427     ms
@   5km/h Tms =  282.57456828885404  ms
@  50km/h Tms =   28.257456828885402 ms
@ 100km/h Tms =   14.128728414442701 ms
@ 140km/h Tms =   10.091948867459072 ms
</pre>