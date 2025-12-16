import pytest
import requests
import requests_mock
import liftstatus
import liftstatus.exceptions
import liftstatus.apis.powdr
import importlib
import datetime
import dateutil

# from . import resources

TEST_URL="http://skunkpa.ws/api/test"

class StubMountain(liftstatus.apis.powdr.POWDRMountain):
    def __init__(self, session: requests.Session = requests.Session()):
        super().__init__(
            name="Test Mountain",
            server_url=TEST_URL,
            timezone=datetime.UTC,
            session=session
        )
        self.map_lift_type = None
        self.map_lift_name = None
        self.map_lift_status = None
        self.map_open_time = None
        self.map_closed_time = None
    
    def _map_lift_type(self, lift):
        if self.map_lift_type is not None:
            return self.map_lift_type(lift)
        return super()._map_lift_type(lift)
    
    def _map_lift_status(self, lift):
        if self.map_lift_status is not None:
            return self.map_lift_status(lift)
        return super()._map_lift_status(lift)
    
    def _map_lift_name(self, lift):
        if self.map_lift_name is not None:
            return self.map_lift_name(lift)
        return super()._map_lift_name(lift)
    
    def _map_open_time(self, lift):
        if self.map_open_time is not None:
            return self.map_open_time(lift)
        return super()._map_open_time(lift)
    
    def _map_closed_time(self, lift):
        if self.map_closed_time is not None:
            return self.map_closed_time(lift)
        return super()._map_closed_time(lift)

def test_bad_error_code(requests_mock):
    requests_mock.get(TEST_URL, status_code=404)

    with pytest.raises(requests.exceptions.HTTPError):
        StubMountain().get_lift_status()

def test_blank_response(requests_mock):
    mock_content = ""
    requests_mock.get(TEST_URL, text=mock_content)

    with pytest.raises(requests.exceptions.JSONDecodeError):
        StubMountain().get_lift_status()

def test_invalid_json(requests_mock):
    mock_content = "{"
    requests_mock.get(TEST_URL, text=mock_content)

    with pytest.raises(requests.exceptions.JSONDecodeError):
        StubMountain().get_lift_status()

def test_null_response(requests_mock):
    mock_content = "null"
    requests_mock.get(TEST_URL, text=mock_content)

    with pytest.raises(liftstatus.exceptions.APIParseException):
        StubMountain().get_lift_status()

def test_non_list_response(requests_mock):
    mock_content = "{}"
    requests_mock.get(TEST_URL, text=mock_content)

    with pytest.raises(liftstatus.exceptions.APIParseException):
        StubMountain().get_lift_status()

def test_empty_list(requests_mock):
    mock_content = []
    requests_mock.get(TEST_URL, json=mock_content)
    assert [] == StubMountain().get_lift_status()

def test_map_lift_name(requests_mock):
    mock_content = [
        {
            "name": "Test 1",
            "status": "closed",
            "updated": 0,
            "wait_time": ''
        },
        {
            "name": "Test 2",
            "status": "closed",
            "updated": 0,
            "wait_time": ''
        },
    ]
    requests_mock.get(TEST_URL, json=mock_content)

    expected_response = [
        liftstatus.Lift(
            name='Test 3',
            type=None,
            status=liftstatus.LiftStatus.CLOSED,
            updated_at=datetime.datetime(1970, 1, 1, 0, 0, tzinfo=datetime.timezone.utc),
            open_time=None,
            closed_time=None,
            wait_time=None),
        liftstatus.Lift(
            name='Test 4',
            type=None,
            status=liftstatus.LiftStatus.CLOSED,
            updated_at=datetime.datetime(1970, 1, 1, 0, 0, tzinfo=datetime.timezone.utc),
            open_time=None,
            closed_time=None,
            wait_time=None),
    ]

    def map_lift_name(lift):
        return lift['name'][:-1] + str(int(lift['name'][-1]) + 2)

    mountain = StubMountain()
    mountain.map_lift_name = map_lift_name
    assert expected_response == mountain.get_lift_status()




# def test_blank_response(requests_mock):
#     mock_content = ""
#     requests_mock.get(TEST_URL, text=mock_content)
#     with pytest.raises(requests.exceptions.JSONDecodeError):
#         liftstatus.apis.powdr.get_lift_status(TEST_URL)

# def test_non_list_response(requests_mock):
#     mock_content = {}
#     requests_mock.get(TEST_URL, json=mock_content)
#     with pytest.raises(liftstatus.exceptions.APIParseException):
#         liftstatus.apis.powdr.get_lift_status(TEST_URL)

# def test_good_responses(requests_mock):
#     mock_content = [
#         {
#             'name': 'Lift 1',
#             'type': 'test',
#             'status': 'closed',
#             'hours': '',
#             'wait_time': '',
#             'updated': 0,
#             'TEST_EXPECTED_STATUS': liftstatus.LiftStatus.CLOSED,
#             'TEST_EXPECTED_OPEN_TIME': None,
#             'TEST_EXPECTED_CLOSED_TIME': None,
#             'TEST_EXPECTED_WAIT_TIME': None,
#         },
#         {
#             'name': 'Lift 2',
#             'type': 'test',
#             'status': 'open',
#             'hours': '9am - 3:30pm',
#             'wait_time': '',
#             'updated': 0,
#             'TEST_EXPECTED_STATUS': liftstatus.LiftStatus.OPEN,
#             'TEST_EXPECTED_OPEN_TIME': 900,
#             'TEST_EXPECTED_CLOSED_TIME': 1530,
#             'TEST_EXPECTED_WAIT_TIME': None,
#         },
#         {
#             'name': 'Lift 3',
#             'type': 'test',
#             'status': 'open',
#             'hours': 'Race Training Only',
#             'wait_time': '5',
#             'updated': 0,
#             'TEST_EXPECTED_STATUS': liftstatus.LiftStatus.RESTRICTED,
#             'TEST_EXPECTED_OPEN_TIME': None,
#             'TEST_EXPECTED_CLOSED_TIME': None,
#             'TEST_EXPECTED_WAIT_TIME': 5,
#         },
#         {
#             'name': 'Lift 4',
#             'type': 'test',
#             'status': 'delayed',
#             'hours': '8:15A-3:30P',
#             'wait_time': '5',
#             'updated': 0,
#             'TEST_EXPECTED_STATUS': liftstatus.LiftStatus.DELAYED,
#             'TEST_EXPECTED_OPEN_TIME': 815,
#             'TEST_EXPECTED_CLOSED_TIME': 1530,
#             'TEST_EXPECTED_WAIT_TIME': 5,
#         },
#         {
#             'name': 'Lift 5',
#             'type': 'test',
#             'status': 'hold',
#             'hours': '9a to 4p, M-F | 8:30a to 4p, S-Su',
#             'wait_time': '',
#             'updated': 0,
#             'TEST_EXPECTED_STATUS': liftstatus.LiftStatus.HOLD,
#             'TEST_EXPECTED_OPEN_TIME': 1000,
#             'TEST_EXPECTED_CLOSED_TIME': 1600,
#             'TEST_EXPECTED_WAIT_TIME': None,
#         },
#         {
#             'name': 'Lift 6',
#             'type': 'test',
#             'status': 'expected',
#             'hours': '9a to 4p, M/W/F | 8:30a to 4p, Sat/Sun',
#             'wait_time': '',
#             'updated': 0,
#             'TEST_EXPECTED_STATUS': liftstatus.LiftStatus.SCHEDULED,
#             'TEST_EXPECTED_OPEN_TIME': 1100,
#             'TEST_EXPECTED_CLOSED_TIME': 1600,
#             'TEST_EXPECTED_WAIT_TIME': None,
#         },
#         # "10AM—4PM"
#         # "Closed"
#         # "Scenic Ride Only: 10am - 3pm"
#         # "TBD"
#         # "9 am - 5 pm"
#     ]
#     requests_mock.get(TEST_URL, json=mock_content)
#     for index, lift in enumerate(liftstatus.apis.powdr.get_lift_status(TEST_URL)):
#         assert mock_content[index]['TEST_EXPECTED_STATUS'] == lift.status
#         # assert mock_content[index]['TEST_EXPECTED_OPEN_TIME'] == lift.open_time
#         # assert mock_content[index]['TEST_EXPECTED_CLOSED_TIME'] == lift.closed_time
#         # assert mock_content[index]['TEST_EXPECTED_WAIT_TIME'] == lift.wait_time
#         # updated_at


# # def test_good_response(requests_mock):
# #     with importlib.resources.path(resources, "good_response.aspx") as path:
# #         with open(path, 'r') as file:
# #             requests_mock.get(TEST_URL, text=file.read())
    
# #     expected_response = [
# #         liftstatus.Lift(name='Avanti Express #2',
# #             type="six",
# #             status=liftstatus.LiftStatus.SCHEDULED,
# #             updated_at=datetime.datetime(2025, 11, 29, 19, 39, 21, 605776, tzinfo=dateutil.tz.tzoffset(None, -25200)),
# #             open_time=900,
# #             closed_time=1530,
# #             wait_time=0),
# #         liftstatus.Lift(name='Eagle Bahn Gondola #19',
# #             type="gondola",
# #             status=liftstatus.LiftStatus.SCHEDULED,
# #             updated_at=datetime.datetime(2025, 11, 29, 19, 39, 21, 605776, tzinfo=dateutil.tz.tzoffset(None, -25200)),
# #             open_time=900,
# #             closed_time=1515,
# #             wait_time=0),
# #         liftstatus.Lift(name='Gondola One',
# #             type="gondola",
# #             status=liftstatus.LiftStatus.SCHEDULED,
# #             updated_at=datetime.datetime(2025, 11, 29, 19, 39, 21, 605776, tzinfo=dateutil.tz.tzoffset(None, -25200)),
# #             open_time=900,
# #             closed_time=1515,
# #             wait_time=0),
# #         liftstatus.Lift(name='Little Eagle #15',
# #             type="quad",
# #             status=liftstatus.LiftStatus.SCHEDULED,
# #             updated_at=datetime.datetime(2025, 11, 29, 19, 39, 21, 605776, tzinfo=dateutil.tz.tzoffset(None, -25200)),
# #             open_time=900,
# #             closed_time=1530,
# #             wait_time=None),
# #         liftstatus.Lift(name='Mountaintop Express #4',
# #             type="six",
# #             status=liftstatus.LiftStatus.SCHEDULED,
# #             updated_at=datetime.datetime(2025, 11, 29, 19, 39, 21, 605776, tzinfo=dateutil.tz.tzoffset(None, -25200)),
# #             open_time=900,
# #             closed_time=1530,
# #             wait_time=0),
# #         liftstatus.Lift(name='Thunder Cat Carpet #35',
# #             type="conveyor",
# #             status=liftstatus.LiftStatus.SCHEDULED,
# #             updated_at=datetime.datetime(2025, 11, 29, 19, 39, 21, 605776, tzinfo=dateutil.tz.tzoffset(None, -25200)),
# #             open_time=900,
# #             closed_time=1530,
# #             wait_time=None)
# #     ]

# #     status = liftstatus.apis.powdr.get_lift_status(TEST_URL)
# #     assert status == expected_response

# # @pytest.mark.parametrize('filename',
# #                          ['missing_json.aspx', 'invalid_json.aspx', 'missing_lifts.aspx', 'invalid_date.aspx', 'invalid_status.aspx'])
# # def test_bad_response(requests_mock, filename):
# #     with importlib.resources.path(resources, filename) as path:
# #         with open(path, 'r') as file:
# #             requests_mock.get(TEST_URL, text=file.read())
# #     with pytest.raises(liftstatus.exceptions.APIParseException):
#         liftstatus.apis.powdr.get_lift_status(TEST_URL)
