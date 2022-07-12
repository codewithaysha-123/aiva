from bs4 import BeautifulSoup
import notification
import requests
import speak as sp

# requesting the url
def make_request(url):
    response = requests.get(url)
    return response.text

def cases():
    html_data = make_request('https://www.worldometers.info/coronavirus/')
    soup = BeautifulSoup(html_data, 'html.parser')

    total_global_row = soup.find_all('tr', {'class': 'total_row'})[-1]
    total_cases = total_global_row.find_all('td')[2].get_text()
    new_cases = total_global_row.find_all('td')[3].get_text()
    total_recovered = total_global_row.find_all('td')[6].get_text()

    sp.speak(f'total cases :  {total_cases}')
    sp.speak(f'New cases: {new_cases[1:]}')
    sp.speak(f'Total recovered: {total_recovered}')

    sp.speak("Here are the stats for COVID-19")