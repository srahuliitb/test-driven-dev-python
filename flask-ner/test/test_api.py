import unittest
import json
from flask import request

from app import app

class TestApi(unittest.TestCase):
	def test_ner_endpoint_given_some_json_body_returns_200(self):
		with app.test_client() as client:
			response = client.post('/ner', json={"sentence": "Hire me as a senior software engineer"})
			assert response._status_code == 200

	def test_ner_endpoint_given_json_body_with_known_entities_returns_entity_result_in_reponse(self):
		with app.test_client() as client:
			response = client.post('/ner', json={"sentence": "Lionel Messi"})
			data = json.loads(response.get_data())
			# assert len(data['entities']) > 0
			# print(data['entities'][0]['ent'])
			assert data['entities'][0]['ent'] == 'Messi'
			assert data['entities'][0]['label'] == 'Person'