"""
CP1404/CP5632 Practical
Write a program to read this file, process the data and display processed
information:
-the champions and how many times they have won.
-the countries of the champions in alphabetical order
Wimbledon Time Estimate:
Estimate: 60 minutes
Actual:  240 minutes
"""

FILENAME = "wimbledon.csv"
CHAMPION_TO_WIN = {'John Newcombe': 0, 'Jan Kodeš':0, 'Pat Cash':0, 'Stefan Edberg':0, 'Andy Murray':0, 'Jimmy Connors':0,
                 'John McEnroe':0, 'Lleyton Hewitt':0, 'Rafael Nadal':0, 'Rod Laver':0, 'Arthur Ashe':0, 'Andre Agassi':0,
                 'Michael Stich':0, 'Björn Borg':0, 'Roger Federer':0, 'Goran Ivanišević':0, 'Novak Djokovic':0, 'Pete Sampras':0,
                 'Stan Smith':0, 'Boris Becker':0, 'Richard Krajicek':0}


def main():
    wimbledon_records = get_wimbledon_records()
    striped_wimbledon_records = clean_data(wimbledon_records)

    # clearn key data created
    wimbledon_keys = get_keys(striped_wimbledon_records)

    # remove key value from striped_wimbledon_records
    striped_wimbledon_records.remove('Year,Country,Champion,Country,Runner-up,Score in the final')

    # clean value data created
    wimbledon_values = get_values(striped_wimbledon_records)

    # map created
    string_to_value = create_wimbledon_map(wimbledon_keys, wimbledon_values)
    print_results(string_to_value)

def calculate_champion_total(champion_to_win, champions):
    """Total each occurrence of a word in a string"""
    for word in champions:
        champion_to_win[word] = champion_to_win.get(word, 0) + 1
    return champion_to_win

def print_results(string_to_value):
    """Print results to console"""
    countries = []
    champions = []
    for value in string_to_value:
        countries.append(value['Country'])
        champions.append(value['Champion'])

    #champion win totals output
    champion_to_win = calculate_champion_total(CHAMPION_TO_WIN, champions)
    print("Wimbledon Champions:")
    for champion, win in champion_to_win.items():
        print(champion, win)
    print()

    #sorted country output
    country_set = set(countries)
    sort_countries = list(country_set)
    sort_countries.sort()
    print(f"These {len(sort_countries)} countries have won Wimbledon:")
    print(sort_countries)


def create_wimbledon_map(keys, values):
    """Extracted keys used to match values with zip() creating map"""
    wimbledon_maps = []
    for value in values:
        temporary_dictionary = dict(zip(keys, value))
        wimbledon_maps.append(temporary_dictionary)
    return wimbledon_maps


def get_values(striped_wimbledon_records):
    """Convert wimbledon values to list, remove unnecessary fields"""
    list_items_converted = []
    for record in striped_wimbledon_records:
        # remove score and whitespace
        string_list_item_scores = record.split('"')
        string_list_item_scores.remove('')
        del string_list_item_scores[1]

        # remove duplicate country and runner-up field
        string_list_item_remove_fields = string_list_item_scores[0].split(",")
        del string_list_item_remove_fields[4]
        del string_list_item_remove_fields[3]
        del string_list_item_remove_fields[0]
        list_items_converted.append(string_list_item_remove_fields)
    return list_items_converted


def get_keys(striped_wimbledon_records):
    """"Extract key values from wimbledon list, remove unnecessary fields"""
    wimbledon_keys = []
    wimbledon_keys_string = striped_wimbledon_records[0]
    wimbledon_keys = wimbledon_keys_string.split(',')
    del wimbledon_keys[5]
    del wimbledon_keys[4]
    del wimbledon_keys[3]
    del wimbledon_keys[0]
    return wimbledon_keys


def clean_data(wimbledon_records):
    """Remove line breaks from all records"""
    striped_wimbledon_records = []
    for line in wimbledon_records:
        line = line.strip()
        striped_wimbledon_records.append(line)
    return striped_wimbledon_records


def get_wimbledon_records():
    """Read from wimbledon file and save records as a list"""
    with open(FILENAME, 'r', encoding='utf-8-sig') as in_file:
        wimbledon_records = in_file.readlines()
    return wimbledon_records


main()
