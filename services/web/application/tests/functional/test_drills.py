import json

from application.api.drills.models import Drill


def test_add_drill(test_app, test_database):
    client = test_app.test_client()
    resp = client.post(
        "/drills",
        data=json.dumps({"part_number": "201TESTDRILL"}),
        content_type="application/json",
    )
    data = json.loads(resp.data.decode())
    assert resp.status_code == 201
    assert "201TESTDRILL was added successfully!" in data["message"]


def test_add_drill_invalid_json(test_app, test_database):
    client = test_app.test_client()
    resp = client.post("/drills", data=json.dumps({}), content_type="application/json",)

    data = json.loads(resp.data.decode())

    assert resp.status_code == 400
    assert "Input payload validation failed" in data["message"]


def test_add_drill_invalid_json_keys(test_app, test_database):
    client = test_app.test_client()
    resp = client.post(
        "/drills",
        data=json.dumps({"part_num": "201TESTDRILL"}),
        content_type="application/json",
    )
    data = json.loads(resp.data.decode())
    assert resp.status_code == 400
    assert "Input payload validation failed" in data["message"]


def test_add_drill_duplicate_part_number(test_app, test_database):

    client = test_app.test_client()
    client.post(
        "/drills",
        data=json.dumps({"part_number": "201TESTDRILL"}),
        content_type="application/json",
    )

    resp = client.post(
        "/drills",
        data=json.dumps({"part_number": "201TESTDRILL"}),
        content_type="application/json",
    )

    data = json.loads(resp.data.decode())
    assert resp.status_code == 400
    assert "Sorry. That part number already exists." in data["message"]


def test_single_drill(test_app, test_database, add_drill):
    drill = add_drill("201TESTDRILL")

    client = test_app.test_client()
    resp = client.get(f"/drills/{drill.id}")
    data = json.loads(resp.data.decode())

    assert resp.status_code == 200
    assert "201TESTDRILL" in data["part_number"]


def test_single_drill_incorrect_id(test_app, test_database):
    client = test_app.test_client()
    resp = client.get("drills/999")
    data = json.loads(resp.data.decode())
    assert resp.status_code == 404
    assert "Drill 999 not found" in data["message"]


def test_all_drills(test_app, test_database, add_drill):
    test_database.session.query(Drill).delete()
    add_drill("201TESTDRILL")
    add_drill("202TESTDRILL")
    client = test_app.test_client()
    resp = client.get("/drills")
    data = json.loads(resp.data.decode())
    assert resp.status_code == 200
    assert len(data) == 2
    assert "201TESTDRILL" in data[0]["part_number"]
    assert "202TESTDRILL" in data[1]["part_number"]
