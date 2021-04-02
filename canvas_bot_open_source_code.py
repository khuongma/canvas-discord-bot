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
canvas_course_id = [''] #course id found through the canvas api
discord_bot_token = '' #bot token here
canvas_api = token = '' #canvas api you generated from your account

def due_date(time):
    return datetime.strptime(timezone('US/Pacific').normalize(datetime.strptime(time,"%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=utc).astimezone(timezone('US/Pacific'))).strftime('%Y-%m-%dT%I:%M:%SZ'), '%Y-%m-%dT%I:%M:%SZ')

def current_time():
    date_format='%Y-%m-%d %I:%M:%S'
    date = datetime.now(tz=utc)
    date = date.astimezone(timezone('US/Pacific'))
    pstDateTime=date.strftime(date_format)
    pstDateTime = datetime.strptime(pstDateTime, '%Y-%m-%d %I:%M:%S')
    return pstDateTime

def embed_function(Color, Name, result):
    embed = discord.Embed(color=Color)
    embed.add_field(name='**'+Name+'**', value=result, inline=True)
    embed.set_author(name='...\t\tCANVAS BOT\t\t...')
    return embed

def get_course_names():
    course_names = []
    for course in canvas_course_id:
        headers = {'Authorization': 'Bearer '+ token}
        course_names.append(requests.get('https://canvas.uw.edu/api/v1/courses/'+course, headers=headers).json()['name'])
    return course_names

def call_canvas_api(category): #assignments, quizzes, discussion_topics
    courses = []
    for course in canvas_course_id:
        headers = {'Authorization': 'Bearer '+ token}
        courses.append(requests.get('https://canvas.uw.edu/api/v1/courses/'+course+'/'+category, headers=headers))
    return courses

def get_category(category):
    result = ''
    course_names = get_course_names()
    api_response = call_canvas_api(category)
    name_title = 'title'
    if category == 'assignments':
        name_title = 'name'
    assignment_number = 0
    for item in range(len(api_response)):
        result += '**' + course_names[item] + '**\n'
        if 'discussion_topics' not in category:
            data = sorted(api_response[item].json(), key=lambda k : k['due_at'])
        else:
            data = sorted(api_response[item].json(), key=lambda k : k['created_at'])
        for i in range(len(data)):
            name = str(data[i][name_title])
            if 'discussion_topics' not in category:
                due_at = due_date(data[i]['due_at']) - current_time()
                points_possible = str(data[i]['points_possible']) + ' points possible'
                result += str(assignment_number)+') *'+name+'* ['+points_possible+'] **due in '+str(due_at.days)+' day(s)**\n'
            elif 'discussion_topics' in category:
                result += str(assignment_number)+') *'+name+'*\n'
            assignment_number += 1
    return result+'\nCurrent datetime: **'+str(current_time())+'**'


def get_assignment(api_response, index):
    assignment_number = 0
    for item in range(len(api_response)):
        if 'discussion_topics' not in category:
            data = sorted(api_response[item].json(), key=lambda k : k['due_at'])
        else:
            data = sorted(api_response[item].json(), key=lambda k : k['created_at'])
        for i in range(len(data)):
            if assignment_number == index:
                return data[i]
            assignment_number += 1


def get_index(category, index):
    name_title = 'title'
    if category == 'assignments':
        name_title = 'name'
    api_response = call_canvas_api(category)
    assignment = get_assignment(api_response, index)
    def get_cat(cat):
        return assignment[cat]
    if 'discussion_topics' not in category:
        desc = get_cat('description')
    else:
        desc = get_cat('message')
    desc = desc.encode("utf-8")
    desc = BeautifulSoup(desc).get_text()[0:900] + ' ...'
    if 'discussion_topics' not in category:
        due_days = due_date(get_cat('due_at')) - current_time()
        due_at = 'due at '+str(due_date(get_cat('due_at')))+'\nIN '+str(due_days.days)+' day(s)'
        points = str(get_cat('points_possible'))+' points possible'
    name = get_cat(name_title)
    if 'discussion_topics' not in category:
        return name+' ['+points+']\n\n'+desc+'\n\n**'+due_at+'**'
    else: 
        return '**'+name+'**'+'\n\n'+desc

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    channel = message.channel
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
            if len(send) > 1024:
                send = send[:1021] + '...'
            await channel.send(embed=embed_function(purple,cat[0][1:].upper(),send))
        else:
            await channel.send(embed=embed_function(red, 'Error', 'Please try again!'))

client.run(discord_bot_token)
