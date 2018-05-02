from __future__ import unicode_literals

from .logic_adapter import LogicAdapter


class MultipleResponses(LogicAdapter):

    #A logic adapter that returns a response multiple responses to a single input, if applicable

    def get(self, input_statement):
        # Takes a statement string and a list of statement strings.
        #Returns the closest matching statements from the list.
        statement_list = self.chatbot.storage.get_response_statements()
        # Find the closest matching known statement
        highest_confidence = 0
        second_highest_confidence = 0
        for statement in statement_list:
            confidence = self.compare_statements(input_statement, statement)

            if confidence > highest_confidence:
                highest_confidence = confidence
                statement1 = statement

            elif confidence > second_highest_confidence and confidence < highest_confidence:
                second_highest_confidence = confidence
                statement2=statement

            response = statement1 + statement2
        return response

    def can_process(self, statement):
        """
        Check that the chatbot's storage adapter is available to the logic
        adapter and there is at least one statement in the database.
        """
        return self.chatbot.storage.count()

    def process(self, statement):
        response = self.get(self, statement)

        response_list = self.chatbot.storage.filter(
            in_response_to__contains=response.text
        )
        highest_confidence = 0
        for response in response_list:
            confidence = self.compare_statements(response, statement)
            if confidence >highest_confidence:
                highest_confidence = confidence


        if highest_confidence > .3:
            return response
        else :
            return "I'm sorry I don't know what to say to that"