rom chatterbot import ChatBot

bot = ChatBot(
    'Feedback Learning Bot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.BestMatch'
    ],
    input_adapter='chatterbot.input.TerminalAdapter',
    output_adapter='chatterbot.output.TerminalAdapter'
)

DEFAULT_SESSION_ID = bot.default_conversation_id

def get_feedback():
    from chatterbot.utils import input_function

    text = input_function()

    if 'yes' in text.lower():
        return True
    elif 'no' in text.lower():
        return False
    else:
        print('Please type either "Yes" or "No"')
        return get_feedback()


print('Type something to begin...')

while True:
    try:
        input_statement = bot.input.process_input_statement()
        statement, response = bot.generate_response(input_statement, DEFAULT_SESSION_ID)

        print('\n Is "{}" this a coherent response to "{}"? \n'.format(response, input_statement))

        if get_feedback():
            bot.learn_response(response, input_statement)

        bot.output.process_response(response)
        bot.storage.add_to_conversation(bot.default_session, statement, response)

    except (KeyboardInterrupt, EOFError, SystemExit):
        break
