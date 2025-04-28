# トップページテスト
def test_index(client):
    # 実際のユーザーのアクセスを再現
    res = client.get("/")
    # 期待するレスポンスチェック
    assert res.status_code == 200