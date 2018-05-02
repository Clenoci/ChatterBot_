# ChatterBot_
Senior Design and Development Final project, fixing bugs and adding enhancements to ChatterBot, a project by gunthercox on Github 

Group
Paul Hanlon, Andrew Marchisio, Chris Lenoci, Mark Hawker
2018-4-11
COMP 490
Chatterbot Sitrep
A machine learning conversation bot
https://github.com/gunthercox/ChatterBot


Instructions on how to run ChatterBot:

## How it works

An untrained instance of ChatterBot starts off with no knowledge of how to communicate. Each time a user enters a statement, the library saves the text that they entered and the text that the statement was in response to. As ChatterBot receives more input the number of responses that it can reply and the accuracy of each response in relation to the input statement increase. The program selects the closest matching response by searching for the closest matching known statement that matches the input, it then returns the most likely response to that statement based on how frequently each response is issued by the people the bot communicates with.

## Installation

This package can be installed from [PyPi](https://pypi.python.org/pypi/ChatterBot) by running:

```
pip install chatterbot
```

## Basic Usage

```
from chatterbot import ChatBot

chatbot = ChatBot(
    'Ron Obvious',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
)

# Train based on the english corpus
chatbot.train("chatterbot.corpus.english")

# Get a response to an input statement
chatbot.get_response("Hello, how are you today?")

```



Issues we worked on:

Issue #682: Slack Input/Output Adapter
https://github.com/gunthercox/ChatterBot/issues/682
Andrew Marchisio // Paul Hanlon
Branch:SlackInputOutputAdapter  
Files: ChatterBot-master/chatterbot/Input/
Paul added: startbot_with8ball.py
Andrew added: startbot.py (w/ input adapter)


Issue #38: Weight responses by Identity 
https://github.com/gunthercox/ChatterBot/issues/38
Chris Lenoci
Branch:
Files:

Issue #1255: Get a list of all responses to a statement
https://github.com/gunthercox/ChatterBot/issues/1255
Mark Hawker
Branch: GetAll  
Files: ChatterBot-master/chatterbot/logic/AllResponse.py

Issue #962: Send multiple responses for a single input
https://github.com/gunthercox/ChatterBot/issues/962
Group Issue 
Branch:ChatterBot-master/chatterbot/logic/Multiple_Responses.py  
Files: Multiple_Responses.py  

Issue #1170: Unit Conversion Logic Adapter
https://github.com/gunthercox/ChatterBot/issues/1170 
Paul Hanlon
Branch:ChatterBot-master/chatterbot/logic/PH_UnitAdapter  
Files: PH_UnitAdapter.py  
Chris added:  
Files: unit_conversion.py 

Issue #1277: Datetime parsing does not recognize am/pm
https://github.com/gunthercox/ChatterBot/issues/1277
Chris Lenoci
Branch: ChatterBot-master/chatterbot/parsing.py   
Files: parsing.py 

Issue #920: Feedback Example 
https://github.com/gunthercox/ChatterBot/issues/920
Andrew Marchisio
Branch: ChatterBot-master/chatterbot/feedback.py
Files: feedback.py

