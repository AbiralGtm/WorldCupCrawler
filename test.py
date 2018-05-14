import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents
from modals.team import Team
from util import Util

cred = credentials.Certificate('serviceAccountKey.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://sportsapp-8c683.firebaseio.com/'
})

# As an admin, the app has access to read and write all data, regradless of Security Rules
ref = db.reference('worldcup/teams')
team_ref = ref.child('teams')

file_name = 'teams.json'
util = Util(file_name)

for team in util.get_json():
    team = Team.create_class_from_json(team)
    ref.push(team.to_dict())

