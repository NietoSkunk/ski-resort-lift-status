
import liftstatus
import liftstatus.apis.powdr
import pytz
import requests
import datetime

class SodaSprings(liftstatus.apis.powdr.POWDRMountain):
    """Implementation of :class:`liftstatus.Mountain` for Soda Springs, CA"""
    
    def __init__(self, session: requests.Session = requests.Session()):
        super().__init__(
            name="Soda Springs",
            server_url="https://api.skisodasprings.com/api/v1/dor/drupal/lifts",
            timezone=pytz.timezone('US/Pacific'),
            session=session
        )

    def _map_lift_type(self, lift):
        if lift['type'] in ['triple']:
            return liftstatus.LiftType.CLF_3
        elif lift['type'] in ['double']:
            return liftstatus.LiftType.CLF_2
        elif lift['type'] in ['surface', 'carpet', 'snowcat']:
            return liftstatus.LiftType.SL
        
        raise liftstatus.exceptions.APIParseException(f"Unknown Type value for lift {lift['name']}: {lift['type']}")
    