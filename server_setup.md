# Server Setup

This doc will guide you through the basics of setting up a server on Linux and Windows.

## Port forwarding

If you want other players to be able to play on the server via internet, you have to forward a port to the server (default is 8303). http://portforward.com/ has a lot information on how to do this.

The master server will warn if players can't connect.

## Configuring the server

To configure the server you need to create a .cfg-file so that the server knows what to do. Use your favorite text editor to create a config that uses the following syntax:

```
setting value
setting2 value2
```

To find the available settings, read the [Server Settings](server_settings.md) doc. You may also be interested in [Server Commands](server_commands.md).

You can find example configurations below.

## Starting the server

To start the server you must specify a config for it to load. This is done by adding the flag `-f` to the server start command, like this:
`teeworlds_srv -f serverconfig.cfg`

### Windows

Start the command tool by pressing `Win`+`R` write `cmd` followed by enter, and use the command `cd` to navigate to the teeworlds directory.

When you get there, start the server by typing `teeworlds_srv.exe -f serverconfig.cfg`
where you replace `serverconfig.cfg` with the name of your config file.

### Linux

Open up a terminal and use the command `cd` to enter the teeworlds directory.

To start the server, type
 `teeworlds_srv -f serverconfig.cfg`
where you replace `serverconfig.cfg` with the name of your config file.

## Remote console

To be able to execute server commands while playing, there is a remote console. To open it, press `F2` (or the key you have chosen). You will now be asked to enter a password. If you did not set up a password in your config, a random one will have been generated: check the server log.

To find out what commands that are available on the server, read the [Server Commands](server_commands.md) doc.

## Support

If you have any questions, read the [FAQ](support/faq.md). If you can't find an answer, please use the support forum.


## Example configurations

### Sample DM config
```
sv_name Teeworlds sample dm
sv_map dm1
sv_scorelimit 20
sv_timelimit 10
sv_gametype dm
sv_motd Teeworlds sample deathmatch configuration
sv_max_clients 12
sv_spectator_slots 10
```

### Sample CTF config
```
sv_name Teeworlds sample ctf
sv_map ctf2
sv_scorelimit 400
sv_gametype ctf
sv_motd Teeworlds sample capture the flag configuration
```

### Sample LTS config
```
sv_name Teeworlds sample LTS
sv_map lms1
sv_scorelimit 10
sv_gametype lts
sv_motd Teeworlds sample team survival configuration
```

## FAQ

**Q: How do I setup a LAN server?**

Set `sv_register` to 0. This will make sure that it doesn't show up on the internet tab.

**Q: Why doesn't my server show up in the server browser?**

You have probably not setup your router correctly. See http://portforward.com for help.
