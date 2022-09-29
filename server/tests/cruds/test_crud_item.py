class TestCrudItem:
    def test_create(self):
        """
        依存がない項目のcreate test.
        初期状態: tableはclean.
        実行後: itemが作成されている.
        minimum検証方法:
        - crud.createのreturn is not None.
        - crud.read_one_by_values() is not None
        :return:
        """
        pass

    def test_read(self):
        """
        依存がない項目のread test.
        初期状態: tableはclean
        分岐:
        - item 0件. 空のリスト
        - item 2件. 2個のリストが入力したものと等しい.
        :return:
        """
        pass

    def test_read_one_by_id(self):
        """
        依存がない項目のread test.
        初期状態: tableはclean.
        分岐:
        - 存在しない
        - 存在する
        :return:
        """
        pass

    def test_read_one_by_value(self):
        """
        依存がない状態のread test.
        :return:
        初期状態: tableはclean.
        分岐:
        - 存在しない
        - 存在する
        """
        pass

    def test_update(self):
        """
        依存がない状態のupdate test.
        初期状態: tableはclean.
        - データが存在しない.
        - データが存在する.
        :return:
        """
        pass

    def test_delete(self):
        pass
