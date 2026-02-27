from django.core.management.base import BaseCommand
from django.conf import settings
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']

        # Drop collections if they exist
        db.users.drop()
        db.teams.drop()
        db.activities.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Create unique index on email for users
        db.users.create_index([('email', 1)], unique=True)

        # Sample users
        users = [
            {'name': 'Iron Man', 'email': 'ironman@marvel.com', 'team': 'marvel'},
            {'name': 'Captain America', 'email': 'cap@marvel.com', 'team': 'marvel'},
            {'name': 'Spider-Man', 'email': 'spiderman@marvel.com', 'team': 'marvel'},
            {'name': 'Batman', 'email': 'batman@dc.com', 'team': 'dc'},
            {'name': 'Superman', 'email': 'superman@dc.com', 'team': 'dc'},
            {'name': 'Wonder Woman', 'email': 'wonderwoman@dc.com', 'team': 'dc'},
        ]
        db.users.insert_many(users)

        # Sample teams
        teams = [
            {'name': 'marvel', 'members': ['ironman@marvel.com', 'cap@marvel.com', 'spiderman@marvel.com']},
            {'name': 'dc', 'members': ['batman@dc.com', 'superman@dc.com', 'wonderwoman@dc.com']},
        ]
        db.teams.insert_many(teams)

        # Sample activities
        activities = [
            {'user': 'ironman@marvel.com', 'activity': 'run', 'distance': 5},
            {'user': 'batman@dc.com', 'activity': 'cycle', 'distance': 10},
            {'user': 'superman@dc.com', 'activity': 'swim', 'distance': 2},
        ]
        db.activities.insert_many(activities)

        # Sample leaderboard
        leaderboard = [
            {'team': 'marvel', 'points': 150},
            {'team': 'dc', 'points': 120},
        ]
        db.leaderboard.insert_many(leaderboard)

        # Sample workouts
        workouts = [
            {'user': 'ironman@marvel.com', 'workout': 'pushups', 'reps': 50},
            {'user': 'wonderwoman@dc.com', 'workout': 'squats', 'reps': 40},
        ]
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
