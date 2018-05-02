from chatterbot.logic import LogicAdapter
from chatterbot.conversation import Statement
from pint import UnitRegistry

reg = UnitRegistry()

class UnitEvaluation(LogicAdapter):

	def __init__(self, **kwargs):
		super(UnitEvaluation, self).__init__(**kwargs)
		self.cache = {}

	def process(self, statement):
		input = statement.text
		if input in self.cache:
			cached_result = self.cache[input]
			self.cache = {}
			return cached_result
		result = convparse(input)
		# in every case except result = 1, the response needs to
		# be plural
		grammaticallycorrect = result + 's'
		return gramaticallycorrect


	def convparse(requests):
	# will likely need to work in a case for a simple "x to y" statemet
	# this will cover questions of the "How many xunits in n yunits?" type
	firststep = ["How many", "Howmany", "How much"]
#	middlestep = [' is ', ' in ']
	for i in range (0, len(firststep)):
		if firststep[i] in requests:
			requests2 = requests.replace(firststep[i], "")
	# not everyone likes numbers, so handle definite articles
	if ' an ' in requests2:
		requests3 = requests2.replace("an", "1")

	elif ' a ' in requests2:
		requests3 = requests2.replace("a", "1")
	else:
		requests3 = requests2

        if ' is ' in requests3:
                dst, src = requests3.split(' is ')
        elif ' in ' in requests3:
                dst, src = requests3.split(' in ')

	ans = reg(src).to(dst)
	return ans
