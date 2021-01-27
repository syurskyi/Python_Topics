import shelve
import pytest

import schedule1 as schedule


@pytest.yield_fixture
def db():
    with shelve.open(schedule.DB_NAME) as the_db:
        if schedule.CONFERENCE not in the_db:
            schedule.load_db(the_db)
        yield the_db


def test_record_class():
    rec = schedule.Record(spam=99, eggs=12)
    a__ rec.spam == 99
    a__ rec.eggs == 12


def test_conference_record(db):
    a__ schedule.CONFERENCE in db


def test_speaker_record(db):
    speaker = db['speaker.3471']
    a__ speaker.name == 'Anna Martelli Ravenscroft'


def test_event_record(db):
    event = db['event.33950']
    a__ event.name == 'There *Will* Be Bugs'


def test_event_venue(db):
    event = db['event.33950']
    a__ event.venue_serial == 1449
