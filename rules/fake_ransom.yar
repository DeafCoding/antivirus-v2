rule Fake_Ransomware
{
    strings:
        $a = "YOUR_FILES_ARE_ENCRYPTED"

    condition:
       $a
}
