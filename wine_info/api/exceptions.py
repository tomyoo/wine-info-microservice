class ApiException(Exception):
    def __init__(self, errors=[], *args, **kwargs):
        super(ApiException, self).__init__(*args, **kwargs)
        self.errors = errors


class RequestDataException(Exception):
    def __init__(self, errors=[], *args, **kwargs):
        super(RequestDataException, self).__init__(*args, **kwargs)
        self.errors = errors


class ThirdPartyException(Exception):
    def __init__(self, errors=[], *args, **kwargs):
        super(ThirdPartyException, self).__init__(*args, **kwargs)
        self.errors = errors
