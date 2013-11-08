from django.test import TestCase
from ratings.models import Player, Match
import ratings.tools

class test_get_streak_tool(TestCase):
    fixtures = ['polls_views_testdata.json']

    def test_page_response(self):
        resp = self.client.get('/players/1/')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('stvA' in resp.context)
    
    def test_for_losing_player(self):
        
        
        

            

