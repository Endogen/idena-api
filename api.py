import json
import requests

from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry


def list_args_to_comma_separated(func):
    """Return function that converts list input arguments to comma-separated strings"""
    def input_args(*args, **kwargs):
        for v in kwargs:
            # check in **kwargs for lists and convert to comma-separated string
            if isinstance(kwargs[v], list): kwargs[v] = ','.join(kwargs[v])
        # check in *args for lists and convert to comma-separated string
        args=[','.join(v) if isinstance(v, list) else v for v in args]
        return func(*args, **kwargs)
    return input_args


def get_comma_separated_values(values):
    """Return the values as a comma-separated string"""

    # Make sure values is a list or tuple
    if not isinstance(values, list) and not isinstance(values, tuple):
        values = [values]
    return ','.join(values)


class IdenaAPI:

    __API_URL = 'http://localhost'
    __API_PORT = "9009"

    def __init__(self, api_url=__API_URL, api_port=__API_PORT):
        self.api_url = api_url
        self.api_port = api_port

        self.request_timeout = 120

        self.session = requests.Session()
        retries = Retry(total=5, backoff_factor=0.5, status_forcelist=[502, 503, 504])
        self.session.mount('http://', HTTPAdapter(max_retries=retries))

    def __request(self, url):
        try:
            response = self.session.get(url, timeout = self.request_timeout)
            response.raise_for_status()
            content = json.loads(response.content.decode('utf-8'))
            return content
        except Exception as e:
            # check if json (with error message) is returned
            try:
                content = json.loads(response.content.decode('utf-8'))
                raise ValueError(content)
            # if no json
            except json.decoder.JSONDecodeError:
                pass
            #except UnboundLocalError as e:
            #    pass
            raise

    def __api_url_params(self, api_url, params):
        if params:
            api_url += '?'
            for key, value in params.items():
                api_url += "{0}={1}&".format(key, value)
            api_url = api_url[:-1]
        return api_url


    #---------- SIMPLE ----------#
    @list_args_to_comma_separated
    def get_price(self, ids, vs_currencies, **kwargs):
        """Get the current price of any cryptocurrencies in any other supported currencies that you need"""

        ids=ids.replace(' ','')
        kwargs['ids'] = ids
        vs_currencies=vs_currencies.replace(' ','')
        kwargs['vs_currencies'] = vs_currencies

        api_url = '{0}simple/price'.format(self.api_url)
        api_url = self.__api_url_params(api_url, kwargs)

        return self.__request(api_url)


    @list_args_to_comma_separated
    def get_token_price(self, id, contract_addresses, vs_currencies, **kwargs):
        """Get the current price of any tokens on this coin (ETH only at this stage as per api docs) in any other supported currencies that you need"""

        contract_addresses=contract_addresses.replace(' ','')
        kwargs['contract_addresses'] = contract_addresses
        vs_currencies=vs_currencies.replace(' ','')
        kwargs['vs_currencies'] = vs_currencies

        api_url = '{0}simple/token_price/{1}'.format(self.api_url, id)
        api_url = self.__api_url_params(api_url, kwargs)
        return self.__request(api_url)


    def get_supported_vs_currencies(self):
        """Get list of supported_vs_currencies"""

        api_url = '{0}simple/supported_vs_currencies'.format(self.api_url)
        return self.__request(api_url)


    #---------- COINS ----------#
    @list_args_to_comma_separated
    def get_coins(self, **kwargs):
        """List all coins with data (name, price, market, developer, community, etc)"""

        api_url = '{0}coins'.format(self.api_url)
        #['order', 'per_page', 'page', 'localization']
        api_url = self.__api_url_params(api_url, kwargs)

        return self.__request(api_url)


    def get_coins_list(self):
        """List all supported coins id, name and symbol (no pagination required)"""

        api_url = '{0}coins/list'.format(self.api_url)

        return self.__request(api_url)


    @list_args_to_comma_separated
    def get_coins_markets(self, vs_currency, **kwargs):
        """List all supported coins price, market cap, volume, and market related data (no pagination required)"""

        kwargs['vs_currency'] = vs_currency

        api_url = '{0}coins/markets'.format(self.api_url)
        api_url = self.__api_url_params(api_url, kwargs)

        return self.__request(api_url)


    @list_args_to_comma_separated
    def get_coin_by_id(self, id, **kwargs):
        """Get current data (name, price, market, ... including exchange tickers) for a coin"""

        api_url = '{0}coins/{1}/'.format(self.api_url, id)
        api_url = self.__api_url_params(api_url, kwargs)

        return self.__request(api_url)


    @list_args_to_comma_separated
    def get_coin_ticker_by_id(self, id, **kwargs):
        """Get coin tickers (paginated to 100 items)"""

        api_url = '{0}coins/{1}/tickers'.format(self.api_url, id)
        api_url = self.__api_url_params(api_url, kwargs)

        return self.__request(api_url)


    @list_args_to_comma_separated
    def get_coin_history_by_id(self, id, date, **kwargs):
        """Get historical data (name, price, market, stats) at a given date for a coin"""

        kwargs['date'] = date

        api_url = '{0}coins/{1}/history'.format(self.api_url, id)
        api_url = self.__api_url_params(api_url, kwargs)

        return self.__request(api_url)


    @list_args_to_comma_separated
    def get_coin_market_chart_by_id(self, id, vs_currency, days):
        """Get historical market data include price, market cap, and 24h volume (granularity auto)"""

        api_url = '{0}coins/{1}/market_chart?vs_currency={2}&days={3}'.format(self.api_url, id, vs_currency, days)

        return self.__request(api_url)


    @list_args_to_comma_separated
    def get_coin_market_chart_range_by_id(self, id, vs_currency, from_timestamp, to_timestamp):
        """Get historical market data include price, market cap, and 24h volume within a range of timestamp (granularity auto)"""

        api_url = '{0}coins/{1}/market_chart/range?vs_currency={2}&from={3}&to={4}'.format(self.api_url, id, vs_currency, from_timestamp, to_timestamp)

        return self.__request(api_url)


    @list_args_to_comma_separated
    def get_coin_status_updates_by_id(self, id, **kwargs):
        """Get status updates for a given coin"""

        api_url = '{0}coins/{1}/status_updates'.format(self.api_url, id)
        api_url = self.__api_url_params(api_url, kwargs)

        return self.__request(api_url)
