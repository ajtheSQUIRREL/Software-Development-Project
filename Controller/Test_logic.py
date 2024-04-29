import unittest
from unittest.mock import patch
from Logic import weather_data
import json


class TestWeatherData(unittest.TestCase):

    @patch("server.requests.get")
    def test_weather_data(self, mock_get):
        mock_response = {
            "main": {"temp": 289.15},
            "weather": [{"description": "clear sky"}],
            "main": {
                "humidity": 80,
                "pressure": 1013,
            },
            "wind": {"speed": 3.6},
        }
        mock_get.return_value.content.decode.return_value = json.dumps(mock_response)

        # Test with a valid location
        location = "New York"
        expected_result = {
            "Temperature": 16.0,
            "Condition": "Clear sky",
            "Humidity": 80,
            "Pressure": 1013,
            "Wind": 3.6,
        }
        self.assertEqual(weather_data(location), expected_result)

        # Test with invalid location
        invalid_location = "Invalid Location"
        self.assertIsNone(weather_data(invalid_location))


if __name__ == "__main__":
    unittest.main()
