# Server Setup

This doc will guide you through the basics of setting up a server on Linux and Windows.

### Port forwarding

If you want other players to be able to play on the server via internet, you have to forward a port to the server. http://portforward.com/ has a lot information on how to do this.

### Configuring the server

To configure the server you need to create a .cfg-file so that the server knows what to do. Use your favorite text editor to create a config that uses the following syntax:

```setting value
setting2 value2
 ```
To find the available settings, read the URLTOServer Settings doc.

### Starting the server

To start the server you must specify a config for it to load. This is done by adding the flag "-f" to the server start command, like this:

 ```teeworlds_srv -f serverconfig.cfg
  ```

##### Windows

Start the command tolk by pressing Windows key+R, write "cmd" followed by enter, and use the command "cd" to get to the teeworlds directory.

When you get there, start the server by typing

 ```teeworlds_srv.exe -f serverconfig.cfg
  ```
where you replace "serverconfig.cfg" with the name of your config file.

##### Linux

Open up a terminal and use the command "cd" to enter the teeworlds directory.

To start the server, type

 ```teeworlds_srv -f serverconfig.cfg
  ```
where you replace "serverconfig.cfg" with the name of your config file.

### Remote console

To be able to execute server commands while playing, there is a remote console. To open it, press f2 (or the key you have chosen). You will now be asked to enter a password. If the console says that there are no password, you have to set the sv_rcon_password variable to enable that. Read more about it in the Server Settings doc.

To find out what commands that are available on the server, read the Server Commands doc.

### Support

If you have any questions, read the FAQ. If you can't find an answer, please use the support forum.