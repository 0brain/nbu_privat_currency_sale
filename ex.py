from datetime import datetime
from nbu_privat_currency_sale import nbu_privat_currency_info_in_date_range, filter_by_currency_name, \
                                     group_by_bank_name, graph_banks_currency

date1 = datetime(2020, 4, 22)
date2 = datetime(2020, 4, 27)

currency_info = nbu_privat_currency_info_in_date_range(date1, date2)
filtered_currency_info = filter_by_currency_name(currency_info, 'USD')
grouped_info = group_by_bank_name(filtered_currency_info)
graph_banks_currency(grouped_info)
# Output: