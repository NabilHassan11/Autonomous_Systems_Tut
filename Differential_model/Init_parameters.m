%%%% Differential Robot Parameters %%%%
r = 25e-3; % radius of wheel is 2.5 cm
L = 150e-3; % width of the robot is 15 cm

%%%% Initial Conditions %%%%
x = 0;
y = 0;
theta = 0;

time = (0:0.1:10)';  % Time from 0 to 10 seconds in steps of 0.1
 
%Note: if you are using constant speed then w = [0,w_in]
%Note: if you are using varying speed then w = [time,w_in]

W_L = [0,10]; % input angular speed of the left wheel
W_R = [0,10]; % input angular speed of the left wheel