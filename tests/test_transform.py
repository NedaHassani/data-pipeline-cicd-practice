from etl.transform import clean_record

def test_clean_record_strips_and_titles_name():
    raw = {"id": "7" , "name": "  anna MAYER  "}
    assert clean_record(raw) == {"id": 7 , "name": "Anna Mayer"}