time = (0:0.1:10)';  % Time from 0 to 10 seconds in steps of 0.1

% v_in = 10; %Constant input speed 
%Note: if you are using constant speed then V = [0,v_in]

% %Sinusoidal input speed
% v_in = sin(time); %Input speed
% v_in = sin(time); %Input speed

% omega_in = 10; %Constant input angular speed 
%Note: if you are using constant speed then Omega = [0,omega_in]

% %Sinusoidal input angular speed
% omega_in = sin(time); %Input speed
% omega_in = sin(time); %Input speed


% inputData = [time, data];  % Combine into a matrix
V = [time,v_in];  %Input speed 

Omega = [0,0];  %Input angular speed

