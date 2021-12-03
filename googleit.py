import webbrowser

def ggrks(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as e:
            query = 'https://www.google.com/search?q=python '
            query += str(e)
            webbrowser.open(query)
    return wrapper