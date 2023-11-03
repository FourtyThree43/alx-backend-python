# alx-backend-python

## 0x03. Unittests and Integration Tests

`UnitTests` `Back-end` `Integration tests`

* This repo is for learning purposes. All of the files are tests that were used to learn how to use `unittest` and `integration tests` in Python.

---

## Resources

### Read or watch:

* [unittest — Unit testing framework](https://docs.python.org/3/library/unittest.html "unittest — Unit testing framework")
* [unittest.mock — mock object library](https://docs.python.org/3/library/unittest.mock.html "unittest.mock — mock object library")
* [How to mock a readonly property with mock?](https://stackoverflow.com/questions/11993395/how-to-mock-a-readonly-property-with-mock "How to mock a readonly property with mock?")
* [parameterized](https://pypi.org/project/parameterized/ "parameterized")
* [Memoization](https://en.wikipedia.org/wiki/Memoization "Memoization")

---

## Learning Objectives

### General

* The difference between unit and integration tests.
* Common testing patterns such as mocking, parametrizations and fixtures
* How and when to use mocks
* What are the differences between mocks and stubs
* How to implement hooks to alter the behavior of tests
* How to use parameterization to create generic tests
* When to use integration tests

---

## Enviroment

* Language: Python 3.4.3
* OS: Ubuntu 14.04 LTS (Trusty Thar)
* Style guidelines: [PEP 8 (version 1.7) for Python 3.5](https://www.python.org/dev/peps/pep-0008/ "PEP 8 (version 1.7) for Python 3.5")
* Python unit test library
* Python mock module
* parameterized module

---

### [0. Parameterize a unit test](./test_utils.py "0. Parameterize a unit test")
* Familiarize yourself with the `utils.access_nested_map` function and understand its purpose. Play with it in the Python console to make sure you understand.
* In the tests/test_utils.py file you will find the following test cases:
```python
def test_access_nested_map_exception():
	""" Test access_nested_map with exception """
	with self.assertRaises(KeyError):
		access_nested_map({"a": 1}, ("a", "b"))
```

* Update the following test cases:
```python
def test_access_nested_map():
	""" Test access_nested_map """
	nested_map = {"a": {"b": 2}}
	self.assertEqual(access_nested_map(nested_map, ("a", )), {"b": 2})
	self.assertEqual(access_nested_map(nested_map, ("a", "b")), 2)
```

* Update the following test cases:
```python
@parameterized.expand([
	({}, ("a",), KeyError),
	({"a": 1}, ("a", "b"), KeyError)
])
def test_access_nested_map_exception(nested_map, path, expected):
	""" Test access_nested_map with exception """
	with self.assertRaises(expected):
		access_nested_map(nested_map, path)
```

### [1. Parameterize a unit test](./test_utils.py "1. Parameterize a unit test")
* Implement the `TestIntegration.test_integration` method to test the `utils.get_json` function.

* Use the parameterized module to parametrize the following test cases for the `utils.get_json` function.

```python
def test_get_json(self, test_url, test_payload):
	""" Test get_json """
	mock = Mock()
	mock.json.return_value = test_payload
	with patch('requests.get', return_value=mock) as mock_get:
		self.assertEqual(get_json(test_url), test_payload)
		mock_get.assert_called_once()
```

* Use the parameterized module to parametrize the following test cases for the `utils.get_json` function.

```python
@parameterized.expand([
	("http://example.com", {"payload": True}),
	("http://holberton.io", {"payload": False})
])
def test_get_json(self, test_url, test_payload):
	""" Test get_json """
	mock = Mock()
	mock.json.return_value = test_payload
	with patch('requests.get', return_value=mock) as mock_get:
		self.assertEqual(get_json(test_url), test_payload)
		mock_get.assert_called_once()
```


### [2. Mock HTTP calls](./test_utils.py "2. Mock HTTP calls")
* Familiarize yourself with the `utils.get_json` function.
* In the tests/test_utils.py file you will find the following test cases:
```python
def test_get_json(self):
	""" Test get_json """
	mock = Mock()
	mock.json.return_value = {"payload": True}
	with patch('requests.get', return_value=mock) as mock_get:
		self.assertEqual(get_json("http://example.com"), {"payload": True})
		mock_get.assert_called_once()
```

### [3. Parameterize and patch](./test_client.py "3. Parameterize and patch")
* Familiarize yourself with the `client.GithubOrgClient._public_repos_url` method.
* In the tests/test_client.py file you will find the following test cases:
```python
def test_public_repos_url(self):
	""" Test public_repos_url """
	with patch('client.get_json', return_value=[{"name": "Google"}]) as mock_get:
		g = GithubOrgClient("google")
		self.assertEqual(g._public_repos_url, "https://api.github.com/orgs/google/repos")
		mock_get.assert_called_once()
```

* Update the following test cases:
```python
def test_public_repos_url(self):
	""" Test public_repos_url """
	with patch('client.get_json', return_value=[{"name": "Google"}]) as mock_get:
		g = GithubOrgClient("google")
		self.assertEqual(g._public_repos_url, "https://api.github.com/orgs/google/repos")
		mock_get.assert_called_once()
```

### [4. Parameterize and patch as decorators](./test_client.py "4. Parameterize and patch as decorators")
* Familiarize yourself with the `client.GithubOrgClient._public_repos_url` method.
* In the tests/test_client.py file you will find the following test cases:
```python
def test_public_repos(self):
	""" Test public_repos """
	with patch('client.GithubOrgClient._public_repos_url',
			 new_callable=PropertyMock) as mock_public_repos_url:
		with patch('client.get_json', return_value=[{"name": "Google"}]) as mock_get:
			g = GithubOrgClient("google")
			self.assertEqual(g.public_repos(), ["Google"])
			mock_public_repos_url.assert_called_once()
			mock_get.assert_called_once()
```

* Update the following test cases:
```python
@patch('client.GithubOrgClient._public_repos_url', new_callable=PropertyMock)
@patch('client.get_json')
def test_public_repos(self, mock_get_json, mock_public_repos_url):
	""" Test public_repos """
	mock_get_json.return_value = [{"name": "Google"}]
	mock_public_repos_url.return_value = "http://mock.url"
	g = GithubOrgClient("google")
	self.assertEqual(g.public_repos(), ["Google"])
	mock_public_repos_url.assert_called_once()
	mock_get_json.assert_called_once()
```

### [5. Mocking a property](./test_client.py "5. Mocking a property")
* Familiarize yourself with the `client.GithubOrgClient._public_repos_url` method.
* In the tests/test_client.py file you will find the following test cases:
```python
def test_has_license(self):
	""" Test has_license """
	with patch('client.GithubOrgClient._license', new_callable=PropertyMock) as mock_license:
		mock_license.return_value = {"key": "my_license"}
		g = GithubOrgClient("google")
		self.assertEqual(g.has_license("my_license"), True)
		self.assertEqual(g.has_license("other_license"), False)
		mock_license.assert_called_once()
```

* Update the following test cases:
```python
@patch('client.GithubOrgClient._license', new_callable=PropertyMock)
def test_has_license(self, mock_license):
	""" Test has_license """
	mock_license.return_value = {"key": "my_license"}
	g = GithubOrgClient("google")
	self.assertEqual(g.has_license("my_license"), True)
	self.assertEqual(g.has_license("other_license"), False)
	mock_license.assert_called_once()
```

### [6. Patch an object](./test_client.py "6. Patch an object")
* Familiarize yourself with the `client.GithubOrgClient.org` method.
* In the tests/test_client.py file you will find the following test cases:
```python
def test_public_repos_with_license(self):
	""" Test public_repos with the license """
	with patch('client.GithubOrgClient._public_repos_url',
			 new_callable=PropertyMock) as mock_public_repos_url:
		with patch('client.get_json', return_value=[{"name": "Google",
													  "license": {"key": "my_license"}},
													 {"name": "Towels",
													  "license": {"key": "other_license"}}]) as mock_get:
			g = GithubOrgClient("google")
			self.assertEqual(g.public_repos("my_license"), ["Google"])
			self.assertEqual(g.public_repos("other_license"), ["Towels"])
			mock_public_repos_url.assert_called_once()
			mock_get.assert_called_once()
```

* Update the following test cases:
```python
@patch('client.GithubOrgClient._public_repos_url', new_callable=PropertyMock)
@patch('client.get_json')
def test_public_repos_with_license(self, mock_get_json, mock_public_repos_url):
	""" Test public_repos with the license """
	mock_get_json.return_value = [{"name": "Google",
								   "license": {"key": "my_license"}},
								  {"name": "Towels",
								   "license": {"key": "other_license"}}]
	mock_public_repos_url.return_value = "http://mock.url"
	g = GithubOrgClient("google")
	self.assertEqual(g.public_repos("my_license"), ["Google"])
	self.assertEqual(g.public_repos("other_license"), ["Towels"])
	mock_public_repos_url.assert_called_once()
	mock_get_json.assert_called_once()
```

### [7. Parameterize](./test_client.py "7. Parameterize")
* Familiarize yourself with the `client.GithubOrgClient.org` method.
* In the tests/test_client.py file you will find the following test cases:
```python
def test_public_repos_with_license(self):
	""" Test public_repos with the license """
	with patch('client.GithubOrgClient._public_repos_url',
			 new_callable=PropertyMock) as mock_public_repos_url:
		with patch('client.get_json', return_value=[{"name": "Google",
													  "license": {"key": "my_license"}},
													 {"name": "Towels",
													  "license": {"key": "other_license"}}]) as mock_get:
			g = GithubOrgClient("google")
			self.assertEqual(g.public_repos("my_license"), ["Google"])
			self.assertEqual(g.public_repos("other_license"), ["Towels"])
			mock_public_repos_url.assert_called_once()
			mock_get.assert_called_once()
```

* Update the following test cases:
```python
@patch('client.GithubOrgClient._public_repos_url', new_callable=PropertyMock)
@patch('client.get_json')
def test_public_repos_with_license(self, mock_get_json, mock_public_repos_url):
	""" Test public_repos with the license """
	mock_get_json.return_value = [{"name": "Google",
								   "license": {"key": "my_license"}},
								  {"name": "Towels",
								   "license": {"key": "other_license"}}]
	mock_public_repos_url.return_value = "http://mock.url"
	g = GithubOrgClient("google")
	self.assertEqual(g.public_repos("my_license"), ["Google"])
	self.assertEqual(g.public_repos("other_license"), ["Towels"])
	mock_public_repos_url.assert_called_once()
	mock_get_json.assert_called_once()
```

### [8. Integration test: fixtures](./test_client.py "8. Integration test: fixtures")
* Familiarize yourself with the `client.GithubOrgClient.org` method.
* In the tests/test_client.py file you will find the following test cases:
```python
def test_public_repos_with_license(self):
	""" Test public_repos with the license """
	with patch('client.GithubOrgClient._public_repos_url',
			 new_callable=PropertyMock) as mock_public_repos_url:
		with patch('client.get_json', return_value=[{"name": "Google",
													  "license": {"key": "my_license"}},
													 {"name": "Towels",
													  "license": {"key": "other_license"}}]) as mock_get:
			g = GithubOrgClient("google")
			self.assertEqual(g.public_repos("my_license"), ["Google"])
			self.assertEqual(g.public_repos("other_license"), ["Towels"])
			mock_public_repos_url.assert_called_once()
			mock_get.assert_called_once()
```

* Update the following test cases:
```python
@patch('client.GithubOrgClient._public_repos_url', new_callable=PropertyMock)
@patch('client.get_json')
def test_public_repos_with_license(self, mock_get_json, mock_public_repos_url):
	""" Test public_repos with the license """
	mock_get_json.return_value = [{"name": "Google",
								   "license": {"key": "my_license"}},
								  {"name": "Towels",
								   "license": {"key": "other_license"}}]
	mock_public_repos_url.return_value = "http://mock.url"
	g = GithubOrgClient("google")
	self.assertEqual(g.public_repos("my_license"), ["Google"])
	self.assertEqual(g.public_repos("other_license"), ["Towels"])
	mock_public_repos_url.assert_called_once()
	mock_get_json.assert_called_once()
```

## Author
* **FourtyThree43** - [FT43](https://.github.com/FourtyThree43 "FT43")
