from rest_framework.test import APIRequestFactory
from ..views import PostViewSet
from rest_framework.test import RequestsClient
from rest_framework.test import APITestCase
from requests.auth import HTTPBasicAuth

class ApiTest(APITestCase):
	""" Test module for Puppy model """

	def setUp(self):
		self.valid_payload = {
			"titulo": "MyPost4",
			"contenido": "test",
			"fecha_pub": "2017-11-17T03:54:14Z",
			"usuario_pub": "satoshi",
			"categoria": "AC"
		}
		
	def test_list_posts(self):
		# Using the standard RequestFactory API to create a form POST request
		factory = APIRequestFactory()
		request = factory.get('/posts/')

		response = PostViewSet.as_view(actions={'get': 'list'})(request)
		self.assertEqual(response.status_code, 200)
		
	def test_add_post(self):
		# Using the standard RequestFactory API to create a form POST request
		factory = APIRequestFactory()
		request = factory.post('/posts/', self.valid_payload)
		request.auth = HTTPBasicAuth('admin', 'admin12345')
			
		response = PostViewSet.as_view(actions={'get': 'list'})(request)
		print(response)
		self.assertEqual(response.status_code, 401)

	def test_list_post_client(self):
		client = RequestsClient()
		response = client.get('http://127.0.0.1:8000/api/posts/')
		self.assertEqual(response.status_code, 200)