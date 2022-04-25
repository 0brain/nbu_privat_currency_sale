from datetime import datetime
from nbu_privat_currency_sale import get_nbu_currency_info, get_privat_currency_info, \
    nbu_privat_currency_info_in_date_range, filter_by_currency_name, group_by_bank_name

date1 = datetime(2020, 4, 22)
date2 = datetime(2020, 4, 23)

# Return sale rate information about all currency from National Bank of Ukraine
#print(get_nbu_currency_info(date1))

# Output:
# [
#   {'bank': 'National Bank of Ukraine', 'date': '22.04.2020', 'currency': 'AUD', 'rate': 16.9936},
#   {'bank': 'National Bank of Ukraine', 'date': '22.04.2020', 'currency': 'CAD', 'rate': 19.0366},
#   ...
# ]

# Return sale rate information about all currency  from PrivatBank
#print(get_privat_currency_info(date2))

# Output:
# [
#   {'bank': 'PrivatBank', 'date': '22.04.2020', 'currency': 'EUR', 'rate': 29.6},
#   {'bank': 'PrivatBank', 'date': '22.04.2020', 'currency': 'GBP', 'rate': 33.9},
#   ...
# ]

#  Return sale rate information about all currency from National Bank of Ukraine
#  and from PrivatBank in certain date range
#print(nbu_privat_currency_info_in_date_range(date1, date2))

# Output:
# [
#   {'bank': 'National Bank of Ukraine', 'date': '22.04.2020', 'currency': 'AUD', 'rate': 16.9936},
#   ...
#   {'bank': 'National Bank of Ukraine', 'date': '23.04.2020', 'currency': 'AUD', 'rate': 17.1046},
#   ...
#   {'bank': 'PrivatBank', 'date': '22.04.2020', 'currency': 'EUR', 'rate': 29.6},
#   ...
#   {'bank': 'PrivatBank', 'date': '23.04.2020', 'currency': 'EUR', 'rate': 29.5},
#   ...
# ]

# Return sale rate information about all currency from National Bank of Ukraine
#  and from PrivatBank in certain date range filtered by 'currency' key.
currency_info = nbu_privat_currency_info_in_date_range(date1, date2)
currency_value = 'USD'
#print(filter_by_currency_name(currency_info, currency_value))

# Output:
# [
#   {'bank': 'National Bank of Ukraine', 'date': '22.04.2020', 'currency': 'USD', 'rate': 27.0815},
#   {'bank': 'PrivatBank', 'date': '22.04.2020', 'currency': 'USD', 'rate': 27.25},
#   {'bank': 'National Bank of Ukraine', 'date': '23.04.2020', 'currency': 'USD', 'rate': 27.0536},
#   {'bank': 'PrivatBank', 'date': '23.04.2020', 'currency': 'USD', 'rate': 27.25}
# ]

# Return sale rate information about all currency from National Bank of Ukraine
#  and from PrivatBank in certain date range filtered by 'currency' key and grouped by 'bank'.
currency_info = nbu_privat_currency_info_in_date_range(date1, date2)
filtered_currency_info = filter_by_currency_name(currency_info, 'USD')
print(group_by_bank_name(filtered_currency_info))
# Output:
# [
#   [
#     {'bank': 'National Bank of Ukraine', 'date': '22.04.2020', 'currency': 'USD', 'rate': 27.0815},
#     {'bank': 'National Bank of Ukraine', 'date': '23.04.2020', 'currency': 'USD', 'rate': 27.0536}
#   ],
#   [
#     {'bank': 'PrivatBank', 'date': '22.04.2020', 'currency': 'USD', 'rate': 27.25},
#     {'bank': 'PrivatBank', 'date': '23.04.2020', 'currency': 'USD', 'rate': 27.25}
#   ]
# ]
