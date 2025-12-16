import pytest
import liftstatus.mountains

def _print_lifts(lifts):
    for lift in lifts:
        print(f"        '{lift.name.replace('\'', '\\\'')}': liftstatus.LiftType.{lift.type.name},")

def test_arapahoe_basin():
    test_obj = liftstatus.mountains.colorado.ArapahoeBasin()
    assert str(test_obj) == "Mountain<name='Arapahoe Basin'>"

    lifts = test_obj.get_lift_status()

    expected_types = {
        'Black Mountain Express Lift': liftstatus.LiftType.CLD_4,
        'Lenawee Express Lift': liftstatus.LiftType.CLD_6,
        'Pallavicini Lift': liftstatus.LiftType.CLF_2,
        'Beavers': liftstatus.LiftType.CLF_4,
        'Zuma Lift': liftstatus.LiftType.CLF_4,
        'Lazy J Tow': liftstatus.LiftType.SL,
        'Molly Hogan Lift': liftstatus.LiftType.CLF_4,
        'Molly\'s Magic Carpet': liftstatus.LiftType.SL,
        'Pika Place Carpet': liftstatus.LiftType.SL,
    }

    # _print_lifts(lifts)
    for lift in lifts:
        assert expected_types[lift.name] == lift.type
