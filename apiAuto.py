import requests


def testapi():
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    response = requests.get(url)
    data = response.json()
    expected = ['USD', 'GBP', 'EUR']
    bpiKeys = data.get("bpi", {}).keys()
    actualKeys = list(bpiKeys)
    if expected != actualKeys:
        raise AssertionError("Assertion keys are not valid")
    GBPDescription = "British Pound Sterling"
    actualDesp = data.get("bpi", {}).get("GBP",{}).get("description")
    assert actualDesp == GBPDescription, "description matches"
    print(actualDesp)

testapi()