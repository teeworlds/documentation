# Client Settings

There are lots of client settings available, and this doc will guide you through them. If you are looking for client commands, read the [Client Commands](client_commands.md) doc. To find out how to find the config file, read the [Client Config](client_config.md) doc.

### Engine

| Setting       | Description   | Default value  |
| ------------- | ------------- | -------------- |
|`bindaddr`|Address to bind the client to|`""`|
|`password`|Password to the server you want to join|`""`|
|`logfile`|Filename to log all output to|`""`|
|`logfile_timestamp`|Add a time stamp to the log file's name|0|
|`console_output_level`|Adjust the amount of messages in the console |0|
|`show_console_window`|Show console window (0 = never, 1 = debug, 2 = release, 3 = always|1|
|`cl_auto_demo_max`|Maximum number of automatically recorded demos (0 = no limit)|10|
|`cl_auto_demo_record`|Automatically record demos|0|
|`cl_auto_screenshot`|Automatically take game over screenshot|0|
|`cl_auto_screenshot_max`|Maximum number of automatically created screenshots (0 = no limit)|10|
|`cl_auto_statscreenshot`|Automatically take screenshot of game statistics|0|
|`cl_cpu_throttle`|Throttles the main thread (sleep specified number of ms each tick)|0|
|`cl_editor`|View the editor|0|
|`cl_languagefile`|What language file to use|`""`|
|`cl_load_country_flags`|Load and show country flags|1|
|`cl_save_server_passwords`|Save server passwords (0 = never, 1 = only favorites, 2 = all servers)|1|
|`cl_show_welcome`|Show initial set-up dialog|1|
|`cl_version_server`|Server to use to check for new versions|`"version.teeworlds.com"`|

### Player

| Setting       | Description   | Default value  |
| ------------- | ------------- | -------------- |
|`player_clan`|Clan of the player|`""`|
|`player_color_body`|Player body color|0x1B6F74|
|`player_color_decoration`|Player decoration color|0x1B6F74|
|`player_color_eyes`|Player eyes color|0x0000FF|
|`player_color_feet`|Player feet color|0x1C873E|
|`player_color_hands`|Player hands color|0x1B759E|
|`player_color_marking`|Player marking color|0xFF0000FF|
|`player_country`|Country of the player|-1|
|`player_name`|Name of the player|`"nameless tee"`|
|`player_skin`|Player skin|`"default"`|
|`player_skin_body`|Player skin body|`"standard"`|
|`player_skin_decoration`|Player skin decoration|`""`|
|`player_skin_eyes`|Player skin eyes|`"standard"`|
|`player_skin_feet`|Player skin feet|`"standard"`|
|`player_skin_hands`|Player skin hands|`"standard"`|
|`player_skin_marking`|Player skin marking|`""`|
|`player_use_custom_color_body`|Toggles usage of custom colors for body|1|
|`player_use_custom_color_decoration`|Toggles usage of custom colors for decoration|1|
|`player_use_custom_color_eyes`|Toggles usage of custom colors for eyes|1|
|`player_use_custom_color_feet`|Toggles usage of custom colors for feet|1|
|`player_use_custom_color_hands`|Toggles usage of custom colors for hands|1|
|`player_use_custom_color_marking`|Toggles usage of custom colors for marking|1|

### Ingame

|Settings       | Description   | Default value  |
| ------------- | ------------- | -------------- |
|`cl_airjumpindicator`|Show double jump indicator|1|
|`cl_autoswitch_weapons`|Auto switch weapon on pickup|0|
|`cl_colored_broadcast`|Enable colored server broadcasts|1|
|`cl_customize_skin`|Use a customized skin|0|
|`cl_disable_whisper`|Disable completely the whisper feature.|0|
|`cl_filterchat`|Show chat messages from: 0=all, 1=friends only, 2=no one|0|
|`cl_motd_time`|How long to show the server message of the day|10|
|`cl_nameplates`|Show name plates|1|
|`cl_nameplates_always`|Always show name plates disregarding of distance|1|
|`cl_nameplates_size`|Size of the name plates from 0 to 100%|50|
|`cl_nameplates_teamcolors`|Use team colors for name plates|1|
|`cl_predict`|Use prediction for objects in the game world|1|
|`cl_predict_players`|Predict movements of other players|0|
|`cl_predict_projectiles`|Predict position of projectiles|0|
|`cl_show_easter_eggs`|0=never, 1=during easter, 2=always|1|
|`cl_show_local_time_always`|Always show local time|0|
|`cl_show_server_broadcast`|Show server broadcast|1|
|`cl_show_user_id`|Show the ID for every user|0|
|`cl_show_xmas_hats`|0=never, 1=during christmas, 2=always|1|
|`cl_showchat`|Show chat|1|
|`cl_showfps`|Show ingame FPS counter|0|
|`cl_showhud`|Show ingame HUD|1|
|`cl_showsocial`|Show social data like names, clans, chat etc.|1|
|`cl_statboard_infos`|Mask of info to display on the global statboard|1259|
|`cl_warning_teambalance`|Warn about team balance|1|

#### Camera

|Settings       | Description   | Default value  |
| ------------- | ------------- | -------------- |
|`cl_camera_smoothness`|Camera movement speed. 0=instant, 100=slow and smooth|0|
|`cl_camera_stabilizing`|Amount of camera slowdown during cursor movement|0|
|`cl_dynamic_camera`|Switches camera mode. 0=static camera, 1=dynamic camera|0|
|`cl_mouse_deadzone`|Zone that doesn't trigger the dynamic camera|300|
|`cl_mouse_followfactor`|Trigger amount for the dynamic camera|60|
|`cl_mouse_max_distance_dynamic`|Mouse max distance, in dynamic camera mode|1000|
|`cl_mouse_max_distance_static`|Mouse max distance, in static camera mode|400|

### Input

|Settings       | Description   | Default value  |
| ------------- | ------------- | -------------- |
|`inp_grab`|Disable OS mouse settings such as mouse acceleration, use raw mouse input mode|0|
|`inp_mousesens`|Ingame mouse sensitivity|100|
|`joystick_absolute`|Enable absolute joystick aiming ingame|0|
|`joystick_enable`|Enable joystick|0|
|`joystick_guid`|Joystick GUID which uniquely identifies the active joystick|`""`|
|`joystick_sens`|Ingame joystick sensitivity|100|
|`joystick_tolerance`|Joystick Axis tolerance to account for jitter|5|
|`joystick_x`|Joystick axis that controls X axis of cursor|0|
|`joystick_y`|Joystick axis that controls Y axis of cursor|1|
|`ui_mousesens`|Mouse sensitivity for menus/editor|100|
|`ui_joystick_sens`|Joystick sensitivity for menus/editor|100|

### Graphics

|Settings       | Description   | Default value  |
| ------------- | ------------- | -------------- |
|`gfx_asyncrender`|Do rendering asynchronously|0|
|`gfx_borderless`|Borderless window (not to be used with fullscreen)|0|
|`gfx_clear`|Clear screen before rendering|0|
|`gfx_display_all_modes`|Show all screen resolutions in graphics settings|0|
|`gfx_finish`|Wait for OpenGL to finish|1|
|`gfx_fsaa_samples`|Number of Full-Scene Antialiasing samples|0|
|`gfx_fullscreen`|Activate fullscreen|1|
|`gfx_high_detail`|Activate high details|1|
|`gfx_highdpi`|Use high dpi mode if available|1|
|`gfx_limitfps`|Limit fps|0|
|`gfx_maxfps`|Maximum fps (when limit fps is enabled)|144|
|`gfx_noclip`|Disable clipping|0|
|`gfx_screen`|Screen index|0|
|`gfx_screen_height`|Screen resolution height|600|
|`gfx_screen_width`|Screen resolution width|800|
|`gfx_texture_compression`|Activate texture compression|0|
|`gfx_texture_quality`|Use quality textures|1|
|`gfx_use_x11xrandr_wm`|Let SDL use the X11 XRandR window manager|1|
|`gfx_vsync`|Activate VSync|1|

### Sounds

|Settings       | Description   | Default value  |
| ------------- | ------------- | -------------- |
|`snd_async_loading`|Load sound files threaded|1|
|`snd_buffer_size`|Sound buffer size|512|
|`snd_enable`|Enable sounds|1|
|`snd_enable_music`|Play background music|1|
|`snd_init`|Initialize sound systems|1|
|`snd_nonactive_mute`|Mute Teewolds when inactive|0|
|`snd_rate`|Sound mixing rate|48000|
|`snd_volume`|Sound volume|100|

### Menu

|Settings       | Description   | Default value  |
| ------------- | ------------- | -------------- |
|`cl_menu_alpha`|Transparency of the menu background|25|
|`cl_menu_map`|Background map in the menu, auto = automatic based on season|`"auto"`|
|`cl_show_menu_map`|Display background map in the menu|1|
|`cl_show_start_menu_images`|Show start menu images|1|
|`cl_skip_start_menu`|Skip the start menu|0|

#### Camera

|Settings       | Description   | Default value  |
| ------------- | ------------- | -------------- |
|`cl_camera_speed`|Menu camera speed|5|
|`cl_rotation_radius`|Menu camera rotation radius|30|
|`cl_rotation_speed`|Menu camera rotations in seconds|40|

### User interface

|Settings       | Description   | Default value  |
| ------------- | ------------- | -------------- |
|`ui_autoswitch_infotab`|Switch to the info tab when clicking on a server|1|
|`ui_browser_page`|Interface serverbrowser page|5|
|`ui_joystick_sens`|Joystick sensitivity for menus/editor|100|
|`ui_mousesens`|Mouse sensitivity for menus/editor|100|
|`ui_server_address`|Interface server address (Internet page)|`"localhost:8303"`|
|`ui_server_address_lan`|Interface server address (LAN page)|`"localhost:8303"`|
|`ui_settings_page`|Interface settings page|0|
|`ui_wideview`|Extended menus GUI|0|

### Server & Demo browser

The individual server browser filter settings are store separately in the file `ui_settings.json` in the same folder as the config file.

|Settings       | Description   | Default value  |
| ------------- | ------------- | -------------- |
|`br_filter_string`|Server browser filter string|`""`|
|`br_sort`|Id of the column to sort after in the server browser|4|
|`br_sort_order`|Sort order (0 is ascending and 1 is descending) in the server browser|1|
|`br_demo_sort`|Id of the column to sort after in the demo browser|0|
|`br_demo_sort_order`|Sort order (0 is ascending and 1 is descending) in the demo browser|0|
|`br_max_requests`|Number of requests to use when refreshing server browser|25|

### Editor

| Setting       | Description   | Default value  |
| ------------- | ------------- | -------------- |
|`ed_color_grid_inner`|Color inner grid|0xFFFFFF26|
|`ed_color_grid_outer`|Color outer grid|0xFF4C4C4C|
|`ed_color_quad_pivot`|Color of the quad pivot|0x00FF00FF|
|`ed_color_quad_pivot_active`|Color of the active quad pivot|0xFFFFFFFF|
|`ed_color_quad_pivot_hover`|Color of the quad pivot when hovering over with the mouse cursor|0xFFFFFFFF|
|`ed_color_quad_point`|Color of quad points|0x00FF00FF|
|`ed_color_quad_point_active`|Color of active quad points|0xFFFFFFFF|
|`ed_color_quad_point_hover`|Color of quad points when hovering over with the mouse cursor|0xFFFFFFFF|
|`ed_color_selection_quad`|Color of the selection area for a quad|0xFFFFFFFF|
|`ed_color_selection_tile`|Color of the selection area for a tile|0xFFFFFF66|
|`ed_showkeys`|Editor shows which keys are pressed|0|
|`ed_zoom_target`|Zoom to the current mouse target|1|
