# Tuning reference

Tuning is a way to edit physics and weapon settings so that the server is more customizable. Tuning can only be used on non-pure gametypes. Set the gametype to `mod` using `sv_gametype mod` and execute the following in rcon or config to tune a variable:

`tune gravity 1.0`
where you replace `gravity 1.0` with the variable and value you want.

## Physics tuning

|Tuning|	Description|	Default|  Unit|
| ------ | ---------- | -------- | ----- |
|`ground_control_speed`|	Max speed the tee can get on ground|	10.0|
|`ground_control_accel`|	Acceleration speed on the ground|	2.0|
|`ground_friction`|	Friction on the ground|	0.5|
|`ground_jump_impulse`|	Impulse when jumping on ground|	13.2|
|`air_jump_impulse`|	Impulse when jumping in air|	12.0|
|`air_control_speed`|	Max speed the tee can get in the air|	5.0|
|`air_control_accel`|	Acceleration speed in air|	1.5|
|`air_friction`|	Friction in the air|	0.95|
|`hook_length`|	Length of the hook|	380.0|pixels
|`hook_fire_speed`|	How fast the hook is fired|	80.0|
|`hook_drag_accel`|	Acceleration when hook is stuck|	3.0|
|`hook_drag_speed`|	Drag speed of the hook|	15.0|
|`gravity`|	Gravity of the teeworld|	0.5|
|`velramp_start`|	Velocity ramp start|	550.0|
|`velramp_range`|	Velocity ramp range|	2000.0|
|`velramp_curvature`|	Velocity ramp curvature|	1.4|
|`player_collision`|	Enable player collisions|	1|
|`player_hooking`|	Enable player vs player hooking|	1|

## Weapon tuning

|Tuning	|Description|	Default|  Unit|
| ------ | ---------- | -------- | ----- |
|`gun_curvature`|	Gun curvature|	1.25|
|`gun_speed`|	Gun speed|	2200.0|pixels / sec
|`gun_lifetime`|	Gun lifetime|	2.0|sec
|`shotgun_curvature`|	Shotgun curvature|	1.25|
|`shotgun_speed`|	Shotgun speed|	2750.0|pixels / sec
|`shotgun_speeddiff`|	Speed difference between shotgun bullets|	0.8|
|`shotgun_lifetime`|	Shotgun lifetime|	0.20|sec
|`grenade_curvature`|	Grenade curvature|	7.0|
|`grenade_speed`|	Grenade speed|	1000.0|pixels / sec
|`grenade_lifetime`|	Grenade lifetime|	2.0|sec
|`laser_reach`|	How long the laser can reach|	800.0|pixels
|`laser_bounce_delay`|	When bouncing, stop the laser this long|	150.0|ms
|`laser_bounce_num`|	How many times the laser can bounce|	1.0|
|`laser_bounce_cost`|	Remove this much from reach when laser is bouncing|	0.0|pixels
|`laser_damage`|	Laser damage|	5.0|damage
