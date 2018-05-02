from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import logging
logging.basicConfig(level=logging.INFO)

bot = ChatBot(
	'Feedback Learning Bot',
	storage_adapter='chatterbot.storage.SQLStorageAdapter',
	logic_adapters=[
		'chatterbot.logic.BestMatch'
	],
	input_adapter='chatterbot.input.TerminalAdapter',
	output_adapter='chatterbot.output.TerminalAdapter'
	)


CONVERSATION_ID = bot.storage.create_conversation()


def get_feedback():
	from chatterbot.utils import input_function

	text = input_function()

	if 'yes' in text.lower():
		return True
	elif 'no' in text.lower():
		return False
	else:
		print("Please type either 'Yes' or 'No'")
		return get_feedback()

print('Type something to begin')

while True:
	try:
		input_statement = bot.input.process_input_statement()
		statement, response = bot.generate_response(input_statement, CONVERSATION_ID)
		print('\n Is "{}" this a coherent response to "{}"? \n'.format(response, input_statement))

		if get_feedback():
			bot.learn_response(response, input_statement)
			bot.storage.add_to_conversation(CONVERSATION_ID, statement, response)

		bot.output.process_response(response)

	except(KeyboardInterrupt, EOFError, SystemExit):
		break
