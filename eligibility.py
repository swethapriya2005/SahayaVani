def check_eligibility(profile):
    schemes = []

    if profile.get("occupation") == "farmer" and profile.get("income", 0) < 200000:
        schemes.append("YSR రైతు భరోసా")

    if profile.get("age", 0) >= 18:
        schemes.append("PM జనధన్ యోజన")

    return schemes
