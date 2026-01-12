from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='DC Superheroes')

        # Create users
        users = [
            User(name='Tony Stark', email='tony@marvel.com', team='Marvel'),
            User(name='Steve Rogers', email='steve@marvel.com', team='Marvel'),
            User(name='Bruce Wayne', email='bruce@dc.com', team='DC'),
            User(name='Clark Kent', email='clark@dc.com', team='DC'),
        ]
        for user in users:
            user.save()

        # Create activities
        Activity.objects.create(user=users[0], type='Running', duration=30)
        Activity.objects.create(user=users[1], type='Cycling', duration=45)
        Activity.objects.create(user=users[2], type='Swimming', duration=60)
        Activity.objects.create(user=users[3], type='Yoga', duration=20)

        # Create leaderboard
        Leaderboard.objects.create(team=marvel, points=150)
        Leaderboard.objects.create(team=dc, points=120)

        # Create workouts
        Workout.objects.create(name='Push Ups', description='Upper body exercise', suggested_for='Marvel')
        Workout.objects.create(name='Squats', description='Lower body exercise', suggested_for='DC')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
