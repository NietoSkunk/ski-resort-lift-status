import pytest
import liftstatus.mountains

def _print_lifts(lifts):
    for lift in lifts:
        print(f"        '{lift.name.replace('\'', '\\\'')}': liftstatus.LiftType.{lift.type.name},")

def test_big_sky():
    test_obj = liftstatus.mountains.montana.BigSky()
    assert str(test_obj) == "Mountain<name='Big Sky'>"

    lifts = test_obj.get_lift_status()

    expected_types = {
        'Bear Back': liftstatus.LiftType.SL,
        'Bear Basin Carpet': liftstatus.LiftType.SL,
        'Beehive Basin Carpet': liftstatus.LiftType.SL,
        'Cabin 3': liftstatus.LiftType.CLF_3,
        'Cascade 3': liftstatus.LiftType.CLF_3,
        'Challenger 3': liftstatus.LiftType.CLF_3,
        'Dakota 3': liftstatus.LiftType.CLF_3,
        'Derringer 4': liftstatus.LiftType.CLF_4,
        'Explorer Gondola': liftstatus.LiftType.MGD,
        'Headwaters 2': liftstatus.LiftType.CLF_2,
        'Highlands 3': liftstatus.LiftType.CLF_3,
        'Homer Poma': liftstatus.LiftType.SL,
        'Iron Horse 4': liftstatus.LiftType.CLF_4,
        'Jayhawk 3': liftstatus.LiftType.CLF_3,
        'Lewis and Clark 4': liftstatus.LiftType.CLD_4,
        'Little Thunder 2': liftstatus.LiftType.CLF_2,
        'Lone Moose 3': liftstatus.LiftType.CLF_3,
        'Lone Peak Tram': liftstatus.LiftType.ATW,
        'Lone Tree 4': liftstatus.LiftType.CLF_4,
        'Madison 8': liftstatus.LiftType.CLD_8,
        'Middle Basin Carpet': liftstatus.LiftType.SL,
        'One&Only Gondola': liftstatus.LiftType.MGD,
        'Pea Shooter Carpet': liftstatus.LiftType.SL,
        'Pony Express 3': liftstatus.LiftType.CLF_3,
        'Portable Park Tow': liftstatus.LiftType.SL,
        'Powder Seeker 6': liftstatus.LiftType.CLD_6,
        'Pull-Up Tow': liftstatus.LiftType.SL,
        'Ramcharger 8': liftstatus.LiftType.CLD_8,
        'Sacajawea 3': liftstatus.LiftType.CLF_3,
        'Shedhorn 4': liftstatus.LiftType.CLD_4,
        'Skiwee Carpet': liftstatus.LiftType.SL,
        'Small Fry Carpet': liftstatus.LiftType.SL,
        'Southern Comfort 4': liftstatus.LiftType.CLD_4,
        'Spanish Peaks Carpet 2': liftstatus.LiftType.SL,
        'Spanish Peaks Carpet': liftstatus.LiftType.SL,
        'Stagecoach 2': liftstatus.LiftType.CLF_2,
        'Swift Current 6': liftstatus.LiftType.CLD_6,
        'Thunder Wolf 4': liftstatus.LiftType.CLD_4,
        'Tweener Poma': liftstatus.LiftType.SL,
        'White Otter 2': liftstatus.LiftType.CLF_2,
    }

    # _print_lifts(lifts)
    for lift in lifts:
        assert expected_types[lift.name] == lift.type

def test_boyne():
    test_obj = liftstatus.mountains.michigan.BoyneMountain()
    assert str(test_obj) == "Mountain<name='Boyne Mountain'>"

    lifts = test_obj.get_lift_status()

    expected_types = {
        'Alpine': liftstatus.LiftType.CLF_2,
        'Boyneland': liftstatus.LiftType.CLF_4,
        'Disciples 8': liftstatus.LiftType.CLD_8,
        'Hemlock': liftstatus.LiftType.CLF_2,
        'Estelle\'s Way': liftstatus.LiftType.SL,
        'Meadows': liftstatus.LiftType.CLF_4,
        'Mountain Express': liftstatus.LiftType.CLD_6,
        'Ramshead': liftstatus.LiftType.CLF_4,
        'Superbowl': liftstatus.LiftType.CLF_3,
        'Victor': liftstatus.LiftType.CLF_4,
    }

    # _print_lifts(lifts)
    for lift in lifts:
        assert expected_types[lift.name] == lift.type


def test_brighton():
    test_obj = liftstatus.mountains.utah.Brighton()
    assert str(test_obj) == "Mountain<name='Brighton'>"

    lifts = test_obj.get_lift_status()

    expected_types = {
        'Caterpillar': liftstatus.LiftType.SL,
        'Crest 6': liftstatus.LiftType.CLD_6,
        'Explorer': liftstatus.LiftType.CLF_3,
        'Great Western Express': liftstatus.LiftType.CLD_4,
        'Majestic': liftstatus.LiftType.CLF_4,
        'Milly Express': liftstatus.LiftType.CLD_4,
        'Porcupine': liftstatus.LiftType.SL,
        'Snake Creek': liftstatus.LiftType.CLD_4,
    }

    # _print_lifts(lifts)
    for lift in lifts:
        assert expected_types[lift.name] == lift.type


def test_cypress():
    test_obj = liftstatus.mountains.britishcolumbia.CypressMountain()
    assert str(test_obj) == "Mountain<name='Cypress Mountain'>"

    lifts = test_obj.get_lift_status()

    expected_types = {
        'Eagle Express': liftstatus.LiftType.CLD_4,
        'Easy Rider': liftstatus.LiftType.CLF_4,
        'Lions Express': liftstatus.LiftType.CLD_4,
        'Midway Chair': liftstatus.LiftType.CLF_2,
        'Raven Ridge': liftstatus.LiftType.CLF_4,
        'Sky Quad': liftstatus.LiftType.CLF_4,
    }

    # _print_lifts(lifts)
    for lift in lifts:
        assert expected_types[lift.name] == lift.type


def test_sugarloaf():
    test_obj = liftstatus.mountains.maine.Sugarloaf()
    assert str(test_obj) == "Mountain<name='Sugarloaf'>"

    lifts = test_obj.get_lift_status()

    expected_types = {
        '#3 T-Bar/Bateau': liftstatus.LiftType.SL,
        'Bucksaw Express': liftstatus.LiftType.CLD_4,
        'CVA/Colby T-Bar': liftstatus.LiftType.SL,
        'Double Runner East': liftstatus.LiftType.CLF_2,
        'Double Runner West': liftstatus.LiftType.CLF_2,
        'King Pine': liftstatus.LiftType.CLF_4,
        'Moose-calator': liftstatus.LiftType.SL,
        'Sawduster': liftstatus.LiftType.CLF_2,
        'Skidway': liftstatus.LiftType.CLF_2,
        'Skyline': liftstatus.LiftType.CLF_4,
        'Snubber': liftstatus.LiftType.CLF_3,
        'SuperQuad': liftstatus.LiftType.CLD_4,
        'Timberline': liftstatus.LiftType.CLF_4,
        'West Mountain': liftstatus.LiftType.CLF_2,
        'Whiffletree SuperQuad': liftstatus.LiftType.CLD_4,
    }

    # _print_lifts(lifts)
    for lift in lifts:
        assert expected_types[lift.name] == lift.type


def test_snoqualmie():
    test_obj = liftstatus.mountains.washington.Snoqualmie()
    assert str(test_obj) == "Mountain<name='Summit at Snoqualmie'>"

    lifts = test_obj.get_lift_status()

    expected_types = {
        'Alpental Magic': liftstatus.LiftType.SL,
        'Armstrong Express': liftstatus.LiftType.CLD_4,
        'Central Carpet': liftstatus.LiftType.SL,
        'Central Express': liftstatus.LiftType.CLD_4,
        'Dodge Ridge Chair': liftstatus.LiftType.CLF_2,
        'East Peak Chair': liftstatus.LiftType.CLF_3,
        'Easy Street Chair': liftstatus.LiftType.CLF_2,
        'Edelweiss Chair': liftstatus.LiftType.CLF_3,
        'Gallery Chair': liftstatus.LiftType.CLF_2,
        'Hidden Valley Chair': liftstatus.LiftType.CLF_3,
        'Holiday Chair': liftstatus.LiftType.CLF_4,
        'Internationale Chair': liftstatus.LiftType.CLF_3,
        'Julie\'s Chair': liftstatus.LiftType.CLF_2,
        'Little Thunder Chair': liftstatus.LiftType.CLF_4,
        'Pacific Crest Chair': liftstatus.LiftType.CLF_4,
        'Rampart Chair': liftstatus.LiftType.CLF_4,
        'Reggie\'s Chair': liftstatus.LiftType.CLF_2,
        'Sessel Chair': liftstatus.LiftType.CLF_3,
        'Silver Fir Express': liftstatus.LiftType.CLD_4,
        'St. Bernard Chair': liftstatus.LiftType.CLF_2,
        'Triple 60 Chair': liftstatus.LiftType.CLF_3,
        'West Lower Carpet': liftstatus.LiftType.SL,
        'West Middle Carpet': liftstatus.LiftType.SL,
        'West Upper Carpet': liftstatus.LiftType.SL,
        'Wildside Chair': liftstatus.LiftType.CLF_4,
    }

    # _print_lifts(lifts)
    for lift in lifts:
        assert expected_types[lift.name] == lift.type



def test_sunday_river():
    test_obj = liftstatus.mountains.maine.SundayRiver()
    assert str(test_obj) == "Mountain<name='Sunday River'>"

    lifts = test_obj.get_lift_status()

    expected_types = {
        'Alera Group Competition Lift #5': liftstatus.LiftType.SL,
        'Aurora Peak Quad #12': liftstatus.LiftType.CLF_4,
        'Barker 6 #1': liftstatus.LiftType.CLD_6,
        'Chondola #7': liftstatus.LiftType.CGD,
        'Jordan 8 Lift #14': liftstatus.LiftType.CLD_8,
        'Jordan Mountain Double #13': liftstatus.LiftType.CLF_2,
        'Little White Cap Quad #11': liftstatus.LiftType.CLF_4,
        'Locke Mountain Triple #4': liftstatus.LiftType.CLF_3,
        'Lower Sundance Surface Lift #16': liftstatus.LiftType.SL,
        'Merrill Hill Triple #19': liftstatus.LiftType.CLF_3,
        'Middle Sundance Surface Lift #17': liftstatus.LiftType.SL,
        'North Peak Express #6': liftstatus.LiftType.CLD_4,
        'OZ Quad #15': liftstatus.LiftType.CLF_4,
        'Quantum Leap Triple #3': liftstatus.LiftType.CLF_3,
        'South Ridge Express #2': liftstatus.LiftType.CLD_4,
        'Spruce Peak Triple #8': liftstatus.LiftType.CLF_3,
        'Upper Sundance Surface Lift #18': liftstatus.LiftType.SL,
        'White Cap Quad #9': liftstatus.LiftType.CLF_4,
        'White Heat Quad #10': liftstatus.LiftType.CLF_4,
    }

    # _print_lifts(lifts)
    for lift in lifts:
        assert expected_types[lift.name] == lift.type


def test_loon():
    test_obj = liftstatus.mountains.newhampshire.LoonMountain()
    assert str(test_obj) == "Mountain<name='Loon Mountain'>"

    lifts = test_obj.get_lift_status()

    expected_types = {
        'Children\'s Center Carpet': liftstatus.LiftType.SL,
        'East Basin Double': liftstatus.LiftType.CLF_2,
        'Kancamagus 8': liftstatus.LiftType.CLD_8,
        'Kissin\' Cousin Double': liftstatus.LiftType.CLF_2,
        'Lincoln Express Quad': liftstatus.LiftType.CLD_4,
        'Little Sass Carpet': liftstatus.LiftType.SL,
        'Little Sister Double': liftstatus.LiftType.CLF_2,
        'North Peak Express Quad': liftstatus.LiftType.CLD_4,
        'River\'s Edge Double': liftstatus.LiftType.CLF_2,
        'Sarsaparilla Carpet': liftstatus.LiftType.SL,
        'Seven Brothers Express Quad': liftstatus.LiftType.CLD_4,
        'Timbertown Quad': liftstatus.LiftType.CLF_4,
        'Tote Road Connector': liftstatus.LiftType.CLF_4,
        'White Mountain Express Gondola': liftstatus.LiftType.MGD,
    }

    # _print_lifts(lifts)
    for lift in lifts:
        assert expected_types[lift.name] == lift.type


def test_highlands():
    test_obj = liftstatus.mountains.michigan.BoyneHighlands()
    assert str(test_obj) == "Mountain<name='Boyne Highlands'>"

    lifts = test_obj.get_lift_status()

    expected_types = {
        'Amy\'s': liftstatus.LiftType.CLF_4,
        'Camelot 6': liftstatus.LiftType.CLD_6,
        'Challenger': liftstatus.LiftType.CLF_4,
        'Heather Express': liftstatus.LiftType.CLD_4,
        'Interconnect': liftstatus.LiftType.CLF_3,
        'Magic Carpet': liftstatus.LiftType.SL,
        'North Face': liftstatus.LiftType.CLF_4,
        'Renate\'s Express': liftstatus.LiftType.SL,
    }

    # _print_lifts(lifts)
    for lift in lifts:
        assert expected_types[lift.name] == lift.type


def test_pleasant_mtn():
    test_obj = liftstatus.mountains.maine.PleasantMountain()
    assert str(test_obj) == "Mountain<name='Pleasant Mountain'>"

    lifts = test_obj.get_lift_status()

    expected_types = {
        'Li\'l Pine Beginner Carpet': liftstatus.LiftType.SL,
        'Pine Quad': liftstatus.LiftType.CLF_4,
        'Rabbit Run': liftstatus.LiftType.CLF_3,
        'Snow Pine Carpet': liftstatus.LiftType.SL,
        'Summit Express': liftstatus.LiftType.CLD_4,
        'Sunnyside Triple': liftstatus.LiftType.CLF_3,
    }

    # _print_lifts(lifts)
    for lift in lifts:
        assert expected_types[lift.name] == lift.type

