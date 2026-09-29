<<<<<<< HEAD
from scripts.claim_ownerless import claim_json_entries
=======
from scripts.claim_ownerless import claim_json_entries, owner_arg
>>>>>>> e3035826bce87dca91a6036e133f0f892ef50bdc


def test_claim_json_entries_skips_invalid_rows():
    rows = [
        {"id": "a"},
        "bad-row",
        None,
        {"id": "b", "owner": "already"},
    ]

    assert claim_json_entries(rows, "admin") == 1
    assert rows == [
        {"id": "a", "owner": "admin"},
        "bad-row",
        None,
        {"id": "b", "owner": "already"},
    ]
<<<<<<< HEAD
=======


def test_owner_arg_rejects_blank_owner():
    assert owner_arg(["claim_ownerless.py"]) is None
    assert owner_arg(["claim_ownerless.py", "   "]) is None
    assert owner_arg(["claim_ownerless.py", " admin "]) == "admin"
>>>>>>> e3035826bce87dca91a6036e133f0f892ef50bdc
