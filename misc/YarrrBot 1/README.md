# YarrrBot 1

## Description

Yarrr m'hearty, I've heard tails of treasure hidden in a new pirate discord bot. go pillage YarrrBot's dm.

**Category:** misc

**Difficulty:** Easy

**Author:** Rhys

**Flag:** AHOY{55rf_y3_thund3r1ng_typh00n5}

## Exploit

The YarrrBot takes in a url and translates the text into pirate speak. As it is taking a url from the user and requesting it server side we can access webservers that the server has access to. This is called Server-Side Request Forgery (SSRF).

In this case there is a webserver running locally on the same server as YarrrBot that cannot be accessed from the outside world. YarrrBot can access it at http://localhost

1. Open a direct message chat with YarrrBot in the VECCTF discord server

2. Type in the command /yarrr http://localhost

3. Get the flag
