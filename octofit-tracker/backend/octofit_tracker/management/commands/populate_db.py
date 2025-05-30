from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Populate users
        User.objects.create(username="JohnDoe", email="john@example.com", password="password123")
        User.objects.create(username="JaneDoe", email="jane@example.com", password="password123")

        # Populate teams
        Team.objects.create(name="Team Alpha")
        Team.objects.create(name="Team Beta")

        # Populate activities
        Activity.objects.create(activity_type="Running", duration="00:30:00")
        Activity.objects.create(activity_type="Swimming", duration="01:00:00")

        # Populate leaderboard
        Leaderboard.objects.create(score=100)
        Leaderboard.objects.create(score=200)

        # Populate workouts
        Workout.objects.create(name="Push-ups", description="Do 20 push-ups")
        Workout.objects.create(name="Sit-ups", description="Do 30 sit-ups")

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
