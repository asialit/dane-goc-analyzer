import operator


def calculate_pass_rate(data, territory: str, year: int, counter: int, gender="both"):
    women_pass_quantity = 0
    men_pass_quantity = 0
    women_all_quantity = 0
    men_all_quantity = 0
    i = 0

    while counter > 0:
        item = data.get_list()[i]
        if item.get_territory() == territory:
            if item.get_status() == "przystąpiło" and int(item.get_year()) == year:
                if item.get_gender() == "kobiety":
                    women_all_quantity += int(item.get_number())
                else:
                    men_all_quantity += int(item.get_number())
            elif item.get_status() == "zdało" and int(item.get_year()) == year:
                if item.get_gender() == "kobiety":
                    women_pass_quantity += int(item.get_number())
                else:
                    men_pass_quantity += int(item.get_number())
            i += 1
            counter -= 1
        else:
            i += counter

    if gender == "both":
        return int((women_pass_quantity + men_pass_quantity) / (women_all_quantity + men_all_quantity) * 100)
    elif gender == "women":
        return int((women_pass_quantity / women_all_quantity) * 100)
    elif gender == "men":
        return int((men_pass_quantity / men_all_quantity) * 100)


class Data:

    def __init__(self, territory: str, status: str, gender: str, year: int, number: int):
        self.territory = territory
        self.status = status
        self.gender = gender
        self.year = year
        self.number = number

    def get_territory(self):
        return self.territory

    def get_status(self):
        return self.status

    def get_gender(self):
        return self.gender

    def get_year(self):
        return self.year

    def get_number(self):
        return self.number


class DataSet:

    def __init__(self, data_list: list):
        self.list = data_list

    def get_list(self):
        return self.list

    START_YEAR = 2010

    # calculation of the average number of people who took the exam for a given territory
    # over the years, up to and including the year
    def territory_average(self, territory, year, gender="both"):
        women_all_quantity = 0
        men_all_quantity = 0

        for item in self.get_list():
            if item.get_territory() == territory:
                if item.get_status() == "przystąpiło" and int(item.get_year()) <= year:
                    if item.get_gender() == "kobiety":
                        women_all_quantity += int(item.get_number())
                    else:
                        men_all_quantity += int(item.get_number())
                elif int(item.get_year()) > year:
                    break

        if gender == "both":
            print(f"{year} - {int((men_all_quantity + women_all_quantity) / (year - self.START_YEAR + 1))}")
        elif gender == "women":
            print(f"{year} - {int(women_all_quantity / (year - self.START_YEAR + 1))}")
        elif gender == "men":
            print(f"{year} - {int(men_all_quantity / (year - self.START_YEAR + 1))}")

    # calculation of the percentage of pass rate for a given province over the years
    def territory_pass_rate(self, territory, counter, gender="both"):
        final_year = self.START_YEAR + counter / 4
        year = self.START_YEAR
        while year < final_year:
            print(f"{year} - {calculate_pass_rate(self, territory, year, counter, gender)} %")
            year += 1

    # providing the territory with the best pass rate in a given year
    def best_pass_rate(self, counter, year, gender="both"):
        territories = {'Dolnośląskie': '', 'Kujawsko-pomorskie': '', 'Lubelskie': '',
                       'Łódzkie': '', 'Małopolskie': '', 'Mazowieckie': '',
                       'Opolskie': '', 'Podkarpackie': '', 'Podlaskie': '',
                       'Pomorskie': '', 'Śląskie': '', 'Świętokrzyskie': '',
                       'Warmińsko-Mazurskie': '', 'Wielkopolskie': '', 'Zachodniopomorskie': ''}

        for name in territories:
            territories[name] = calculate_pass_rate(self, name, year, counter, gender)

        best_rate = max(territories.items(), key=operator.itemgetter(1))[0]

        print(f"{year} - ", end="")
        for k, v in territories.items():
            if v == territories[best_rate]:
                print(k, end=" ")
        print('')

    # detection of territory, which recorded regression, if they are in the collection
    def regression(self, counter, gender="both"):
        years = dict()
        final_year = int(self.START_YEAR + counter / 4)
        for x in range(self.START_YEAR, final_year):
            elem = {x: ''}
            years.update(elem)

        territories = ['Dolnośląskie', 'Kujawsko-pomorskie', 'Lubelskie', 'Łódzkie', 'Małopolskie',
                       'Mazowieckie', 'Opolskie', 'Podkarpackie', 'Podlaskie', 'Pomorskie', 'Śląskie',
                       'Świętokrzyskie', 'Warmińsko-Mazurskie', 'Wielkopolskie', 'Zachodniopomorskie']

        for territory in territories:
            for x in range(self.START_YEAR, final_year):
                years[x] = calculate_pass_rate(self, territory, x, counter, gender)

            for k in range(self.START_YEAR, final_year - 1):
                if years[k] > years[k + 1]:
                    print(f"Województwo {territory}: {k} -> {k + 1}")

    # comparison of two territories - for the two territories listed,
    # listing which of the provinces had a better pass rate in each available year
    def compare_territories(self, territory1, territory2, counter, gender="both"):
        final_year = self.START_YEAR + counter / 4
        year = self.START_YEAR
        while year < final_year:
            territory1_result = calculate_pass_rate(self, territory1, year, counter, gender)
            territory2_result = calculate_pass_rate(self, territory2, year, counter, gender)

            if territory1_result > territory2_result:
                print(f"{year} - {territory1}")
            elif territory1_result < territory2_result:
                print(f"{year} - {territory2}")
            else:
                print(f"{year} - same results")
            year += 1
