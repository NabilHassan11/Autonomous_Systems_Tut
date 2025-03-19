%%%% Ackermann model Parameters %%%%

L = 250e-3; % width of the robot is 15 cm

%%%% Initial Conditions %%%%
x = 0;
y = 0;
theta = 0;
phi = 0;

time = (0:0.1:10)';  % Time from 0 to 10 seconds in steps of 0.1
 
%Note: if you are using constant speed then v = [0,v_in]
%Note: if you are using varying speed then v = [time,v_in]

Vd = [0,10]; % input angular speed of the left wheel
phi = [0,0.1]; % input angular speed of the left wheel