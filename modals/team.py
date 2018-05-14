import json


class Team:
    def __init__(self, _id, name, flag_image, rank_fifa, appearances, group, titles, stats):
        self.stats = stats
        self.titles = titles if type(titles) is int else int(titles)
        self.group = group
        self.appearances = appearances if type(appearances) is int else int(appearances)
        self.rank_fifa = rank_fifa if type(rank_fifa) is int else int(rank_fifa)
        self.flag_image = flag_image
        self.name = name
        self.id = _id

    @classmethod
    def create_class_from_json(cls, team_json):
        _id = team_json['id']
        name = team_json['team_name']
        flag_image = team_json['flag_img']
        rank_fifa = team_json['team_info']['fifa_rank']
        appearances = team_json['team_info']['appearances']
        titles = team_json['team_info']['titles']
        # group = team_json['group']
        group = None
        # stats = team_json['stats']
        stats = None
        return cls(_id, name, flag_image, rank_fifa, appearances, group, titles, stats)

    def to_json(self):
        data_dict = self.to_dict()
        data_json = json.dumps(data_dict)
        return data_json

    def to_dict(self):
        data_dict = {"id": self.id,
                     "team_name": self.name,
                     "appearances": self.appearances,
                     "titles": self.titles,
                     "fifa_rank": self.rank_fifa,
                     "flag_img": self.flag_image}
        return data_dict
