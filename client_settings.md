# Client Settings

There are lots of client settings available, and this doc will guide you through them. If you are looking for client commands, read the [Client Commands](client_commands.md) doc. To find out how to find the config file, read the [Client Config](client_config.md) doc.

### Engine Settings

|Settings      | Description           | Default value  |
| ------------- | ------------- | ----- |
|`player_name`      | Your nickname | nameless tee |
|`player_clan`      | The name of your clan      |    |
|`password` | Password to the server you want to join      |     |
|`logfile`  | Path to a logfile  |   |  
|`console_output_level`	| Adjust the amount of messages in the console | 0 |
|`cl_cpu_throttle` | Add a sleep after each tick | 0 |
|`cl_editor` | Activate the editor (Only ingame)	| 0 |
|`cl_auto_demo_record` | 	Activate automatic demo-reccording| 	0|
|`cl_auto_demo_max` | 	Maximum number of automatically recorded demos| 	10|
|`cl_auto_screenshot`| 	Activate automatic screenshots at the end of rounds| 	0|
|`cl_auto_screenshot_max`| 	Maximum number of automatically captured screenshots| 	10|
|`cl_eventthread`| 	Use thread to pump the events| 	0|
|`inp_grab`| 	Forceful input grabbing| 	0|
|`b_filter_string`| 	Server browser filter string| 	|
|`b_filter_full`| 	Filter out full servers| 	0|
|`b_filter_empty`| 	Filter out empty servers| 	0|
|`b_filter_spectators`| 	Filter out spectators from player numbers| 	0|
|`b_filter_friends`| 	Filter out servers with no friends| 	0|
|`b_filter_serveraddress`| 	Filter out servers that don't correspond to the entered address|  |
|`b_filter_pw`| 	Filter out password protected servers| 	0|
|`b_filter_ping`| 	Filter out servers with ping higher than this| 	999|
|`b_filter_gametype`| 	Filter out server that run other gametypes than this one| 	|
|`b_filter_pure`| 	Filter out non-standard servers in server browser| 	1|
|`b_filter_pure_map`| 	Filter out servers that run non-standard maps| 	1|
|`b_filter_compatversion`| 	Filter out non-compatible servers| 	1|
|`b_sort`| 	Id of the column to sort after| 	0|
|`b_sort_order`| 	Sort order (0 is ascending and 1 is descending)| 	0|
|`b_max_requestsv`| 	Number of requests to use when refreshing server browser| 	10|
|`snd_buffer_size`| 	Sound buffer size| 	512|
|`snd_rate`| 	Sound mixing rate| 	48000|
|`snd_enable`| 	Enable sound| 	1|
|`snd_volume`| 	Sound volume| 	100|
|`snd_nonactive_mute`| 	Mute Teewolds when inactive| 	0|
|`gfx_screen_width`| 	Screen resolution width| 	800|
|`gfx_screen_height`| 	Screen resolution height| 	600|
|`gfx_fullscreen`| 	Activate fullscreen| 	1|
|`gfx_alphabits`| 	Alpha bits for framebuffer (fullscreen only)| 	0|
|`gfx_color_depth`| 	Color bits for framebuffer (fullscreen only)| 	24|
|`gfx_clear`| 	Clear screen before rendering| 	0|
|`gfx_vsync`| 	Activate vertical synchrosnisation| 	1|
|`gfx_display_all_modes`| 	Show all screen resolutions in graphics settings| 	0|
|`gfx_texture_compression`| 	Activate texture compression| 	0|
|`gfx_high_detail`| 	Activate high details| 	1|
|`gfx_texture_quality`| 	Use quality textures| 	1|
|`gfx_fsaa_samples`| 	Number of Full-Scene Antialiasing samples| 	0|
|`gfx_refresh_rate`| 	Screen refresh rate| 	0|
|`gfx_finish`| 	Wait for OpenGL to finish| 	1|
|`inp_mousesens`	| Mouse sensitivity	| 100 |

### Game settings

|Settings      | Description           | Default value  |
| ------------- | ------------- | ----- |
|`cl_predict`| 	Use prediction| 	1|
|`cl_nameplates`| 	Show nameplates| 	0|
|`cl_nameplates_always`| 	Always show nameplates| 	0|
|`cl_nameplates_teamcolors`| 	Use teamcolors for nameplates| 	1|
|`cl_nameplates_size`| 	Size of nameplates in %| 	50|
|`cl_autoswitch_weapons`| 	Automatically switch weapon on pickup| 	0|
|`cl_showhud`| 	Display the hud| 	1|
|`cl_showfps`| 	Display fps| 	0|
|`cl_airjumpindicator`| 	Make feet darker when double jump has been used| 	1|
|`cl_threadsoundloading`| 	Load soundfiles threaded| 	0|
|`cl_warning_teambalance`| 	Warning if teams are unbalanced| 	1|
|`cl_mouse_deadzone`| 	Maximum distance the mouse can be moved without the camera moving| 	400|
|`cl_mouse_followfactor`| Set how fast the camera will follow the cursor| 	60|
|`cl_mouse_max_distance`| 	Maximum distance between cursor and player(pre 0.7.1 setting)| 	800|
|`cl_dynamic_camera`| 	Switches camera mode (0 = static camera, 1 = dynamic camera)| 	0|
|`cl_mouse_max_distance_dynamic`| 	Set how fast the camera will follow the cursor, in dynamic camera mode| 	1000|
|`cl_mouse_max_distance_static`| 	Set how fast the camera will follow the cursor, in static camera mode| 	400|
|`cl_filterchat`| 	Show chat messages (0 = all, 1 = friends only, 2 = no one)| 	0|
|`ed_showkeys`| 	Show the pressed key(s) in the editor| 	0|
|`cl_show_welcome`| 	Show the first launch popup| 	1|
|`cl_motd_time`| 	Time in seconds the motd is shown| 	10|
|`cl_version_server`| 	Version checking server| 	version.teeworlds.com|
|`cl_languagefile`| 	The language file to use	| |
|`player_use_custom_color`| 	Toggle use custom colors on/off| 	0|
|`player_color_body`| Player body color| 	65408|
|`player_color_feet`| 	Player feet color| 	65408|
|`player_skin`| 	Player skin| 	default|
|`ui_page`| 	Interface page| 	5|
|`ui_toolbox_page`| 	Interface toolbox page| 	5|
|`ui_server_address`| 	Interface server address	| localhost:8303|
|`ui_scale`| 	Interface scale| 	100|
|`ui_color_hue`| 	Interface color hue| 	160|
|`ui_color_sat`| 	Interface color saturation| 	70|
|`ui_color_lht`| 	Interface color lightness| 	175|
|`ui_color_alpha`| 	Interface alpha| 	228|
|`gfx_noclip`| 	Disable clipping| 	0|
|`cl_show_menu_map`| 	Display background map in the menu| 	1|
|`cl_camera_speed`| 	Set how fast the camera from the background map is moving| 	50|
|`cl_skip_start_menu`| 	Skip start menu| 	0|