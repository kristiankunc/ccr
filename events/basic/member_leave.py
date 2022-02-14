from discord.ext import commands

class MemberLeave(commands.Cog):
    def __init__(self, client, config):
        self.client = client
        self.config = config

    @commands.Cog.listener()
    async def on_member_leave(self, member):
        membercount_channel = self.client.get_channel(self.config.membercount_channel)

        await membercount_channel.edit(name=f"Members: {membercount_channel.guild.member_count}")
        
def setup(client, config):
    client.add_cog(MemberLeave(client, config))