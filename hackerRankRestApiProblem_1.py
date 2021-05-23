import requests


def makeRequest(year):
    requestQuery = 'https://jsonmock.hackerrank.com/api/football_matches?year='+str(year)+'&page=1'

    resp = requests.get(requestQuery)
    print(resp.json())


makeRequest(2011)