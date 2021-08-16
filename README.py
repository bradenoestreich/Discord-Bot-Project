"""
Hi there!

This bot will eventually have three primary features, each of which are currently
handled in my personal server by its own bot. They are as follows:

The first feature is an autoresponse protocol for messages sent by users. The bot
will parse the string content of messages sent by non-bot users and check it
against a key word or phrase. If the expression evaluates as true, it responds
with a relevant inside joke, quote, meme, imgur link, etc. The first iteration of
this feature is complete.

The second feature is a standard "reaction roles" feature, which is pretty
typical in a large server community. It will allow users to assign themselves
roles in the server with different permissions based on their interests. In short,
if the server has some mixture of people interested in movies, games, books, and
music, the reaction roles will allow each user to curate their own chat
experience with little cross-talk. This feature has yet to be implemented, by the
solution seems straightforward according to the available tools in the discord.py
library.

The third feature is a public music player. Users will be able to command the bot
to join a voice channel and play the audio from a YouTube link, allowing those in
the voice channel to listen to music semi-synchronously. This will be the last
feature implemented into the bot, and I have a much less clear picture of how to
do this.

Thanks for checking it out!
"""