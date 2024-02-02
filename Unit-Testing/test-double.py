from unittest.mock import Mock


mock = Mock()

print(mock)

mock.api.return_value = {
    'id': 1,
    'message': 'Hello'
    }
print(mock.api)
print(mock.api())