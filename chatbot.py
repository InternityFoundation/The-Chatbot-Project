# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 12:15:21 2019

@author: user
"""

from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import os
bot = ChatBot('Test')

bot.set_trainer(ListTrainer) #set the trainer
#bot.train(conv) #train the bot
for _file in os.listdir(r'C:\Users\user\Desktop\ChatBOt'):
    chats = open(r'C:\Users\user\Desktop\ChatBOt/' + _file, 'r').readlines()
    bot.train(chats)
while True:
    request = input('You :')
    response = bot.get_response(request)
    
    print('Bot:', response)