import pytest
import liftstatus.mountains

def _print_lifts(lifts):
    for lift in lifts:
        print(f"        '{lift.name.replace('\'', '\\\'')}': liftstatus.LiftType.{lift.type.name},")

def test_copper():
    test_obj = liftstatus.mountains.colorado.Copper()
    assert str(test_obj) == "Mountain<name='Copper Mountain'>"

    lifts = test_obj.get_lift_status()

    expected_types = {
        'Super Bee': liftstatus.LiftType.CLD_6,
        'Mountain Chief': liftstatus.LiftType.CLF_2,
        'Black Jack': liftstatus.LiftType.CLF_2,
        'Three Bears': liftstatus.LiftType.CLF_3,
        'Storm King': liftstatus.LiftType.SL,
        'Resolution': liftstatus.LiftType.CLF_3,
        'Sierra': liftstatus.LiftType.CLF_3,
        'Rendezvous': liftstatus.LiftType.CLF_3,
        'Celebrity Ridge': liftstatus.LiftType.SL,
        'Pitchfork': liftstatus.LiftType.CLF_2,
        'Gem': liftstatus.LiftType.SL,
        'Easy Rider': liftstatus.LiftType.SL,
        'American Eagle': liftstatus.LiftType.CGD,
        'Tubing Hill': liftstatus.LiftType.SL,
        'Alpine': liftstatus.LiftType.CLF_2,
        'Woodward Express': liftstatus.LiftType.CLD_4,
        'Timberline Express': liftstatus.LiftType.CLD_6,
        'Slingshot/Glide': liftstatus.LiftType.SL,
        'Rugrat': liftstatus.LiftType.SL,
        'Lumberjack': liftstatus.LiftType.CLF_3,
        'Kokomo Express': liftstatus.LiftType.CLD_4,
        'Excelerator': liftstatus.LiftType.CLD_4,
        'American Flyer': liftstatus.LiftType.CLD_6,
    }

    # _print_lifts(lifts)
    for lift in lifts:
        assert expected_types[lift.name] == lift.type


def test_eldora():
    test_obj = liftstatus.mountains.colorado.Eldora()
    assert str(test_obj) == "Mountain<name='Eldora'>"

    lifts = test_obj.get_lift_status()

    expected_types = {
        'Caribou': liftstatus.LiftType.CLF_2,
        'Little Hawk': liftstatus.LiftType.CLF_2,
        'Sundance': liftstatus.LiftType.CLF_2,
        'Corona': liftstatus.LiftType.CLF_4,
        'Alpenglow': liftstatus.LiftType.CLD_6,
        'Sunkid': liftstatus.LiftType.SL,
        'Indian Peaks': liftstatus.LiftType.CLF_4,
        'Race': liftstatus.LiftType.SL,
        'EZ': liftstatus.LiftType.CLF_3,
        'Tenderfoot': liftstatus.LiftType.SL,
    }

    # _print_lifts(lifts)
    for lift in lifts:
        assert expected_types[lift.name] == lift.type

def test_boreal():
    test_obj = liftstatus.mountains.california.Boreal()
    assert str(test_obj) == "Mountain<name='Boreal'>"

    lifts = test_obj.get_lift_status()

    expected_types = {
        'Accelerator Express Quad Charilift': liftstatus.LiftType.CLD_4,
        'Castle Peak Quad Chairlift': liftstatus.LiftType.CLF_4,
        'California Cruiser Quad Chairlift': liftstatus.LiftType.CLF_4,
        'Discovery Carpet': liftstatus.LiftType.SL,
        'Cedar Ridge Triple Chairlift': liftstatus.LiftType.CLF_3,
        '49er Triple Chairlift': liftstatus.LiftType.CLF_3,
        'Lost Dutchman Triple Chairlift': liftstatus.LiftType.CLF_3,
        'Tahoe Tubing Carpet': liftstatus.LiftType.SL,
    }

    # _print_lifts(lifts)
    for lift in lifts:
        assert expected_types[lift.name] == lift.type

def test_soda_springs():
    test_obj = liftstatus.mountains.california.SodaSprings()
    assert str(test_obj) == "Mountain<name='Soda Springs'>"

    lifts = test_obj.get_lift_status()

    expected_types = {
        'Lion\'s Head': liftstatus.LiftType.CLF_2,
        'Crystal Bowl': liftstatus.LiftType.CLF_3,
        'Planet Kids - Carousel': liftstatus.LiftType.SL,
        'Planet Kids - East Sunrise Carpet': liftstatus.LiftType.SL,
        'Planet Kids - West Meadows Carpet': liftstatus.LiftType.SL,
        'Tube Town - Tube Express Carpet': liftstatus.LiftType.SL,
    }

    # _print_lifts(lifts)
    for lift in lifts:
        assert expected_types[lift.name] == lift.type

def test_mt_bachelor():
    test_obj = liftstatus.mountains.oregon.MountBachelor()
    assert str(test_obj) == "Mountain<name='Mount Bachelor'>"

    lifts = test_obj.get_lift_status()

    expected_types = {
        'Alpenglow': liftstatus.LiftType.CLF_3,
        'Chipmunk Carpet': liftstatus.LiftType.SL,
        'Cloudchaser': liftstatus.LiftType.CLD_4,
        'Early Riser': liftstatus.LiftType.CLF_4,
        'First Rays': liftstatus.LiftType.SL,
        'Lava Tube': liftstatus.LiftType.SL,
        'Little Pine (Summer)': liftstatus.LiftType.CLD_4,
        'Little Pine': liftstatus.LiftType.CLD_4,
        'Northwest': liftstatus.LiftType.CLD_4,
        'Outback': liftstatus.LiftType.CLD_4,
        'Pine Marten (Summer)': liftstatus.LiftType.CLD_4,
        'Pine Marten': liftstatus.LiftType.CLD_4,
        'Rainbow': liftstatus.LiftType.CLF_3,
        'Red Chair': liftstatus.LiftType.CLF_3,
        'Skyliner Express': liftstatus.LiftType.CLD_6,
        'Summit': liftstatus.LiftType.CLD_4,
        'Sunrise': liftstatus.LiftType.CLD_4,
    }

    # _print_lifts(lifts)
    for lift in lifts:
        assert expected_types[lift.name] == lift.type

def test_snowbird():
    test_obj = liftstatus.mountains.utah.Snowbird()
    assert str(test_obj) == "Mountain<name='Snowbird'>"

    lifts = test_obj.get_lift_status()

    expected_types = {
        'Aerial Tram': liftstatus.LiftType.ATW,
        'Baby Thunder Conveyor': liftstatus.LiftType.SL,
        'Baby Thunder': liftstatus.LiftType.CLF_2,
        'Baldy': liftstatus.LiftType.CLD_4,
        'Chickadee Conveyor': liftstatus.LiftType.SL,
        'Chickadee': liftstatus.LiftType.CLF_2,
        'Gad 2': liftstatus.LiftType.CLD_4,
        'Gadzoom': liftstatus.LiftType.CLD_4,
        'Little Cloud': liftstatus.LiftType.CLD_4,
        'Mid-Gad': liftstatus.LiftType.CLF_2,
        'Mineral Basin': liftstatus.LiftType.CLD_4,
        'Peruvian Tunnel': liftstatus.LiftType.SL,
        'Peruvian': liftstatus.LiftType.CLD_4,
        'Wilbere': liftstatus.LiftType.CLF_4,
    }

    # _print_lifts(lifts)
    for lift in lifts:
        assert expected_types[lift.name] == lift.type
