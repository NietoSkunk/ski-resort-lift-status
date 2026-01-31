import pytest
import liftstatus

def _print_lifts(lifts):
    for lift in lifts:
        print(f"        '{lift.name.replace('\'', '\\\'')}': liftstatus.LiftType.{lift.type.name},")

def test_winter_park():
    test_obj = liftstatus.mountains.colorado.WinterPark()
    assert str(test_obj) == "Mountain<name='Winter Park'>"

    lifts = test_obj.get_lift_status()

    expected_types = {
        'Arrow': liftstatus.LiftType.CLF_3,
        'Cabriolet': liftstatus.LiftType.CABRIO,
        'Comet': liftstatus.LiftType.SL,
        'Discovery': liftstatus.LiftType.CLF_2,
        'Endeavour': liftstatus.LiftType.CLF_3,
        'Explorer Express': liftstatus.LiftType.CLD_4,
        'Gemini Express': liftstatus.LiftType.CLD_4,
        'Gondola': liftstatus.LiftType.MGD,
        'Hi-Lonesome Express': liftstatus.LiftType.CLD_4,
        'Looking Glass': liftstatus.LiftType.CLF_2,
        'Meteor': liftstatus.LiftType.SL,
        'Olympia Express': liftstatus.LiftType.CLD_4,
        'Prospector Express': liftstatus.LiftType.CLD_4,
        'Spirit': liftstatus.LiftType.SL,
        'Challenger': liftstatus.LiftType.CLF_2,
        'Galloping Goose': liftstatus.LiftType.CLF_2,
        'Iron Horse': liftstatus.LiftType.CLF_2,
        'Lariat': liftstatus.LiftType.SL,
        'Pony Express': liftstatus.LiftType.CLF_2,
        'Sunnyside Express': liftstatus.LiftType.CLD_6,
        'Super Gauge Express': liftstatus.LiftType.CLD_6,
        'Wild Spur Express': liftstatus.LiftType.CLD_6,
        'Wild Spur Express Mid-Way Station': liftstatus.LiftType.CLD_6,
        'Panoramic Express': liftstatus.LiftType.CLD_6,
        'Eagle Wind': liftstatus.LiftType.CLF_3,
        'Cirque Sled': liftstatus.LiftType.SL,
    }

    # _print_lifts(lifts)
    for lift in lifts:
        assert expected_types[lift.name] == lift.type
    
def test_steamboat():
    test_obj = liftstatus.mountains.colorado.Steamboat()
    assert str(test_obj) == "Mountain<name='Steamboat'>"

    lifts = test_obj.get_lift_status()

    expected_types = {
        'Steamboat Gondola': liftstatus.LiftType.MGD,
        'Wild Blue Gondola Lower': liftstatus.LiftType.MGD,
        'Wild Blue Gondola Upper': liftstatus.LiftType.MGD,
        'Bar-UE': liftstatus.LiftType.CLF_2,
        'Bashor': liftstatus.LiftType.CLF_2,
        'Burgess Creek': liftstatus.LiftType.CLF_3,
        'Christie Peak Express': liftstatus.LiftType.CLD_6,
        'Elkhead Express': liftstatus.LiftType.CLD_4,
        'Four Points': liftstatus.LiftType.CLF_3,
        'Greenhorn Ranch Express': liftstatus.LiftType.CLD_4,
        'Mahogany Ridge Express': liftstatus.LiftType.CLD_4,
        'Morningside': liftstatus.LiftType.CLF_3,
        'Pony Express': liftstatus.LiftType.CLD_4,
        'South Peak': liftstatus.LiftType.CLF_3,
        'Storm Peak Express': liftstatus.LiftType.CLD_4,
        'Sundown Express': liftstatus.LiftType.CLD_4,
        'Sunshine Express': liftstatus.LiftType.CLD_4,
        'Thunderhead Express': liftstatus.LiftType.CLD_4,
        'Wrangler Carpet': liftstatus.LiftType.SL,
        'Bonanza': liftstatus.LiftType.SL,
        'Buckaroo Carpet': liftstatus.LiftType.SL,
        'Easy Rider': liftstatus.LiftType.SL,
        'Two Whoops 1': liftstatus.LiftType.SL,
        'Two Whoops 2': liftstatus.LiftType.SL,
    }

    # _print_lifts(lifts)
    for lift in lifts:
        assert expected_types[lift.name] == lift.type
    
def test_bear_mountain():
    test_obj = liftstatus.mountains.california.BearMountain()
    assert str(test_obj) == "Mountain<name='Bear Mountain'>"

    lifts = test_obj.get_lift_status()

    expected_types = {
        'Chair 3': liftstatus.LiftType.CLF_2,
        'Chair 4': liftstatus.LiftType.CLF_2,
        'Chair 5': liftstatus.LiftType.CLD_6,
        'Chair 6': liftstatus.LiftType.CLD_4,
        'Chair 7': liftstatus.LiftType.CLF_3,
        'Chair 8': liftstatus.LiftType.CLF_3,
        'Chair 9': liftstatus.LiftType.CLD_4,
    }

    # _print_lifts(lifts)
    for lift in lifts:
        assert expected_types[lift.name] == lift.type
  
def test_snow_summit():
    test_obj = liftstatus.mountains.california.SnowSummit()
    assert str(test_obj) == "Mountain<name='Snow Summit'>"

    lifts = test_obj.get_lift_status()

    expected_types = {
        'Chair 1': liftstatus.LiftType.CLD_4,
        'MC 1': liftstatus.LiftType.SL,
        'Chair 2': liftstatus.LiftType.CLD_4,
        'Chair 3': liftstatus.LiftType.CLF_2,
        'Chair 4': liftstatus.LiftType.CLF_3,
        'Chair 5': liftstatus.LiftType.CLF_2,
        'Chair 6': liftstatus.LiftType.CLF_2,
        'Chair 7': liftstatus.LiftType.CLF_2,
        'Chair 8': liftstatus.LiftType.CLF_3,
        'Chair 9': liftstatus.LiftType.CLF_3,
        'Chair 10': liftstatus.LiftType.CLF_3,
    }

    # _print_lifts(lifts)
    for lift in lifts:
        assert expected_types[lift.name] == lift.type
  
def test_snow_valley():
    test_obj = liftstatus.mountains.california.SnowValley()
    assert str(test_obj) == "Mountain<name='Snow Valley'>"

    lifts = test_obj.get_lift_status()

    expected_types = {
        'Chair 1': liftstatus.LiftType.CLD_6,
        'MC 16': liftstatus.LiftType.SL,
        'Chair 2': liftstatus.LiftType.CLF_3,
        'Chair 3': liftstatus.LiftType.CLF_3,
        'Chair 6': liftstatus.LiftType.CLF_2,
        'Chair 8': liftstatus.LiftType.CLF_2,
        'Chair 9': liftstatus.LiftType.CLF_2,
        'Chair 11': liftstatus.LiftType.CLF_3,
        'Coyote Creek Chair': liftstatus.LiftType.CLF_2,
        'Chair 13': liftstatus.LiftType.CLF_3,
    }

    # _print_lifts(lifts)
    for lift in lifts:
        assert expected_types[lift.name] == lift.type
  
def test_blue_mountain():
    test_obj = liftstatus.mountains.ontario.BlueMountain()
    assert str(test_obj) == "Mountain<name='Blue Mountain'>"

    lifts = test_obj.get_lift_status()

    expected_types = {
        'Easy Rider': liftstatus.LiftType.SL,
        'Explorer': liftstatus.LiftType.SL,
        'Graduate': liftstatus.LiftType.CLF_3,
        'Little Ripper': liftstatus.LiftType.SL,
        'Orchard Express': liftstatus.LiftType.CLD_6,
        'Silver Bullet': liftstatus.LiftType.CLD_6,
        'Southern Comfort': liftstatus.LiftType.CLD_6,
        'Undergrad': liftstatus.LiftType.SL,
        'Valley Express': liftstatus.LiftType.CLD_6,
        'Voyageur': liftstatus.LiftType.CLF_4,
        'Weider Express': liftstatus.LiftType.CLD_6,
    }

    # _print_lifts(lifts)
    for lift in lifts:
        assert expected_types[lift.name] == lift.type
 
def test_crystal_mountain():
    test_obj = liftstatus.mountains.washington.CrystalMountain()
    assert str(test_obj) == "Mountain<name='Crystal Mountain'>"

    lifts = test_obj.get_lift_status()

    expected_types = {
        'Chair 6': liftstatus.LiftType.CLF_2,
        'Chinook Express': liftstatus.LiftType.CLD_6,
        'Discovery Conveyor': liftstatus.LiftType.SL,
        'Discovery': liftstatus.LiftType.CLF_3,
        'Forest Queen Express': liftstatus.LiftType.CLD_6,
        'Gold Hills': liftstatus.LiftType.CLF_3,
        'Green Valley': liftstatus.LiftType.CLD_4,
        'Mt. Rainier Gondola': liftstatus.LiftType.MGD,
        'Northway': liftstatus.LiftType.CLF_2,
        'Quicksilver': liftstatus.LiftType.CLF_4,
        'Rainier Express': liftstatus.LiftType.CLD_4,
    }

    # _print_lifts(lifts)
    for lift in lifts:
        assert expected_types[lift.name] == lift.type

def test_deer_valley():
    test_obj = liftstatus.mountains.utah.DeerValley()
    assert str(test_obj) == "Mountain<name='Deer Valley'>"

    lifts = test_obj.get_lift_status()

    expected_types = {
        'Aurora': liftstatus.LiftType.CLF_4,
        'Burns Express': liftstatus.LiftType.CLD_4,
        'Carpenter Express': liftstatus.LiftType.CLD_4,
        'Crown Point': liftstatus.LiftType.CLF_3,
        'East Village Gondola Mid Station': liftstatus.LiftType.MGD,
        'East Village Gondola': liftstatus.LiftType.MGD,
        'Empire Express': liftstatus.LiftType.CLD_4,
        'Galena Express': liftstatus.LiftType.CLD_4,
        'Homestake Express': liftstatus.LiftType.CLD_4,
        'Hoodoo Express': liftstatus.LiftType.CLD_4,
        'Jordanelle Express Gondola': liftstatus.LiftType.MGD,
        'Judge': liftstatus.LiftType.CLF_3,
        'Keetley Express': liftstatus.LiftType.CLD_6,
        'Lady Morgan Express': liftstatus.LiftType.CLD_4,
        'Mayflower': liftstatus.LiftType.CLF_3,
        'Mountaineer Express': liftstatus.LiftType.CLD_4,
        'Neptune Express': liftstatus.LiftType.CLD_4,
        'Northside Express': liftstatus.LiftType.CLD_4,
        'Pinyon Express': liftstatus.LiftType.CLD_6,
        'Pioche Express': liftstatus.LiftType.CLD_4,
        'Quincy Express': liftstatus.LiftType.CLD_4,
        'Red Cloud': liftstatus.LiftType.CLF_3,
        'Revelator Express': liftstatus.LiftType.CLD_4,
        'Ruby Express': liftstatus.LiftType.CLD_4,
        'Silver Lake Express': liftstatus.LiftType.CLD_4,
        'Silver Strike Express': liftstatus.LiftType.CLD_4,
        'Snowflake': liftstatus.LiftType.CLF_2,
        'Sterling Express': liftstatus.LiftType.CLD_4,
        'Sultan Express': liftstatus.LiftType.CLD_4,
        'Viking': liftstatus.LiftType.CLF_3,
        'Vulcan Express': liftstatus.LiftType.CLD_4,
        'Wasatch Express': liftstatus.LiftType.CLD_4,
    }

    # _print_lifts(lifts)
    for lift in lifts:
        assert expected_types[lift.name] == lift.type

def test_june_mountain():
    test_obj = liftstatus.mountains.california.JuneMountain()
    assert str(test_obj) == "Mountain<name='June Mountain'>"

    lifts = test_obj.get_lift_status()

    expected_types = {
        'J1': liftstatus.LiftType.CLF_2,
        'J2': liftstatus.LiftType.CLF_2,
        'J3': liftstatus.LiftType.CLF_2,
        'J4': liftstatus.LiftType.CLF_2,
        'J6': liftstatus.LiftType.CLD_4,
        'J7': liftstatus.LiftType.CLD_4,
        'Public Carpet': liftstatus.LiftType.SL,
    }

    # _print_lifts(lifts)
    for lift in lifts:
        assert expected_types[lift.name] == lift.type

def test_mammoth():
    test_obj = liftstatus.mountains.california.MammothMountain()
    assert str(test_obj) == "Mountain<name='Mammoth Mountain'>"

    lifts = test_obj.get_lift_status()

    expected_types = {
        'Broadway Express 1': liftstatus.LiftType.CLD_6,
        'Canyon Express 16': liftstatus.LiftType.CLD_6,
        'Chair 12': liftstatus.LiftType.CLF_2,
        'Chair 13': liftstatus.LiftType.CLF_2,
        'Chair 14': liftstatus.LiftType.CLF_2,
        'Chair 20': liftstatus.LiftType.CLF_3,
        'Chair 21': liftstatus.LiftType.CLF_3,
        'Chair 22': liftstatus.LiftType.CLF_3,
        'Chair 23': liftstatus.LiftType.CLF_3,
        'Chair 25': liftstatus.LiftType.CLF_4,
        'Chair 7': liftstatus.LiftType.CLF_3,
        'Chair 8': liftstatus.LiftType.CLF_3,
        'Cloud Nine Express 9': liftstatus.LiftType.CLD_6,
        'Discovery Express 11': liftstatus.LiftType.CLD_4,
        'Eagle Express 15': liftstatus.LiftType.CLD_6,
        'Face Lift Express 3': liftstatus.LiftType.CLD_4,
        'Gold Rush Express 10': liftstatus.LiftType.CLD_4,
        'High 5 Express': liftstatus.LiftType.CLD_4,
        'Panorama Lower': liftstatus.LiftType.MGD,
        'Panorama Upper': liftstatus.LiftType.MGD,
        'Roller Coaster Express 4': liftstatus.LiftType.CLD_4,
        'Schoolyard Express 17': liftstatus.LiftType.CLD_4,
        'Stump Alley Express 2': liftstatus.LiftType.CLD_4,
        'Unbound Express 6': liftstatus.LiftType.CLD_4,
        'Village Gondola': liftstatus.LiftType.MGD,
    }

    # _print_lifts(lifts)
    for lift in lifts:
        assert expected_types[lift.name] == lift.type

def test_snowshoe():
    test_obj = liftstatus.mountains.westvirginia.Snowshoe()
    assert str(test_obj) == "Mountain<name='Snowshoe'>"

    lifts = test_obj.get_lift_status()

    expected_types = {
        'Ballhooter': liftstatus.LiftType.CLD_4,
        'Cascade': liftstatus.LiftType.CLF_3,
        'Cubb Run': liftstatus.LiftType.CLF_4,
        'Flying Eagle': liftstatus.LiftType.CLF_4,
        'Grabhammer': liftstatus.LiftType.CLF_3,
        'Magic Carpet': liftstatus.LiftType.SL,
        'Mountaineer Rope Tow': liftstatus.LiftType.SL,
        'Mountaineer': liftstatus.LiftType.CLF_3,
        'Powder Monkey': liftstatus.LiftType.CLF_4,
        'Powderidge': liftstatus.LiftType.CLF_3,
        'Skidder': liftstatus.LiftType.CLF_3,
        'Soaring Eagle Express': liftstatus.LiftType.CLD_4,
        'Western Express': liftstatus.LiftType.CLD_4,
        'Wonder Carpet': liftstatus.LiftType.SL,
    }

    # _print_lifts(lifts)
    for lift in lifts:
        assert expected_types[lift.name] == lift.type

def test_solitude():
    test_obj = liftstatus.mountains.utah.Solitude()
    assert str(test_obj) == "Mountain<name='Solitude'>"

    lifts = test_obj.get_lift_status()

    expected_types = {
        'Link': liftstatus.LiftType.CLF_2,
        'Moonbeam Express': liftstatus.LiftType.CLD_4,
        'Magic Carpet': liftstatus.LiftType.SL,
        'Eagle Express': liftstatus.LiftType.CLD_6,
        'Powderhorn II': liftstatus.LiftType.CLF_4,
        'Apex Express': liftstatus.LiftType.CLD_4,
        'Sunrise': liftstatus.LiftType.CLF_3,
        'Summit Express': liftstatus.LiftType.CLD_4,
        'Honeycomb Return': liftstatus.LiftType.CLF_4,
        'Soli Parks Tow': liftstatus.LiftType.SL
    }

    # _print_lifts(lifts)
    for lift in lifts:
        assert expected_types[lift.name] == lift.type

def test_palisades_tahoe():
    test_obj = liftstatus.mountains.california.PalisadesTahoe()
    assert str(test_obj) == "Mountain<name='Palisades Tahoe'>"

    lifts = test_obj.get_lift_status()

    expected_types = {
        'Aerial Tram': liftstatus.LiftType.ATW,
        'Ahsoka': liftstatus.LiftType.SL,
        'Alpine Bowl Chair': liftstatus.LiftType.CLF_2,
        'Bailey\'s Beach': liftstatus.LiftType.CLF_3,
        'Base to Base Gondola to Alpine': liftstatus.LiftType.MGD,
        'Base to Base Gondola to Palisades': liftstatus.LiftType.MGD,
        'Belmont': liftstatus.LiftType.CLF_2,
        'Big Blue Express': liftstatus.LiftType.CLD_6,
        'Big Carpet': liftstatus.LiftType.SL,
        'Broken Arrow': liftstatus.LiftType.CLF_2,
        'Emigrant': liftstatus.LiftType.CLF_3,
        'Exhibition': liftstatus.LiftType.CLF_4,
        'Far East Express': liftstatus.LiftType.CLD_6,
        'First Venture': liftstatus.LiftType.CLF_3,
        'Funitel': liftstatus.LiftType.FUN,
        'Gold Coast Express': liftstatus.LiftType.CLD_6,
        'Granite Chief': liftstatus.LiftType.CLF_3,
        'Headwall Express': liftstatus.LiftType.CLD_6,
        'High Camp Carpet': liftstatus.LiftType.SL,
        'Kangaroo': liftstatus.LiftType.CLF_2,
        'KT-22 Express': liftstatus.LiftType.CLD_4,
        'Lakeview': liftstatus.LiftType.CLF_3,
        'Meadow': liftstatus.LiftType.CLF_2,
        'Mountain Meadow': liftstatus.LiftType.CLF_3,
        'Olympic Lady': liftstatus.LiftType.CLF_2,
        'Red Dog': liftstatus.LiftType.CLD_6,
        'Resort Chair': liftstatus.LiftType.CLF_3,
        'Roundhouse': liftstatus.LiftType.CLD_4,
        'Scott': liftstatus.LiftType.CLF_3,
        'Sherwood Express': liftstatus.LiftType.CLD_4,
        'Shirley Lake Express': liftstatus.LiftType.CLD_6,
        'Siberia Express': liftstatus.LiftType.CLD_6,
        'Silverado': liftstatus.LiftType.CLF_3,
        'Solitude': liftstatus.LiftType.CLF_3,
        'Subway': liftstatus.LiftType.CLF_2,
        'Summit Express': liftstatus.LiftType.CLD_6,
        'Treeline Cirque': liftstatus.LiftType.CLD_4,
        'Wa She Shu': liftstatus.LiftType.CLD_4,
        'Yellow': liftstatus.LiftType.CLF_2,
    }

    # _print_lifts(lifts)
    for lift in lifts:
        assert expected_types[lift.name] == lift.type

def test_schweitzer():
    test_obj = liftstatus.mountains.idaho.Schweitzer()
    assert str(test_obj) == "Mountain<name='Schweitzer'>"

    lifts = test_obj.get_lift_status()

    expected_types = {
        'Basin Express': liftstatus.LiftType.CLD_4,
        'Cedar Park Express': liftstatus.LiftType.CLD_4,
        'Colburn Triple ': liftstatus.LiftType.CLF_3,
        'Creekside Express': liftstatus.LiftType.CLD_4,
        'Great Escape Quad': liftstatus.LiftType.CLD_4,
        'Idyle Our T-Bar': liftstatus.LiftType.SL,
        'Lakeview Triple': liftstatus.LiftType.CLF_3,
        'Musical Carpet': liftstatus.LiftType.SL,
        'Stella Express': liftstatus.LiftType.CLD_6,
        'Sunnyside Double': liftstatus.LiftType.CLF_2,
    }

    # _print_lifts(lifts)
    for lift in lifts:
        assert expected_types[lift.name] == lift.type

def test_stratton():
    test_obj = liftstatus.mountains.vermont.Stratton()
    assert str(test_obj) == "Mountain<name='Stratton'>"

    lifts = test_obj.get_lift_status()

    expected_types = {
        'American Express': liftstatus.LiftType.CLD_6,
        'Cub Carpet': liftstatus.LiftType.SL,
        'Gondola': liftstatus.LiftType.MGD,
        'Oso Carpet': liftstatus.LiftType.SL,
        'Shooting Star': liftstatus.LiftType.CLD_6,
        'Snow Bowl Express': liftstatus.LiftType.CLD_4,
        'Solstice': liftstatus.LiftType.CLF_4,
        'South American': liftstatus.LiftType.CLF_4,
        'Sunrise Express': liftstatus.LiftType.CLD_6,
        'Tamarack': liftstatus.LiftType.CLF_3,
        'Theodore Carpet': liftstatus.LiftType.SL,
        'Tyro Tube': liftstatus.LiftType.SL,
        'URSA Express': liftstatus.LiftType.CLD_6,
        'Villager': liftstatus.LiftType.CLF_2,
    }

    # _print_lifts(lifts)
    for lift in lifts:
        assert expected_types[lift.name] == lift.type

def test_sugarbush():
    test_obj = liftstatus.mountains.vermont.Sugarbush()
    assert str(test_obj) == "Mountain<name='Sugarbush'>"

    lifts = test_obj.get_lift_status()

    expected_types = {
        'Castlerock Double': liftstatus.LiftType.CLF_2,
        'Easy Up': liftstatus.LiftType.SL,
        'Gate House Express Quad': liftstatus.LiftType.CLD_4,
        'Green Mountain Express Quad': liftstatus.LiftType.CLD_4,
        'Heaven\'s Gate Quad': liftstatus.LiftType.CLF_4,
        'Inverness Quad': liftstatus.LiftType.CLF_4,
        'North Lynx Triple': liftstatus.LiftType.CLF_3,
        'North Ridge Express Quad': liftstatus.LiftType.CLD_4,
        'Schoolhouse Lift': liftstatus.LiftType.SL,
        'Slide Brook Express Quad': liftstatus.LiftType.CLD_4,
        'Summit Quad': liftstatus.LiftType.CLF_4,
        'Sunshine Quad': liftstatus.LiftType.CLF_4,
        'Super Bravo Express Quad': liftstatus.LiftType.CLD_4,
        'Valley House Quad': liftstatus.LiftType.CLF_4,
        'Village Quad': liftstatus.LiftType.CLF_4,
        'Welcome Mat': liftstatus.LiftType.SL,
    }

    # _print_lifts(lifts)
    for lift in lifts:
        assert expected_types[lift.name] == lift.type

def test_tremblant():
    test_obj = liftstatus.mountains.quebec.Tremblant()
    assert str(test_obj) == "Mountain<name='Mont Tremblant'>"

    lifts = test_obj.get_lift_status()

    expected_types = {
        'Cabriolet': liftstatus.LiftType.CABRIO,
        'Duncan Express': liftstatus.LiftType.CLD_4,
        'Edge': liftstatus.LiftType.CLF_4,
        'Expo Express': liftstatus.LiftType.CLD_4,
        'Flying Mile': liftstatus.LiftType.CLD_4,
        'Le Soleil': liftstatus.LiftType.CLD_4,
        'Lowell Thomas Express': liftstatus.LiftType.CLD_4,
        'Porte du Soleil': liftstatus.LiftType.CLF_3,
        'Tapis Magique Équilibre 1': liftstatus.LiftType.SL,
        'Tapis Magique Équilibre 2': liftstatus.LiftType.SL,
        'Tapis Magique Onésime': liftstatus.LiftType.SL,
        'Télécabine Casino Express': liftstatus.LiftType.MGD,
        'Télécabine Express': liftstatus.LiftType.MGD,
        'TGV': liftstatus.LiftType.CLD_4,
    }

    # _print_lifts(lifts)
    for lift in lifts:
        assert expected_types[lift.name] == lift.type
