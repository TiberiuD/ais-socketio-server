import datetime


class DuplicateChecker:
    def __init__(self):
        self.message_list = {}
        self.last_cleanup = datetime.datetime.now()
        self.cache_duration = 30

    def is_duplicate(self, message):
        was_found = message in self.message_list

        current_time = datetime.datetime.now()
        self.message_list[message] = current_time

        if (current_time - self.last_cleanup).seconds > self.cache_duration:
            self.do_cleanup()

        return was_found

    def do_cleanup(self):
        messages_to_delete = []

        current_time = datetime.datetime.now()
        for message, timestamp in self.message_list.items():
            if (current_time - timestamp).seconds > self.cache_duration:
                messages_to_delete.append(message)

        for message in messages_to_delete:
            del self.message_list[message]
