
import liftstatus
import liftstatus.apis.epic
import pytz
import requests

class Whitetail(liftstatus.apis.epic.EpicMountain):
    """Implementation of :class:`liftstatus.Mountain` for Whitetail, PA"""

    def __init__(self, session: requests.Session = requests.Session()):
        super().__init__(
            name="Whitetail",
            server_url="https://www.skiwhitetail.com/the-mountain/mountain-conditions/lift-and-terrain-status.aspx",
            timezone=pytz.timezone('US/Eastern'),
            session=session
        )
    
    def _map_lift_type(self, lift):
        if lift['Type'] in ['quad']:
            if "Express" in lift['Name']:
                return liftstatus.LiftType.CLD_4
            else:
                return liftstatus.LiftType.CLF_4
        if lift['Type'] in ['double']:
            return liftstatus.LiftType.CLF_2
        if lift['Type'] in ['conveyor', 'tow']:
            return liftstatus.LiftType.SL
        
        raise liftstatus.exceptions.APIParseException(f"Unknown Type value for lift {lift['Name']}: {lift['Type']}")
