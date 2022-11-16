import typing

import cProfile
import pstats
import unittest
from unittest.mock import patch, MagicMock

from luisd import ApiClient
from luisd.apis.tags.transaction_portfolios_api import TransactionPortfoliosApi


class DeserializationTests(unittest.TestCase):
    """
    to generate the client
    java -jar /Users/justinblack/programming/openapi-generator/modules/openapi-generator-cli/target/openapi-generator-cli.jar generate -i data/lusid.json -o python/luisd -g python-experimental --package-name luisd

    # install lib locally in the luisd folder
    python3 -m venv venv
    source venv/bin/activate
    # install lib in developer mode
    pip install -e .

    # run test
    python main.py
    """

    def test_deserialize(self):
        with open("../data/response.json") as f:
            data = f.read()

        mock_response = MagicMock()
        mock_response.status = 200
        mock_response.reason = "OK"
        mock_response.data = str.encode(data)
        mock_response.getheader.return_value = "application/json"

        type_counts = {
            str: 0,
            int: 0,
            float: 0,
            type(None): 0,
            list: 0,
            dict: 0,
            bool: 0,
        }
        # def count_items(data: typing.Any, count: int=0) -> int:
        #     if isinstance(data, dict):
        #         type_counts[dict] += 1
        #         count += 1
        #         for value in data.values():
        #             count = count_items(value, count)
        #     elif isinstance(data, list):
        #         print(f'list_length={len(data)}')
        #         type_counts[list] += 1
        #         count += 1
        #         for value in data:
        #             count = count_items(value, count)
        #     else:
        #         if isinstance(data, str):
        #             type_counts[str] += 1
        #         elif isinstance(data, int):
        #             type_counts[int] += 1
        #         elif isinstance(data, float):
        #             type_counts[float] += 1
        #         elif data is None:
        #             type_counts[type(None)] += 1
        #         elif isinstance(data, bool):
        #             type_counts[bool] += 1
        #
        #         count += 1
        #     return count

        import json
        json_data = json.loads(data)
        # json_items = count_items(json_data)
        # print(f'json_items={json_items}\n')
        # type_counts = {k: v for k, v in sorted(type_counts.items(), key=lambda item: item[1])}
        # print(f'type_counts={type_counts}\n')

        with patch.object(ApiClient, "request", return_value=mock_response):
            api = TransactionPortfoliosApi()

            profiler = cProfile.Profile()
            profiler.enable()

            api.get_transactions(path_params=dict(scope='a', code='a'))

            profiler.disable()
            stats = pstats.Stats(profiler).sort_stats(pstats.SortKey.CUMULATIVE)
            stats.print_stats()


if __name__ == '__main__':
    unittest.main()

"""
Bugs:
- v6.2.1 there is a duplicate path enum
- v6.2.1 LusidValidationProblemDetails.MetaOapg.properties.errors.MetaOapg.additional_properties.MetaOapg.additional_properties
  incorrectly named, it should be items
- ApiValueError: Value does not conform to the required ISO-8601 datetime format. Invalid value '2022-01-01T00:00:00.0000000+00:00'
  This is correct, there is an extra fractional second
  For now comment out the code

Questions:
1. Where can performance be gained?
validationmetadata use key access

2. Why are there multiple calls that happen n*3?
schemas.py:1359(_get_new_instance_without_conversion)
schemas.py:1486(cast_to_allowed_types)
"""