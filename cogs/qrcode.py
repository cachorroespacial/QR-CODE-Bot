import discord
from discord import app_commands
from discord.ext import commands
import pyqrcode
import os
import io

class QRCodeCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @app_commands.command(
        name="qrcode",
        description="Generates a QR Code from text or URL"
    )
    @app_commands.describe(
        content="The content (URL or text) to generate the QR Code",
        size="QR Code size (default: 10)",
        scale="QR Code scale (default: 5)"
    )
    async def qrcode(
        self,
        interaction: discord.Interaction,
        content: str,
        size: int = 10,
        scale: int = 5
    ):
        
        
        if not content.strip():
            await interaction.response.send_message("Please provide some content to generate the QR Code.", ephemeral=True)
            return
        
        
        if size < 1 or size > 20:
            await interaction.response.send_message("Size must be between 1 and 20.", ephemeral=True)
            return
            
        if scale < 1 or scale > 10:
            await interaction.response.send_message("Scale must be between 1 and 10.", ephemeral=True)
            return
        
        try:
            
            qr = pyqrcode.create(content)
            
            
            buffer = io.BytesIO()
            
            
            qr.png(buffer, scale=scale, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xff])
            buffer.seek(0)
            
            
            file = discord.File(buffer, filename="qrcode.png")
            
            
            embed = discord.Embed(
                title="Generated QR Code",
                description=f"Content: `{content}`",
                color=discord.Color.blue()
            )
            embed.set_image(url="attachment://qrcode.png")
            
           
            await interaction.response.send_message(embed=embed, file=file)
            
        except Exception as e:
            await interaction.response.send_message(f"An error occurred while generating the QR Code", ephemeral=True) # se quiser que mostre o erro, coloque '{e}'  /  if you want it to show the error, put '{e}'

async def setup(bot):
    await bot.add_cog(QRCodeCog(bot))