import csv
import json
import sys
import getopt
import requests
from data_manager import Data, DataSet


def get_data():
    data_list = list()

    url = 'https://api.dane.gov.pl/resources/17363'

    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.HTTPError:
        print('Failed to download data')

    response_text = json.loads(response.text)

    url = response_text['data']['attributes']['file_url']
    response = requests.get(url)
    content = response.content.decode('Windows-1250')

    file = csv.DictReader(content.splitlines())
    for row in file:
        element = row.popitem()
        item = list(element)[1].split(';')
        data = Data(item[0], item[1], item[2], item[3], item[4])
        data_list.append(data)

    return data_list


def get_parameter(parameters_list: list, option: str):
    for item in parameters_list:
        if option in item:
            return item[item.index(option) + 1]


# calculation of the average number of people who took the exam for a given territory
# over the years, up to and including the year
def average(data: DataSet, parameters: list):
    territory = get_parameter(parameters, '-t')
    year = int(get_parameter(parameters, '-y'))
    if '-g' in sys.argv:
        gender = get_parameter(parameters, '-g')
        if gender != 'women' or gender != 'men':
            print("Wrong parameters after -g")
            sys.exit()
        else:
            data.territory_average(territory, year, gender)
    else:
        file_data.territory_average(territory, year)


# calculation of the percentage of pass rate for a given province over the years
def territory_pass_rate(data: DataSet, parameters: list, counter: int):
    territory = get_parameter(parameters, '-t')
    if '-g' in sys.argv:
        gender = get_parameter(parameters, '-g')
        if gender != 'women' or gender != 'men':
            print("Wrong parameters after -g")
            sys.exit()
        else:
            data.territory_pass_rate(territory, counter, gender)
    else:
        data.territory_pass_rate(territory, counter)


# providing the territory with the best pass rate in a given year
def best_pass_rate(data: DataSet, parameters: list, counter: int):
    year = int(get_parameter(parameters, '-y'))
    if '-g' in sys.argv:
        gender = get_parameter(parameters, '-g')
        if gender != 'women' or gender != 'men':
            print("Wrong parameters after -g")
            sys.exit()
        else:
            data.best_pass_rate(counter, year, gender)
    else:
        file_data.best_pass_rate(counter, year)


# detection of territory, which recorded regression, if they are in the collection
def regression(data: DataSet, parameters: list, counter: int):
    if '-g' in sys.argv:
        gender = get_parameter(parameters, '-g')
        if gender != 'women' or gender != 'men':
            print("Wrong parameters after -g")
            sys.exit()
        else:
            data.regression(counter, gender)
    else:
        data.regression(counter)


# comparison of two territories - for the two territories listed,
# listing which of the provinces had a better pass rate in each available year
def compare(data: DataSet, parameters: list, counter: int):
    territory1 = get_parameter(parameters, '-t')
    territory2 = get_parameter(parameters, '-w')
    if '-g' in sys.argv:
        gender = get_parameter(parameters, '-g')
        if gender != 'women' or gender != 'men':
            print("Wrong parameters after -g")
            sys.exit()
        else:
            data.compare_territories(territory1, territory2, counter, gender)
    else:
        data.compare_territories(territory1, territory2, counter)


def read_commands(data: DataSet, counter: int):

    commands = ['--average', '--territory-pass-rate', '--best-pass-rate', '--regression', '--compare']

    if len(sys.argv) > 1:
        if sys.argv[1] in commands:
            parameters = getopt.getopt(sys.argv[2:], 't:y:g:w:')
            parameters = list(parameters[0])
            if sys.argv[1] == "--average":
                average(data, parameters)
            elif sys.argv[1] == "--territory-pass-rate":
                territory_pass_rate(data, parameters, counter)
            elif sys.argv[1] == "--best-pass-rate":
                best_pass_rate(data, parameters, counter)
            elif sys.argv[1] == "--regression":
                regression(data, parameters, counter)
            elif sys.argv[1] == "--compare":
                compare(data, parameters, counter)
        else:
            print()
            sys.exit('Wrong parameters')
    else:
        print('Too few parameters')
        sys.exit()


if __name__ == '__main__':

    file_data = DataSet(get_data())

    # how many fields in the array belong to one territory
    FIELD_COUNTER = int(len(file_data.get_list()) // 17)

    read_commands(file_data, FIELD_COUNTER)
