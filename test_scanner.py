from scanner import load_rules, scan_file, hash_file, load_hashes



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

def test_hash_only_file_is_known_malware():
    bad_hashes = load_hashes("hashes/bad_hashes.txt")
    assert hash_file("samples/hash_only.txt") in bad_hashes


def test_clean_file_is_not_known_malware():
    bad_hashes = load_hashes("hashes/bad_hashes.txt")
    assert hash_file("samples/clean.txt") not in bad_hashes