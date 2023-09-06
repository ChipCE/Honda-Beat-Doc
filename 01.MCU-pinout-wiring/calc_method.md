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
- 0.0015698587127158557 km/revolution (or per 4 pulse)



