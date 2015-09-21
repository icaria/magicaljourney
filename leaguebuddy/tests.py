from django.test import TestCase
from django.utils import timezone
from leaguebuddy.models import *
from leaguebuddy.tasks import *

# Create your tests here.
class AccountTestCase(TestCase):
    def setUp(self):
        League.objects.create(LeagueId=1, Description="Diamond")
        Division.objects.create(DivisionId=1, Description="V")
        Account.objects.create(AccountId=21631196, LeagueId=League.objects.first(), DivisionId=Division.objects.first(), Level=30, LastUpdated=timezone.now(), IsOnline=1)

    def test_animals_can_speak(self):
        str = update_account()
