rule juancho_test
{
    strings:
        $a = "JUANCHO_TEST_MALWARE"

    condition:
       $a
}
