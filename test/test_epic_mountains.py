import pytest
import liftstatus

def _print_lifts(lifts):
    for lift in lifts:
        print(f"        '{lift.name.replace('\'', '\\\'')}': liftstatus.LiftType.{lift.type.name},")

def test_whistler_blackcomb():
    test_obj = liftstatus.mountains.britishcolumbia.WhistlerBlackcomb()
    assert str(test_obj) == "Mountain<name='Whistler Blackcomb'>"

    lifts = test_obj.get_lift_status()
    expected_types = {
        '7th Heaven Express': liftstatus.LiftType.CLD_4,
        'Admin Carpet - Blackcomb': liftstatus.LiftType.SL,
        'Adult Mini Carpet - Whistler - Olympic Zone': liftstatus.LiftType.SL,
        'Base 2 - Blackcomb - Ski and Ride School Only': liftstatus.LiftType.SL,
        'Big Red Express': liftstatus.LiftType.CLD_6,
        'Blackcomb Gondola - Lower': liftstatus.LiftType.MGD,
        'Blackcomb Gondola - Upper': liftstatus.LiftType.MGD,
        'Bubly Tube Park': liftstatus.LiftType.SL,
        'Catskinner Express': liftstatus.LiftType.CLD_4,
        'Chateau Carpet - Blackcomb': liftstatus.LiftType.SL,
        'CLC Mini Carpet - Whistler - CLC - Whistler Kids Only': liftstatus.LiftType.SL,
        'Creekside Carpet - Whistler - Whistler Kids Only': liftstatus.LiftType.SL,
        'Creekside Gondola': liftstatus.LiftType.MGD,
        'Crystal Ridge Express': liftstatus.LiftType.CLD_4,
        'Emerald 6 Express': liftstatus.LiftType.CLD_6,
        'Excalibur Gondola - Lower': liftstatus.LiftType.MGD,
        'Excalibur Gondola - Upper': liftstatus.LiftType.MGD,
        'Excelerator Express': liftstatus.LiftType.CLD_4,
        'Fantastic Carpet - Whistler - Olympic Zone': liftstatus.LiftType.SL,
        'Fitzsimmons 8 Express': liftstatus.LiftType.CLD_8,
        'Franz\'s Chair': liftstatus.LiftType.CLF_3,
        'Garbanzo Express': liftstatus.LiftType.CLD_4,
        'Glacier Express': liftstatus.LiftType.CLD_4,
        'Harmony 6 Express': liftstatus.LiftType.CLD_6,
        'Jersey Cream Express': liftstatus.LiftType.CLD_6,
        'Magic Chair': liftstatus.LiftType.CLF_3,
        'Olympic Chair': liftstatus.LiftType.CLF_3,
        'PEAK 2 PEAK Gondola': liftstatus.LiftType.TGD,
        'Peak Express': liftstatus.LiftType.CLD_4,
        'Scampland Carpet - Whistler - CLC -Whistler Kids Only': liftstatus.LiftType.SL,
        'Showcase T-Bar': liftstatus.LiftType.SL,
        'Snowboard Carpet - Whistler - Olympic Zone': liftstatus.LiftType.SL,
        'Super Carpet - Whistler - Olympic Zone': liftstatus.LiftType.SL,
        'Symphony Express': liftstatus.LiftType.CLD_4,
        'T-Bar': liftstatus.LiftType.SL,
        'Whistler Village Gondola  - Lower': liftstatus.LiftType.MGD,
        'Whistler Village Gondola - Upper': liftstatus.LiftType.MGD,
    }

    # _print_lifts(lifts)
    for lift in lifts:
        assert expected_types[lift.name] == lift.type

def test_heavenly():
    test_obj = liftstatus.mountains.california.Heavenly()
    assert str(test_obj) == "Mountain<name='Heavenly'>"

    lifts = test_obj.get_lift_status()
    expected_types = {
        'Bear Cave': liftstatus.LiftType.SL,
        'Big Easy': liftstatus.LiftType.CLF_4,
        'Boulder': liftstatus.LiftType.CLF_3,
        'Boulder Carpet': liftstatus.LiftType.SL,
        'Canyon': liftstatus.LiftType.CLD_4,
        'Comet': liftstatus.LiftType.CLD_4,
        'Dipper': liftstatus.LiftType.CLD_4,
        'Enchanted Forest': liftstatus.LiftType.SL,
        'First Ride': liftstatus.LiftType.CLF_3,
        'Galaxy': liftstatus.LiftType.CLF_3,
        'Gondola': liftstatus.LiftType.MGD,
        'Groove': liftstatus.LiftType.CLF_3,
        'Gunbarrel': liftstatus.LiftType.CLD_4,
        'Mott': liftstatus.LiftType.CLF_2,
        'North Bowl': liftstatus.LiftType.CLD_4,
        'Olympic': liftstatus.LiftType.CLD_4,
        'Patsy\'s': liftstatus.LiftType.CLF_3,
        'Pioneer': liftstatus.LiftType.SL,
        'Powderbowl': liftstatus.LiftType.CLD_6,
        'Red Fir': liftstatus.LiftType.SL,
        'Sky': liftstatus.LiftType.CLD_4,
        'Stagecoach': liftstatus.LiftType.CLD_4,
        'Tamarack': liftstatus.LiftType.CLD_6,
        'The Meadow Carpet': liftstatus.LiftType.SL,
        'The Tram': liftstatus.LiftType.ATW,
        'Tube Lift': liftstatus.LiftType.SL,
        'World Cup': liftstatus.LiftType.CLF_2,
    }

    # _print_lifts(lifts)
    for lift in lifts:
        assert expected_types[lift.name] == lift.type

def test_kirkwood():
    test_obj = liftstatus.mountains.california.Kirkwood()
    assert str(test_obj) == "Mountain<name='Kirkwood'>"

    lifts = test_obj.get_lift_status()
    expected_types = {
        '#1 Snowkirk': liftstatus.LiftType.CLF_3,
        '#2 Caples Crest': liftstatus.LiftType.CLF_3,
        '#3 Iron Horse': liftstatus.LiftType.CLF_2,
        '#4 Sunrise': liftstatus.LiftType.CLF_4,
        '#5 Solitude': liftstatus.LiftType.CLF_3,
        '#6 Cornice Express': liftstatus.LiftType.CLD_4,
        '#7 TC Express': liftstatus.LiftType.CLD_4,
        '#8 Tow Rope': liftstatus.LiftType.SL,
        '#9 Bunny': liftstatus.LiftType.CLF_3,
        '#10 The Wall': liftstatus.LiftType.CLF_3,
        '#11 The Reut': liftstatus.LiftType.CLF_3,
        '#12 Ski School Magic Carpet': liftstatus.LiftType.SL,
        '#13 Public Magic Carpet': liftstatus.LiftType.SL,
        '#14 Vista T-Bar': liftstatus.LiftType.SL,
    }

    # _print_lifts(lifts)
    for lift in lifts:
        assert expected_types[lift.name] == lift.type

def test_northstar():
    test_obj = liftstatus.mountains.california.Northstar()
    assert str(test_obj) == "Mountain<name='Northstar'>"

    lifts = test_obj.get_lift_status()

    expected_types = {
        'Arrow Express': liftstatus.LiftType.CLD_4,
        'Backside Express': liftstatus.LiftType.CLD_4,
        'Big Springs Express Gondola': liftstatus.LiftType.MGD,
        'Comstock Express': liftstatus.LiftType.CLD_6,
        'Hemlock Carpet': liftstatus.LiftType.SL,
        'Highlands Gondola': liftstatus.LiftType.MGD,
        'Jeffrey Pines Carpet': liftstatus.LiftType.SL,
        'Juniper Carpet': liftstatus.LiftType.SL,
        'Lookout Link Platter': liftstatus.LiftType.SL,
        'Martis Camp Express': liftstatus.LiftType.CLD_4,
        'Promised Land Express': liftstatus.LiftType.CLD_4,
        'Rendezvous Triple': liftstatus.LiftType.CLF_3,
        'Sugar Pine Carpet': liftstatus.LiftType.SL,
        'Tahoe Zephyr Express': liftstatus.LiftType.CLD_6,
        'The Big Easy Quad': liftstatus.LiftType.CLF_4,
        'The Spruces Carpet': liftstatus.LiftType.SL,
        'Timberline Triple': liftstatus.LiftType.CLF_3,
        'Village Express': liftstatus.LiftType.CLD_4,
        'Vista Express': liftstatus.LiftType.CLD_4,
    }

    # _print_lifts(lifts)
    for lift in lifts:
        assert expected_types[lift.name] == lift.type

def test_beaver_creek():
    test_obj = liftstatus.mountains.colorado.BeaverCreek()
    assert str(test_obj) == "Mountain<name='Beaver Creek'>"

    lifts = test_obj.get_lift_status()
    expected_types = {
        'Arrow Bahn Express': liftstatus.LiftType.CLD_4,
        'Bachelor Gulch Express': liftstatus.LiftType.CLD_4,
        'Bibber Bahn': liftstatus.LiftType.SL,
        'Birds of Prey Express': liftstatus.LiftType.CLD_4,
        'Centennial Express': liftstatus.LiftType.MGD,
        'Centennial Express: Chair 6': liftstatus.LiftType.CLD_6,
        'Cinch Express': liftstatus.LiftType.CLD_4,
        'Elkhorn Lift': liftstatus.LiftType.CLF_3,
        'Grouse Mountain Express': liftstatus.LiftType.CLD_4,
        'Haymeadow Express': liftstatus.LiftType.MGD,
        'Highlands Lift': liftstatus.LiftType.CLF_2,
        'Jitterbug': liftstatus.LiftType.SL,
        'Larkspur Express': liftstatus.LiftType.CLD_4,
        'Lower BC Mtn Express': liftstatus.LiftType.CLD_4,
        'Magic Carpet': liftstatus.LiftType.SL,
        'McCoy Park Express': liftstatus.LiftType.CLD_4,
        'Red Buffalo Express': liftstatus.LiftType.CLD_4,
        'Reunion Lift': liftstatus.LiftType.CLD_4,
        'Ritz Bahn': liftstatus.LiftType.SL,
        'Riverfront Express Gondola': liftstatus.LiftType.MGD,
        'Rose Bowl Express': liftstatus.LiftType.CLD_4,
        'Snowflake': liftstatus.LiftType.SL,
        'Strawberry Park Express': liftstatus.LiftType.CLD_4,
        'Trail Rider': liftstatus.LiftType.SL,
        'Upper BC Mtn Express': liftstatus.LiftType.CLD_4,
        'Wagon Train': liftstatus.LiftType.SL,
    }

    # _print_lifts(lifts)
    for lift in lifts:
        assert expected_types[lift.name] == lift.type

def test_breckenridge():
    test_obj = liftstatus.mountains.colorado.Breckenridge()
    assert str(test_obj) == "Mountain<name='Breckenridge'>"

    lifts = test_obj.get_lift_status()
    expected_types = {
        '6-Chair': liftstatus.LiftType.CLF_2,
        'A-Chair': liftstatus.LiftType.CLF_3,
        'Admin Carpet 1': liftstatus.LiftType.SL,
        'Admin Carpet 2': liftstatus.LiftType.SL,
        'Beaver Run SuperChair': liftstatus.LiftType.CLD_4,
        'BR Adult Carpet': liftstatus.LiftType.SL,
        'BR Kids Carpet': liftstatus.LiftType.SL,
        'BreckConnect Gondola': liftstatus.LiftType.MGD,
        'Camelback Carpet': liftstatus.LiftType.SL,
        'Camelback Platter': liftstatus.LiftType.SL,
        'C-Chair': liftstatus.LiftType.CLF_2,
        'Colorado SuperChair': liftstatus.LiftType.CLD_6,
        'E-Chair': liftstatus.LiftType.CLF_2,
        'El Dorado Carpet': liftstatus.LiftType.SL,
        'El Dorado Platter': liftstatus.LiftType.SL,
        'Falcon SuperChair': liftstatus.LiftType.CLD_6,
        'Five SuperChair': liftstatus.LiftType.CLD_4,
        'Freedom SuperChair': liftstatus.LiftType.CLD_4,
        'Horseshoe Bowl T-Bar': liftstatus.LiftType.SL,
        'Imperial SuperChair': liftstatus.LiftType.CLD_4,
        'Independence SuperChair': liftstatus.LiftType.CLD_6,
        'Kensho SuperChair': liftstatus.LiftType.CLD_6,
        'Mercury SuperChair': liftstatus.LiftType.CLD_4,
        'Peak 8 Kids Carpet 1': liftstatus.LiftType.SL,
        'Peak 8 Kids Carpet 2': liftstatus.LiftType.SL,
        'Peak 8 SuperConnect': liftstatus.LiftType.CLD_4,
        'Quicksilver SuperChair': liftstatus.LiftType.CLD_6,
        'Rip\'s Ride': liftstatus.LiftType.CLD_4,
        'Rocky Mountain SuperChair': liftstatus.LiftType.CLD_4,
        'Snowflake': liftstatus.LiftType.CLF_2,
        'Trygve\'s Platter': liftstatus.LiftType.SL,
        'Tweener Carpet': liftstatus.LiftType.SL,
        'Village Carpet A': liftstatus.LiftType.SL,
        'Village Carpet B': liftstatus.LiftType.SL,
        'Zendo Chair': liftstatus.LiftType.CLF_4,
    }

    # _print_lifts(lifts)
    for lift in lifts:
        assert expected_types[lift.name] == lift.type

def test_crested_butte():
    test_obj = liftstatus.mountains.colorado.CrestedButte()
    assert str(test_obj) == "Mountain<name='Crested Butte'>"

    lifts = test_obj.get_lift_status()
    expected_types = {
        'Aspen Carpet': liftstatus.LiftType.SL,
        'East River Express': liftstatus.LiftType.CLD_4,
        'Gold Link Lift': liftstatus.LiftType.CLF_3,
        'High Lift T-Bar': liftstatus.LiftType.SL,
        'North Face Lift T-Bar': liftstatus.LiftType.SL,
        'Painter Boy Lift': liftstatus.LiftType.CLF_3,
        'Paradise Express': liftstatus.LiftType.CLD_4,
        'Peachtree Lift': liftstatus.LiftType.CLF_3,
        'Pine Carpet': liftstatus.LiftType.SL,
        'Prospect Lift': liftstatus.LiftType.CLF_4,
        'Red Lady Express': liftstatus.LiftType.CLD_4,
        'Silver Queen Express': liftstatus.LiftType.CLD_4,
        'Spruce Carpet': liftstatus.LiftType.SL,
        'Teocalli Lift': liftstatus.LiftType.CLF_4,
        'West Wall Lift': liftstatus.LiftType.CLF_4,
    }

    # _print_lifts(lifts)
    for lift in lifts:
        assert expected_types[lift.name] == lift.type

def test_keystone():
    test_obj = liftstatus.mountains.colorado.Keystone()
    assert str(test_obj) == "Mountain<name='Keystone'>"

    lifts = test_obj.get_lift_status()
    expected_types = {
        'A-51': liftstatus.LiftType.CLF_2,
        'Bergman Express': liftstatus.LiftType.CLD_6,
        'Cadillac': liftstatus.LiftType.SL,
        'Discovery': liftstatus.LiftType.CLF_2,
        'Double Barrel 1': liftstatus.LiftType.SL,
        'Double Barrel 2': liftstatus.LiftType.SL,
        'Kokomo': liftstatus.LiftType.SL,
        'Mid-Station Ski School': liftstatus.LiftType.SL,
        'Montezuma Express': liftstatus.LiftType.CLD_6,
        'Outback Express': liftstatus.LiftType.CLD_4,
        'Outpost Gondola': liftstatus.LiftType.MGD,
        'Peru Express': liftstatus.LiftType.CLD_6,
        'Ranger': liftstatus.LiftType.CLF_3,
        'River Run Gondola': liftstatus.LiftType.MGD,
        'Ruby Express': liftstatus.LiftType.CLD_6,
        'Santiago Express': liftstatus.LiftType.CLD_4,
        'Summit Express': liftstatus.LiftType.CLD_4,
        'Sun Kid': liftstatus.LiftType.SL,
        'Triangle': liftstatus.LiftType.SL,
        'Tubing Hill': liftstatus.LiftType.SL,
        'Wayback': liftstatus.LiftType.CLF_4,
    }

    # _print_lifts(lifts)
    for lift in lifts:
        assert expected_types[lift.name] == lift.type

def test_vail():
    test_obj = liftstatus.mountains.colorado.Vail()
    assert str(test_obj) == "Mountain<name='Vail'>"

    lifts = test_obj.get_lift_status()
    expected_types = {
        '#10 Highline Express': liftstatus.LiftType.CLD_4,
        '#11 Northwoods Express': liftstatus.LiftType.CLD_6,
        '#12 Gopher Hill': liftstatus.LiftType.CLF_3,
        '#14 Sourdough Express': liftstatus.LiftType.CLD_4,
        '#15 Little Eagle': liftstatus.LiftType.CLD_4,
        '#17 Sun Down Express': liftstatus.LiftType.CLD_4,
        '#18 Lightning Coyote': liftstatus.LiftType.SL,
        '#19 Eagle Bahn Gondola': liftstatus.LiftType.MGD,
        '#2 Avanti Express': liftstatus.LiftType.CLD_6,
        '#20 Cascade Village': liftstatus.LiftType.CLF_4,
        '#21 Orient Express': liftstatus.LiftType.CLD_4,
        '#22 Mongolia Platter': liftstatus.LiftType.SL,
        '#24 Wapiti Platter': liftstatus.LiftType.SL,
        '#25 Elvis Bahn': liftstatus.LiftType.SL,
        '#26 Pride Express': liftstatus.LiftType.CLD_4,
        '#27 Black Forest': liftstatus.LiftType.SL,
        '#29 Rip\'s Ride Carpet': liftstatus.LiftType.SL,
        '#3 Wildwood Express': liftstatus.LiftType.CLD_4,
        '#34 Lionshead Magic Carpet': liftstatus.LiftType.SL,
        '#35 Thunder Cat Carpet': liftstatus.LiftType.SL,
        '#36 Tea Cup Express': liftstatus.LiftType.CLD_4,
        '#37 Skyline Express': liftstatus.LiftType.CLD_4,
        '#38 Earl\'s Express': liftstatus.LiftType.CLD_4,
        '#39 Pete\'s Express': liftstatus.LiftType.CLD_4,
        '#4 Mountaintop Express': liftstatus.LiftType.CLD_6,
        '#5 High Noon Express': liftstatus.LiftType.CLD_4,
        '#6 Riva Bahn Express': liftstatus.LiftType.CLD_4,
        '#7 Game Creek Express': liftstatus.LiftType.CLD_6,
        '#8 Born Free Express': liftstatus.LiftType.CLD_4,
        '#9 Sun Up Express': liftstatus.LiftType.CLD_4,
        'Golden Peak T-Bar': liftstatus.LiftType.SL,
        'Gondola One': liftstatus.LiftType.MGD,
        'Patty Bahn': liftstatus.LiftType.SL,
    }

    # _print_lifts(lifts)
    for lift in lifts:
        assert expected_types[lift.name] == lift.type

def test_paoli_peaks():
    test_obj = liftstatus.mountains.indiana.PaoliPeaks()
    assert str(test_obj) == "Mountain<name='Paoli Peaks'>"

    lifts = test_obj.get_lift_status()
    expected_types = {
        '300\' Carpet': liftstatus.LiftType.SL,
        'Double': liftstatus.LiftType.CLF_2,
        'Triple': liftstatus.LiftType.CLF_3,
        'Quad': liftstatus.LiftType.CLF_4,
        'CTEC I': liftstatus.LiftType.CLF_3,
    }

    # _print_lifts(lifts)
    for lift in lifts:
        assert expected_types[lift.name] == lift.type

def test_mt_brighton():
    test_obj = liftstatus.mountains.michigan.MountBrighton()
    assert str(test_obj) == "Mountain<name='Mt. Brighton'>"

    lifts = test_obj.get_lift_status()
    expected_types = {
        'Carpet 10': liftstatus.LiftType.SL,
        'Carpet 7': liftstatus.LiftType.SL,
        'Chair 1': liftstatus.LiftType.CLF_3,
        'Chair 2': liftstatus.LiftType.CLF_3,
        'Chair 3': liftstatus.LiftType.CLF_4,
        'Chair 4': liftstatus.LiftType.CLF_4,
        'Chair 5': liftstatus.LiftType.CLF_3,
        'Rope Tow 8': liftstatus.LiftType.SL,
        'Rope Tow 9': liftstatus.LiftType.SL,
        'Rope Tow 12': liftstatus.LiftType.SL,
        'Rope Tow  11': liftstatus.LiftType.SL,
    }

    # _print_lifts(lifts)
    for lift in lifts:
        assert expected_types[lift.name] == lift.type

def test_afton_alps():
    test_obj = liftstatus.mountains.minnesota.AftonAlps()
    assert str(test_obj) == "Mountain<name='Afton Alps'>"

    lifts = test_obj.get_lift_status()
    expected_types = {
        'Chair 1': liftstatus.LiftType.CLF_2,
        'Chair 2': liftstatus.LiftType.CLF_4,
        'Chair 3': liftstatus.LiftType.CLF_3,
        'Chair 4': liftstatus.LiftType.CLF_2,
        'Chair 5': liftstatus.LiftType.CLF_2,
        'Chair 6': liftstatus.LiftType.CLF_2,
        'Chair 7': liftstatus.LiftType.CLF_2,
        'Chair 9': liftstatus.LiftType.CLF_2,
        'Chair 10': liftstatus.LiftType.CLF_2,
        'Chair 11': liftstatus.LiftType.CLF_2,
        'Chair 12': liftstatus.LiftType.CLF_2,
        'Chair 13': liftstatus.LiftType.CLF_3,
        'Chair 14': liftstatus.LiftType.CLF_2,
        'Chair 15': liftstatus.LiftType.CLF_2,
        'Chair 16': liftstatus.LiftType.CLF_2,
        'Chair 17': liftstatus.LiftType.CLF_2,
        'Chair 18': liftstatus.LiftType.CLF_2,
        'East Rope': liftstatus.LiftType.SL,
        'Magic Conveyor': liftstatus.LiftType.SL,
        'Meadows Conveyor': liftstatus.LiftType.SL,
        'Tubing Carpet': liftstatus.LiftType.SL,
        'West Rope': liftstatus.LiftType.SL,
    }

    # _print_lifts(lifts)
    for lift in lifts:
        assert expected_types[lift.name] == lift.type

def test_hidden_valley_mo():
    test_obj = liftstatus.mountains.missouri.HiddenValley()
    assert str(test_obj) == "Mountain<name='Hidden Valley'>"

    lifts = test_obj.get_lift_status()
    expected_types = {
        'Bunny Carpet': liftstatus.LiftType.SL,
        'East Mtn': liftstatus.LiftType.CLF_2,
        'Gateway': liftstatus.LiftType.CLF_3,
        'Lewis and Clark': liftstatus.LiftType.CLF_4,
        'Ozark': liftstatus.LiftType.CLF_3,
        'Rope Tow': liftstatus.LiftType.SL,
        'Ski Carpet': liftstatus.LiftType.SL,
        'Tubing East': liftstatus.LiftType.SL,
        'Tubing West': liftstatus.LiftType.SL,
        'West Mtn': liftstatus.LiftType.CLF_4,
    }

    # _print_lifts(lifts)
    for lift in lifts:
        assert expected_types[lift.name] == lift.type

def test_snow_creek():
    test_obj = liftstatus.mountains.missouri.SnowCreek()
    assert str(test_obj) == "Mountain<name='Snow Creek'>"

    lifts = test_obj.get_lift_status()
    expected_types = {
        'Easy Rider': liftstatus.LiftType.SL,
        'Jayhawk': liftstatus.LiftType.CLF_3,
        'Long Rider': liftstatus.LiftType.SL,
        'Show Me': liftstatus.LiftType.CLF_3,
        'Tiger': liftstatus.LiftType.CLF_2,
        'Twister (Tubing Lift)': liftstatus.LiftType.SL,
    }

    # _print_lifts(lifts)
    for lift in lifts:
        assert expected_types[lift.name] == lift.type

def test_attitash():
    test_obj = liftstatus.mountains.newhampshire.Attitash()
    assert str(test_obj) == "Mountain<name='Attitash'>"

    lifts = test_obj.get_lift_status()

    expected_types = {
        'Abenaki Quad': liftstatus.LiftType.CLF_4,
        'Flying Bear': liftstatus.LiftType.CLD_4,
        'Flying Yankee': liftstatus.LiftType.CLD_4,
        'Kachina': liftstatus.LiftType.CLF_3,
        'Learning Center': liftstatus.LiftType.CLF_3,
        'Progression Quad': liftstatus.LiftType.CLF_4,
        'Snowbelt': liftstatus.LiftType.SL,
        'The Mountaineer': liftstatus.LiftType.CLD_4,
    }

    # _print_lifts(lifts)
    for lift in lifts:
        assert expected_types[lift.name] == lift.type

def test_crotched():
    test_obj = liftstatus.mountains.newhampshire.CrotchedMountain()
    assert str(test_obj) == "Mountain<name='Crotched Mountain'>"

    lifts = test_obj.get_lift_status()

    expected_types = {
        'Lift Off': liftstatus.LiftType.SL,
        'Rocket': liftstatus.LiftType.CLD_4,
        'Rover': liftstatus.LiftType.CLF_3,
        'Valley': liftstatus.LiftType.CLF_4,
        'West Double': liftstatus.LiftType.CLF_2,
    }

    # _print_lifts(lifts)
    for lift in lifts:
        assert expected_types[lift.name] == lift.type

def test_mt_sunapee():
    test_obj = liftstatus.mountains.newhampshire.MountSunapee()
    assert str(test_obj) == "Mountain<name='Mount Sunapee'>"

    lifts = test_obj.get_lift_status()

    expected_types = {
        'Clipper Ship Quad': liftstatus.LiftType.CLF_4,
        'Flying Carpet': liftstatus.LiftType.SL,
        'Little Carpet': liftstatus.LiftType.SL,
        'Middle Carpet': liftstatus.LiftType.SL,
        'North Peak Triple': liftstatus.LiftType.CLF_3,
        'Piggyback': liftstatus.LiftType.SL,
        'Spruce Triple': liftstatus.LiftType.CLF_3,
        'Sunapee Express': liftstatus.LiftType.CLD_4,
        'Sunbowl Express': liftstatus.LiftType.CLD_4,
        'Small Carpet': liftstatus.LiftType.SL,
    }

    # _print_lifts(lifts)
    for lift in lifts:
        assert expected_types[lift.name] == lift.type
    
def test_wildcat():
    test_obj = liftstatus.mountains.newhampshire.Wildcat()
    assert str(test_obj) == "Mountain<name='Wildcat'>"

    lifts = test_obj.get_lift_status()

    expected_types = {
        'Bobcat': liftstatus.LiftType.CLF_3,
        'Snowbelt': liftstatus.LiftType.SL,
        'Snowcat': liftstatus.LiftType.CLF_3,
        'Tomcat': liftstatus.LiftType.CLF_3,
        'Wildcat Express': liftstatus.LiftType.CLD_4,
    }

    # _print_lifts(lifts)
    for lift in lifts:
        assert expected_types[lift.name] == lift.type

def test_hunter():
    test_obj = liftstatus.mountains.newyork.HunterMountain()
    assert str(test_obj) == "Mountain<name='Hunter Mountain'>"

    lifts = test_obj.get_lift_status()

    expected_types = {
        '20th Century (C Lift)': liftstatus.LiftType.CLF_4,
        'Broadway Express': liftstatus.LiftType.CLD_6,
        'Discovery Carpet': liftstatus.LiftType.SL,
        'F Lift': liftstatus.LiftType.CLF_3,
        'Frostland Carpet': liftstatus.LiftType.SL,
        'H Lift': liftstatus.LiftType.CLF_2,
        'Hunter East Carpet': liftstatus.LiftType.SL,
        'Kaatskill Flyer': liftstatus.LiftType.CLD_6,
        'Northern Express': liftstatus.LiftType.CLD_6,
        'Otis Quad': liftstatus.LiftType.CLF_4,
        'Tubing Carpet': liftstatus.LiftType.SL,
        'Zephyr Express': liftstatus.LiftType.CLD_4,
    }

    # _print_lifts(lifts)
    for lift in lifts:
        assert expected_types[lift.name] == lift.type

def test_alpine_valley():
    test_obj = liftstatus.mountains.ohio.AlpineValley()
    assert str(test_obj) == "Mountain<name='Alpine Valley'>"

    lifts = test_obj.get_lift_status()

    expected_types = {
        'Carpet Lift': liftstatus.LiftType.SL,
        'Handle Tow': liftstatus.LiftType.SL,
        'Snowbelt': liftstatus.LiftType.CLF_3,
        'Sycamore Lake': liftstatus.LiftType.CLF_3,
        'The Pine': liftstatus.LiftType.CLF_4,
    }

    # _print_lifts(lifts)
    for lift in lifts:
        assert expected_types[lift.name] == lift.type

def test_bmbw():
    test_obj = liftstatus.mountains.ohio.BostonMillsBrandywine()
    assert str(test_obj) == "Mountain<name='Boston Mills / Brandywine'>"

    lifts = test_obj.get_lift_status()

    expected_types = {
        'Buena Vista - Boston Mills': liftstatus.LiftType.CLF_4,
        'Carpet Lift': liftstatus.LiftType.SL,
        'Conveyour - Boston Mills': liftstatus.LiftType.SL,
        'Handle Tow': liftstatus.LiftType.SL,
        'Lift 1 - Boston Mills': liftstatus.LiftType.CLF_2,
        'Lift 1 - Brandywine': liftstatus.LiftType.CLF_4,
        'Lift 2 - Boston Mills': liftstatus.LiftType.CLF_3,
        'Lift 2 - Brandywine': liftstatus.LiftType.CLF_4,
        'Lift 3 - Boston Mills': liftstatus.LiftType.CLF_3,
        'Lift 4 - Boston Mills': liftstatus.LiftType.CLF_3,
        'Lift 4 - Brandywine': liftstatus.LiftType.CLF_3,
        'Lift 5 - Brandywine': liftstatus.LiftType.CLF_3,
        'Lift 6 - Boston Mills': liftstatus.LiftType.CLF_3,
        'Ram Quad - Brandywine': liftstatus.LiftType.CLF_4,
        'Tubing Carpet Lift - Conveyor Snow Tubing 1': liftstatus.LiftType.SL,
        'Tubing Carpet Lift - Conveyor Snow Tubing 2': liftstatus.LiftType.SL,
    }

    # _print_lifts(lifts)
    for lift in lifts:
        assert expected_types[lift.name] == lift.type

def test_mad_river():
    test_obj = liftstatus.mountains.ohio.MadRiver()
    assert str(test_obj) == "Mountain<name='Mad River'>"

    lifts = test_obj.get_lift_status()

    expected_types = {
        'Adventure Place Handle Tow': liftstatus.LiftType.SL,
        'Bubly Carpet 1': liftstatus.LiftType.SL,
        'Bubly Carpet 2': liftstatus.LiftType.SL,
        'Discovery Handle Tow': liftstatus.LiftType.SL,
        'Fanny Hill Handle Tow': liftstatus.LiftType.SL,
        'Flight Deck': liftstatus.LiftType.CLF_2,
        'Four Star Express': liftstatus.LiftType.CLF_4,
        'Momentum Triple': liftstatus.LiftType.CLF_3,
        'Skid Row Carpet': liftstatus.LiftType.SL,
        'Sugarbush': liftstatus.LiftType.CLF_2,
        'Sundowner Triple': liftstatus.LiftType.CLF_3,
    }

    # _print_lifts(lifts)
    for lift in lifts:
        assert expected_types[lift.name] == lift.type

def test_hidden_valley_pa():
    test_obj = liftstatus.mountains.pennsylvania.HiddenValley()
    assert str(test_obj) == "Mountain<name='Hidden Valley'>"

    lifts = test_obj.get_lift_status()

    expected_types = {
        'Avalanche': liftstatus.LiftType.CLF_4,
        'Blizzard': liftstatus.LiftType.CLF_4,
        'Bobcat Conveyor': liftstatus.LiftType.SL,
        'Crossover Handle Tow': liftstatus.LiftType.SL,
        'Jaguar Handle Tow': liftstatus.LiftType.SL,
        'Rippers Conveyor': liftstatus.LiftType.SL,
        'Sunrise': liftstatus.LiftType.CLF_3,
        'Sunset': liftstatus.LiftType.CLF_3,
    }

    # _print_lifts(lifts)
    for lift in lifts:
        assert expected_types[lift.name] == lift.type

def test_jfbb():
    test_obj = liftstatus.mountains.pennsylvania.JackFrostBigBoulder()
    assert str(test_obj) == "Mountain<name='Jack Frost / Big Boulder'>"

    lifts = test_obj.get_lift_status()

    expected_types = {
        'A Lift': liftstatus.LiftType.CLF_4,
        'Big Boulder': liftstatus.LiftType.CLF_3,
        'Big Boulder Beginner Carpet': liftstatus.LiftType.SL,
        'Blue Heron': liftstatus.LiftType.CLF_4,
        'D1 Lift': liftstatus.LiftType.CLF_2,
        'D2 Lift': liftstatus.LiftType.CLF_2,
        'Harmony': liftstatus.LiftType.CLF_4,
        'Paradise': liftstatus.LiftType.CLF_4,
        'Pocono': liftstatus.LiftType.CLF_4,
        'Ski School Carpet': liftstatus.LiftType.SL,
        'Surface': liftstatus.LiftType.SL,
        'Tannenbaum': liftstatus.LiftType.CLF_2,
        'Tobyhanna': liftstatus.LiftType.CLF_4,
    }

    # _print_lifts(lifts)
    for lift in lifts:
        assert expected_types[lift.name] == lift.type

def test_laurel():
    test_obj = liftstatus.mountains.pennsylvania.LaurelMountain()
    assert str(test_obj) == "Mountain<name='Laurel Mountain'>"

    lifts = test_obj.get_lift_status()

    expected_types = {
        'Laurel Lift': liftstatus.LiftType.CLF_4,
        'Laurel Tow': liftstatus.LiftType.SL,
    }

    # _print_lifts(lifts)
    for lift in lifts:
        assert expected_types[lift.name] == lift.type

def test_liberty():
    test_obj = liftstatus.mountains.pennsylvania.LibertyMountain()
    assert str(test_obj) == "Mountain<name='Liberty Mountain'>"

    lifts = test_obj.get_lift_status()

    expected_types = {
        'Alpine Quad': liftstatus.LiftType.CLF_4,
        'Dipsy Quad': liftstatus.LiftType.CLF_4,
        'Eastwind Quad': liftstatus.LiftType.CLF_4,
        'First Class Carpet': liftstatus.LiftType.SL,
        'First Class Quad': liftstatus.LiftType.CLF_4,
        'Snow Cat Alley': liftstatus.LiftType.SL,
        'Strata Quad': liftstatus.LiftType.CLF_4,
    }

    # _print_lifts(lifts)
    for lift in lifts:
        assert expected_types[lift.name] == lift.type

def test_roundtop():
    test_obj = liftstatus.mountains.pennsylvania.Roundtop()
    assert str(test_obj) == "Mountain<name='Roundtop'>"

    lifts = test_obj.get_lift_status()

    expected_types = {
        'Drummer Boy Quad': liftstatus.LiftType.CLF_4,
        'Exhibition Quad': liftstatus.LiftType.CLF_4,
        'Fife & Drum Triple': liftstatus.LiftType.CLF_3,
        'J-bar': liftstatus.LiftType.SL,
        'Magic Mountain Carpet': liftstatus.LiftType.SL,
        'Minuteman Quad': liftstatus.LiftType.CLF_4,
        'Ramrod Triple': liftstatus.LiftType.CLF_3,
        'Revere\'s Ride Carpet': liftstatus.LiftType.SL,
        'Tubing Carpet': liftstatus.LiftType.SL
    }

    # _print_lifts(lifts)
    for lift in lifts:
        assert expected_types[lift.name] == lift.type

def test_seven_springs():
    test_obj = liftstatus.mountains.pennsylvania.SevenSprings()
    assert str(test_obj) == "Mountain<name='Seven Springs'>"

    lifts = test_obj.get_lift_status()

    expected_types = {
        'Avalanche': liftstatus.LiftType.CLF_4,
        'Beginner Conveyor': liftstatus.LiftType.SL,
        'Blitzen': liftstatus.LiftType.CLF_3,
        'Cortina': liftstatus.LiftType.CLF_4,
        'Easy Rider Conveyor': liftstatus.LiftType.SL,
        'Giant Steps': liftstatus.LiftType.CLF_3,
        'Gunnar': liftstatus.LiftType.CLD_6,
        'North Face': liftstatus.LiftType.CLF_4,
        'North Pole': liftstatus.LiftType.CLF_4,
        'Polar Bear Express': liftstatus.LiftType.CLD_6,
        'Santa\'s Beard Rope Tow': liftstatus.LiftType.SL,
        'Southwind': liftstatus.LiftType.CLF_3,
        'Tyrol': liftstatus.LiftType.CLF_3,
        'Tyrol Conveyor': liftstatus.LiftType.SL,
    }

    # _print_lifts(lifts)
    for lift in lifts:
        assert expected_types[lift.name] == lift.type

def test_whitetail():
    test_obj = liftstatus.mountains.pennsylvania.Whitetail()
    assert str(test_obj) == "Mountain<name='Whitetail'>"

    lifts = test_obj.get_lift_status()

    expected_types = {
        'Expert\'s Choice Quad': liftstatus.LiftType.CLF_4,
        'EZ Rider Quad': liftstatus.LiftType.CLF_4,
        'First Class Magic Carpet': liftstatus.LiftType.SL,
        'Lift Off Quad': liftstatus.LiftType.CLF_4,
        'The Launching Pad': liftstatus.LiftType.SL,
        'U-Me Double': liftstatus.LiftType.CLF_2,
        'Whitetail Express Quad': liftstatus.LiftType.CLD_4,
    }

    # _print_lifts(lifts)
    for lift in lifts:
        assert expected_types[lift.name] == lift.type

def test_park_city():
    test_obj = liftstatus.mountains.utah.ParkCity()
    assert str(test_obj) == "Mountain<name='Park City'>"

    lifts = test_obj.get_lift_status()

    expected_types = {
        '3 Kings Lift': liftstatus.LiftType.CLF_3,
        '9990 Express': liftstatus.LiftType.CLD_4,
        'Bonanza Lift': liftstatus.LiftType.CLD_6,
        'Cabriolet': liftstatus.LiftType.CABRIO,
        'Crescent Lift': liftstatus.LiftType.CLD_4,
        'Day Break': liftstatus.LiftType.CLF_3,
        'Dreamcatcher': liftstatus.LiftType.CLF_4,
        'Dreamscape': liftstatus.LiftType.CLF_4,
        'Eagle Lift': liftstatus.LiftType.CLF_3,
        'Eaglet Lift': liftstatus.LiftType.CLF_3,
        'First Time Lift': liftstatus.LiftType.CLD_4,
        'Flat Iron': liftstatus.LiftType.CLF_2,
        'Frostwood Gondola': liftstatus.LiftType.MGD,
        'High Meadow': liftstatus.LiftType.CLD_4,
        'Iron Mtn. Express': liftstatus.LiftType.CLD_4,
        'Jupiter Lift': liftstatus.LiftType.CLF_2,
        'King Con Lift': liftstatus.LiftType.CLD_6,
        'McConkey\'s Lift': liftstatus.LiftType.CLD_6,
        'Mine Cart': liftstatus.LiftType.SL,
        'Motherlode Lift': liftstatus.LiftType.CLD_4,
        'Mule Train': liftstatus.LiftType.SL,
        'Orange Bubble Express': liftstatus.LiftType.CLD_4,
        'Over and Out': liftstatus.LiftType.CLF_4,
        'PayDay Lift': liftstatus.LiftType.CLD_6,
        'Peak 5': liftstatus.LiftType.CLF_4,
        'Pioneer Lift': liftstatus.LiftType.CLF_3,
        'Quicksilver Canyons Side': liftstatus.LiftType.MGD,
        'Quicksilver MV Side': liftstatus.LiftType.MGD,
        'Red Pine Gondola': liftstatus.LiftType.MGD,
        'Rip Cord': liftstatus.LiftType.SL,
        'Saddleback Express': liftstatus.LiftType.CLD_4,
        'Shortcut': liftstatus.LiftType.CLF_3,
        'Silver Lining': liftstatus.LiftType.SL,
        'Silver Star Lift': liftstatus.LiftType.CLF_3,
        'Silverlode Lift': liftstatus.LiftType.CLD_6,
        'Sun Peak Express': liftstatus.LiftType.CLD_4,
        'Sunrise Gondola': liftstatus.LiftType.MGD,
        'Super Condor Express': liftstatus.LiftType.CLD_4,
        'Sweet Pea': liftstatus.LiftType.SL,
        'Thaynes Lift': liftstatus.LiftType.CLF_2,
        'Timberline': liftstatus.LiftType.CLF_4,
        'Tombstone Express': liftstatus.LiftType.CLD_4,
        'Tommy Knocker': liftstatus.LiftType.SL,
        'Town Lift': liftstatus.LiftType.CLF_3,
    }

    # _print_lifts(lifts)
    for lift in lifts:
        assert expected_types[lift.name] == lift.type

def test_mount_snow():
    test_obj = liftstatus.mountains.vermont.MountSnow()
    assert str(test_obj) == "Mountain<name='Mount Snow'>"

    lifts = test_obj.get_lift_status()

    expected_types = {
        'Apollo': liftstatus.LiftType.SL,
        'Bear Trap': liftstatus.LiftType.CLF_2,
        'Bluebird Express': liftstatus.LiftType.CLD_6,
        'Canyon Express': liftstatus.LiftType.CLD_4,
        'Challenger': liftstatus.LiftType.CLF_3,
        'Covered Bridge': liftstatus.LiftType.SL,
        'Discovery Shuttle': liftstatus.LiftType.CLF_3,
        'Ego Alley': liftstatus.LiftType.CLF_3,
        'Gemini': liftstatus.LiftType.SL,
        'Grand Summit Express': liftstatus.LiftType.CLD_4,
        'Grommet': liftstatus.LiftType.SL,
        'Heavy Metal': liftstatus.LiftType.CLF_3,
        'Mercury': liftstatus.LiftType.SL,
        'Nitro Express': liftstatus.LiftType.CLD_4,
        'Outpost': liftstatus.LiftType.CLF_3,
        'Seasons': liftstatus.LiftType.CLF_2,
        'Sunbrook Express': liftstatus.LiftType.CLD_4,
        'Sundance Express': liftstatus.LiftType.CLD_6,
        'Voyager': liftstatus.LiftType.SL,
    }

    # _print_lifts(lifts)
    for lift in lifts:
        assert expected_types[lift.name] == lift.type

def test_okemo():
    test_obj = liftstatus.mountains.vermont.Okemo()
    assert str(test_obj) == "Mountain<name='Okemo'>"

    lifts = test_obj.get_lift_status()

    expected_types = {
        'Black Ridge Triple': liftstatus.LiftType.CLF_3,
        'Coleman Brook Express Quad': liftstatus.LiftType.CLD_4,
        'Evergreen Summit Express': liftstatus.LiftType.CLD_4,
        'F-10 Carpet': liftstatus.LiftType.SL,
        'Glades Peak Quad': liftstatus.LiftType.CLF_4,
        'Morning Star Triple': liftstatus.LiftType.CLF_3,
        'Orion\'s Belt Carpet': liftstatus.LiftType.SL,
        'Quantum Six': liftstatus.LiftType.CLD_6,
        'Sachem Quad': liftstatus.LiftType.CLF_4,
        'Ski and Ride School Carpet': liftstatus.LiftType.SL,
        'Skywalker Carpet': liftstatus.LiftType.SL,
        'Snowstar Carpet': liftstatus.LiftType.SL,
        'Solitude Express Quad': liftstatus.LiftType.CLD_4,
        'South Face Express Quad': liftstatus.LiftType.CLD_4,
        'South Ridge Quad A': liftstatus.LiftType.CLF_4,
        'South Ridge Quad B': liftstatus.LiftType.CLF_4,
        'Stargazer': liftstatus.LiftType.SL,
        'Starlight': liftstatus.LiftType.SL,
        'Sunburst Six': liftstatus.LiftType.CLD_6,
        'Sunshine Quad': liftstatus.LiftType.CLF_4,
        'The Pull': liftstatus.LiftType.SL,
    }

    # _print_lifts(lifts)
    for lift in lifts:
        assert expected_types[lift.name] == lift.type

def test_stowe():
    test_obj = liftstatus.mountains.vermont.Stowe()
    assert str(test_obj) == "Mountain<name='Stowe'>"

    lifts = test_obj.get_lift_status()

    expected_types = {
        'Adventure Carpet': liftstatus.LiftType.SL,
        'Adventure Triple': liftstatus.LiftType.CLF_3,
        'FourRunner Quad': liftstatus.LiftType.CLD_4,
        'Lookout Double': liftstatus.LiftType.CLF_2,
        'Mansfield Gondola': liftstatus.LiftType.MGD,
        'Meadows Carpet': liftstatus.LiftType.SL,
        'Meadows Quad': liftstatus.LiftType.CLF_4,
        'Over Easy Gondola': liftstatus.LiftType.MGD,
        'Sensation Quad': liftstatus.LiftType.CLD_4,
        'Sunny Spruce Quad': liftstatus.LiftType.CLD_4,
        'Sunrise Lift': liftstatus.LiftType.CLD_6,
        'Toll House Double': liftstatus.LiftType.CLF_2,
    }

    # _print_lifts(lifts)
    for lift in lifts:
        assert expected_types[lift.name] == lift.type

def test_stevens_pass():
    test_obj = liftstatus.mountains.washington.StevensPass()
    assert str(test_obj) == "Mountain<name='Stevens Pass'>"

    lifts = test_obj.get_lift_status()

    expected_types = {
        'Brooks Express': liftstatus.LiftType.CLD_4,
        'Daisy': liftstatus.LiftType.CLF_4,
        'Double Diamond': liftstatus.LiftType.CLF_3,
        'Hogsback Express': liftstatus.LiftType.CLD_4,
        'Jupiter Express': liftstatus.LiftType.CLD_4,
        'Kehr\'s': liftstatus.LiftType.CLF_4,
        'Marmot Carpet': liftstatus.LiftType.SL,
        'Pika Carpet': liftstatus.LiftType.SL,
        'Rope Tow 1': liftstatus.LiftType.SL,
        'Rope Tow 2': liftstatus.LiftType.SL,
        'Seventh Heaven': liftstatus.LiftType.CLF_2,
        'Skyline Express': liftstatus.LiftType.CLD_4,
        'Southern Cross': liftstatus.LiftType.CLF_3,
        'Tye Mill': liftstatus.LiftType.CLF_3,
    }

    # _print_lifts(lifts)
    for lift in lifts:
        assert expected_types[lift.name] == lift.type

def test_wilmot():
    test_obj = liftstatus.mountains.wisconsin.WilmotMountain()
    assert str(test_obj) == "Mountain<name='Wilmot Mountain'>"

    lifts = test_obj.get_lift_status()

    expected_types = {
        'Beginner Carpet North': liftstatus.LiftType.SL,
        'Beginner Carpet South': liftstatus.LiftType.SL,
        'Chair 1': liftstatus.LiftType.CLF_2,
        'Chair 10 (South Rope)': liftstatus.LiftType.SL,
        'Chair 11 (North Rope)': liftstatus.LiftType.SL,
        'Chair 12': liftstatus.LiftType.SL,
        'Chair 13': liftstatus.LiftType.SL,
        'Chair 2': liftstatus.LiftType.CLF_4,
        'Chair 3': liftstatus.LiftType.CLF_4,
        'Chair 4': liftstatus.LiftType.CLF_2,
        'Chair 5': liftstatus.LiftType.CLF_3,
        'Chair 6': liftstatus.LiftType.CLF_4,
    }

    # _print_lifts(lifts)
    for lift in lifts:
        assert expected_types[lift.name] == lift.type