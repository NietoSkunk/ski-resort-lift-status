
import liftstatus
import liftstatus.apis.powdr
import pytz
import requests
import datetime

def _day_text_to_num_of_week(day):
    if day.upper() in ['M', 'MON', 'MONDAY']:
        return 1
    if day.upper() in ['T', 'TU', 'TUESDAY']:
        return 2
    if day.upper() in ['W', 'WED', 'WEDNESDAY']:
        return 3
    if day.upper() in ['TH', 'THU', 'THURSDAY']:
        return 4
    if day.upper() in ['F', 'FRI', 'FRIDAY']:
        return 5
    if day.upper() in ['S', 'SA', 'SAT', 'SATURDAY']:
        return 6
    if day.upper() in ['SU', 'SUN', 'SUNDAY']:
        return 0
    raise ValueError(f"Unrecognized date text: {day}")

class Eldora(liftstatus.apis.powdr.POWDRMountain):
    """Implementation of :class:`liftstatus.Mountain` for Eldora, CO"""

    def __init__(self, session: requests.Session = requests.Session()):
        super().__init__(
            name="Eldora",
            server_url="https://api.eldora.com/api/v1/dor/drupal/lifts",
            timezone=pytz.timezone('US/Mountain'),
            session=session
        )

    def _map_lift_type(self, lift):
        if lift['type'] in ['six_person']:
            return liftstatus.LiftType.CLD_6
        if lift['type'] in ['quad']:
            return liftstatus.LiftType.CLF_4
        if lift['type'] in ['triple']:
            return liftstatus.LiftType.CLF_3
        if lift['type'] in ['double']:
            return liftstatus.LiftType.CLF_2
        if lift['type'] in ['surface', 'carpet']:
            return liftstatus.LiftType.SL
        
        raise liftstatus.exceptions.APIParseException(f"Unknown Type value for lift {lift['name']}: {lift['type']}")

    def _map_lift_status(self, lift):
        if 'Only' in lift['hours']:
            return liftstatus.LiftStatus.RESTRICTED
        return super()._map_lift_status(lift)
