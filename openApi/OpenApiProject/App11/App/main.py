from App1.services.ai_service import ask_ai


result = ask_ai(
  """
What is System prompt ?"""
)

print(result["content"])