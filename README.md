<h1>Discord Bot created with Python</h1>

<h2> Using the Bot </h2>

Requires discord.py library.

First the bot must be online, this is done by executing the Python file.
Once it is online, a message is displayed with the username of the bot and it's status (online) in the server:



<img src= "images/pythonBot1.PNG" > 

Interacting with the bot is done with commands that follow a prefix (in this case I used '?').


<h2> Commands available </h2>

Currently the bot has commands to play 8ball game, mute and unmute users, clear messages, display number of users in a server, kick and ban users. These are done in the following way:

<h3> 8Ball game: </h3>

Ask questions to the bot like an 8Ball game (?8ball + question)

<img src= "images/pythonBot2.PNG" > 

<h3> Mute and unmute users: </h3>

Mute users, it will set them to a role of the server which doesn't have talking rights (?mute + username)

<img src= "images/pythonBot3.PNG" > 

Here you can see the user that was muted as his role was changed by the bot to "Muted".

<img src= "images/pythonBot4.PNG" > 

Muted users can also be unmuted again. (?unmute + username)

<img src= "images/pythonBot5.PNG" > 

As you can see, the "Muted" role is reverted to None. Using roles allows to administrate the priviledges of users in the server and facilitates moderation in bigger comunity servers.

<img src= "images/pythonBot6.PNG" > 

<h3> Kick and Ban users: </h3>

Users can also be kicked from the channels (?kick + username)

<img src= "images/pythonBot7.PNG" > 

Banning users will remove them from the channel and not allow them to re-join (?ban + username)

<img src= "images/pythonBot8.PNG" > 

User was removed from the server list.

<img src= "images/pythonBot9.PNG" > 


<h2> Further improvements/features </h2>

There are more features that I will add in the future such as automoderating channels and working with databases.

