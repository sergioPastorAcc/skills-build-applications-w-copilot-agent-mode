from django.core.management.base import BaseCommand
from octofit_tracker.api.models import User, Team, Activity, Leaderboard, Workout
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='Marvel', description='Marvel superheroes team')
        dc = Team.objects.create(name='DC', description='DC superheroes team')

        # Users
        users = [
            User(email='tony@stark.com', name='Tony Stark', team=marvel.name),
            User(email='steve@rogers.com', name='Steve Rogers', team=marvel.name),
            User(email='bruce@wayne.com', name='Bruce Wayne', team=dc.name),
            User(email='clark@kent.com', name='Clark Kent', team=dc.name),
        ]
        for user in users:
            user.save()

        # Activities
        Activity.objects.create(user='tony@stark.com', activity_type='run', duration=30, date=timezone.now().date())
        Activity.objects.create(user='steve@rogers.com', activity_type='cycle', duration=45, date=timezone.now().date())
        Activity.objects.create(user='bruce@wayne.com', activity_type='swim', duration=25, date=timezone.now().date())
        Activity.objects.create(user='clark@kent.com', activity_type='fly', duration=60, date=timezone.now().date())

        # Leaderboard
        Leaderboard.objects.create(team=marvel.name, points=150)
        Leaderboard.objects.create(team=dc.name, points=120)

        # Workouts
        Workout.objects.create(name='Pushups', description='Upper body strength', difficulty='Easy')
        Workout.objects.create(name='Sprints', description='Speed training', difficulty='Medium')
        Workout.objects.create(name='Deadlift', description='Strength training', difficulty='Hard')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
