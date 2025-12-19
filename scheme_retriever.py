SCHEMES = {
    "YSR రైతు భరోసా": {
        "benefit": "₹13,500 వార్షిక సహాయం",
        "documents": ["ఆధార్", "భూమి పత్రాలు"]
    },
    "PM జనధన్ యోజన": {
        "benefit": "జీరో బ్యాలెన్స్ బ్యాంక్ ఖాతా",
        "documents": ["ఆధార్"]
    }
}

def retrieve_scheme(schemes):
    if not schemes:
        return None
    return SCHEMES[schemes[0]]
