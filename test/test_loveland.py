import pytest
import liftstatus.mountains

def _print_lifts(lifts):
    for lift in lifts:
        print(f"        '{lift.name.replace('\'', '\\\'')}': liftstatus.LiftType.{lift.type.name},")

def test_loveland():
    test_obj = liftstatus.mountains.colorado.Loveland()
    assert str(test_obj) == "Mountain<name='Loveland Basin/Valley'>"

    lifts = test_obj.get_lift_status()

    expected_types = {
        'Rainbow Magic Carpet': liftstatus.LiftType.SL,
        'Chet\'s Dream': liftstatus.LiftType.CLD_4,
        'Lift 2': liftstatus.LiftType.CLF_3,
        'Ptarmigan': liftstatus.LiftType.CLF_3,
        'Lift 3': liftstatus.LiftType.CLF_4,
        'Lift 4': liftstatus.LiftType.CLF_3,
        'Lift 6': liftstatus.LiftType.CLF_3,
        'Lift 7': liftstatus.LiftType.CLF_4,
        'Lift 8': liftstatus.LiftType.CLF_4,
        'Lift 9': liftstatus.LiftType.CLF_4,
    }

    # _print_lifts(lifts)
    for lift in lifts:
        assert expected_types[lift.name] == lift.type
