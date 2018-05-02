from __future__ import unicode_literals

from sqlalchemy import true

from chatterbot.logic import LogicAdapter
from chatterbot.conversation import Statement
from pint import UnitRegistry

reg = UnitRegistry()


def CheckIfInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


class UnitConversion(LogicAdapter):

    def __init__(self, **kwargs):
        super(UnitConversion, self).__init__(**kwargs)

        self.language = kwargs.get('language', 'ENG')
        self.cache = {}

    def can_process(self, statement):
        """
        Determines whether it is appropriate for this
        adapter to respond to the user input.
        """
        response = self.process(statement)
        self.cache[statement.text] = response
        return response.confidence == 1

    def process(self, statement):
        input = statement.text
        if input in self.cache:
            cached_result = self.cache[input]
            self.cache = {}
            return cached_result
        result = self.convparse(input)
        # in every case except result = 1, the response needs to
        # be plural
        gramaticallycorrect = result + 's'
        return gramaticallycorrect

    def convparse(requests):
        # will likely need to work in a case for a simple "x to y" statemet::: Attempted down below
        # this will cover questions of the "How many xunits in n yunits?" type
        firststep = ["How many", "Howmany", "How much","convert","Convert"]
        #	middlestep = [' is ', ' in ']
        for i in range(0, len(firststep)):
            if firststep[i] in requests:
                requests2 = requests.replace(firststep[i], "")

        # Value to differernt unit
        #if simple "x to y" statement just covert the first number into whatever the measurement is.
        if ' in 'in requests2 and CheckIfInt(requests2[0])==true:
            dst, src = requests2.split(' in ')
            ans =reg(src).to(dst)
            return ans
        # not everyone likes numbers, so handle definite articles
        if ' an ' in requests2:
            requests3 = requests2.replace("an", "1")

        elif ' a ' in requests2:
            requests3 = requests2.replace("a", "1")
        elif ' one ' in requests2:
            requests3=requests2 .replace("one","1")
        else:
            requests3 = requests2

        if ' is ' in requests3:
            dst, src = requests3.split(' is ')
        elif ' in ' in requests3:
            dst, src = requests3.split(' in ')

        ans = reg(src).to(dst)
        return ans


#original attempt to manually do all convertions, Paul found pint library.
    #      if ' Miles ' in requests2:
    #
    #
    #         elif ' Kilometers ' in requests2:
    #
    #         elif ' Feet ' in requests2:
    #
    #         elif ' Inches ' in requests2:
    #
    #         elif ' Centimeters ' in requests2:
    #
    #         elif ' Meters ' in requests2:
        #
    #         elif ' Pounds ' in requests2:
        #
    #         elif ' Kilograms ' in requests2:
        #
    #         elif '  ' in requests2:
        #
    #         elif ' Centimeters ' in requests2:
        #
    #         else:
    #             requests3 = requests2
    #
    #

    class EmptyDatasetException(Exception):

        def __init__(self, value='An empty set was received when at least one statement was expected.'):
            self.value = value

        @property
        def __str__(self):
            return repr(self.value)
