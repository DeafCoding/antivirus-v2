from scanner import load_rules, scan_file

rules = load_rules("rules")


def test_clean_file_has_no_matches():
    matches = scan_file(rules, "samples/clean.txt")
    assert matches == []


def test_infected_file_matches_test_rule():
    matches = scan_file(rules, "samples/infected.txt")
    assert [m.rule for m in matches] == ["juancho_test"]


def test_ransom_file_matches_ransom_rule():
    matches = scan_file(rules, "samples/ransom.txt")
    assert [m.rule for m in matches] == ["Fake_Ransomware"]


def test_all_rule_files_are_loaded():
    matches = scan_file(rules, "samples/ransom.txt")
    assert len(matches) == 1
