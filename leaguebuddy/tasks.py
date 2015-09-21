from leaguebuddy import models
from magicaljourney import settings
import requests


def update_account():
    accountid = ",".join(map(str, models.Account.objects.all().values_list("AccountId", flat=True)))
    account_status_url = "https://na.api.pvp.net/api/lol/na/v1.4/summoner/{0}?api_key={1}".format(accountid,
                                                                                                  settings.RIOT_API_KEY)
    response = requests.get(account_status_url)
    accounts = response.json()

    for account in accounts:
        for field in accounts[account]:
            print accounts[account][field]
