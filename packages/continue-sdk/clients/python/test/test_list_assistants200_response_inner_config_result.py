# coding: utf-8

"""
    Continue Hub IDE API

    API for Continue IDE to fetch assistants and other related information. These endpoints are primarily used by the Continue IDE extensions for VS Code and JetBrains. 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.list_assistants200_response_inner_config_result import ListAssistants200ResponseInnerConfigResult

class TestListAssistants200ResponseInnerConfigResult(unittest.TestCase):
    """ListAssistants200ResponseInnerConfigResult unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListAssistants200ResponseInnerConfigResult:
        """Test ListAssistants200ResponseInnerConfigResult
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListAssistants200ResponseInnerConfigResult`
        """
        model = ListAssistants200ResponseInnerConfigResult()
        if include_optional:
            return ListAssistants200ResponseInnerConfigResult(
                config = None,
                config_load_interrupted = True,
                errors = [
                    ''
                    ]
            )
        else:
            return ListAssistants200ResponseInnerConfigResult(
                config = None,
                config_load_interrupted = True,
        )
        """

    def testListAssistants200ResponseInnerConfigResult(self):
        """Test ListAssistants200ResponseInnerConfigResult"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
