from ratings.models import Player, Match
import ratings.tools

def test_losing_streak():
    """
    maru pk = 
    has a losing streak of -2 versus Protoss
    """

    maru = Player.objects.get(pk=49)
    return ratings.tools.get_streak(maru,'P') == -2



