
import liftstatus
import liftstatus.apis.powdr
import pytz
import requests
import datetime

class MountBachelor(liftstatus.apis.powdr.POWDRMountain):
    """Implementation of :class:`liftstatus.Mountain` for Mount Bachelor, OR"""
    
    def __init__(self, session: requests.Session = requests.Session()):
        super().__init__(
            name="Mount Bachelor",
            server_url="https://api.mtbachelor.com/api/v1/dor/drupal/lifts",
            timezone=pytz.timezone('US/Pacific'),
            session=session
        )

    def _map_lift_type(self, lift):
        if lift['type'] in ['six_person']:
            return liftstatus.LiftType.CLD_6
        if lift['type'] in ['quad']:
            if lift['name'] in ['Early Riser']:
                return liftstatus.LiftType.CLF_4
            else:
                return liftstatus.LiftType.CLD_4
        if lift['type'] in ['triple']:
            return liftstatus.LiftType.CLF_3
        if lift['type'] in ['surface', 'carpet']:
            return liftstatus.LiftType.SL
        
        raise liftstatus.exceptions.APIParseException(f"Unknown Type value for lift {lift['name']}: {lift['type']}")
