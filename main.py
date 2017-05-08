
# coding=utf-8

import lxml.html
from lxml.cssselect import CSSSelector
import requests
import sys

reload(sys)
sys.setdefaultencoding('utf8')

page_request = requests.get('https://www.sinoptik.bg/vidin-bulgaria-100725905')
tree = lxml.html.fromstring(page_request.text)

forecast_text_sel = CSSSelector('.wfCurrentContent > strong')
current_temp_sel = CSSSelector('.wfCurrentTemp')
wind_sel = CSSSelector('.wfCurrentWind.windImgW')
detailed_stats_sel = CSSSelector('.wfNonCurrentValue')

forecast_text = forecast_text_sel(tree)[0].text
current_temp = current_temp_sel(tree)[0].text
wind = wind_sel(tree)[0].get('title')
detailed_stats = detailed_stats_sel(tree)
rain_probability = detailed_stats[0].text
storm_probability = detailed_stats[2].text

print('Времето за Видин за днес')
print(forecast_text)
print('Температура: ' + current_temp)
print('Вятър: ' + wind)
print('Вероятност за валежи: ' + rain_probability)
print('Вероятност за буря: ' + storm_probability)