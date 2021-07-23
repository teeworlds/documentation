# Client Commands

There are lots of client commands that can be executed in the console, or in the configuration file. This doc shows them all. If you look for client settings, read the [Client Settings](client_settings.md) doc. To find out how to find the config file, read the [Client Config](client_config.md) doc.

### Console

All these commands can be executed in the console. To open the console, press the console-key (f1 is default).

### Engine

|Command |  Syntax | Description|
| ------ | ------- | ---------- |
|`echo`|`echo text`|Print out the text to the console|
|`exec`|`exec file`|Execute the commands in the specified file|
|`eval_if`|`eval_if config comparison value command else command`|Execute command if condition is true|
|`quit`|`quit`|Quit Teeworlds|
|`exit`|`exit`|Quit Teeworlds|
|`minimize`|`minimize`|Minimize Teeworlds|
|`screenshot`|`screenshot`|Take a screenshot|
|`save_config`|`save_config [file]`|Save config to file (or default file if none)|
|`toggle`|`toggle config_option value1 value2`|Toggle config value|
|`+toggle`|`+toggle config_option value1 value2`|Toggle config value via keypress|
|`snd_toggle`|`snd_toggle`|Toggle sounds on and off|

### Servers

|Command |  Syntax | Description|
| ------ | ------- | ---------- |
|`connect`|`connect host:port`|Connect to the specified server|
|`disconnect`|`disconnect`|Disconnect from the server|
|`ping`|`ping`|Ping the server|
|`rcon`|`rcon command`|Execute the command in rcon|
|`rcon_auth`|`rcon_auth password`|Authenticate with rcon|
|`add_favorite`|`add_favorite host:port [password]`|Add the server as a favorite, optionally saving the password|
|`remove_favorite`|`remove_favorite host:port`|Remove the server from your favorites|

### Gameplay

|Command |  Syntax | Description|
| ------ | ------- | ---------- |
|`+left`|`+left`|Move left|
|`+right`|`+right`|Move right|
|`+jump`|`+jump`|Jump|
|`+hook`|`+hook`|Fire hook|
|`+fire`|`+fire`|Fire a shot|
|`+weapon1`|`+weapon1`|Switch to weapon 1 (hammer)|
|`+weapon2`|`+weapon2`|Switch to weapon 2 (gun)|
|`+weapon3`|`+weapon3`|Switch to weapon 3 (shotgun)|
|`+weapon4`|`+weapon4`|Switch to weapon 4 (grenade launcher)|
|`+weapon5`|`+weapon5`|Switch to weapon 5 (rifle)|
|`+nextweapon`|`+nextweapon`|Switch to the next weapon|
|`+prevweapon`|`+prevweapon`|Switch to the previous weapon|
|`+scoreboard`|`+scoreboard`|Show the scoreboard|
|`+stats`|`+stats`|Show stats|
|`team`|`team team_id`|Switch to the specified team (0 = red, 1 = blue, -1 = spectators)|
|`ready_change`|`ready_change`|Change ready state|
|`kill`|`kill`|Respawn|

### Social

|Command |  Syntax | Description|
| ------ | ------- | ---------- |
|`say`|`say message`|Send a global chat message|
|`say_self`|`say_self message`|Send a chat message just to yourself|
|`say_team`|`say_team message`|Send a chat message to your team|
|`chat`|`chat all/team`|Enable chat in the chosen mode|
|`+show_chat`|`+show_chat`|Show more chat messages|
|`chat_command`|`chat_command command arguments`|Execute a chat command with arguments|
|`+emote`|`+emote`|Open emote selector|
|`emote`|`emote number`|Send a specific emote|
|`callvote`|`callvote type value`|Call a vote|
|`vote`|`vote yes/no`|Vote yes or no|
|`add_friend`|`add_friend name clan`|Add the player to your friendlist|
|`remove_friend`|`remove_friend name clan`|Remove the player from your friendlist|
|`add_ignore`|`add_ignore name clan`|Add the player to your ignorelist|
|`remove_ignore`|`remove_ignore name clan`|Remove the player from your ignorelist|

### Key binds

|Command |  Syntax | Description|
| ------ | ------- | ---------- |
|`bind`|`bind key command`|Bind the command to the key|
|`unbind`|`unbind key`|Unbind the key|
|`unbindall`|`unbindall`|Unbind all the keys|
|`binds`|`binds`|List all key binds|

### Spectating
|Command |  Syntax | Description|
| ------ | ------- | ---------- |
|`+spectate`|`+spectate`|Show the spectator mode selector|
|`spectate`|`spectate client_id`|Spectate the player corresponding to `client_id` (-1 = freeview)|
|`spectate_next`|`spectate_next`|Spectate the next player|
|`spectate_previous`|`spectate_previous`|Spectate the previous player|
|`set_position`|`set_position index x y`|Set saved camera position at index to be the position (x, y)|

### Console

|Command |  Syntax | Description|
| ------ | ------- | ---------- |
|`toggle_local_console`|`toggle_local_console`|Toggle the local console|
|`clear_local_console`|`clear_local_console`|Clear the local console|
|`dump_local_console`|`dump_local_console`|Write local console contents to a text file|
|`toggle_remote_console`|`toggle_remote_console`|Toggle the remote console|
|`clear_remote_console`|`clear_remote_console`|Clear the remote console|
|`dump_remote_console`|`dump_remote_console`|Write remote console contents to a text file|

### Demo recorder/player

|Command |  Syntax | Description|
| ------ | ------- | ---------- |
|`play`|`play filename`|Play the file in the demo player|
|`record`|`record filename`|Start a recording to the specified file (omit filename to use timestamp)|
|`stoprecord`|`stoprecord`|Stop the recording|
|`add_demomarker`|`add_demomarker`|Add a demo marker at the current time (while recording a demo)|

### Startup commands

To start Teeworlds on Windows with the debug console open, use `teeworlds.exe -c` or `teeworlds.exe --console`.
It is also possible to add the parameter to a windows shortcut.
