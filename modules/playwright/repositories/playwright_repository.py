from db.execute import execute_query

def get_enterprises():
    result = execute_query("SELECT * FROM empresa")
    if result:
        print(result)
    return result

