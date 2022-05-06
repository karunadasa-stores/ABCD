class Script(object):
    G_ADMINS_TXT = """
<b>Group Admins</b>
Group Admin ලට group management bot කෙනෙක් විදිහට පාවිච්චි කරනවා නම්

<b>NOTE:</b>
• I should have admin privillage.
• These commands works only group.
• These commands can be used by Only Group admin.
    """
    ANY_TXT = """
<b>Subtitles වලට සම්බන්දයක් නෑ.. ප්‍රයෝජනවත් වෙන Options ට්කක් 🙂❤</b>️
"""
    START_TXT = """හෙලෝ {},
<b>ඔයාලා ඉල්ලන ඕනම Film, TV series එකක සිංහල උපසිරසි ඉක්මනටම හොයලා දෙන්න මට පුළුවන් 🙂👊..</b>"""

    HELP_TXT = """<b>පාවිච්චි කරන විදිහ දන්නැති අයට 🧐</b>"""

    ABOUT_TXT = """<b>➥ My name: {}
➥ Maintain by: <a href='https://t.me/Gavindu_Tharaka'>Gavindu Tharaka</a>
➥ Library: <a href='https://docs.pyrogram.org/'>Pyrogram</a>
➥ Language: Python 𝟹
➥ Data Base: <a href='https://www.mongodb.com/'>MongoDB</a>
➥ Bot Server: <a href='https://heroku.com'>Heroku</a>
➥ Build Status: v01.0.1 [ Beta ]"""

    SOURCE_TXT = """<b>Source:</b>

"""

    MANUALFILTER_TXT = """<b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and Dingdi will respond whenever a keyword is found the message

<b>NOTE:</b>
1. I should have admin privillage.
2. Only admins can add filters in a chat.
3. Alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - add a filter in chat.
• /filters - list all the filters of a chat.
• /del - delete a specific filter in chat.
• /delall - delete the whole filters in a chat (chat owner only)."""

    BUTTON_TXT = """<b>Buttons</b>

- tgmoviebot support both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. IMDb supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format.

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/josprojects)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""

    FILLINGS_TXT = """<b>Fillings</b>

You can also customise the contents of your message with contextual data. For example, you could mention a user by name in the filter message, or mention them in a filter!

<b>Supported fillings:</b>
- <code>{first}</code>: The user's first name.
- <code>{last}</code>: The user's last name.
- <code{username}</code>: The user's username.
- <code>{mention}</code>: Mentions the user with their firstname.
- <code>{id}</code>: The user's ID.
- <code>{dcid}</code>: The user's DC ID.
- <code>{chatname}</code>: The chat's name.
- <code>{query}</code>: Any Replied Message.

<b>Example:</b>
<b>- Save a filter using the mention.</b>
-> <code>/filter test Hello {mention} This Is your Username : {username} And This Is your ID : {id}.</code>
"""

    AUTOFILTER_TXT = """<b>ඔයාලගෙ උපසිරසි අපිට දෙන්නෙ කොහොමද?</b>
- මුලින්ම ඔයාගේ උපසිරසි තියෙන ගෲප් එකට හරි චැනල් එකට හරි බොට්ව ඇඩ් කරල ඇඩ්මින් දෙන්න.
- දැන් චැනල් එකේ අන්තිමට තියෙන මැසේජ් එක අපේ බොට් ට ෆෝවර්ඩ් කරන්න
"""

    CONNECTION_TXT = """<b>Connections</b>

- Used to connect bot to PM for managing filters 
- It helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - connect a particular chat to your PM.
• /disconnect  - disconnect from a chat.
• /connections - list all your connections."""

    AUTO_MANUAL_TXT = """<b>Filters</b>

<b>Select a filters type Below:</b>"""

    PASTE_TXT = """<b>Paste</b>

Paste some texts or documents on a website!

<b>Commands and Usage:</b>
• /paste [text] - paste the given text on Pasty
• /paste [reply] - paste the replied text on Pasty

<b>NOTE:</b>
• I should have admin privillage.
• These commands works on both pm and group.
• These commands can be used by any group member."""

    TGRAPH_TXT = """<b>TGraph & Paste</b>

Do as you wish with telegra.ph module!

<b>Commands and Usage:</b>
• /tgmedia or /tgraph - upload supported media (within 5MB) to telegraph.

<b>NOTE:</b>
• I should have admin privillage.
• These commands works on both pm and group.
• These commands can be used by any group member."""

    INFO_TXT = """<b>Information</b>

Get information about something!

<b>Commands and Usage:</b>
• /id - get id of a specified user.
• /info  - get information about a user.
• /json - get the json details of a message.

<b>NOTE:</b>
• I should have admin privillage.
• These commands works on both pm and group.
• These commands can be used by any group member."""

    TORRENT_TXT = """<b>Torrent Search</b>

<b>Commands and Usage:</b>
• /torrent or /tor <movie name>: Get Your Torrent Link From Various Resource.

<b>NOTE:</b>
• I should have admin privillage.
• These commands works on both pm and group.
• These commands can be used by any group member."""

    GTRANS_TXT = """<b>Google Translator</b>

Translate texts to a specific language!

<b>Commands and Usage:</b>
• /tr [language code][reply] - translate replied message to specific language.

<b>NOTE:</b>
• I should have admin privillage.
• These commands works on both pm and group.
• I can translate texts to 200+ languages."""

    SEARCH_TXT = """<b>IMDb</b>

Search many things without leaving telegram!

<b>Commands and Usage:</b>
• /imdb  - get the film information from IMDb source.
• /search  - get the film information from various sources.

<b>NOTE:</b>
• I should have admin privillage.
• More search tools can be found on inline.
• Those commands works on both pm and group."""

    PURGE_TXT = """<b>Purge</b>

Need to delete lots of messages? That's what purges are for!

<b>Commands and Usage:</b>
• /purge - delete all messages from the replied to message, to the current message.

<b>NOTE:</b>
• I should have admin privillage.
• These commands works on group.
• These commands can be used by Only admin."""

    RESTRIC_TXT = """<b>Restrictions</b>

Some people need to be publicly banned; spammers, annoyances, or just trolls.

This module allows you to do that easily, by exposing some common actions, so everyone will see!

<b>Commands and Usage:</b>
• /ban - ban a user.
• /tban - temporarily ban a user. Example time values: 4m = 4 minutes, 3h = 3 hours, 6d = 6 days, 5w = 5 weeks.
• /mute - mute a user.
• /tmute - temporarily mute a user. Example time values: 4m = 4 minutes, 3h = 3 hours, 6d = 6 days, 5w = 5 weeks.
• /unban or /unmute - unmute a user & unban a user.

<b>Examples:</b>
- Mute a user for two hours.
-> <code>/tmute @username 2h</code>

<b>NOTE:</b>
• I should have admin privillage.
• These commands works on group.
• These commands can be used by Only admin."""

    PIN_MESSAGE_TXT = """<b>Pin Message</b>

All the pin related commands can be found here; keep your chat up to date on the latest news with a simple pinned message!

<b>Commands and Usage:</b>
• /pin: Pin the message you replied to. Add 'loud' or 'notify' to send a notification to group members.
• /unpin: Unpin the current pinned message. If used as a reply, unpins the replied to message.

<b>NOTE:</b>
• I should have admin privillage.
• These commands works only group.
• These commands can be used by Only admin."""

    ADMIN_TXT = """<b>Admin Mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - to get the rescent errors.
• /stats - to get status of files in db.
• /delete - to delete a specific file from db.
• /users - to get list of my users and ids.
• /chats - to get list of the my chats and ids.
• /leave - to leave from a chat.
• /disable - do disable a chat.
• /ban_users - to ban a user.
• /unban_users - to unban a user.
• /channel - to get list of total connected channels.
• /broadcast - to broadcast a message to all users."""

    STATUS_TXT = """<b>Total Files:</b> <code>{}</code>
<b>Total Users:</b> <code>{}</code>
<b>Total Chats:</b> <code>{}</code>
<b>Used Storage:</b> <code>{}</code> MiB
<b>Free Storage:</b> <code>{}</code> MiB"""

    FORCESUB_TXT = """**♦️ READ THIS INSTRUCTION ♦️**

__🗣 In Order To Get The Movie Requested By You in Our Groups, You Will Have To Join Our Official Channel First. After That, Try Accessing That Movie Again From Our Group. I'll Send You That Movie Privately 🙈__

**👇 JOIN THIS CHANNEL & TRY AGAIN 👇**"""

    URL_SHORTNER_TXT = """<b>URL Shortner</b>

Some URLs is Shortner

<b>Commands and Usage:</b>
• /short <code>(link)</code> - I will send the shorted links.

<b>Example:</b>
<code>/short https://t.me/josprojects</code>

<b>NOTE:</b>
• I should have admin privillage.
• These commands works on both pm and group.
• These commands can be used by any group member."""

    TTS_TXT = """<b>Text to Speech</b>

A module to convert text to voice with language support.

<b>Commands and Usage:</b>
• /tts - Reply to any text message with language code to convert as audio.

<b>NOTE:</b>
• I should have admin privillage.
• These commands works on both pm and group.
• These commands can be used by any group member."""

    MUSIC_TXT = """<b>Music</b>

Music download modules, for those who love music.

<b>Commands and Usage:</b>
• /song or /mp3 (songname) - download song from yt servers.
• /video or /mp4 (songname) - download video from yt servers.

<b>YouTube Thumbnail Download</b>
• /ytthumb (youtube link)
<b>Example:</b> <code>/ytthumb https://youtu.be/h6PtzFYaMxQ</code>

<b>NOTE:</b>
• I should have admin privillage.
• These commands works on both pm and group.
• These commands can be used by any group member."""

    PASSWORD_GEN_TXT = """<b>Password Generator</b>

There Is Nothing To Know More. Send Me The Limit Of Your Password.
- I Will Give The Password Of That Limit.

<b>Commands and Usage:</b>
• /genpassword or /genpw <code>20</code>

<b>NOTE:</b>
• Only Digits Are Allowed
• Maximum Allowed Digits Till 84 
(I Can't Generate Passwords Above The Length 84)
• I should have admin privillage.
• These commands works on both pm and group.
• These commands can be used by any group member."""

    SHARE_TXT = """<b>Sharing Text Maker</b>

a bot to create a link to share text in the telegram.

<b>Commands and Usage:</b>
• /share (text or reply to message)

<b>NOTE:</b>
• I should have admin privillage.
• These commands works on both pm and group.
• These commands can be used by any group member."""

    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""

    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}"""

    ZOMBIES_TXT = """<b>Zombies</b>

<b>Kick incative members from group. Add me as admin with ban users permission in group.</b>

<b>Commands and Usage:</b>
• /inkick - command with required arguments and i will kick members from group.
• /instatus - to check current status of chat member from group.
• /inkick within_month long_time_ago - to kick users who are offline for more than 6-7 days.
• /inkick long_time_ago - to kick members who are offline for more than a month and Deleted Accounts.
• /dkick - to kick deleted accounts."""

    CREATOR_REQUIRED = """❗You have to be the group creator to do that."""

    INPUT_REQUIRED = "❗ **Arguments Required**"

    KICKED = """✔️ Successfully Kicked {} members according to the arguments provided."""

    START_KICK = """🚮 Removing inactive members this may take a while..."""

    ADMIN_REQUIRED = """❗I am not an admin here\n__Leaving this chat, add me again as admin with ban user permission."""

    DKICK = """✔️ Kicked {} Deleted Accounts Successfully."""

    FETCHING_INFO = """Collecting users information..."""

    STATUS = """{}\nChat Member Status**\n\n```recently``` - {}\n```within_week``` - {}\n```within_month``` - {}\n```long_time_ago``` - {}\nDeleted Account - {}\nBot - {}\nUnCached - {}
"""
