def test_hostname_file(host):
    f = host.file("/etc/hostname")
    assert f.exists
    assert f.is_file
    assert f.mode == 0o644
    assert f.contains(host.check_output("hostname -s"))
