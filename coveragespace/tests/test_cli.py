# pylint: disable=unused-variable,expression-not-assigned,singleton-comparison

from mock import patch, Mock
from expecter import expect

from coveragespace import cli


def describe_call():

    @patch('coveragespace.cache.Cache.get', Mock())
    def it_handles_invalid_response():
        expect(cli.call('slug', 'metric', 42)) == False
