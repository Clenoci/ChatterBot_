import os
import time
import re
from slackclient import SlackClient
from random import randint
from chatterbot import ChatBot

factlist = ["Jeff Gordon was born in 1970 in Vallejo, CA. Type 'do facts' again to learn even more trivia.", "Penicillin was discovered BY ACCIDENT in 1928 by Alexander Fleming.", "John Titor was an alledged time-traveler from 2036 who claimed on various Internet forums that he went back in time to retrieve an IBM 5100 for gov't purposes. He used these forums around 2000 to warn people of an impending Civil War 2 and World War III - which never came to fruition since he set us off on a different timeline by doing that.", "The Akatsuki-class was a class of 4 destroyers in the Imperal Japanese Navy. Built between 1931 and 1933, the Akatsuki-class consisted of the ships Akatsuki (Dawn), Hibiki (Echo), Inazuma (Lightning), and Ikazuchi (Thunder). They each weighed 1778 tons, were 118.5 meters long, and could accomodate crews of up to 233, with a max speed of 38 knots. Hibiki was the only one to survive WWII, whereafter she was surrenderd to the Soviets and renamed Verniy."]

# instantiate Slack client
slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))
# starterbot's user ID in Slack: value is assigned after the bot starts up
starterbot_id = None

# constants
RTM_READ_DELAY = 1 # 1 second delay between reading from RTM
EXAMPLE_COMMAND = "do"
MENTION_REGEX = "^<@(|[WU].+?)>(.*)"


# chatbot = ChatBot(
#     'ChatterBot',
#     trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
# )
#
# chatbot.train('chatterbot.corpus.english')
#
# # The following loop will execute each time the user enters input
# while True:
#     try:
#         response = chatbot.get_response(None)
#
#     # Press ctrl-c or ctrl-d on the keyboard to exit
#     except (KeyboardInterrupt, EOFError, SystemExit):
#         break
def post(self, request, *args, **kwargs):
    """
    Return a response to the statement in the posted data.
    """
    input_data = json.loads(request.read().decode('utf-8'))

    self.validate(input_data)

    conversation = self.get_conversation(request)

    response = self.chatterbot.get_response(input_data, conversation.id)
    response_data = response.serialize()

    return JsonResponse(response_data, status=200)
def parse_bot_commands(slack_events):
    """
        Parses a list of events coming from the Slack RTM API to find bot commands.
        If a bot command is found, this function returns a tuple of command and channel.
        If its not found, then this function returns None, None.
    """
    for event in slack_events:
        if event["type"] == "message" and not "subtype" in event:
            user_id, message = parse_direct_mention(event["text"])
            if user_id == starterbot_id:
                return message, event["channel"]
    return None, None

def parse_direct_mention(message_text):
    """
        Finds a direct mention (a mention that is at the beginning) in message text
        and returns the user ID which was mentioned. If there is no direct mention, returns None
    """
    matches = re.search(MENTION_REGEX, message_text)
    # the first group contains the username, the second group contains the remaining message
    return (matches.group(1), matches.group(2).strip()) if matches else (None, None)

def handle_command(command, channel):
    """
        Executes bot command if the command is known
    """
    # Default response is help text for the user
    default_response = "Not sure what you mean. Try *{}*.".format(EXAMPLE_COMMAND)

    # Finds and executes the given command, filling in response
    response = None
    # This is where you start to implement more commands!

    if command.startswith(EXAMPLE_COMMAND):
        response = "Sure...write some more code then I can do that!"

    elif "facts" in command:
        response = factlist[randint(0,3)]
#        response = Chatbot.bot.get_response(None) #this crashes the program when called


    # Sends the response back to the channel
    slack_client.api_call(
        "chat.postMessage",
        channel=channel,
        text=response or default_response
    )


if __name__ == "__main__":
    if slack_client.rtm_connect(with_team_state=False):
        print("Starter Bot connected and running!")
        # Read bot's user ID by calling Web API method `auth.test`
        starterbot_id = slack_client.api_call("auth.test")["user_id"]
        while True:
            command, channel = parse_bot_commands(slack_client.rtm_read())
            if command:
                handle_command(command, channel)
            time.sleep(RTM_READ_DELAY)
    else:
        print("Connection failed. Exception traceback printed above.")
