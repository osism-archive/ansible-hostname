def test_hostname_file(host):
    f = host.file("/etc/hostname")
    assert f.exists
    assert f.is_file
