%%%% Differential Robot Parameters %%%%
r = 25e-3;   % radius of wheel is 2.5 cm
L = 150e-3;  % width of the robot is 15 cm
m = 1.0;      % Mass [kg]
J = 0.1;     % Moment of inertia [kg·m²] 

%%%% Initial Conditions %%%%
x = 0;
y = 0;
theta = 0;
omega = 0;
v = 0;

time = (0:0.1:10)';  % Time from 0 to 10 seconds in steps of 0.1
 
%Note: if you are using constant speed then w = [0,w_in]
%Note: if you are using varying speed then w = [time,w_in]

T_L = [0,1e-3]; % input angular speed of the left wheel
T_R = [0,2e-5]; % input angular speed of the left wheel