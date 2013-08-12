## What will be

##### An optional registration to uniquely identify you

You will have an id and password that you can login with to let other people know that you are you. This id will be shown on the scoreboard.

##### A way to find people

You will be able to find your friends, clan mates and enemies.

## What it won't be

##### It will never be a requirement

We want Teeworlds to be a game that you just can download and play without any hassle.

##### It will not be a mean to reserve a nick

You will never be able to reserve a nick. Your user name will be displayed along with your current nick name in the score board.

##### It will not be used to ban people

As it isn't a requirement, it will be quite useless to ban people by their user.

## Technical

##### Example Scenario

Items:

- A game server referred to as G
- An account server referred to as A located at users.example.com
- Two players called P1 and P2. P1 has the id of p1@users.example.com

Flow:

1. (action by user) P1 logins into A with his user name and password
2. (action by user) P1 finds G in the server browser and connects
3. (action by code) P1 report that it has connected to G and was assigned slot X
4. (action by user) P2 finds G in the server browser and connects
5. (action by code) P2 gets all the players on the server and their ids
6. (action by code) P2 connects to A and asks where player with id p1 is playing
7. (action by code) A responds with the game server address and the slot P1s client reported
8. (action by code) P2 highlights the nick with green if the server address and slot matches, else red
