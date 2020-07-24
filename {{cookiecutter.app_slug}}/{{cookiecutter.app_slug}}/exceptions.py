class APIError(Exception):
    def __init__(self, code=500, message="Server Error", input_error=[]):
        self.code = code
        self.message = message
        self.input_error = input_error

    @property
    def response(self):
        json = {"error": {
            "code": self.code,
            "message": self.message,
        }}

        if self.input_error:
            json['error'].update({"input_error": self.input_error})

        return json
