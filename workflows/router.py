from . import home_office, self_employed

def route(question: str) -> str:
    q = question.lower()
    if "home office" in q:
        return home_office.run()
    elif "self-employed" in q or "self employed" in q:
        return self_employed.run()
    else:
        return "Sorry, I couldn't find a matching workflow yet."
