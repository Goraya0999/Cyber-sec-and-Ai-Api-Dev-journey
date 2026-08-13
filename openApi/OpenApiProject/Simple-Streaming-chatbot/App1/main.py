from App1.clients.openrouter_client import OpenRouterError
from App1.services.ai_service import ask_ai_stream


def main() -> None:
    print("Ask your Python/security tutor anything (Ctrl+C to quit)\n")

    while True:
        try:
            question = input("You: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nBye!")
            break

        if not question:
            continue

        print("AI: ", end="", flush=True)
        try:
            for chunk in ask_ai_stream(question):
                print(chunk, end="", flush=True)
            print("\n")
        except ValueError as e:
            # Bad input (empty / too long) — don't crash, just tell the user
            print(f"\n[Input error: {e}]\n")
        except OpenRouterError as e:
            # Network/API failure — don't leak internals, log would go here
            print(f"\n[Something went wrong talking to the model: {e}]\n")


if __name__ == "__main__":
    main()
