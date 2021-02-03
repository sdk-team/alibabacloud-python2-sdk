# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_tea_util import models as util_models
from alibabacloud_yanhjtest20200202 import models as yanhj_test_20200202_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('yanhjtest', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def send_commond_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        return yanhj_test_20200202_models.SendCommondResponse().from_map(
            self.do_rpcrequest('SendCommond', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def send_commond(self):
        runtime = util_models.RuntimeOptions()
        return self.send_commond_with_options(runtime)

    def get_all_product_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return yanhj_test_20200202_models.GetAllProductResponse().from_map(
            self.do_rpcrequest('GetAllProduct', '2020-02-02', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_all_product(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_all_product_with_options(request, runtime)
