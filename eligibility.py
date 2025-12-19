def check_eligibility(profile):
    schemes = []

    age = profile.get("age", 0)
    income = profile.get("income", 0)
    occupation = profile.get("occupation", "")
    gender = profile.get("gender", "")

    # 1️⃣ YSR రైతు భరోసా
    if occupation == "farmer" and income < 200000:
        schemes.append("YSR రైతు భరోసా")

    # 2️⃣ PM జనధన్ యోజన
    if age >= 18:
        schemes.append("PM జనధన్ యోజన")

    # 3️⃣ PM కిసాన్ సమ్మాన్ నిధి
    if occupation == "farmer" and income < 150000:
        schemes.append("PM కిసాన్ సమ్మాన్ నిధి")

    # 4️⃣ వృద్ధాప్య పెన్షన్
    if age >= 60 and income < 100000:
        schemes.append("వృద్ధాప్య పెన్షన్ పథకం")

    # 5️⃣ PM ఉజ్వల యోజన
    if gender == "female" and income < 200000:
        schemes.append("PM ఉజ్వల యోజన")

    # 6️⃣ ఆయుష్మాన్ భారత్
    if income < 250000:
        schemes.append("ఆయుష్మాన్ భారత్")

    return schemes
