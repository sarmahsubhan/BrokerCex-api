# coding: utf-8

"""
    Broker API.

    the purpose of this application is to provide an application that is using plain go code to define an API  This should demonstrate all the possible comment annotations that are available to turn go code into a fully compliant swagger 2.0 spec. There are no TOS at this moment, use at your own risk we take no responsibility  # noqa: E501

    OpenAPI spec version: 0.0.1
    Contact: support@cexbro.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class MarketPairInfo(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'ask': 'float',
        'base_currency': 'str',
        'bid': 'float',
        'change1h': 'float',
        'change24h': 'float',
        'funding_rate_percent': 'float',
        'index_price': 'float',
        'last_price': 'float',
        'name': 'str',
        'next_funding_rate': 'datetime',
        'open_interest': 'float',
        'product_type': 'str',
        'target_currency': 'str',
        'volume24h': 'float',
        'volume24h_usd': 'float'
    }

    attribute_map = {
        'ask': 'ask',
        'base_currency': 'baseCurrency',
        'bid': 'bid',
        'change1h': 'change1h',
        'change24h': 'change24h',
        'funding_rate_percent': 'fundingRatePercent',
        'index_price': 'indexPrice',
        'last_price': 'lastPrice',
        'name': 'name',
        'next_funding_rate': 'nextFundingRate',
        'open_interest': 'openInterest',
        'product_type': 'productType',
        'target_currency': 'targetCurrency',
        'volume24h': 'volume24h',
        'volume24h_usd': 'volume24hUSD'
    }

    def __init__(self, ask=None, base_currency=None, bid=None, change1h=None, change24h=None, funding_rate_percent=None, index_price=None, last_price=None, name=None, next_funding_rate=None, open_interest=None, product_type=None, target_currency=None, volume24h=None, volume24h_usd=None):  # noqa: E501
        """MarketPairInfo - a model defined in Swagger"""  # noqa: E501

        self._ask = None
        self._base_currency = None
        self._bid = None
        self._change1h = None
        self._change24h = None
        self._funding_rate_percent = None
        self._index_price = None
        self._last_price = None
        self._name = None
        self._next_funding_rate = None
        self._open_interest = None
        self._product_type = None
        self._target_currency = None
        self._volume24h = None
        self._volume24h_usd = None
        self.discriminator = None

        if ask is not None:
            self.ask = ask
        if base_currency is not None:
            self.base_currency = base_currency
        if bid is not None:
            self.bid = bid
        if change1h is not None:
            self.change1h = change1h
        if change24h is not None:
            self.change24h = change24h
        if funding_rate_percent is not None:
            self.funding_rate_percent = funding_rate_percent
        if index_price is not None:
            self.index_price = index_price
        if last_price is not None:
            self.last_price = last_price
        if name is not None:
            self.name = name
        if next_funding_rate is not None:
            self.next_funding_rate = next_funding_rate
        if open_interest is not None:
            self.open_interest = open_interest
        if product_type is not None:
            self.product_type = product_type
        if target_currency is not None:
            self.target_currency = target_currency
        if volume24h is not None:
            self.volume24h = volume24h
        if volume24h_usd is not None:
            self.volume24h_usd = volume24h_usd

    @property
    def ask(self):
        """Gets the ask of this MarketPairInfo.  # noqa: E501


        :return: The ask of this MarketPairInfo.  # noqa: E501
        :rtype: float
        """
        return self._ask

    @ask.setter
    def ask(self, ask):
        """Sets the ask of this MarketPairInfo.


        :param ask: The ask of this MarketPairInfo.  # noqa: E501
        :type: float
        """

        self._ask = ask

    @property
    def base_currency(self):
        """Gets the base_currency of this MarketPairInfo.  # noqa: E501


        :return: The base_currency of this MarketPairInfo.  # noqa: E501
        :rtype: str
        """
        return self._base_currency

    @base_currency.setter
    def base_currency(self, base_currency):
        """Sets the base_currency of this MarketPairInfo.


        :param base_currency: The base_currency of this MarketPairInfo.  # noqa: E501
        :type: str
        """

        self._base_currency = base_currency

    @property
    def bid(self):
        """Gets the bid of this MarketPairInfo.  # noqa: E501


        :return: The bid of this MarketPairInfo.  # noqa: E501
        :rtype: float
        """
        return self._bid

    @bid.setter
    def bid(self, bid):
        """Sets the bid of this MarketPairInfo.


        :param bid: The bid of this MarketPairInfo.  # noqa: E501
        :type: float
        """

        self._bid = bid

    @property
    def change1h(self):
        """Gets the change1h of this MarketPairInfo.  # noqa: E501


        :return: The change1h of this MarketPairInfo.  # noqa: E501
        :rtype: float
        """
        return self._change1h

    @change1h.setter
    def change1h(self, change1h):
        """Sets the change1h of this MarketPairInfo.


        :param change1h: The change1h of this MarketPairInfo.  # noqa: E501
        :type: float
        """

        self._change1h = change1h

    @property
    def change24h(self):
        """Gets the change24h of this MarketPairInfo.  # noqa: E501


        :return: The change24h of this MarketPairInfo.  # noqa: E501
        :rtype: float
        """
        return self._change24h

    @change24h.setter
    def change24h(self, change24h):
        """Sets the change24h of this MarketPairInfo.


        :param change24h: The change24h of this MarketPairInfo.  # noqa: E501
        :type: float
        """

        self._change24h = change24h

    @property
    def funding_rate_percent(self):
        """Gets the funding_rate_percent of this MarketPairInfo.  # noqa: E501


        :return: The funding_rate_percent of this MarketPairInfo.  # noqa: E501
        :rtype: float
        """
        return self._funding_rate_percent

    @funding_rate_percent.setter
    def funding_rate_percent(self, funding_rate_percent):
        """Sets the funding_rate_percent of this MarketPairInfo.


        :param funding_rate_percent: The funding_rate_percent of this MarketPairInfo.  # noqa: E501
        :type: float
        """

        self._funding_rate_percent = funding_rate_percent

    @property
    def index_price(self):
        """Gets the index_price of this MarketPairInfo.  # noqa: E501


        :return: The index_price of this MarketPairInfo.  # noqa: E501
        :rtype: float
        """
        return self._index_price

    @index_price.setter
    def index_price(self, index_price):
        """Sets the index_price of this MarketPairInfo.


        :param index_price: The index_price of this MarketPairInfo.  # noqa: E501
        :type: float
        """

        self._index_price = index_price

    @property
    def last_price(self):
        """Gets the last_price of this MarketPairInfo.  # noqa: E501


        :return: The last_price of this MarketPairInfo.  # noqa: E501
        :rtype: float
        """
        return self._last_price

    @last_price.setter
    def last_price(self, last_price):
        """Sets the last_price of this MarketPairInfo.


        :param last_price: The last_price of this MarketPairInfo.  # noqa: E501
        :type: float
        """

        self._last_price = last_price

    @property
    def name(self):
        """Gets the name of this MarketPairInfo.  # noqa: E501


        :return: The name of this MarketPairInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MarketPairInfo.


        :param name: The name of this MarketPairInfo.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def next_funding_rate(self):
        """Gets the next_funding_rate of this MarketPairInfo.  # noqa: E501


        :return: The next_funding_rate of this MarketPairInfo.  # noqa: E501
        :rtype: datetime
        """
        return self._next_funding_rate

    @next_funding_rate.setter
    def next_funding_rate(self, next_funding_rate):
        """Sets the next_funding_rate of this MarketPairInfo.


        :param next_funding_rate: The next_funding_rate of this MarketPairInfo.  # noqa: E501
        :type: datetime
        """

        self._next_funding_rate = next_funding_rate

    @property
    def open_interest(self):
        """Gets the open_interest of this MarketPairInfo.  # noqa: E501


        :return: The open_interest of this MarketPairInfo.  # noqa: E501
        :rtype: float
        """
        return self._open_interest

    @open_interest.setter
    def open_interest(self, open_interest):
        """Sets the open_interest of this MarketPairInfo.


        :param open_interest: The open_interest of this MarketPairInfo.  # noqa: E501
        :type: float
        """

        self._open_interest = open_interest

    @property
    def product_type(self):
        """Gets the product_type of this MarketPairInfo.  # noqa: E501


        :return: The product_type of this MarketPairInfo.  # noqa: E501
        :rtype: str
        """
        return self._product_type

    @product_type.setter
    def product_type(self, product_type):
        """Sets the product_type of this MarketPairInfo.


        :param product_type: The product_type of this MarketPairInfo.  # noqa: E501
        :type: str
        """

        self._product_type = product_type

    @property
    def target_currency(self):
        """Gets the target_currency of this MarketPairInfo.  # noqa: E501


        :return: The target_currency of this MarketPairInfo.  # noqa: E501
        :rtype: str
        """
        return self._target_currency

    @target_currency.setter
    def target_currency(self, target_currency):
        """Sets the target_currency of this MarketPairInfo.


        :param target_currency: The target_currency of this MarketPairInfo.  # noqa: E501
        :type: str
        """

        self._target_currency = target_currency

    @property
    def volume24h(self):
        """Gets the volume24h of this MarketPairInfo.  # noqa: E501


        :return: The volume24h of this MarketPairInfo.  # noqa: E501
        :rtype: float
        """
        return self._volume24h

    @volume24h.setter
    def volume24h(self, volume24h):
        """Sets the volume24h of this MarketPairInfo.


        :param volume24h: The volume24h of this MarketPairInfo.  # noqa: E501
        :type: float
        """

        self._volume24h = volume24h

    @property
    def volume24h_usd(self):
        """Gets the volume24h_usd of this MarketPairInfo.  # noqa: E501


        :return: The volume24h_usd of this MarketPairInfo.  # noqa: E501
        :rtype: float
        """
        return self._volume24h_usd

    @volume24h_usd.setter
    def volume24h_usd(self, volume24h_usd):
        """Sets the volume24h_usd of this MarketPairInfo.


        :param volume24h_usd: The volume24h_usd of this MarketPairInfo.  # noqa: E501
        :type: float
        """

        self._volume24h_usd = volume24h_usd

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(MarketPairInfo, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, MarketPairInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
