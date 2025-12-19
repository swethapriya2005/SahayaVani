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

while True:
    user_text = speech_to_text()
    print("USER:", user_text)

    # Simple Telugu info extraction
    if "వయసు" in user_text:
        memory.update("age", 45)

    if "ఆదాయం" in user_text:
        memory.update("income", 150000)

    if "రైతు" in user_text:
        memory.update("occupation", "farmer")

    plan = planner.plan(memory.get_all())
    print("PLANNER:", plan)

    if plan["action"] == "ASK_INFO":
        speak("దయచేసి మీ వయసు, ఆదాయం, వృత్తి చెప్పండి")
        continue

    result = executor.execute(memory.get_all())
    status = evaluator.evaluate(result)

    if status == "SUCCESS":
        speak("మీకు పథకం అర్హత ఉంది")
        speak(f"లాభం: {result['benefit']}")
        break
    else:
        speak("క్షమించండి, ప్రస్తుతం అర్హత లేదు")
        break
