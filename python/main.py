import cProfile
import pstats
import unittest
from unittest.mock import patch, MagicMock

from lusid import TransactionPortfoliosApi, ApiClient


class DeserializationTests(unittest.TestCase):

    def test_deserialize(self):
        with open("../data/response.json") as f:
            data = f.read()

        mock_response = MagicMock()
        mock_response.status = 200
        mock_response.reason = "OK"
        mock_response.data = str.encode(data)
        mock_response.getheader.return_value = "application/json; charset=utf-8"

        with patch.object(ApiClient, "request", return_value=mock_response):
            api = TransactionPortfoliosApi()

            profiler = cProfile.Profile()
            profiler.enable()

            api.get_transactions("mocked", "mocked", )

            profiler.disable()
            stats = pstats.Stats(profiler).sort_stats(pstats.SortKey.CUMULATIVE)
            stats.print_stats()


if __name__ == '__main__':
    unittest.main()
