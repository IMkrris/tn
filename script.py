class Script(object):

    START_MSG = """<b>Hy {},

Im a simple bot which is designed and built for adding unlimited filters in any group
Hit <i>/help</i> for more information.</b>
"""


    HELP_MSG = """
<b>What is a filter bot?;</b>

<i>A bot were group admins can set replies for a particular keyword and the bot will automatically send preset replies whenever that keyword enountered in the chat.</i>

/start - <code>Check if I'm alive!</code>
/help - <code>Command help</code>
/about -<code>Something about me!</code>


<b>Filter Commands;</b>

<code>/add name reply</code>  -  Add filter for name

<code>/del name</code>  -  Delete filter

<code>/delall</code>  -  Delete entire filters (Group Owner Only!)

<code>/viewfilters</code>  -  List all filters in chat


<b>Connection Commands;</b>

<code>/connect groupid</code>  -  Connect your group to my PM. You can also simply use,
<code>/connect</code> in groups.

<code>/connections</code>  -  Manage your connections.


<b>Extras;</b>

/status  -  Shows current status of your bot (Auth User Only)

/id  -  Shows ID information

<code>/info userid</code>  -  Shows User Information. Use <code>/info</code> as reply to some message for their details!


@TN_Bots
"""


    ABOUT_MSG = """⭕️<b>My Name : TN Filter Bot</b>

⭕️<b>Creater :</b> @TN_Bots    

⭕️<b>Language :</b> <code>Python3</code>

⭕️<b>Library :</b> <a href='https://docs.pyrogram.org/'>Pyrogram 1.0.7</a> 

"""
