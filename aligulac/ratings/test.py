import datetime
from django.test import TestCase
from ratings.models import * 
import ratings.tools

class test_get_streak_tool(TestCase):

    #{{{ setup up dummy data for testing
    def setUp(self):
        period = Period.objects.create(start=datetime.date(2013,7,13), end=datetime.date(2013,9,13), computed=True)
        self.winning_player = Player.objects.create(tag="winning_player",race='P')
        self.losing_player = Player.objects.create(tag="losing_player",race='T')
        self.no_match_player = Player.objects.create(tag="no_match_player",race='Z') 
        self.player4 = Player.objects.create(tag="player4",race='R')
        self.player5 = Player.objects.create(tag="player5",race='T')

        match1 = Match.objects.create(period = period,
            date = datetime.date(2013,8,30),
            pla = self.winning_player,
            plb = self.losing_player,
            sca = 3,
            scb = 1,
            rca = self.winning_player.race,
            rcb = self.losing_player.race,
            treated = True,
            game = 'HOTS',
            offline = True
            )

        match2 = Match.objects.create(period = period,
            date = datetime.date(2013,9,1),
            pla = self.winning_player,
            plb = self.losing_player,
            sca = 2,
            scb = 1,
            rca = self.winning_player.race,
            rcb = self.losing_player.race,
            treated = True,
            game = 'HOTS',
            offline = True
            )

        match3 = Match.objects.create(period = period,
            date = datetime.date(2013,9,3),
            pla = self.player4,
            plb = self.player5,
            sca = 2,
            scb = 1,
            rca = 'P',
            rcb = self.player5.race,
            treated = True,
            game = 'HOTS',
            offline = True
            )
        #}}}

    def test_winning_streaks(self):
        vp, vt, vz, va = ratings.tools.get_streaks(self.winning_player.get_matchset(),
            self.winning_player)
        self.assertEqual(va,2)
        self.assertEqual(vt,2)
        self.assertEqual(vp,0)
        self.assertEqual(vz,0)

    def test_losing_streak(self):
        vp, vt, vz, va = ratings.tools.get_streaks(self.losing_player.get_matchset(),
            self.losing_player)
        self.assertEqual(va,-2)
        self.assertEqual(vt,0)
        self.assertEqual(vp,-2)
        self.assertEqual(vz,0)

    def test_no_matches(self):
        vp, vt, vz, va = ratings.tools.get_streaks(self.no_match_player.get_matchset(),
            self.losing_player)
        self.assertEqual(va,0)
        self.assertEqual(vt,0)
        self.assertEqual(vp,0)
        self.assertEqual(vz,0)





    
    

    
        
        
        

            

