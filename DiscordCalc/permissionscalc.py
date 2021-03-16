# coding=utf-8
"""
The MIT License (MIT)

Copyright (c) 2015-2021 AraHaan

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

# Values to these comes from: https://discordapi.com/permissions.html
# Note: this must only be used to help generate a oauth2 bot url with custom permissions.
# Translated from JS to Python.


class General:
    """
        This Class contains Genral Discord Permissions.
    """
    def __init__(self):
        self.Administrator = eval(0x8)
        self.Manage_Roles = eval(0x10000000)
        self.Kick_Members = eval(0x2)
        self.Create_Instant_Invite = eval(0x1)
        self.Manage_Nicknames = eval(0x8000000)
        self.Manage_Webhooks = eval(0x20000000)
        self.Manage_Server = eval(0x20)
        self.Manage_Channels = eval(0x10)
        self.Ban_Members = eval(0x4)
        self.Change_Nickname = eval(0x4000000)
        self.Manage_Emojis = eval(0x40000000)
        self.View_Audit_Log = eval(0x80)
        self.View_Server_Insights = eval(0x80000)
        # This below Adds all of these permissions together for you.
        self.all = (self.Administrator + self.Manage_Roles + self.Kick_Members + self.Create_Instant_Invite + 
                    self.Manage_Nicknames + self.Manage_Webhooks + self.Manage_Server + self.Manage_Channels +
                    self.Ban_Members + self.Change_Nickname + self.Manage_Emojis + self.View_Audit_Log +
                    self.View_Server_Insights)


class Text:
    """
        This Class contains Text Channel Permissions.
    """
    def __init__(self):
        self.Read_Messages = eval(0x400)
        self.Send_TTS_Messages = eval(0x1000)
        self.Embed_Links = eval(0x4000)
        self.Read_Message_History = eval(0x10000)
        self.Use_External_Emojis = eval(0x40000)
        self.Send_Messages = eval(0x800)
        self.Manage_Messages = eval(0x2000)
        self.Attach_Files = eval(0x8000)
        self.Mention_Everyone = eval(0x20000)
        self.Add_Reactions = eval(0x40)
        # This below Adds all of these permissions together for you.
        self.all = (self.Read_Messages + self.Send_TTS_Messages + self.Embed_Links + self.Read_Message_History +
                    self.Use_External_Emojis + self.Send_Messages + self.Manage_Messages + self.Attach_Files +
                    self.Mention_Everyone + self.Add_Reactions)


class Voice:
    """
        This Class contains Voice Channel Permissions.
    """
    def __init__(self):
        self.Connect = eval(0x100000)
        self.Mute_Members = eval(0x400000)
        self.Move_Members = eval(0x1000000)
        self.Speak = eval(0x200000)
        self.Deafen_Members = eval(0x800000)
        self.Use_Voice_Activity = eval(0x2000000)
        self.Video = eval(0x200)
        self.Priority_Speaker = eval(0x100)
        self.View_Channel = eval(0x400)
        # This below Adds all of these permissions together for you.
        self.all = (self.Connect + self.Mute_Members + self.Move_Members + self.Speak + self.Deafen_Members +
                    self.Use_Voice_Activity + self.Video + self.Priority_Speaker + self.View_Channel)
