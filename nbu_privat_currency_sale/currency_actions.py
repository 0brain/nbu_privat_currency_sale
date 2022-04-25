import collections
import csv
import json
from datetime import datetime, timedelta
from itertools import chain
from typing import Union, List, Dict, Any

import requests as requests

import matplotlib.pyplot as plt


NBU_BANK_API_URL = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?date={date_to_get}&json'
PRIVAT_BANK_API_URL = 'https://api.privatbank.ua/p24api/exchange_rates?json&date={date_to_get}'


def get_privat_currency_info(date: datetime) -> List[Dict[str, Union[str, float]]]:
    """
    Get datetime object. Return normalized list of dicts with currency info
    of PrivatBank on specified date.
    """
    formatted_date = date.strftime("%d.%m.%Y")
    response = requests.get(PRIVAT_BANK_API_URL.format(date_to_get=formatted_date))
    r = response.json()
    current_date = r['date']
    l = []
    for i in r['exchangeRate'][1:]:
        d = {}
        d["bank"] = "PrivatBank"
        d["date"] = current_date
        d["currency"] = i['currency']
        d["rate"] = i.get('saleRate', 0.0)
        l.append(d)
    return l


def get_nbu_currency_info(date: datetime) -> List[Dict[str, Union[str, float]]]:
    """
    Get datetime object. Return normalized list of dicts with currency info
    of National Bank of Ukraine on specified date.
    """
    formatted_date = date.strftime("%Y%m%d")
    response = requests.get(NBU_BANK_API_URL.format(date_to_get=formatted_date))
    r = response.json()
    l = []
    for i in r:
        d = {}
        d["bank"] = "National Bank of Ukraine"
        d["date"] = i["exchangedate"]
        d["currency"] = i["cc"]
        d["rate"] = i["rate"]
        l.append(d)
    return l


def nbu_privat_currency_info_in_date_range(start_date: datetime,
                                           end_date: datetime) -> List[Dict[str, Union[str, float]]]:
    """
    Get two datetime objects which define query limits.
    Return normalized list of dicts with currency info
    of National Bank of Ukraine and PrivatBank on specified date range.
    """
    one_day = timedelta(days=1)
    current_day = start_date
    l = []
    while current_day <= end_date:
        l.extend(get_nbu_currency_info(current_day) + get_privat_currency_info(current_day))
        current_day += one_day

    return l


def filter_by_currency_name(list_of_dicts: List[Dict[str, Union[str, float]]],
                            currency_name: str) -> List[Dict[str, Union[str, float]]]:
    """
    Get list of dicts with currency info of National Bank of Ukraine and PrivatBank.
    Return list filtered by 'currency' key.
    """
    res = list(filter(lambda x: x['currency'] == currency_name, list_of_dicts))
    return res


def group_by_bank_name(list_of_dicts: List[Dict[str, Union[str, float]]]) \
                                   -> List[List[Dict[str, Union[str, float]]]]:
    """
    Get list of dicts with currency info of National Bank of Ukraine and PrivatBank.
    Return list which contains lists of grouped dicts by 'bank' key.
    """
    result = collections.defaultdict(list)
    for d in list_of_dicts:
        result[d['bank']].append(d)
    result_list = list(result.values())
    return result_list


def graph_banks_currency(lst: List[List[Dict[str, Union[str, float]]]]) -> None:
    """
    Get filtered by 'currency' key value list, which contains lists of grouped dicts by 'bank' key.
    Display a graph of National Bank of Ukraine and PrivatBank currency sale rate.
    """
    x1 = [i["date"] for i in lst[0]]
    y1 = [i["rate"] for i in lst[0]]
    plt.plot(x1, y1, label=f"{lst[0][0]['bank']}")

    x2 = [i["date"] for i in lst[1]]
    y2 = [i["rate"] for i in lst[1]]
    plt.plot(x2, y2, label=f"{lst[1][0]['bank']}")

    plt.grid(True)
    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    plt.title('Banks currency sale rate')

    plt.legend()

    plt.grid(color='green', linestyle='--', linewidth=0.5)
    plt.xlabel('period')
    plt.ylabel('exchange rate')

    plt.show()


def save_as_json(lst: Any) -> None:
    """Save received information in JSON format."""
    with open('data_json.json', 'w', encoding='utf-8') as f:
        json.dump(lst, f, ensure_ascii=False)


def save_as_csv(lst: Union[List[Dict[str, Union[str, float]]],
                           List[List[Dict[str, Union[str, float]]]]]):
    """Save received information in CSV format."""
    fieldnames = []
    with open('data_csv.csv', 'w', newline='') as output_file:
        if isinstance(lst[0], dict):
            fieldnames = lst[0].keys()
        elif isinstance(lst[0], list):
            fieldnames = lst[0][0].keys()
        dict_writer = csv.DictWriter(output_file, fieldnames)
        dict_writer.writeheader()
        dict_writer.writerows(lst if isinstance(lst[0], dict) else chain.from_iterable(lst))
