from bot.base import AbstractBot
from youtube_dl import YoutubeDL
import discord

class DJShen(AbstractBot):

    async def on_ready(self):
        pass
    
    async def on_message(self, msg):
        #cuando una persona ponga uwu.play <link de una cancion> 
        #que confirme que es un link correcto, que verifique que ha puesto el link, 
        #y en caso de cumplirse ninguna de las dos poner un mensaje de error
        if not msg.author.bot:
            if msg.content.startswith("uwu.play"):
                link = msg.content.split(' ')[1]
                vc = await self.join_channel(msg.author.voice.channel.id)
                await self.send_message(msg.channel.id, link)
                self.play_audio(link, vc)


    async def play_audio(self, link, voice_client):
        print("Estoy dentro")
        options = {
        'format': 'bestaudio/best',
        'outtmpl': 'audio.mp3',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192'
            }]
        }
        
        ydl = YoutubeDL()
        info = ydl.extract_info(link, download=False)
        url = info['url']
        source = self.getClient().FFmpegPCMAudio(url)
        voice_client.play(source)
        


def main():
    bot = DJShen()
    bot.run()

if __name__ == '__main__':
    main()