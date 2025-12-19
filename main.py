import re
from stt_telugu import speech_to_text
from tts_telugu import speak
from memory_store import MemoryStore
from planner import Planner
from executor import Executor
from evaluator import Evaluator

memory = MemoryStore()
planner = Planner()
executor = Executor()
evaluator = Evaluator()

speak("నమస్కారం! నేను ప్రభుత్వ పథక సహాయకుడిని.")

FIELD_ORDER = ["age", "income", "occupation", "gender"]

# 🔹 Extract numbers from text
def extract_number(text):
    numbers = re.findall(r'\d+', text)
    if numbers:
        return int(numbers[0])
    return None

# 🔹 Detect occupation from text
def detect_occupation(text):
    text = text.lower()
    if "రైతు" in text or "వ్యవసాయ" in text:
        return "farmer"
    elif "ఉద్యోగి" in text or "కర్మचारी" in text:
        return "employee"
    # Add more occupations as needed
    return None

# 🔹 Detect gender from text
def detect_gender(text):
    text = text.lower()
    if "స్త్రీ" in text or "మహిళ" in text:
        return "female"
    elif "పురుషుడు" in text or "మగ" in text:
        return "male"
    return None

while True:
    plan = planner.plan(memory.get_all())
    missing_fields = plan.get("fields", [])

    if missing_fields:
        current_field = missing_fields[0]

        # 🔹 Ask for the current missing field
        prompts = {
            "age": "దయచేసి మీ వయసు చెప్పండి.",
            "income": "దయచేసి మీ ఆదాయం చెప్పండి.",
            "occupation": "దయచేసి మీ వృత్తి చెప్పండి.",
            "gender": "దయచేసి మీ లింగం చెప్పండి."
        }
        speak(prompts[current_field])

        user_text = speech_to_text()
        if not user_text or user_text.strip() == "":
            speak("క్షమించండి, నేను వినలేకపోయాను. దయచేసి మళ్లీ చెప్పండి.")
            continue

        print("USER:", user_text)

        # 🔹 Process the input naturally
        if current_field == "age":
            age = extract_number(user_text)
            if age:
                status = memory.update("age", age)
            else:
                speak("క్షమించండి, దయచేసి వయసును సంఖ్యలలో చెప్పండి.")
                continue

        elif current_field == "income":
            income = extract_number(user_text)
            if income:
                # Convert to actual amount if user said "1 లక్ష" etc.
                if "లక్ష" in user_text:
                    income *= 100000
                status = memory.update("income", income)
            else:
                speak("క్షమించండి, దయచేసి ఆదాయాన్ని సంఖ్యలలో చెప్పండి.")
                continue

        elif current_field == "occupation":
            occupation = detect_occupation(user_text)
            if occupation:
                status = memory.update("occupation", occupation)
            else:
                speak("క్షమించండి, నేను గుర్తించలేకపోయాను. దయచేసి మీ వృత్తి చెప్పండి.")
                continue

        elif current_field == "gender":
            gender = detect_gender(user_text)
            if gender:
                status = memory.update("gender", gender)
            else:
                speak("దయచేసి సరైన లింగం చెప్పండి.")
                continue

        # 🔹 Handle contradiction
        if status == "CONTRADICTION":
            speak(f"మీ {current_field} సమాచారం భిన్నంగా ఉంది. దయచేసి స్పష్టంగా చెప్పండి.")
            continue

        continue  # Loop again to check next missing field

    # 🔹 All info collected → execute and evaluate
    result = executor.execute(memory.get_all())
    status = evaluator.evaluate(result)

    print("🧠 MEMORY:", memory.get_all())
    print("🧠 EXECUTOR RESULT:", result)
    print("🧠 EVALUATOR STATUS:", status)

    if status == "SUCCESS":
        speak("మీకు ప్రభుత్వ పథకం అర్హత ఉంది.")
        speak(f"లాభం: {result['benefit']}")
        speak("అవసరమైన పత్రాలు:")
        for doc in result["documents"]:
            speak(doc)
        break
    else:
        speak("క్షమించండి. మీరు ప్రస్తుతం ఏ పథకానికి అర్హులు కావు.")
        break
