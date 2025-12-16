import pytest
import liftstatus.mountains

def _print_lifts(lifts):
    for lift in lifts:
        print(f"        '{lift.name.replace('\'', '\\\'')}': liftstatus.LiftType.{lift.type.name},")

def test_jackson_hole():
    test_obj = liftstatus.mountains.wyoming.JacksonHole()
    assert str(test_obj) == "Mountain<name='Jackson Hole'>"

    lifts = test_obj.get_lift_status()

    expected_types = {
        'Aerial Tram': liftstatus.LiftType.ATW,
        'Apres Vous Quad': liftstatus.LiftType.CLD_4,
        'Bridger Gondola': liftstatus.LiftType.MGD,
        'Casper Quad': liftstatus.LiftType.CLD_4,
        'Eagle\'s Rest Quad': liftstatus.LiftType.CLF_4,
        'Marmot Double': liftstatus.LiftType.CLF_2,
        'Moose Creek Quad': liftstatus.LiftType.CLF_4,
        'Sublette Quad': liftstatus.LiftType.CLF_4,
        'Sweetwater Gondola': liftstatus.LiftType.MGD,
        'Teewinot Quad': liftstatus.LiftType.CLD_4,
        'Teton Quad': liftstatus.LiftType.CLD_4,
        'Thunder Quad': liftstatus.LiftType.CLD_4,
        'Union Pass Quad': liftstatus.LiftType.CLF_4,
    }

    # _print_lifts(lifts)
    for lift in lifts:
        assert expected_types[lift.name] == lift.type
