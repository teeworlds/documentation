# Set up a server

- Configure firewall/nat/router to let though 8303 (or the port you want). The master server will warn if players can't connect. Check http://portforward.com for help on setting up your router.
- Create a configuration for your server. Add the settings you want (each line in the config represents a setting).
- Start the server by running `teeworlds_srv -f my_server_config.cfg`

### FAQ

**Q: How do I setup a LAN server?**

Set `sv_register` to 0. This will make sure that it doesn't show up on the internet tab.

**Q: Why doesn't my server show up in the server browser?**

You have probably not setup your router correctly. See http://portforward.com for help.

**Q: Why doesn't my 0.x.x-config work in 0.4.x?**

The configuration file syntax has changed. Try replaceing all the `=` with space, and read this documentation.

## Example configurations

### Sample DM config
```
sv_name Teeworlds sample dm
sv_map dm1
sv_scorelimit 20
sv_timelimit 10
sv_gametype dm
sv_rcon_password remember
sv_motd Teeworlds sample dm configuration
sv_max_clients 12
sv_spectator_slots 10
```
### Sample TDM config
```
sv_name Teeworlds sample tdm
sv_map dm6
sv_scorelimit 50
sv_gametype tdm
sv_rcon_password remember
sv_motd Teeworlds sample tdm configuration
```

### Sample CTF config
```
sv_name Teeworlds sample ctf
sv_map ctf2
sv_scorelimit 400
sv_gametype ctf
sv_rcon_password remember
sv_motd Teeworlds sample ctf configuration
```

## Server settings and commands

For server settings see [Server Settings](server_settings.md) and for server commands see [Server Commands](server_commands.md).
