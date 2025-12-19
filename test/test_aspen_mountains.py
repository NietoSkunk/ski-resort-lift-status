import pytest
import liftstatus.mountains

def _print_lifts(lifts):
    for lift in lifts:
        print(f"        '{lift.name.replace('\'', '\\\'')}': liftstatus.LiftType.{lift.type.name},")

def test_aspen_mountain():
    test_obj = liftstatus.mountains.colorado.AspenMountain()
    assert str(test_obj) == "Mountain<name='Aspen Mountain'>"

    lifts = test_obj.get_lift_status()

    expected_types = {
        'Hero\'s': liftstatus.LiftType.CLD_4,
        'Bell Mountain': liftstatus.LiftType.CLF_2,
        'Little Nell': liftstatus.LiftType.CLF_4,
        'Shadow Mountain': liftstatus.LiftType.CLF_2,
        'Silver Queen Gondola': liftstatus.LiftType.MGD,
        'Ajax Express': liftstatus.LiftType.CLD_4,
        'F.I.S.': liftstatus.LiftType.CLF_2,
        'Ruthies': liftstatus.LiftType.CLD_3,
    }

    # _print_lifts(lifts)
    for lift in lifts:
        assert expected_types[lift.name] == lift.type

def test_aspen_highlands():
    test_obj = liftstatus.mountains.colorado.AspenHighlands()
    assert str(test_obj) == "Mountain<name='Aspen Highlands'>"

    lifts = test_obj.get_lift_status()

    expected_types = {
        'Exhibition': liftstatus.LiftType.CLD_4,
        'Thunderbowl': liftstatus.LiftType.CLF_3,
        'Cloud Nine': liftstatus.LiftType.CLD_4,
        'Deep Temerity': liftstatus.LiftType.CLF_3,
        'Loge Peak': liftstatus.LiftType.CLF_4,
    }

    # _print_lifts(lifts)
    for lift in lifts:
        assert expected_types[lift.name] == lift.type

def test_snowmass():
    test_obj = liftstatus.mountains.colorado.Snowmass()
    assert str(test_obj) == "Mountain<name='Snowmass'>"

    lifts = test_obj.get_lift_status()

    expected_types = {
        'Alpine Springs': liftstatus.LiftType.CLD_4,
        'Assay Hill Carpet': liftstatus.LiftType.SL,
        'High Alpine': liftstatus.LiftType.CLD_4,
        'Big Burn': liftstatus.LiftType.CLD_6,
        'Cirque Surface Lift': liftstatus.LiftType.SL,
        'Sheer Bliss': liftstatus.LiftType.CLD_4,
        'Campground': liftstatus.LiftType.CLF_2,
        'Assay Hill': liftstatus.LiftType.CLF_4,
        'Bear Bottom Carpet': liftstatus.LiftType.SL,
        'Elk Camp Chairlift': liftstatus.LiftType.CLD_6,
        'Elk Camp Gondola': liftstatus.LiftType.MGD,
        'Meadows Carpet': liftstatus.LiftType.SL,
        'Meadows Chairlift': liftstatus.LiftType.CLF_4,
        'Coney Express': liftstatus.LiftType.CLD_4,
        'Sam\'s Knob': liftstatus.LiftType.CLD_4,
        'Scooper Surface Lift': liftstatus.LiftType.SL,
        'Sky Cab Gondola': liftstatus.LiftType.MGD,
        'Treehouse Carpet': liftstatus.LiftType.SL,
        'Village Express': liftstatus.LiftType.CLD_6,
        'Two Creeks': liftstatus.LiftType.CLD_4,
    }

    # _print_lifts(lifts)
    for lift in lifts:
        assert expected_types[lift.name] == lift.type

def test_buttermilk():
    test_obj = liftstatus.mountains.colorado.Buttermilk()
    assert str(test_obj) == "Mountain<name='Buttermilk'>"

    lifts = test_obj.get_lift_status()

    expected_types = {
        'Mighty Mite': liftstatus.LiftType.SL,
        'Panda Peak': liftstatus.LiftType.CLF_2,
        'Summit Express': liftstatus.LiftType.CLD_4,
        'Tiehack Express': liftstatus.LiftType.CLD_4,
        'West Buttermilk Express': liftstatus.LiftType.CLD_4,
    }

    # _print_lifts(lifts)
    for lift in lifts:
        assert expected_types[lift.name] == lift.type
