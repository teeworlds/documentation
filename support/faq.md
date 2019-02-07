# FAQ

### Running the game

**Q: Why doesn't the game start? This is the first time I run it.**

**A:** The game uses OpenGL to do the acceleration. Make sure that you have installed the latest drivers for you graphics card.

**Q: The game stopped working, how do I fix it?**

**A:** Probably something has gone wrong with the config. The easiest thing to try is deleting the `settings.cfg`. See [Client Config](../client_config.md) to find the configuration file.

**Q: I have Graphical errors, white and rainbow textures, low FPS etc**

**A:** Try these following solutions:

- Delete the settings file. See [Client Config](../client_config.md) to find the configuration file.
- Make sure that you have the latest drivers for your graphics card installed.
- Make sure that you have unpacked everything.
- Make sure that you start the game from it's own directory.

### Server related

**Q: How do I setup a server?**

**A:** Take a look at the [Setting up a server page](../server_setup.md).

**Q: How do I setup a server on Mac OS X?**

**A:** Just click on the "Teeworlds Server" application bundle, you will then be prompted for a configuration file to use for the server.

**Q: Why isn't my server listed?**

**A:** The server or router isn't configured correctly.

- Make sure that you have the line `sv_register 1` in your configuration file.
- Make sure that you have forwarded ports from your router. http://portforward.com/ has a lot information on how to do this.
- Make sure that your router supports internal connections to the external ip, to be able to see a local server in the Internet tab.

**Q: Why doesn't my server start?**

**A:** You probably configured something wrong.

- Make sure you use a map that is in the data/maps-folder in the teeworlds directory, otherwise it wont work.
- Make sure the port isn't used.

### Hacking the source

**Q: How do I compile the source?**

**A:** There is a separate document for this located [here](../hacking.md).
