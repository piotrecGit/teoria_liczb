from flask import make_response


class ResponseSchema:
    def __init__(self, error=None, message=None, data=None):
        self.error = error
        self.message = message
        self.data = data


class ApiResponse:

    def __init__(self, code, flag, message, data):
        self.response_object = ResponseSchema(flag, message, data)
        self.response = make_response(self.response_object.__dict__)
        self.response.headers['Content-Type'] = 'application/json; charset=utf-8'
        self.response.status_code = code
