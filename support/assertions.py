from support.error_messages import AssertionErrors
import urllib.parse

class Assertions:
    @staticmethod
    def assert_equal(actual, expected):
        assert actual == expected, f'Expected:{expected}, {actual}'
        # expected_decoded = urllib.parse.unquote(expected)
        # actual_decoded = urllib.parse.unquote(actual)
        # assert (expected_decoded == actual_decoded,
        #         AssertionErrors.URL_NOT_FOUND.format(
        #             expected_decoded,
        #             actual_decoded)

        # if error_type == 'url':
        #     assert (expected_decoded == actual_decoded,
        #         AssertionErrors.URL_NOT_FOUND.format(
        #             expected_decoded,
        #             actual_decoded
        #         )
        #     )
        # elif error_type == 'message':
        #     assert (expected_decoded == actual_decoded,
        #             AssertionErrors.MESSAGE_NOT_SENT.format(
        #                 expected_decoded,
        #             )
        #     )
