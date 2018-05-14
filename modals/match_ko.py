from datetime import datetime
import json
from dateutil.parser import parse

from const import country_to_id


def string_to_datetime(date_time):
    # 14 Jun 2018 - 18:00
    # date_time = datetime.strptime(date_time, "%d %b %Y -%I:%M")
    date_time = parse(date_time)
    return date_time


class Match_KO:
    def __init__(self, _id, date_time, stadium, city, teams):
        self.teams = teams
        self.city = city
        self.stadium = stadium
        self.date_time = date_time
        self._id = _id

    @classmethod
    def create_class_from_json(cls, json_data):
        _id = json_data['id'] if type(json_data['id']) is int else int(json_data['id'])
        date_time = json_data['date_time']
        stadium = json_data['stadium']
        city = json_data['city']
        teams = json_data['teams']
        return cls(_id, date_time, stadium, city, teams)

    def to_dict(self):
        return {"id": self._id,
                "date_time": self.date_time,
                "stadium": self.stadium,
                "city": self.city,
                "teams": self.teams}

    def to_json(self):
        data_dict = self.to_dict()
        data_json = json.dumps(data_dict)
        return data_json

