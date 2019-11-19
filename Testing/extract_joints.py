import matplotlib.pyplot as plt
import numpy as np
from lib.dmp_experiments.Python import train_dmp, DMP_runner
from Session import Trial
from Vicon import Vicon

trial = Trial.Trial(vicon_file="/home/nathanielgoldfarb/stairclimbing/CSV_files/subject_00/11_07_2019/subject_00 walk_01.csv")
traj = trial.get_joint_trajectories()["Rhip"][0]

T = Trial.calc_kinematics(traj)

#Name of the file
name = 'Simple_dmps.xml'

#Set no. of basis functions
n_rfs = 10000

#Set the time-step
dt = traj.time[1] - traj.time[0]

Important_values = train_dmp.train_dmp(name, n_rfs, T, dt)
start = traj.data[0]
goal = traj.data[-1]
my_runner = DMP_runner.DMP_runner(name, start, goal)

Y = []
tau = 1


for i in np.arange(0,125):

    my_runner.step(tau,dt)
    Y.append(my_runner.y)
#my_runner = DMP_runner(name,start,goal)


plt.xlabel("Frame")
plt.ylabel("Angle")

plt.plot(traj.data)
plt.plot(Y)
plt.legend(["raw", "DMP"])
plt.show()