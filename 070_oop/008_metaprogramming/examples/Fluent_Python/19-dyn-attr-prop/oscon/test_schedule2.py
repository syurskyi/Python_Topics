import shelve
import pytest

import schedule2 as schedule


@pytest.yield_fixture
def db():
    with shelve.open(schedule.DB_NAME) as the_db:
        if schedule.CONFERENCE not in the_db:
            schedule.load_db(the_db)
        yield the_db


def test_record_attr_access():
    rec = schedule.Record(spam=99, eggs=12)
    a__ rec.spam == 99
    a__ rec.eggs == 12


def test_record_repr():
    rec = schedule.DbRecord(spam=99, eggs=12)
    a__ 'DbRecord object at 0x' in repr(rec)
    rec2 = schedule.DbRecord(serial=13)
    a__ repr(rec2) == "<DbRecord serial=13>"


def test_conference_record(db):
    a__ schedule.CONFERENCE in db


def test_speaker_record(db):
    speaker = db['speaker.3471']
    a__ speaker.name == 'Anna Martelli Ravenscroft'


def test_missing_db_exception():
    with pytest.raises(schedule.MissingDatabaseError):
        schedule.DbRecord.fetch('venue.1585')


def test_dbrecord(db):
    schedule.DbRecord.set_db(db)
    venue = schedule.DbRecord.fetch('venue.1585')
    a__ venue.name == 'Exhibit Hall B'


def test_event_record(db):
    event = db['event.33950']
    a__ repr(event) == "<Event 'There *Will* Be Bugs'>"


def test_event_venue(db):
    schedule.Event.set_db(db)
    event = db['event.33950']
    a__ event.venue_serial == 1449
    a__ event.venue == db['venue.1449']
    a__ event.venue.name == 'Portland 251'


def test_event_speakers(db):
    schedule.Event.set_db(db)
    event = db['event.33950']
    a__ len(event.speakers) == 2
    anna_and_alex = [db['speaker.3471'], db['speaker.5199']]
    a__ event.speakers == anna_and_alex


def test_event_no_speakers(db):
    schedule.Event.set_db(db)
    event = db['event.36848']
    a__ len(event.speakers) == 0
