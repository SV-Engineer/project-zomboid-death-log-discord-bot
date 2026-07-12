'''! @file discord_user_control.py

'''

class DiscordUserControl
  def __init__(self, bot_handle, name=__name__):
        r''' @fn def __init__(self, name=__name__)
        @brief Class constructor
        '''
        super.__init__(name)
        self.__bot_handle = bot_handle

  def list_members(ctx):
    for member in ctx.guild.members:
        print(member.name, member.id)
