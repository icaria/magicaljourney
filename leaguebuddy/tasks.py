from leaguebuddy import models
from magicaljourney import settings
from django.utils import timezone
import requests
import datetime


def update():
    accountid = ",".join(map(str, models.Account.objects.all().values_list("id", flat=True)))
    account_status_url = "https://na.api.pvp.net/api/lol/na/v1.4/summoner/{0}?api_key={1}".format(accountid,
                                                                                                  settings.RIOT_API_KEY)
    response = requests.get(account_status_url)
    summoners = response.json()

    for summoner in summoners:
        account_db = models.Account.objects.get(id=summoner)

        check_level(account_db, summoners[summoner])

        last_modified = datetime.datetime.fromtimestamp(summoners[summoner]["revisionDate"])

        for field in summoners[summoner]:
            print summoners[summoner][field]
        print


def check_level(summoner, data):
    level = long(data["summonerLevel"])
    if summoner.level != level:
        create_notification(summoner, "{0} has reached Level {1}.".format(summoner.name, level))
        summoner.level = level
        summoner.save()


def create_notification(summoner, notification):
    models.Notification.objects.create(message=notification, date_time=timezone.now(), account_id=summoner.id)
