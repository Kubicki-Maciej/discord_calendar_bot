import datetime
import json
from collections import namedtuple
from json import JSONEncoder
from datetime import timedelta, datetime


class DataReader:

    def __init__(self, filename):

        self.data = json.load(open(filename))
        self.file_name = filename

    def load_users(self):
        users = []
        for user in self.data['User']:
            users.append(user)
        return users

    def load_event(self):
        events = []
        for event in self.data['Event']:
            events.append(event)
        return events

    def load_calendar(self):
        calendar = []
        for events in self.data['Calendar']:
            calendar.append(events)
        return calendar

    def add_to_json(self, dic_name, data):
        self.data[dic_name].append(
            data
        )
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
        if username not in self.data['User']:
            self.data['User'].append(
                User(user_name=username).return_objects()
            )
            self.save_data()

    def add_event(self, event):
        if event not in self.data['User']:
            self.data['User'].append(
                Event(calendar_id=event).return_objects()
            )
            self.save_data()

    def save_data(self):
        with open(self.file_name, 'w') as file:
            json.dump(self.data, file, indent=1)


df = DataReader('event.json')


class CalendarManager:

    def __init__(self):
        self.users = []
        self.calendars = []
        self.event = []

    def load_users_from_DataReader(self):

        for user in df.load_users():
            obj_user = User(user['user_name'])
            obj_user.event_hook = user['event_hook']
            self.users.append(obj_user)

    def load_calendars_from_DataReader(self):

        for events in df.load_calendar():
            obj_events = Calendar()
            obj_events.register_events = events['register_events']
            self.users.append(obj_events)

    def load_event_from_DataReader(self):

        for event in df.load_event():
            obj_event = Event(event['id_event'])
            obj_event.event_created = Event['event_created']
            obj_event.users = Event['users']
            self.users.append(obj_event)


class User:

    def __init__(self, user_name):
        self.user_name = user_name
        self.event_hook = []

    def return_object(self):
        return self.__dict__

    def comment_other_user(self):
        pass

    def save_user_to_db(self):
        df.save_event_to_db('User',self.return_objects())

# https://pynative.com/python-convert-json-data-into-custom-python-object/
class UserEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


class Event:
    class_counter = 1

    def __init__(self, calendar_id):
        self.id_event = Event.class_counter
        self.event_created = datetime.now().strftime('%d,%m,%y/%H:%m')
        self.users = []
        Event.class_counter += 1


    def check_if_object_have_id(self):
        if self.id_event == 0:
            self.id_event = Event.class_counter
            Event.class_counter += 1

    def return_objects(self):
        return self.__dict__

    def add_user_to_event(self, user_obj):
        user_obj.event_hook.append(self.id_event)
        self.users.append(user_obj.return_object())

    def save_event_to_db(self):
        df.add_to_json('Event', self.return_objects())


class Calendar:

    def __init__(self):
        self.register_events = []

    def register_event(self, event):
        self.register_events.append(event)

    def return_objects(self):
        return self.__dict__

    def save_event_to_db(self):
        df.add_to_json('Calendar', self.return_objects())

    def calendar_normalize_to_disc(self):
        pass





""" create USER"""
us = User("Maciej")
usdwa = User("Aleksandra")

event_calendar = Calendar()

event_jeden = Event(event_calendar)
event_dwa = Event(event_calendar)

event_calendar.register_event(event_jeden)
event_calendar.register_event(event_dwa)

event_jeden.add_user_to_event(us)
event_jeden.add_user_to_event(usdwa)
event_dwa.add_user_to_event(us)
event_dwa.add_user_to_event(usdwa)

event_calendar.return_objects()



#
# class SingleEvent:
#     def __init__(self, date, users):
#         self.users = users
#         self.date = date
#         self.users_choice = {}
#         self.create_users_choice()
#
#     def switch_user_choice(self, user, choice):
#         if self.users_choice[user] != choice:
#             self.users_choice[user] = choice
#
#     def create_users_choice(self):
#         for user in self.users:
#             self.users_choice[user] = "decline"
#
#     def return_objects(self):
#         return self.__dict__
#
#
# class Events:
#
#     def __init__(self, event_start, event_length, user_invited):
#         self.event_id = DataReader('event.json').put_events_id()
#         self.event_created = datetime.now().strftime('%d,%m,%y/%H:%m')
#         self.event_start = event_start.strftime('%d,%m,%y')
#         self.event_length = event_length
#         self.user_invited = user_invited
#         self.event_days = self.get_event_days(event_start)
#         self.list_of_events = []
#
#     def get_event_days(self, date_time):
#         """
#         :param x_days: number of days
#         :param date_time: starting date time
#         :return: list of next date objects
#         """
#         date_list = []
#         for x in range(self.event_length):
#             date_list.append((date_time + timedelta(days=x)).strftime('%d,%m,%y'))
#         return date_list
#
#     def create_event(self):
#         for event in self.event_days:
#             single_event_object = SingleEvent(event, self.user_invited)
#             self.list_of_events.append(single_event_object.return_objects())
#
#     def save_data(self):
#         DataReader('event.json').add_event(self.return_objects())
#
#     def return_objects(self):
#         return self.__dict__
#
# # e = Events(datetime.now(), 7, ['sattis', 'basanti', 'raxxar', 'bula'])