# Server Commands

To kick players from the server and to do other similar things, you have to use the server commands. This doc will show you these. If you want to know how to set up a server, read the [Server Setup](server_setup.md) doc. For server settings, see the [Server Settings](server_settings.md) doc.

## Engine

| Command | Syntax     | Description |
| ------- | ---------- | ----------- |
|`broadcast`|`broadcast text`|Broadcast the text|
|`echo`|`echo text`|Print a text in console|
|`eval_if`|`eval_if config comparison value command else command`|Execute command if condition is true|
|`exec`|`exec file`|Execute the commands in the file|
|`logout`|`logout`|Logout of rcon|
|`mod_command`|`mod_command command (access-level)`|Specify command accessibility for moderators|
|`mod_status`|`mod_status`|List all commands which are accessible for moderators|
|`record`|`record filename`|Start a recording to the specified file (omit filename to use timestamp)|
|`save_config`|`save_config [file]`|Save config to file (or default file if none)|
|`say`|`say text`|Send a chat message|
|`shutdown`|`shutdown [reason]`|Shut the server down|
|`stoprecord`|`stoprecord`|Stop the recording|
|`toggle`|`toggle config_option value1 value2`|Toggle config value|
|`tune`|`tune variable [value]`|Tune the variable or show its current value. See the [Server Tuning](server_tuning.md) doc|
|`tune_reset`|`tune_reset [variable]`|Reset all or one tuning variable to default|
|`tunes`|`tunes`|List all tuning variables and their values|

## Game

| Command | Syntax     | Description |
| ------- | ---------- | ----------- |
|`change_map`|`change_map mapname`|Change to the specified map|
|`force_teambalance`|`force_teambalance`|Force team balance|
|`lock_teams`|`lock_teams`|Lock/unlock teams|
|`paused`|`paused`|Pause/unpause game|
|`reload`|`reload`|Reload the map|
|`restart`|`restart [time]`|Restart the round (-1 = abort)|
|`set_team`|`set_team client_id team_id`|Move a player to a specific team (0 = red, 1 = blue, -1 = spectators)|
|`set_team_all`|`set_team_all team_id`|Move all players to a specific team|
|`shuffle_teams`|`shuffle_teams`|Shuffle the current teams|
|`swap_teams`|`swap_teams`|Swap the current teams|

## Players

| Command | Syntax     | Description |
| ------- | ---------- | ----------- |
|`ban`|`ban ip/id minutes`|Ban the ip from the server for the given time|
|`bans`|`bans`|Show a list of bans|
|`bans_save`|`bans_save file`|Save banlist in a file|
|`kick`|`kick id`|Kick the user with the specified id directly|
|`status`|`status`|List the player's id, ip, name and score|
|`unban`|`unban ip`|Unban the ip|

## Votes

| Command | Syntax     | Description |
| ------- | ---------- | ----------- |
|`add_vote`|`add_vote description command`|Add a vote option for the provided command with the provided description ( description is optional)|
|`clear_votes`|`clear votes`|remove all vote options|
|`force_vote`|`force_vote type option/player_id reason`|Force a certain vote to be executed immediately (type can be "option", "kick" or "spectate")|
|`remove_vote`|`remove_vote command`|remove a vote option|
|`vote`|`vote yes/no`|Force the end result of the vote to yes/no|
