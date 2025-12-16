import pytest
import requests
import requests_mock
import liftstatus
import liftstatus.exceptions
import liftstatus.apis.epic
import importlib
import datetime
import dateutil
import json

from . import epic_resources

TEST_URL="http://skunkpa.ws/api/test"

class StubMountain(liftstatus.apis.epic.EpicMountain):
    def __init__(self, session: requests.Session = requests.Session()):
        super().__init__(
            name="Test Mountain",
            server_url=TEST_URL,
            timezone=datetime.UTC,
            session=session
        )

    def _map_lift_type(self, lift):
        if lift['Type'] == 'six':
            return liftstatus.LiftType.CLD_6
        if lift['Type'] == 'gondola':
            return liftstatus.LiftType.MGD
        if lift['Type'] == 'quad':
            return liftstatus.LiftType.CLD_4
        if lift['Type'] == 'conveyor':
            return liftstatus.LiftType.SL

def test_bad_error_code(requests_mock):
    requests_mock.get(TEST_URL, status_code=404)

    with pytest.raises(requests.exceptions.HTTPError):
        StubMountain()._find_terrain_status()

def test_blank_response(requests_mock):
    mock_content = ""
    requests_mock.get(TEST_URL, text=mock_content)

    with pytest.raises(liftstatus.exceptions.APIParseException):
        StubMountain()._find_terrain_status()

def test_good_response(requests_mock):
    with importlib.resources.path(epic_resources, "good_response.aspx") as path:
        with open(path, 'r') as file:
            requests_mock.get(TEST_URL, text=file.read())
    
    expected_response = [
        liftstatus.Lift(name='Avanti Express #2',
            type=liftstatus.LiftType.CLD_6,
            status=liftstatus.LiftStatus.SCHEDULED,
            updated_at=datetime.datetime(2025, 11, 29, 19, 39, 21, 605776, tzinfo=dateutil.tz.tzoffset(None, -25200)),
            open_time=datetime.time(9, 0, tzinfo=datetime.timezone.utc),
            closed_time=datetime.time(15, 30, tzinfo=datetime.timezone.utc),
            wait_time=datetime.timedelta(0)),
        liftstatus.Lift(name='Eagle Bahn Gondola #19',
            type=liftstatus.LiftType.MGD,
            status=liftstatus.LiftStatus.SCHEDULED,
            updated_at=datetime.datetime(2025, 11, 29, 19, 39, 21, 605776, tzinfo=dateutil.tz.tzoffset(None, -25200)),
            open_time=datetime.time(9, 0, tzinfo=datetime.timezone.utc),
            closed_time=datetime.time(15, 15, tzinfo=datetime.timezone.utc),
            wait_time=datetime.timedelta(0)),
        liftstatus.Lift(name='Gondola One',
            type=liftstatus.LiftType.MGD,
            status=liftstatus.LiftStatus.SCHEDULED,
            updated_at=datetime.datetime(2025, 11, 29, 19, 39, 21, 605776, tzinfo=dateutil.tz.tzoffset(None, -25200)),
            open_time=datetime.time(9, 0, tzinfo=datetime.timezone.utc),
            closed_time=datetime.time(15, 15, tzinfo=datetime.timezone.utc),
            wait_time=datetime.timedelta(0)),
        liftstatus.Lift(name='Little Eagle #15',
            type=liftstatus.LiftType.CLD_4,
            status=liftstatus.LiftStatus.SCHEDULED,
            updated_at=datetime.datetime(2025, 11, 29, 19, 39, 21, 605776, tzinfo=dateutil.tz.tzoffset(None, -25200)),
            open_time=datetime.time(9, 0, tzinfo=datetime.timezone.utc),
            closed_time=datetime.time(15, 30, tzinfo=datetime.timezone.utc),
            wait_time=None),
        liftstatus.Lift(name='Mountaintop Express #4',
            type=liftstatus.LiftType.CLD_6,
            status=liftstatus.LiftStatus.SCHEDULED,
            updated_at=datetime.datetime(2025, 11, 29, 19, 39, 21, 605776, tzinfo=dateutil.tz.tzoffset(None, -25200)),
            open_time=datetime.time(9, 0, tzinfo=datetime.timezone.utc),
            closed_time=datetime.time(15, 30, tzinfo=datetime.timezone.utc),
            wait_time=datetime.timedelta(0)),
        liftstatus.Lift(name='Thunder Cat Carpet #35',
            type=liftstatus.LiftType.SL,
            status=liftstatus.LiftStatus.SCHEDULED,
            updated_at=datetime.datetime(2025, 11, 29, 19, 39, 21, 605776, tzinfo=dateutil.tz.tzoffset(None, -25200)),
            open_time=datetime.time(9, 0, tzinfo=datetime.timezone.utc),
            closed_time=datetime.time(15, 30, tzinfo=datetime.timezone.utc),
            wait_time=None)
    ]

    status = StubMountain().get_lift_status()
    assert status == expected_response

@pytest.mark.parametrize('filename',
                         ['invalid_json.aspx'])
def test_bad_json_response(requests_mock, filename):
    with importlib.resources.path(epic_resources, filename) as path:
        with open(path, 'r') as file:
            requests_mock.get(TEST_URL, text=file.read())
    with pytest.raises(json.decoder.JSONDecodeError):
        StubMountain().get_lift_status()

@pytest.mark.parametrize('filename',
                         ['invalid_date.aspx'])
def test_bad_date(requests_mock, filename):
    with importlib.resources.path(epic_resources, filename) as path:
        with open(path, 'r') as file:
            requests_mock.get(TEST_URL, text=file.read())
    with pytest.raises(dateutil.parser._parser.ParserError):
        StubMountain().get_lift_status()


@pytest.mark.parametrize('filename',
                         ['missing_json.aspx', 'invalid_status.aspx'])
def test_bad_response(requests_mock, filename):
    with importlib.resources.path(epic_resources, filename) as path:
        with open(path, 'r') as file:
            requests_mock.get(TEST_URL, text=file.read())
    with pytest.raises(liftstatus.exceptions.APIParseException):
        StubMountain().get_lift_status()

@pytest.mark.parametrize('filename',
                         ['missing_lifts.aspx'])
def test_closed_resort(requests_mock, filename):
    with importlib.resources.path(epic_resources, filename) as path:
        with open(path, 'r') as file:
            requests_mock.get(TEST_URL, text=file.read())
    StubMountain().get_lift_status()
