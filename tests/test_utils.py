from vulga_serializers.utils import get_versions, has_diff


def test_get_versions():
    token_entry = {
        "W0": {
            "text": "བསྟན་",
            "weight": 100,
            "is_top_weight": True
        },
        "W1": {
            "text": "བསྟན་",
            "weight": 100,
            "is_top_weight": False
        },
        "W2": {
            "text": "ཉིད་",
            "weight": 100,
            "is_top_weight": False
        },
        "W3": {
            "text": "ཉིད་",
            "weight": 100,
            "is_top_weight": False
        },
        "W4": {
            "text": "བསྟན་",
            "weight": 100,
            "is_top_weight": False
        }
    }

    expected_versions = {
        "W0": "བསྟན་",
        "W1": "བསྟན་",
        "W2": "ཉིད་",
        "W3": "ཉིད་",
        "W4": "བསྟན་",
    }

    expected_best_version = "བསྟན་"

    versions, best_version = get_versions(token_entry)

    assert versions == expected_versions
    assert best_version == expected_best_version

def test_has_diff():
    has_diff_versions = {
        "W0": "བསྟན་",
        "W1": "བསྟན་",
        "W2": "ཉིད་",
        "W3": "ཉིད་",
        "W4": "བསྟན་",
    }

    has_no_diff_versions = {
        "W0": "བསྟན་",
        "W1": "བསྟན་",
        "W2": "བསྟན་",
        "W3": "བསྟན་",
        "W4": "བསྟན་",
    }

    assert True == has_diff(has_diff_versions)
    assert False == has_diff(has_no_diff_versions)