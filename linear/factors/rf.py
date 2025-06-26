import requests
#rf(risk free rate) measures how much risk the market prices into safe assets like bonds that are guraanteed

nominal_rf_rate = 0
real_rf_rate = 0

INFLATION_RATE = 0 #calculated by TIPS(inflation protected bonds)? can look at much they rise for inflation 
#Or consumer price index
TEN_YEAR_RATE = 0


treasury_base_url = 'https://api.fiscaldata.treasury.gov/services/api/fiscal_service/'
bonds_avg_rate = '/v2/accounting/od/avg_interest_rates'
most_recent_params = '?sort=-record_date&format=json&page[number]=1&page[size]=1'
cpi_path = 'v1/accounting/od/tips_cpi_data_summary'
cpi_params = '?sort=-original_issue_date&format=json&page[number]=1&page[number]&page[size]=1'


#return interest rate on the day with data in object
def get_nominal_rf_rate():
    r = requests.get(f'{treasury_base_url}{bonds_avg_rate}{most_recent_params}')
    response = r.json
    print(response)
    date = response['data'][0]['record_date']
    interest_rate = response['data'][0]['avg_interest_rate_amt']
    data = {'date': date, 'interest_rate': interest_rate}
    print(data)
    return data

#TODO 
#Update so that you save all of the most recent bond auctions types
#get the cpi data when tips are sold
def get_real_rf_rate():
    url = f'{treasury_base_url}{cpi_path}{cpi_params}'
    r = requests.get(url)
    response = r.json()
    date = response['data'][0]['original_issue_date']
    term = response['data'][0]['security_term']
    rate = response['data'][0]['interest_rate']
    cpi_on_date = response['data'][0]['ref_cpi_on_dated_date']
    data = {'date': date, 'cpi_on_date': cpi_on_date, "rate": rate, "term": term}
    print(data)
    return data


#TIPS = Real rf rate
#bonds rate = nominal rf rate
