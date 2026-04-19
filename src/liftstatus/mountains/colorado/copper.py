
import liftstatus
import liftstatus.apis.powdr
import pytz
import requests
import datetime

class Copper(liftstatus.apis.powdr.POWDRMountain):
    """Implementation of :class:`liftstatus.Mountain` for Copper, CO"""

    def __init__(self, session: requests.Session = requests.Session()):
        super().__init__(
            name="Copper Mountain",
            server_url="https://api.coppercolorado.com/api/v1/dor/drupal/lifts",
            timezone=pytz.timezone('US/Mountain'),
            session=session
        )

    def _map_lift_type(self, lift):
        if lift['type'] in ['six_person']:
            return liftstatus.LiftType.CLD_6
        if lift['type'] in ['quad']:
            return liftstatus.LiftType.CLD_4
        if lift['type'] in ['triple']:
            return liftstatus.LiftType.CLF_3
        if lift['type'] in ['double']:
            return liftstatus.LiftType.CLF_2
        if lift['type'] in ['surface', 'carpet']:
            return liftstatus.LiftType.SL
        if lift['type'] in ['telemix']:
            return liftstatus.LiftType.CGD
        
        raise liftstatus.exceptions.APIParseException(f"Unknown Type value for lift {lift['name']}: {lift['type']}")