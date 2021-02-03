# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from Tea.converter import TeaConverter


class SendCommondResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SendCommondResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: SendCommondResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SendCommondResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAllProductRequest(TeaModel):
    def __init__(self, request_id=None, product=None, env=None):
        # requestId
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        # pop产品
        self.product = TeaConverter.to_unicode(product)  # type: unicode
        # 环境
        self.env = TeaConverter.to_unicode(env)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.product is not None:
            result['Product'] = self.product
        if self.env is not None:
            result['Env'] = self.env
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('Env') is not None:
            self.env = m.get('Env')
        return self


class GetAllProductResponseBodyData(TeaModel):
    def __init__(self, description=None, domains=None, name_space=None, product=None, type=None):
        # description
        self.description = TeaConverter.to_unicode(description)  # type: unicode
        # 域名
        self.domains = domains  # type: list[unicode]
        # nameSpace
        self.name_space = TeaConverter.to_unicode(name_space)  # type: unicode
        # product
        self.product = TeaConverter.to_unicode(product)  # type: unicode
        # type
        self.type = TeaConverter.to_unicode(type)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.domains is not None:
            result['Domains'] = self.domains
        if self.name_space is not None:
            result['NameSpace'] = self.name_space
        if self.product is not None:
            result['Product'] = self.product
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Domains') is not None:
            self.domains = m.get('Domains')
        if m.get('NameSpace') is not None:
            self.name_space = m.get('NameSpace')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetAllProductResponseBody(TeaModel):
    def __init__(self, code=None, data=None, request_id=None, success=None):
        # code
        self.code = TeaConverter.to_unicode(code)  # type: unicode
        # 产品信息
        self.data = data  # type: GetAllProductResponseBodyData
        # Id of the request
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        # success
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetAllProductResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetAllProductResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: GetAllProductResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetAllProductResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


