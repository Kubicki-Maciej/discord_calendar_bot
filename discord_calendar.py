import datetime
import json

from datetime import timedelta, datetime

list_of_week_names = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']


class DataReader:

    def __init__(self, filename):

        self.data = json.load(open(filename))
        self.file_name = filename

    def add_event(self, event):
        self.data["events"].append(
            event
        )
        print(self.data)
        self.save_data()

    def get_last_event_id(self):
        if self.data['events'][-1]['event_id']:
            return self.data['events'][-1]['event_id']
        else:
            return 1

    def put_events_id(self):
        if self.data['events'][-1]['event_id']:
            return self.data['events'][-1]['event_id'] + 1
        else:
            return 1

    def add_user(self, username):
        if username not in self.data['users_signed']:
            self.data['users_signed'].append(
                username
            )
            self.save_data()

    def save_data(self):
        with open(self.file_name, 'w') as file:
            json.dump(self.data, file, intent=1)


class SingleEvent:
    def __init__(self, date, users):
        self.users = users
        self.date = date
        self.users_choice = {}
        self.create_users_choice()

    def switch_user_choice(self, user, choice):
        if self.users_choice[user] != choice:
            self.users_choice[user] = choice

    def create_users_choice(self):
        for user in self.users:
            self.users_choice[user] = "decline"

    def return_objects(self):
        return self.__dict__


class Events:

    def __init__(self, event_start, event_length, user_invited):
        self.event_id = DataReader('event.json').put_events_id()
        self.event_created = datetime.now().strftime('%d,%m,%y/%H:%m')
        self.event_start = event_start.strftime('%d,%m,%y')
        self.event_length = event_length
        self.user_invited = user_invited
        self.event_days = self.get_event_days(event_start)
        self.list_of_events = []

    def get_event_days(self, date_time):
        """
        :param x_days: number of days
        :param date_time: starting date time
        :return: list of next date objects
        """
        date_list = []
        for x in range(self.event_length):
            date_list.append((date_time + timedelta(days=x)).strftime('%d,%m,%y'))
        return date_list

    def create_event(self):
        for event in self.event_days:
            single_event_object = SingleEvent(event, self.user_invited)
            self.list_of_events.append(single_event_object.return_objects())

    def save_data(self):
        DataReader('event.json').add_event(self.return_objects())

    def return_objects(self):
        return self.__dict__

# e = Events(datetime.now(), 7, ['sattis', 'basanti', 'raxxar', 'bula'])