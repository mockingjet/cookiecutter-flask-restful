from {{cookiecutter.app_slug}}.utils import print_exception, wrap_response


class TestUtils:

    def test_print_exception(self):
        import contextlib
        from io import StringIO

        def mock_raise_exception():
            raise Exception("xyz")

        stub_stdout = StringIO()
        with contextlib.redirect_stdout(stub_stdout):
            print_exception(Exception)(mock_raise_exception)()
            output = stub_stdout.getvalue().strip()
            assert output == "xyz"

    def test_wrap_response(self):
        mock = {
            "resource": {
                "name": "xxx",
                "value": "yyy"
            }
        }

        def mock_response():
            return mock

        wrapped_resp = wrap_response()(mock_response)()
        assert wrapped_resp["apiVersion"] == 0.0
        assert wrapped_resp["data"] == mock
