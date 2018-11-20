# Client Commands

There are lots of client commands that can be executed in the console, or in the configuration file. This doc shows them all. If you look for client settings, read the [Client Settings](client_settings.md) doc. To find out how to find the config file, read the [Client Config](client_config.md) doc.

### Console

All these commands can be executed in the console. To open the console, press the console-key (f1 is default).

### Engine commands

|Command |  Syntax | Description|
| ------ | ------- | ---------- |
|`echo`|	echo text|	Print out the text to the console|
|`exec`|	exec file|	Execute the commands in the specified file|
|`quit`|	quit|	Quit Teeworlds|
|`exit`|	exit|	Quit Teeworlds|
|`minimize`|	minimize|	Minimize Teeworlds|
|`connect`|	connect host:port|	Connect to the specified server|
|`disconnect`|	disconnect|	Disconnect from the server|
|`ping`|	ping|	Ping the server|
|`screenshot`|	screenshot|	Take a screenshot|
|`rcon`|	rcon command|	Execute the command in rcon|
|`rcon_auth`|	rcon_auth password|	Authenticate with rcon|
|`play`|	play filename|	Play the file in the demo player|
|`record`|	record filename|	Start a recording to the specified file|
|`stoprecord`| stoprecord|	Stop the recording|
|`add_favorite`|	add_favorite host:port|	Add the server as a favorite|
|`remove_favourite`|	remove_favourite host:port|	Remove the server from your favourites|
|`add_friend`|	add_friend name clan|	Add the player to your friendlist|
|`remove_friend`|	remove_friend name clan|	Remove the player from your friendlist|

### Game commands

|Command |  Syntax | Description|
| ------ | ------- | ---------- |
|`+left`|	+left|	Move left|
|`+right`|	+right|	Move right|
|`+jump`|	+jump|	Jump|
|`+hook`|	+hook|	Fire hook|
|`+fire`|	+fire|	Fire a shot|
|`+weapon1`|	+weapon1|	Switch to weapon 1 (hammer)|
|`+weapon2`|	+weapon2|	Switch to weapon 2 (gun)|
|`+weapon3`|	+weapon3|	Switch to weapon 3 (shotgun)|
|`+weapon4`|	+weapon4|	Switch to weapon 4 (grenade launcher)|
|`+weapon5`|	+weapon5|	Switch to weapon 5 (rifle)|
|`+nextweapon`|	+nextweapon|	Switch to the next weapon|
|`+prevweapon`|	+prevweapon	|Switch to the previous weapon|
|`callvote`|	callvote type value|	Call a vote|
|`vote`|	vote yes/no|	Vote yes or no|
|`+emote`|	+emote|	Open emote selector|
|`emote`|	emote number|	Send a specific emote|
|`+scoreboard`|	+scoreboard|	Show the scoreboard|
|`+spectate`|	+spectate|	Show the spectator mode selector|
|`spectate`|	spectate client_id|	Spectate the player corresponding to client_id (-1 = freeview)|
|`spectate_next`|	spectate_next|	Spectate the next player|
|`spectate_previous`|	spectate_previous|	Spectate the previous player|
|`say`|	say message|	Send a global chat message|
|`say_team`|	say_team message|	Send a chat message to your team|
|`chat`|	chat all/team|	Enable chat in the chosen mode|
|`+show_chat`|	+show_chat|	Show more chat messages|
|`bind`|	bind key command|	Bind the command to the key|
|`unbind`|	unbind key|	Unbind the key|
|`unbindall`|	unbindall|	Unbind all the keys|
|`dump_binds`|	dump_binds|	Dump the binds|
|`toggle_local_console`|	toggle_local_console|	Toggle the local console|
|`clear_local_console`|	clear_local_console|	Clear the local console|
|`dump_local_console`|	dump_local_console|	Dump the local console|
|`toggle_remote_console`|	toggle_remote_console|	Toggle the remote console|
|`clear_remote_console`|	clear_remote_console|	Clear the remote console|
|`dump_remote_console`|	dump_remote_console|	Dump the remote console|
|`team`|	team team_id|	Switch to the specified team (0 = red, 1 = blue, -1 = spectators)|
|`kill`|	kill|	Kill yourself|

### Startup commands

To Start Teeworlds on Windows with the debug console open, use "teeworlds.exe -c" or "teeworlds.exe --console".
It is also possible to add the parameter to a windows shortcut.

