from pycrate_mobile.NAS import parse_NAS5G
from pycrate_core.elt import _with_json


def decode_nas_5f(nas_pdu):
    for pdu in nas_pdu:
        m, e = parse_NAS5G(pdu)
        assert( e == 0 )
        v = m.get_val()
        m.reautomate()
        assert( m.get_val() == v )
        m.set_val(v)
        assert( m.to_bytes() == pdu )
        #
        if _with_json:
            t = m.to_json()
            m.from_json(t)
            assert( m.get_val() == v )


def test_nas_5g(nas_5g_pdu, benchmark):
    benchmark(decode_nas_5f, nas_5g_pdu)
