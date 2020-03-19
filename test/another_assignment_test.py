#pytest style test

from lambdata.assignment import CustomFrame

def test_add_state_names():
    custom_df = CustomFrame({"abbrev": ["ca", "ct", "co", "tx", "dc"]})
 
    assert "name" not in list(custom_df.columns)

    custom_df.add_state_name()

    assert "name" in list(custom_df.columns)

    assert custom_df["abbrev"][0] == "ca"
    assert custom_df["name"][0] == "California"