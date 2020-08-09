from nose.tools ______ assert_equal


class TestRotation(object

    ___ test_rotation(self
        rotation = Rotation()
        assert_equal(rotation.is_rotation('o', 'oo'), False)
        assert_equal(rotation.is_rotation(None, 'foo'), False)
        assert_equal(rotation.is_rotation('', 'foo'), False)
        assert_equal(rotation.is_rotation('', ''), True)
        assert_equal(rotation.is_rotation('foobarbaz', 'barbazfoo'), True)
        print('Success: test_rotation')


___ main(
    test = TestRotation()
    test.test_rotation()


__ __name__ __ '__main__':
    main()