.. currentmodule:: DiscordCalc

Usage:
===============

Version Related Info
---------------------

.. data:: __version__

    A string representation of the version. e.g. ``'0.1.0'``.

DiscordCalc
-------
.. class:: General
    Class for `General` user permissions.
    .. attribute:: Administrator
    .. attribute:: Manage_Roles
    .. attribute:: Kick_Members
    .. attribute:: Create_Instant_Invite
    .. attribute:: Manage_Nicknames
    .. attribute:: Manage_Server
    .. attribute:: Manage_Channels
    .. attribute:: Ban_Members
    .. attribute:: Change_Nickname
    .. attribute:: all

        A shortcut for giving the bot all `General` user permissions.

.. class:: Text
    Class for `Text` channel permissions.
    .. attribute:: Read_Messages
    .. attribute:: Send_TTS_Messages
    .. attribute:: Embed_Links
    .. attribute:: Read_Message_History
    .. attribute:: Send_Messages
    .. attribute:: Manage_Messages
    .. attribute:: Attach_Files
    .. attribute:: Mention_Everyone
    .. attribute:: Use_External_Emojis
    .. attribute:: all

        A shortcut for giving the bot all `Text` channel permissions.

.. class:: Voice
    Class for `Voice` channel permissions.
    .. attribute:: Connect
    .. attribute:: Mute_Members
    .. attribute:: Move_Members
    .. attribute:: Speak
    .. attribute:: Deafen_Members
    .. attribute:: Use_Voice_Activity
    .. attribute:: all

        A shortcut for giving the bot all `Voice` channel permissions.
