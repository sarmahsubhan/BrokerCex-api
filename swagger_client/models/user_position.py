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


class UserPosition(object):
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
        'ask_open': 'object',
        'bid_open': 'object',
        'conv_rate': 'object',
        'fpl': 'object',
        'margin': 'object',
        'position_code': 'str',
        'quantity': 'object',
        'rate': 'object',
        'symbol': 'str',
        'version': 'int'
    }

    attribute_map = {
        'ask_open': 'askOpen',
        'bid_open': 'bidOpen',
        'conv_rate': 'convRate',
        'fpl': 'fpl',
        'margin': 'margin',
        'position_code': 'positionCode',
        'quantity': 'quantity',
        'rate': 'rate',
        'symbol': 'symbol',
        'version': 'version'
    }

    def __init__(self, ask_open=None, bid_open=None, conv_rate=None, fpl=None, margin=None, position_code=None, quantity=None, rate=None, symbol=None, version=None):  # noqa: E501
        """UserPosition - a model defined in Swagger"""  # noqa: E501

        self._ask_open = None
        self._bid_open = None
        self._conv_rate = None
        self._fpl = None
        self._margin = None
        self._position_code = None
        self._quantity = None
        self._rate = None
        self._symbol = None
        self._version = None
        self.discriminator = None

        if ask_open is not None:
            self.ask_open = ask_open
        if bid_open is not None:
            self.bid_open = bid_open
        if conv_rate is not None:
            self.conv_rate = conv_rate
        if fpl is not None:
            self.fpl = fpl
        if margin is not None:
            self.margin = margin
        if position_code is not None:
            self.position_code = position_code
        if quantity is not None:
            self.quantity = quantity
        if rate is not None:
            self.rate = rate
        if symbol is not None:
            self.symbol = symbol
        if version is not None:
            self.version = version

    @property
    def ask_open(self):
        """Gets the ask_open of this UserPosition.  # noqa: E501


        :return: The ask_open of this UserPosition.  # noqa: E501
        :rtype: object
        """
        return self._ask_open

    @ask_open.setter
    def ask_open(self, ask_open):
        """Sets the ask_open of this UserPosition.


        :param ask_open: The ask_open of this UserPosition.  # noqa: E501
        :type: object
        """

        self._ask_open = ask_open

    @property
    def bid_open(self):
        """Gets the bid_open of this UserPosition.  # noqa: E501


        :return: The bid_open of this UserPosition.  # noqa: E501
        :rtype: object
        """
        return self._bid_open

    @bid_open.setter
    def bid_open(self, bid_open):
        """Sets the bid_open of this UserPosition.


        :param bid_open: The bid_open of this UserPosition.  # noqa: E501
        :type: object
        """

        self._bid_open = bid_open

    @property
    def conv_rate(self):
        """Gets the conv_rate of this UserPosition.  # noqa: E501


        :return: The conv_rate of this UserPosition.  # noqa: E501
        :rtype: object
        """
        return self._conv_rate

    @conv_rate.setter
    def conv_rate(self, conv_rate):
        """Sets the conv_rate of this UserPosition.


        :param conv_rate: The conv_rate of this UserPosition.  # noqa: E501
        :type: object
        """

        self._conv_rate = conv_rate

    @property
    def fpl(self):
        """Gets the fpl of this UserPosition.  # noqa: E501


        :return: The fpl of this UserPosition.  # noqa: E501
        :rtype: object
        """
        return self._fpl

    @fpl.setter
    def fpl(self, fpl):
        """Sets the fpl of this UserPosition.


        :param fpl: The fpl of this UserPosition.  # noqa: E501
        :type: object
        """

        self._fpl = fpl

    @property
    def margin(self):
        """Gets the margin of this UserPosition.  # noqa: E501


        :return: The margin of this UserPosition.  # noqa: E501
        :rtype: object
        """
        return self._margin

    @margin.setter
    def margin(self, margin):
        """Sets the margin of this UserPosition.


        :param margin: The margin of this UserPosition.  # noqa: E501
        :type: object
        """

        self._margin = margin

    @property
    def position_code(self):
        """Gets the position_code of this UserPosition.  # noqa: E501


        :return: The position_code of this UserPosition.  # noqa: E501
        :rtype: str
        """
        return self._position_code

    @position_code.setter
    def position_code(self, position_code):
        """Sets the position_code of this UserPosition.


        :param position_code: The position_code of this UserPosition.  # noqa: E501
        :type: str
        """

        self._position_code = position_code

    @property
    def quantity(self):
        """Gets the quantity of this UserPosition.  # noqa: E501


        :return: The quantity of this UserPosition.  # noqa: E501
        :rtype: object
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this UserPosition.


        :param quantity: The quantity of this UserPosition.  # noqa: E501
        :type: object
        """

        self._quantity = quantity

    @property
    def rate(self):
        """Gets the rate of this UserPosition.  # noqa: E501


        :return: The rate of this UserPosition.  # noqa: E501
        :rtype: object
        """
        return self._rate

    @rate.setter
    def rate(self, rate):
        """Sets the rate of this UserPosition.


        :param rate: The rate of this UserPosition.  # noqa: E501
        :type: object
        """

        self._rate = rate

    @property
    def symbol(self):
        """Gets the symbol of this UserPosition.  # noqa: E501


        :return: The symbol of this UserPosition.  # noqa: E501
        :rtype: str
        """
        return self._symbol

    @symbol.setter
    def symbol(self, symbol):
        """Sets the symbol of this UserPosition.


        :param symbol: The symbol of this UserPosition.  # noqa: E501
        :type: str
        """

        self._symbol = symbol

    @property
    def version(self):
        """Gets the version of this UserPosition.  # noqa: E501


        :return: The version of this UserPosition.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this UserPosition.


        :param version: The version of this UserPosition.  # noqa: E501
        :type: int
        """

        self._version = version

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
        if issubclass(UserPosition, dict):
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
        if not isinstance(other, UserPosition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
