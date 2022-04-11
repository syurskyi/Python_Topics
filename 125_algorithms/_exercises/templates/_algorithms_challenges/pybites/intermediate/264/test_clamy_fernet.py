____ d__ _______ d__
____ r__ _______ c..
____ tempfile _______ NamedTemporaryFile

_______ p__

____ clamy_fernet _______ PBKDF2HMAC, ByteString, ClamyFernet, Fernet

KEYS (
    b"rvxePMSDUcZFowEaNxnFb8Pifn1KmhkF70Mz1ZQe2Bw=",
    b"2gODW4C4Lc7H9bjuuhPyn48HkVHriqa96P8lmstABo8=",
    b"mAbAfF5CW3EGlngOEEroDqtxlxVlJILzoUE4TJScMIw=",
)
MESSAGE "This is my secret message"
TMP_FILE NamedTemporaryFile(delete=F..)
FILE TMP_FILE.name


?p__.f..(scope="function")
___ rcf
    password b"#clamybite"
    key c..(KEYS)
    r.. ClamyFernet(password, key)


?p__.f..(scope="module")
___ cf
    r.. ClamyFernet(key=KEYS[0])


___ test_clamyfernet_no_args(rcf
    tmp_cf ClamyFernet()
    ... tmp_cf.key __ n.. N..
    ... tmp_cf.password __ b"pybites"


___ test_clamyfernet_random_key(rcf
    token rcf.encrypt("secret msg")
    ts rcf.clf.extract_timestamp(token)
    dt d__.fromtimestamp(ts)
    ... isi..(rcf, ClamyFernet)
    ... isi..(rcf.clf, Fernet)
    ... isi..(rcf.key, ByteString)
    ... isi..(rcf.kdf, PBKDF2HMAC)
    ... dt.year __ d__.n...year


___ test_clamyfernet(cf
    token cf.encrypt(MESSAGE)
    og_message cf.decrypt(token)
    ... l..(token) __ 120
    ... isi..(token, bytes)
    ... cf.key __ KEYS[0]
    ... og_message __ MESSAGE


___ test_clamyfernet_random(rcf
    token rcf.encrypt(MESSAGE)
    og_message rcf.decrypt(token)
    ... l..(token) __ 120
    ... isi..(token, bytes)
    ... rcf.key __ KEYS
    ... og_message __ MESSAGE