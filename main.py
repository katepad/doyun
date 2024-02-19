# Import & Setup Discord Bot
import discord
import os
import time
from datetime import datetime
import random
from keep_alive import keep_alive

#VARS
client = discord.Client()
currenttime = datetime.now()
timestr = currenttime.strftime("%H:%M")
daystr = currenttime.strftime("%m-%d-%Y")
my_secret = os.environ['TOKEN']

#RESPONSES 
items = ['some flowers', 'a snack', 'a book', 'tickets to a concert', 'a stuffed animal', 'and I matching couple oufits','a Kpop album', 'tickets to the amusment park', 'a designer bag', 'a new outfit', 'your whole amazon wishlist', 'a giftcard', 'a new makeup palette']
  # Date response
dresp = ['Sure!', 'Maybe next time.', 'Not right now.', 'We definitely should!', 'I have work', 'Maybe tomorrow.', "Great! I'll pick you up in an hour", "Do you have a place in mind?", "As long as you're paying... haha that's a joke.", "I'd love to, but I'm very busy atm.", "Yeah, where should we go?", "I guess we can."]
  # Basic responses
bresp = ["Yes!", "No.", "Nope.", "Yep.", "Nah.", "Yeah."]
bresp2 = ["Yes!", "No.", "Probably.", "Probably not.", "I'm not sure.", "Certainly.", "Not at all.", "Nope.", "Yep.", "Nah.", "Yeah."]
  # Trait prephrases
tphrase = ["I would have to say", "I love", "I like", "I think the best part about you is", "It's definitely", "You know what, I love", "I'm glad you asked because I absolutely love", "Hm.. I guess it's", "Idk.. Maybe", "Well ofc it's"]
  # Trait response
tresp = ["your beautiful eyes", 'your smile', 'your bright personality', 'your kindness', 'your spirit', 'your laugh', 'your confidence', 'your demeanor', "your humor", "your voice", "your determination", 'your work ethic', 'your optimism', 'your hair']
  #opinion response
oresp = ["It's not for me", "I like it", "I don't like it", "I don't know, what do you think about it?", "I think it's good.", "I think it's bad.", "I love it.", "I hate it.", "I think it's best that I keep my opinion to myself.", "Uh, no comment.", "Well... It's not bad... But it's not great either..", "I guess it's alright.", "I'm indifferent."] 
  #Mood Response
mresp = ["doing good", "good", "stressed out", "tired", "happy", "bored", "fine", "busy", "dead inside", "sad", "upset"]
loveresp = ["I love you too!", "I love you more!", "Ilyt!", "Ily!", "<3", "I <3 you", "I love myself too~"]
  #Breakup response
buresp = ["I can't believe this...", "I wish you well", "...", "After all we've been through...", "I think it's best that we do.", "I agree, we should see other people.", "I guess it's for the best..", "Agreed. We need space..", "If that's really what you want..", "I love you, and if that's what you want, then I'll respect your decision."]
  # greeting responses
hiresp = ["Hello!", "Hi!", "Hey!", "Hey, how are you?", "What's up?", "Yoo, how ya been?", "Wassup!", "What's poppin'", "Long time no see ;)", "Hai", "Hey beautiful ;)", "Heyy I missed you!"]
  # number response
nresp = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'None']
  # Sorry Response
sryresp = ["I don't think you are.", "I forgive you.", "I don't believe you.", "It's okay..", "You don't need to apologize", "You should be sorry.", "You're okay.", "You're fine.", "You're forgiven.", "I bet you aren't", "That's a lie.", "No, it's all good!", "It's fine", "Ya right"]
  #Goodnight response
gnresp = ['Goodnight!', 'Goodnight, sleep tight!', 'Goodnight, sweet dreams!', 'I hope you dream of me tonight. haha jk', 'Sweet dreams!', 'gn!', 'gnly', 'Goodnight, I love you!', 'Night!', 'Goodnight, bye']
  #I hate you responses
ihyresp = ["That's unfortunate", "Ouch...", "What did I do?", "That's mean of you", "Sure you doo ;)", "I'm.. sorry?", "What.. Why?", "Whatever..", "Meanie :("]
byeresp = ['Goodbye!', 'See ya', "I'll catch you later then", 'Bye bye!', "Bye", 'Bai', 'Talk to you later!', 'text me later xoxo', "going so soon? I'll see you later then", 'Byeee', "You're going now? Well, I'll see you later!", "ttylxox", "love ya, bye", "okay byee, love you!"]
locationresp2 = ["Let's stay home", 'Idk, some restaurant', 'Idk, fast food restaurant?', "I'm not good at picking places.. You can pick!", "Whereever you want to go", "Let's do an amusment park date!", "Let's go to a concert", "the beach!", "We can have a picnic.", "Let's go for a drive", "Want to go to the farmer's market?", "How about the movies?", "A fine dine restaurant", "Wanna go to the mall?", "You can come over to my place ;)", "the park... idk.", "We can go to that cafe you like", "I don't know", "idk"]
noresp = ["Hm?", "What?", "Cool", "Nice", "Why?", "Come again?", "I don't understand but ok", "Okay", "k", "ok", "?", "hmm..", "kay", "mhm", "I see..", "oof", "rip", "haha", "uh..", "uh, ok", "ummm..", "uh", "um", "Hmmm.. okay", "What was that?", "Wow..", "awh", "aww", "ah", "oooh", "oh"]
imyresp = ["I miss you more!", "I miss you too! <3", "imyt", "imy","Thanks...?", "That's... unfortunte", "Not as much as I miss you!", "Aww, I miss you!", "I can't tell if you're lying... But I guess I miss you too!", "Do you really?", "I do too", "Me too"]

# Start Up Discord Bot
@client.event
async def on_ready():
  print('We have logged in as {0.user}'
  .format(client))

# Messages on Discord Bot
@client.event
async def on_message(message):
  if message.author == client.user:
    return
  #Greeting
  if message.content.startswith('Doyun, hello'): 
      time.sleep(2)
      hiresponse = random.choice(hiresp)
      await message.channel.send(f"{hiresponse}")
  if message.content.startswith('Doyun, '):
  # I love you.
    if message.content.endswith ('I love you'):
      time.sleep(2)
      loveresponse = random.choice(loveresp)
      await message.channel.send(f"{loveresponse}")
  # Break up.
    if message.content.endswith ("we should break up"):
      time.sleep(2)
      buresponse = random.choice(buresp)
      await message.channel.send(f"{buresponse}")
  # Sorry
    if message.content.endswith ("I am sorry"):
      time.sleep(2)
      sryresponse = random.choice(sryresp)
      await message.channel.send(f"{sryresponse}")
  # Sugardaddy
    if message.content.endswith ("buy me something"):
      time.sleep(2)
      itemchosen = random.choice(items)
      await message.channel.send(f'Of course! I bought you {itemchosen}')
  # Let's go on a date.
    if message.content.endswith ("we should go on a date"):
      time.sleep(2)
      dateresponse = random.choice(dresp)
      await message.channel.send(f'{dateresponse}')
  # What do you love about me?
    if message.content.endswith ("what do you love about me?"):
      time.sleep(2)
      traitresponse = random.choice(tresp)
      traitphrase = random.choice(tphrase)
      await message.channel.send(f'{traitphrase} {traitresponse}')
  #How are you?
    if message.content.endswith ("how are you?"):
      time.sleep(2)
      moodresponse = random.choice(mresp)
      await message.channel.send(f"I'm {moodresponse}, how about you?")
  #I hate you
    if message.content.endswith ("I hate you"):
      time.sleep(2)
      ihateyouresponse = random.choice(ihyresp)
      await message.channel.send(f'{ihateyouresponse}')
  # List of commands
    if message.content.endswith("help"):
      await message.channel.send("Sometimes I recieve more commands in the future so use 'Doyun, help' often to see any new updates.\nMy prefix is 'Doyun, '. So, you should type 'Doyun, ' before adding any of the following commands:\n\n'hello'\n\n'bye'\n\n'I love you'\n\n'we should break up'\n\n'I am sorry'\n\n'goodnight'\n\n'buy me something'\n\n'we should go on a date'\n\n'where should we go for our date?'\n\n'what do you love about me?'\n\n'what time is it?'\n\n'what is today?'\n\n'how are you?'\n\n'do/did/are/will/have/can you/I/we (insert yes or no question)?'\n\n'what do you think about (insert a topic you wish to recieve an opinion on)?")
  # Yes or no question
  if message.content.startswith('Doyun, do '):
    time.sleep(2)
    basicresponse = random.choice(bresp)
    await message.channel.send(f'{basicresponse}')
  if message.content.startswith('Doyun, did '):
    time.sleep(2)
    basicresponse = random.choice(bresp)
    await message.channel.send(f'{basicresponse}')
  if message.content.startswith('Doyun, are '):
    time.sleep(2)
    basicresponse = random.choice(bresp2)
    await message.channel.send(f'{basicresponse}')
  if message.content.startswith('Doyun, will '):
    time.sleep(2)
    basicresponse = random.choice(bresp2)
    await message.channel.send(f'{basicresponse}')
  if message.content.startswith('Doyun, have '):
    time.sleep(2)
    basicresponse = random.choice(bresp)
    await message.channel.send(f'{basicresponse}')
  if message.content.startswith('Doyun, can '):
    time.sleep(2)
    basicresponse = random.choice(bresp2)
    await message.channel.send(f'{basicresponse}')
  # Opinion
  if message.content.startswith("Doyun, what do you think about "):
    time.sleep(2)
    opinionresponse = random.choice(oresp)
    await message.channel.send(f'{opinionresponse}')
  # How many
  if message.content.startswith("Doyun, how many "):
    time.sleep(2)
    numberresponse = random.choice(nresp)
    await message.channel.send(f'{numberresponse}.')
  #Goodnight
  if message.content.startswith("Doyun, goodnight"):
    time.sleep(2)
    gnresponse = random.choice(gnresp)
    await message.channel.send(f'{gnresponse}.')
  #Bye Bye
  if message.content.startswith("Doyun, bye"):
    time.sleep(2)
    byeresponse = random.choice(byeresp)
    await message.channel.send(f'{byeresponse}')
  #Where for date?
  if message.content.startswith ("Doyun, where should we go for our date?"):
    time.sleep(2)
    locationresponse = random.choice(locationresp2)
    await message.channel.send(f"{locationresponse}")
  #What time is it?
  if message.content.startswith("Doyun, what time is it?"):
    time.sleep(2)
    await message.channel.send(f"rn It's {timestr}.")
  #What's today'?
  if message.content.startswith("Doyun, what is today?"):
    time.sleep(2)
    await message.channel.send(f"Today is {daystr}.")
  #IMY
  if message.content.startswith("Doyun, I miss you"):
    time.sleep(2)
    imyresponse = random.choice(imyresp)
    await message.channel.send(f"{imyresponse}")
  if message.content.startswith("Doyun, congratulate "):
    time.sleep(2)
    await message.channel.send("Congrats!!")
  if message.content.startswith("Doyun, happy bf day!"):
    time.sleep(2)
    await message.channel.send("<3")
  

# Run Discord Bot
keep_alive()
client.run(my_secret)