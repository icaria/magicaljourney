from django.test import TestCase
from django.utils import timezone
from leaguebuddy.models import *
from leaguebuddy.tasks import *


# Create your tests here.
class AccountTestCase(TestCase):
    def setUp(self):
        League.objects.create(id=1, description="Diamond")
        Division.objects.create(id=1, description="V")
        Account.objects.create(id=21631196, league=League.objects.first(), division=Division.objects.first(), level=29,
                               last_updated=timezone.now(), is_online=1)
        Account.objects.create(id=40626864, league=League.objects.first(), division=Division.objects.first(), level=29,
                               last_updated=timezone.now(), is_online=1)

    def test_animals_can_speak(self):
        update()
