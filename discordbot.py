from discord.ext import commands
from discord.ext import tasks
import os
import traceback
import discord
from datetime import datetime 

token = os.environ['DISCORD_BOT_TOKEN']
CHANNEL_ID =698653628176531478  #チャンネルID

# 接続に必要なオブジェクトを生成
client = discord.Client()

@client.event
async def on_ready():
    """起動時に通知してくれる処理"""
    print('ログインしました')
    print(client.user.name)  # ボットの名前
    print(client.user.id)  # ボットのID
    print(discord.__version__)  # discord.pyのバージョン
    print('------')


# 60秒に一回ループ
@tasks.loop(seconds=60)
async def loop():
    # 現在の時刻
    now = datetime.now().strftime('%H:%M')
    
    if now == '00:26':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('=awoo') 
    
    if now == '00:28':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:cafe:699769671234355230>')  
    
    if now == '01:28':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('🥳🎶')     

    if now == '01:29':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('@everyone <:heart02:699580174911668225>are you ready Okay')     

    if now == '01:30':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/throw JPYN 66.66 6 AttenuationDistributed  <:good01:699581068285706301><:JPYNdisco:698471276498649168>⚾Plz receive→/catch')
    
    if now == '01:31':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/throw BGPT 420 6 EquallyDistributed  <:BGPT02:698471366004965406><:good:699580636448423936>⚾Plz receive→/catch')
    
    if now == '01:32':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/throw BEN 240 6 EquallyDistributed  <:BENKEICOIN04:698471407650209832><:benkeicoinsl:698471387064696833>⚾Plz receive→/catch')
    
    if now == '03:12':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:hai_kao:699072592987947117>💦')
    
    if now == '03:30':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:good01:699581068285706301>🎉 ') 
    
    if now == '03:34':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain BEN 444 AttenuationDistributed  <:BENKEICOIN04:698471407650209832><:benkeicoinsl:698471387064696833>Pls receive→/catch')  
    
    if now == '03:37':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/throw BGPT 666 8 EquallyDistributed  <:BGPT02:698471366004965406><:BGPT02:698471366004965406>Pls receive→/catch') 
            
    if now == '03:38':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/throw JPYN 333 8 AttenuationDistributed  <:JPYNdisco:698471276498649168><:JPYNdisco:698471276498649168><:JPYNdisco:698471276498649168>Pls receive→/catch')
    
    if now == '03:41':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('🥳')

    if now == '08:47':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:hai_kao:699072592987947117><:hai_kao:699072592987947117><:hai_kao:699072592987947117>')
        
    if now == '10:00':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:aloha:699581550777597992>Hello,how are you❓ ') 
        
    if now == '10:00':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:aloha:699581550777597992>') 
    
    if now == '10:30':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('🥳') 
     
    if now == '10:31':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/throw BEN 300 6 EquallyDistributed  <:BENKEICOIN04:698471407650209832><:benkeicoinsl:698471387064696833>⚾Plz receive→/catch')

    if now == '12:28':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('=dance') 
    
    if now == '12:29':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:good01:699581068285706301>🎉 ') 
    
    if now == '12:33':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain BEN 444 AttenuationDistributed  <:BENKEICOIN04:698471407650209832><:benkeicoinsl:698471387064696833>Pls receive→/catch')  
    
    if now == '12:35':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/throw BGPT 666 8 EquallyDistributed  <:BGPT02:698471366004965406><:BGPT02:698471366004965406>Pls receive→/catch') 
            
    if now == '12:36':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/throw JPYN 333 8 AttenuationDistributed  <:JPYNdisco:698471276498649168><:JPYNdisco:698471276498649168><:JPYNdisco:698471276498649168>Pls receive→/catch')
    
    if now == '12:40':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('=awoo') 
    
    if now == '14:16':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('🥳')
          
    if now == '21:31':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:gm:699792760651120671>🥳')

#ループ処理実行
loop.start()

@client.event
async def on_message(message):
    """メッセージを処理"""
    if message.author.bot:  # ボットのメッセージをハネる
        return

        
    if message.content == "<:hai_kao:699072592987947117> <:hai_kao:699072592987947117> <:hai_kao:699072592987947117>":
        # チャンネルへメッセージを送信
        await message.channel.send(f"<:hai_kao:699072592987947117> <:hai_kao:699072592987947117> <:hai_kao:699072592987947117>")  # f文字列（フォーマット済み文字列リテラル）
    
    if message.content == "<:ty:699857337980026930><:hai_kao:699072592987947117>":
        # チャンネルへメッセージを送信
        await message.channel.send(f"<:ty:699857337980026930><:hai_kao:699072592987947117>")  # f文字列（フォーマット済み文字列リテラル）
    
    elif message.content == "r/link":
        # リアクションアイコンを付けたい
        q = await message.channel.send("/link ")
        [await q.add_reaction(i) for i in ('⭕', '❌')]  # for文の内包表記

    elif message.content == "r/language":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /language EN ")
        [await q.add_reaction(i) for i in ('⭕', '❌')]  # for文の内包表記
              
    elif message.content == "r/accept":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /accept ")
        [await q.add_reaction(i) for i in ('⭕', '🔑')]  # for文の内包表記

    elif message.content == "b/benzan":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /info ben ")
        [await q.add_reaction(i) for i in ('⭕', '🔑')]  # for文の内包表記
        
    elif message.content == "b/jpynzan":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /info jpyn ")
        [await q.add_reaction(i) for i in ('⭕', '🔑')]  # for文の内包表記      
        
    elif message.content == "b/bgptzan":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /info bgpt ")
        [await q.add_reaction(i) for i in ('⭕', '🔑')]  # for文の内包表記
    
    elif message.content == "b/kenjzan":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /info kenj ")
        [await q.add_reaction(i) for i in ('⭕', '🔑')]  # for文の内包表記
             
    elif message.content == "b/sprtszan":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /info sprts ")
        [await q.add_reaction(i) for i in ('⭕', '🔑')]  # for文の内包表記 

    elif message.content == "b/29zan":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /info 29coin ")
        [await q.add_reaction(i) for i in ('⭕', '🔑')]  # for文の内包表記 
  
# Botの起動とDiscordサーバーへの接続
client.run(token)
