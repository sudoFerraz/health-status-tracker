import rumps
import urllib
import json

class AwesomeStatusBarApp(rumps.App):
    def __init__(self):
        super(AwesomeStatusBarApp, self).__init__("Awesome App")

    @rumps.timer(60)
    def changeTracker(self, _):
        changeUrl = 'https://changeinvest.statuspage.io/api/v2/status.json'
        coinbaseUrl = 'https://api.coinbase.com/v2/prices/%s/spot'
        options = ['BTC-USD','ETH-USD']
        title = ''
        j = json.loads( urllib.urlopen( changeUrl ).read() )
        if (j['status']['description'] == 'All Systems Operational'):
            title = title + '  Change Status: ' + u'\u2713' + '      '
        else:
            title = title + '  Change Status: SOMETHING IS WRONG     '
        for option in options:
            url = coinbaseUrl % option
            j = json.loads( urllib.urlopen( url ).read() )
            if (j['data']['base'] == 'BTC'):
                title = title + u'\u0243' + ' = ' + j['data']['amount'] + ' '
            else:
                title = title + j['data']['base'] + ' = ' + j['data']['amount']
        self.title = title

if __name__ == "__main__":
    AwesomeStatusBarApp().run()
