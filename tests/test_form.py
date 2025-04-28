def test_form_page(client):
    res = client.get("/form")
    # 正常にアクセスできているか
    assert res.status_code == 200