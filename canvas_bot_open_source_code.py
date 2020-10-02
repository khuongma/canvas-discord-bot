#!/usr/bin/python3.6
import html, requests, json, discord
from bs4 import BeautifulSoup
from varname import nameof
from datetime import datetime
from pytz import timezone, utc

#currently this program only gets assignments, quizzes, discussion_topics from the canvas course

category = {
'assignments':'**!assignments** - list the assignments with points and due date',
'assignments []':'**!assignments #** - list the specific assignment details, example: **!assignments 2**',
'quizzes':'**!quizzes** - list the quizzes with points and due date',
'quizzes []':'**!quizzes #** - list the specific assignment details, example: **!quizzes 3**',
'discussion_topics':'**!discussion_topics** - list the discussion_topics with due date'

}
red, green, purple = 0x831000, 0x669d34, 0xb18cfe
discord_bot_token = '' #bot token here
canvas_channel = #discord channel id here
canvas_api = token = '' #canvas api you generated from your account
canvas_course_id = '' #course id found through the canvas api

def due_date(time):
    return datetime.strptime(timezone('US/Pacific').normalize(datetime.strptime(time,"%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=utc).astimezone(timezone('US/Pacific'))).strftime('%Y-%m-%d %I:%M:%S %p %Z'), '%Y-%m-%d %I:%M:%S %p %Z')

def current_time():
    date_format='%Y-%m-%d %I:%M:%S %p %Z'
    date = datetime.now(tz=utc)
    date = date.astimezone(timezone('US/Pacific'))
    pstDateTime=date.strftime(date_format)
    pstDateTime = datetime.strptime(pstDateTime, '%Y-%m-%d %I:%M:%S %p %Z')
    return pstDateTimes

def embed_function(Color, Name, result):
    embed = discord.Embed(color=Color)
    embed.add_field(name='**'+Name+'**', value=result, inline=True)
    embed.set_author(name='...\t\tCANVAS BOT\t\t...')
    return embed

def call_canvas_api(category): #assignments, quizzes, discussion_topics
    return requests.get('https://canvas.instructure.com/api/v1/courses/'+canvas_course_id+'/'+category+'?access_token='+canvas_api)

def get_category(category):
    result = ''
    type = call_canvas_api(category)
    name_title = 'title'
    if category == 'assignments':
        name_title = 'name'
    for i in range(len(type.json())):
        name = str(type.json()[i][name_title])
        if 'discussion_topics' not in category:
            due_at = due_date(type.json()[i]['due_at']) - current_time()
            points_possible = str(type.json()[i]['points_possible']) + ' points possible'
            result += str(i)+') *'+name+'* ['+points_possible+'] **due in '+str(due_at.days)+' day(s)**\n'
        elif 'discussion_topics' in category:
            result += str(i)+') *'+name+'*\n'
    return result+'\nCurrent datetime: **'+str(current_time())+'**'

def get_index(category, index):
    name_title = 'title'
    if category == 'assignments':
        name_title = 'name'
    type = call_canvas_api(category)
    def get_cat(cat):
        return type.json()[index][cat]
    desc = get_cat('description')
    desc = desc.encode("utf-8")
    desc = BeautifulSoup(desc).get_text()[0:900] + ' ...'
    due_days = due_date(get_cat('due_at')) - current_time()
    due_at = 'due at '+str(due_date(get_cat('due_at')))+'\nIN '+str(due_days.days)+' day(s)'
    name = get_cat(name_title)
    points = str(get_cat('points_possible'))+' points possible'
    return name+' ['+points+']\n\n'+desc+'\n\n**'+due_at+'**'

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.channel.id == canvas_channel:
        channel = client.get_channel(canvas_channel)
        if message.content == '!help':
            send = ''
            for key, value in category.items():
                send += value + '\n\n'
            await channel.send(embed=embed_function(purple,'Useful commands',send))
        elif message.content.startswith('!assignments') or message.content.startswith('!quizzes') or message.content.startswith('!discussion_topics'):
            cat = message.content.split(' ')
            print(cat)
            send = get_category(cat[0][1:])
            if len(cat) == 2:
                send = get_index(cat[0][1:], int(cat[1]))
                await channel.send(embed=embed_function(purple,message.content[1:].upper(),send))
            elif len(cat) == 1:
                await channel.send(embed=embed_function(purple,cat[0][1:].upper(),send))
            else:
                await channel.send(embed=embed_function(red, 'Error', 'Please try again!'))
        else:
            await channel.send(embed=embed_function(red, 'Error', 'Please try again! or use command **!help**'))

client.run(discord_bot_token)
