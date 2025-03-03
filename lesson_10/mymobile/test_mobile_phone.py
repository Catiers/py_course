from mobile_phone_class import MobilePhone

def test_turn_on():
    phone1 = MobilePhone(375259003866)
    assert phone1.turn_on() == "Mobile phone 375259003866 is enabled."


def test_call_on():
    phone1 = MobilePhone(375259003866)
    phone1.Switch = True
    assert phone1.call(375223423623) == "Calling 375223423623."


def test_turn_off():
    phone1 = MobilePhone(375259003866)
    assert phone1.turn_off() == "Mobile phone 375259003866 is turned off."


def test_call_off():
    phone1 = MobilePhone(375259003866)
    assert phone1.call(375223423623) == "Mobile phone 375259003866 is turned off."
