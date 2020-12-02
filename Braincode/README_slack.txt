

SIMULATION PARAMETERS
- in the file "simParams.py" you can change
   - the simulation time ("simDuration")
   - the number of threads ("nbcpu"), that will be assigned to -->>.  nest.SetKernelStatus({'local_num_threads': int(sim_params['nbcpu'])})

The number of computational nodes can be defined within the job file, however 1M neurons should run in a good PC with at least 10 threads
If you have any issue on running this, please let me know.
At the end of the simulation I printed the kernel status, showing: 'network_size': 1089137,  'num_connections': 1588469795.

Due the huge number of synapses, I used in this case 14 threads, I was getting an error "too many synapses per process"
with 10 threads. In a PC, this simulation lasted 30 min: 20 for building the network and 10 min for simulation.


LOGGING
I deactivated most of the output files at log, only BG and TH generates .dat files. When using many processes, a single
.dat file will be generated per process and per neural population (or topological layer), so the output scales.
I was getting an error "so many files opened" and Ubuntu couldn't manage it. Let me know if any issue. Thanks, Carlos.


MOTOR OUTPUT
we have a trial on target selection involving BG and TH where we use fake layers to read signals from the
environment and TH activity as proxy to motor output (using NEST 2). Let me check further about it with the team.

I had a discussion with @Jun Igarashi who is the M1 modeler. A very general assumption can consider a primitive mapped
to the neural of a column in M1 L5B-Pyr *neural activity
In that way, 3 columns can generate primitives for left, center and right micro movement
we assume a column as a cluster of that population within 120 micron radius
That could be the easiest approach if we are in hurry. Anyway, @Jun Igarashi will try to accomplish column-minicolum
primitives for movement over the time within this year. Iga-san, can you please provide more details about that ?

As Carlos explained, we assume that M1 generates sequential activation of
L5 columns representing each motor primitives given physiological experiments of movement-related
activity of column (Georgopoulos et al., 2007, Hira et al., 2013), motor primitives (Overduin et al.2012),
sequential neural activity during movement (Beloozerova et al., 2013, Peteres et al., 2014).
On the basis of the observations and our hypothesis, we are developing a brain model, in which reaching movement
trajectory is calculated in M1 through difference between target position commanded by
prefrontal cortex and current position computed in S1 with sensory signals form peripherals. But, the development
has not finished. As a simplest case, we set three columns corresponding to three different
directions of motor primitives in M1. To test communication of signals between brain and body model,
the first version of the brain model Carlos sent should work.