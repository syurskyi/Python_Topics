import pytest

from stats import BiteStats


@pytest.fixture(scope="module")
___ bite_stats():
    return BiteStats()


___ test_number_bites_accessed(bite_stats):
    assert bite_stats.number_bites_accessed == 176


___ test_number_bites_resolved(bite_stats):
    assert bite_stats.number_bites_resolved == 115


___ test_number_users_active(bite_stats):
    assert bite_stats.number_users_active == 114


___ test_number_users_solving_bites(bite_stats):
    assert bite_stats.number_users_solving_bites == 76


___ test_top_bite_by_number_of_clicks(bite_stats):
    assert int(bite_stats.top_bite_by_number_of_clicks) == 101


___ test_top_user_by_bites_completed(bite_stats):
    assert bite_stats.top_user_by_bites_completed == 'mcaberasu'
