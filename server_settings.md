# Server Settings

There are lots of server settings to change all from the score limit, to the speed of the shotgun. This doc will show you what those are, not how to set up a server. Read the [Server Setup](server_setup.md) doc to learn that. For server commands, see the [Server Commands](server_commands.md) doc.

## Physics

To change the game's physics, read the [Server Tuning](server_tuning.md) doc.

## Engine

`*` means it can't be changed while running the server.

| Settings | Description | Default |
| -------- | ----------- | ------- |
|`bindaddr` *|Address to bind|`""`|
|`console_output_level`|Adjust the amount of messages in the console|0|
|`logfile`|Filename to log all output to|`""`|
|`logfile_timestamp`|Add a time stamp to the log file's name|0|
|`net_tcp_abort_on_close`|Aborts tcp connection on close|0|
|`password`|Password to connect to the server|`""`|
|`sv_auto_demo_max`|Maximum number of automatically recorded demos (0 = no limit)|10|
|`sv_auto_demo_record`|Automatically record demos|0|
|`sv_external_port` *|Port to report to the master servers (e.g. in case of a firewall rename)|0|
|`sv_high_bandwidth` *|Use high bandwidth mode. Doubles the bandwidth required for the server. LAN use only|0|
|`sv_hostname`|Server hostname|`""`|
|`sv_inactivekick`|How to deal with inactive clients (1=move player to spectator, 2=move to free spectator slot/kick, 3=kick)|2|
|`sv_inactivekick_spec`|Kick inactive spectators|0|
|`sv_inactivekick_time`|How many minutes to wait before taking care of inactive clients|3|
|`sv_map_download_speed`|Number of map data packages a client gets on each request|8|
|`sv_max_clients` *|Number of clients that can be connected to the server at the same time|12|
|`sv_max_clients_per_ip`|Maximum number of clients with the same IP that can connect to the server|12|
|`sv_motd`|Message of the day, shown in server info and when joining a server|`""`|
|`sv_name`|Name of the server|`"unnamed server"`|
|`sv_port` *|Port the server will listen on|8303|
|`sv_rcon_bantime`|The time a client gets banned if remote console authentication fails. 0 makes it just use kick|5|
|`sv_rcon_max_tries`|Maximum number of tries for remote console authentication|3|
|`sv_rcon_mod_password`|Remote console password for moderators (limited access)|`""`|
|`sv_rcon_password`|Password to access the remote console (if not set, rcon is disabled)|`""`|
|`sv_register`|Register server with master server for public listing|1|
|`sv_silent_spectator_mode`|Mute join/leave message of spectator|1|
|`sv_skill_level`|Skill level shown in serverbrowser (0 = casual, 1 = normal, 2 = competitive)|1|
|`sv_spamprotection`|Spam protection|1|

## Game

| Settings | Description | Default |
| -------- | ----------- | ------- |
|`sv_countdown`|Number of seconds to freeze the game in a countdown before match starts (0 enables only for survival gamemodes, -1 disables)|0|
|`sv_gametype`|Game type (dm, tdm, ctf, lms, lts) (This setting needs the map to be reloaded in order to take effect)|`dm`|
|`sv_map`|Map to use on the server|`dm1`|
|`sv_maprotation`|Maps to rotate between|`""`|
|`sv_match_swap`|Swap teams between matches|1|
|`sv_matches_per_map`|Number of matches on each map before rotating|1|
|`sv_player_ready_mode`|When enabled, players can pause/unpause the game and start the game on warmup via their ready state|0|
|`sv_player_slots`|Number of slots to reserve for players. Replaces `sv_spectator_slots`|8|
|`sv_powerups`|Allow powerups like ninja|1|
|`sv_respawn_delay_tdm`|Time needed to respawn after death in tdm gametype|3|
|`sv_scorelimit`|Score limit of the game (0 disables it)|20|
|`sv_strict_spectate_mode`|Restricts information like health, ammo and armour in spectator mode|0|
|`sv_teambalance_time`|How many minutes to wait before autobalancing teams|1|
|`sv_teamdamage`|Team damage|0|
|`sv_timelimit`|Time limit of the game (in case of equal points there will be sudden death) (0 disables)|0|
|`sv_tournament_mode`|Tournament mode. When enabled, players joins the server as spectator (2=additional restricted spectator chat)|0|
|`sv_vote_kick`|Allow voting to kick players|1|
|`sv_vote_kick_bantime`|The time to ban a player if kicked by vote. 0 makes it just use kick|5|
|`sv_vote_kick_min`|Minimum number of players required to start a kick vote|0|
|`sv_vote_spectate`|Allow voting to move players to spectators|1|
|`sv_vote_spectate_rejoindelay`|How many minutes to wait before a player can rejoin after being moved to spectators by vote|3|
|`sv_warmup`|Number of seconds to do warmup before match starts (0 disables, -1 all players ready)|0|

## External console

| Settings | Description | Default |
| -------- | ----------- | ------- |
|`ec_bindaddr`|Address to bind the external console to. Anything but 'localhost' is dangerous!|`localhost`|
|`ec_port`|Port to use for the external console||
|`ec_password`|External console password||
|`ec_bantime`|The time a client gets banned if econ authentication fails. 0 just closes the connection|0|
|`ec_auth_timeout`|Time in seconds before the the econ authentication times out|30|
|`ec_output_level`|Adjusts the amount of information in the external console|1|
