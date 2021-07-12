def test_empty_object(worksheet):
    ws = worksheet
    sheet_items = ws.sheet_items
    assert sheet_items == []


def test_parse_xlsx_header(worksheet):
    ws = worksheet
    ws.xlsx_to_dict(path="tests/inventory.xlsx", select_sheet='SJ3')
    ws_header = ws.header
    assert ws_header == {
        "country": "Taiwan",
        "city": "Taipei",
        "area (km)": "271.8",
        None: "88",
        "rand_field": "ee",
    }
    assert None in ws_header


def test_parse_xlsx_all_items(worksheet):
    ws = worksheet
    ws_items = ws.xlsx_to_dict(path="tests/inventory.xlsx", select_sheet='SJ3')
    assert "Taipei" in str(ws_items)
    assert "Seoul" in str(ws_items)


def test_parse_xlsx_sheet_items(worksheet):
    ws = worksheet
    ws.xlsx_to_dict(path="tests/inventory.xlsx", select_sheet='SJ3')
    ws_items = ws.sheet_items
    assert "Taipei" in str(ws_items)
    assert "Bratislava" not in str(ws_items)
    assert "None:" in str(ws_items)
    assert None in ws_items[0]
    assert len(ws_items) > 1
    assert len(ws_items) == 6


def test_sanitize_sheet_items(worksheet):
    ws = worksheet
    ws.xlsx_to_dict(path="tests/inventory.xlsx", select_sheet='SJ3')
    ws_items = ws.sanitize_sheet_items
    assert "Taipei" in str(ws_items)
    assert "Bratislava" not in str(ws_items)
    assert "None:" not in str(ws_items)
    assert None not in ws_items[0]


from io import BytesIO

path = "tests/inventory.xlsx"
xlsx_file = open(path, "rb")
xlsx_file = BytesIO(xlsx_file.read())


def test_parse_xlsx_all_items_as_object(worksheet):
    ws = worksheet
    ws_items = ws.xlsx_to_dict(path=xlsx_file, select_sheet='SJ3')
    assert "Taipei" in str(ws_items)
    assert "Bratislava" not in str(ws_items)

def test_parse_xlsx_sheet_items_as_object(worksheet):
    ws = worksheet
    ws.xlsx_to_dict(path=xlsx_file, select_sheet='SJ3')
    ws_items = ws.sheet_items
    assert "Taipei" in str(ws_items)
    assert "Bratislava" not in str(ws_items)
    assert len(ws_items) > 1
    assert len(ws_items) == 6
