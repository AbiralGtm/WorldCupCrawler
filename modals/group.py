import json


class Group:
    def __init__(self, _id, name, teams_ids):
        self._id = _id
        self.teams_ids = teams_ids
        self.name = name

    @classmethod
    def create_class_from_json(cls, group_json):
        _id = group_json['id']
        name = group_json['name']
        teams_ids = [int(i) for i in group_json['teams_ids']]
        return cls(_id, name, teams_ids)

    def to_json(self):
        data_dict = self.to_dict()
        data_json = json.dumps(data_dict)
        return data_json

    def to_dict(self):
        data_dict = {"id": self._id,
                     "name": self.name,
                     "teams_ids": self.teams_ids}
        return data_dict
