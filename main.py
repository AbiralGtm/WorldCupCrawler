from loaders import *

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate('serviceAccountKey.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://sportsapp-8c683.firebaseio.com/'
})


ref_team = db.reference('worldcup/teams')
ref_match = db.reference('worldcup/matches')
ref_match_ko = db.reference('worldcup/matches_ko')
ref_group = db.reference('worldcup/groups')

refs = [ref_team, ref_match, ref_match_ko, ref_group]
functions = [teams, matches, matches_ko, groups]

for f, ref in zip(functions, refs):
    f(ref)
    print("on ref : ", ref)
