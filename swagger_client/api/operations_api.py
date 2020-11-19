# coding: utf-8

"""
    Broker API.

    the purpose of this application is to provide an application that is using plain go code to define an API  This should demonstrate all the possible comment annotations that are available to turn go code into a fully compliant swagger 2.0 spec. There are no TOS at this moment, use at your own risk we take no responsibility  # noqa: E501

    OpenAPI spec version: 0.0.1
    Contact: support@cexbro.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class OperationsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def cancel_order(self, **kwargs):  # noqa: E501
        """cancelOrder  # noqa: E501

        This API allows canceling order on an account. but can only cancel orders on behalf of other accounts if a special permission is set. The request can be used to cancel a single order.  Return status code 200  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.cancel_order(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Body2 body:
        :return: CancelOrderHandlerResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.cancel_order_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.cancel_order_with_http_info(**kwargs)  # noqa: E501
            return data

    def cancel_order_with_http_info(self, **kwargs):  # noqa: E501
        """cancelOrder  # noqa: E501

        This API allows canceling order on an account. but can only cancel orders on behalf of other accounts if a special permission is set. The request can be used to cancel a single order.  Return status code 200  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.cancel_order_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Body2 body:
        :return: CancelOrderHandlerResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method cancel_order" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey']  # noqa: E501

        return self.api_client.call_api(
            '/operations/cancel-order', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CancelOrderHandlerResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def cancel_order_group(self, **kwargs):  # noqa: E501
        """cancelOrderGroup  # noqa: E501

        This API allows canceling order on an account. but can only cancel orders on behalf of other accounts if a special permission is set. The request can be used to cancel a multileg order.  Return status code 200  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.cancel_order_group(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Body3 body:
        :return: CancelOrderGroupHandlerResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.cancel_order_group_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.cancel_order_group_with_http_info(**kwargs)  # noqa: E501
            return data

    def cancel_order_group_with_http_info(self, **kwargs):  # noqa: E501
        """cancelOrderGroup  # noqa: E501

        This API allows canceling order on an account. but can only cancel orders on behalf of other accounts if a special permission is set. The request can be used to cancel a multileg order.  Return status code 200  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.cancel_order_group_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Body3 body:
        :return: CancelOrderGroupHandlerResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method cancel_order_group" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey']  # noqa: E501

        return self.api_client.call_api(
            '/operations/cancel-order-group', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CancelOrderGroupHandlerResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def edit_account_order(self, **kwargs):  # noqa: E501
        """editOrder  # noqa: E501

        This API allows editing order details on an account.  The API is via POST and is idempotent. Only conditional requests are accepted.  Return status code 200  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.edit_account_order(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Body4 body:
        :return: EditAccountOrderHandlerResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.edit_account_order_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.edit_account_order_with_http_info(**kwargs)  # noqa: E501
            return data

    def edit_account_order_with_http_info(self, **kwargs):  # noqa: E501
        """editOrder  # noqa: E501

        This API allows editing order details on an account.  The API is via POST and is idempotent. Only conditional requests are accepted.  Return status code 200  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.edit_account_order_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Body4 body:
        :return: EditAccountOrderHandlerResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method edit_account_order" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey']  # noqa: E501

        return self.api_client.call_api(
            '/operations/edit-account-order', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='EditAccountOrderHandlerResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_account_metrics(self, **kwargs):  # noqa: E501
        """getAccountMetrics  # noqa: E501

        This API allows viewing current \"metrics\" for an account, such as equity, margin, PnL etc.  Values in the API are fluent since they depend on current market data. So the client is either expected to poll the API to get current values or to make use of the notifications API (described in a separate document).  Return status code 200  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_account_metrics(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Body1 body:
        :return: AccountMetricsHandlerResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_account_metrics_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_account_metrics_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_account_metrics_with_http_info(self, **kwargs):  # noqa: E501
        """getAccountMetrics  # noqa: E501

        This API allows viewing current \"metrics\" for an account, such as equity, margin, PnL etc.  Values in the API are fluent since they depend on current market data. So the client is either expected to poll the API to get current values or to make use of the notifications API (described in a separate document).  Return status code 200  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_account_metrics_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Body1 body:
        :return: AccountMetricsHandlerResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_account_metrics" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey']  # noqa: E501

        return self.api_client.call_api(
            '/operations/account-metrics', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AccountMetricsHandlerResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_account_order_history_list(self, **kwargs):  # noqa: E501
        """get_account_order_history_list  # noqa: E501

        Return status code 200  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_account_order_history_list(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Body5 body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_account_order_history_list_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_account_order_history_list_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_account_order_history_list_with_http_info(self, **kwargs):  # noqa: E501
        """get_account_order_history_list  # noqa: E501

        Return status code 200  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_account_order_history_list_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Body5 body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_account_order_history_list" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey']  # noqa: E501

        return self.api_client.call_api(
            '/operations/order-account-history', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_market_data(self, **kwargs):  # noqa: E501
        """getMarketData  # noqa: E501

        This API allows to request for market data events. Supported Quote and Candle market data.  Return status code 200  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_market_data(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Body body:
        :return: MarketDataHandlerResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_market_data_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_market_data_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_market_data_with_http_info(self, **kwargs):  # noqa: E501
        """getMarketData  # noqa: E501

        This API allows to request for market data events. Supported Quote and Candle market data.  Return status code 200  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_market_data_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Body body:
        :return: MarketDataHandlerResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_market_data" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey']  # noqa: E501

        return self.api_client.call_api(
            '/marketdata', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='MarketDataHandlerResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_open_order_list(self, **kwargs):  # noqa: E501
        """getOpenOrderList  # noqa: E501

        This API permits to view all the orders on your account.  Return status code 200  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_open_order_list(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object body:
        :return: OpenOrderListHandlerResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_open_order_list_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_open_order_list_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_open_order_list_with_http_info(self, **kwargs):  # noqa: E501
        """getOpenOrderList  # noqa: E501

        This API permits to view all the orders on your account.  Return status code 200  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_open_order_list_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object body:
        :return: OpenOrderListHandlerResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_open_order_list" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey']  # noqa: E501

        return self.api_client.call_api(
            '/operations/open-orders-list', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='OpenOrderListHandlerResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_order_history_list(self, **kwargs):  # noqa: E501
        """getOrderHistoryList  # noqa: E501

        This API allows viewing historical orders (both working orders and orders in final state) on an account.  The API returns current state of the selected orders.  Return status code 200  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_order_history_list(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Body6 body:
        :return: OrderHistoryListHandlerResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_order_history_list_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_order_history_list_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_order_history_list_with_http_info(self, **kwargs):  # noqa: E501
        """getOrderHistoryList  # noqa: E501

        This API allows viewing historical orders (both working orders and orders in final state) on an account.  The API returns current state of the selected orders.  Return status code 200  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_order_history_list_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Body6 body:
        :return: OrderHistoryListHandlerResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_order_history_list" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey']  # noqa: E501

        return self.api_client.call_api(
            '/operations/order-history', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='OrderHistoryListHandlerResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_user_info(self, **kwargs):  # noqa: E501
        """getUserInfo  # noqa: E501

        This API permits to view details for a user  Return status code 200  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object body:
        :return: UserInfoHandlerResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_user_info_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_user_info_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_user_info_with_http_info(self, **kwargs):  # noqa: E501
        """getUserInfo  # noqa: E501

        This API permits to view details for a user  Return status code 200  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_info_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object body:
        :return: UserInfoHandlerResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user_info" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey']  # noqa: E501

        return self.api_client.call_api(
            '/operations/user-info', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='UserInfoHandlerResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def open_account_order(self, **kwargs):  # noqa: E501
        """placeOrder  # noqa: E501

        The API allows submitting a new order or a group of orders on an account.  The API is via POST, so it’s not idempotent.  To avoid issues with duplicate orders, a client is expected to submit a client-unique id of an order with the request. This id is used to track the order later on.  Return status code 200  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.open_account_order(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Body7 body:
        :return: OpenAccountOrderHandlerResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.open_account_order_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.open_account_order_with_http_info(**kwargs)  # noqa: E501
            return data

    def open_account_order_with_http_info(self, **kwargs):  # noqa: E501
        """placeOrder  # noqa: E501

        The API allows submitting a new order or a group of orders on an account.  The API is via POST, so it’s not idempotent.  To avoid issues with duplicate orders, a client is expected to submit a client-unique id of an order with the request. This id is used to track the order later on.  Return status code 200  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.open_account_order_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Body7 body:
        :return: OpenAccountOrderHandlerResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method open_account_order" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey']  # noqa: E501

        return self.api_client.call_api(
            '/operations/place-account-order', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='OpenAccountOrderHandlerResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
