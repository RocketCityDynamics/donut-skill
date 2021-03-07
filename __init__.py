from mycroft import MycroftSkill, intent_file_handler


class Donut(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('donut.intent')
    def handle_donut(self, message):
        self.speak_dialog('donut')


def create_skill():
    return Donut()

