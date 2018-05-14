from modals.group import Group
from modals.match import Match
from modals.match_ko import Match_KO
from modals.team import Team
from util import Util


def teams(ref):
    util = Util("teams.json")
    for team in util.get_json():
        team = Team.create_class_from_json(team)
        ref.push(team.to_dict())


def groups(ref):
    util = Util("groups.json")
    for group in util.get_json():
        group = Group.create_class_from_json(group)
        ref.push(group.to_dict())


def matches(ref):
    util = Util("matches.json")
    for match in util.get_json():
        match = Match.create_class_from_json(match)
        ref.push(match.to_dict())


def matches_ko(ref):
    util = Util("matches_ko.json")
    for match_ko in util.get_json():
        match_ko = Match_KO.create_class_from_json(match_ko)
        ref.push(match_ko.to_dict())
