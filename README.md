# TOSHVEC

**T**ask **O**ffloading and **S**erving **H**andover of
**V**ehicular **E**dge **C**omputing Networks
Based on Trajectory Prediction

This is a solution finding dqn agent in an edge computing problem . 

Vehicles should decide what to do with their tasks . They have three options : 
* Process it locally 
* Offload it to one of mission vehicles
* Offload it to the cloud 

This project considers lot of parameters like : 
* Delay
* Energy consumption 
* Network bandwidth
* Vehicles storage and capability of processing a task

After simulating the environment we give the states, actions, reward functions and etc to a dqn agent . 

## Stacks
The dqn is written using `mxnet` for now .
