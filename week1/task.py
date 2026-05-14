"""
RuleBot — A simple rule-based chatbot using if-else logic.
Run:  python task_!.py
"""

import random
from datetime import datetime
from typing import Callable, Optional


# ── Configuration ─────────────────────────────────────────────────────────────

class Config:
    """Chatbot configuration constants."""
    BOT_NAME = "RuleBot"
    SEPARATOR_WIDTH = 50
    ENCODING = "utf-8"
    MAX_INPUT_LENGTH = 500


# ── Rule definitions ──────────────────────────────────────────────────────────

class Rule:
    """Encapsulates a single conversation rule with pattern matching and responses."""
    
    def __init__(
        self,
        keywords: list[str],
        responses: Optional[list[str]] = None,
        dynamic: Optional[Callable[[], str]] = None,
        terminal: bool = False
    ):
        """
        Initialize a conversation rule.
        
        Args:
            keywords: Trigger words/phrases (matched via substring search)
            responses: List of possible replies (randomly chosen)
            dynamic: Optional callable that generates dynamic replies
            terminal: If True, ends the session after replying
        """
        self.keywords = keywords
        self.responses = responses or []
        self.dynamic = dynamic
        self.terminal = terminal
    
    def get_response(self) -> str:
        """Generate a response using dynamic function or random selection."""
        if self.dynamic:
            try:
                return self.dynamic()
            except Exception as e:
                return f"Error generating response: {e}"
        return random.choice(self.responses) if self.responses else ""
    
    def matches(self, user_input: str) -> bool:
        """Check if any keyword exists in the user input (case-insensitive)."""
        lower_input = user_input.lower()
        return any(keyword in lower_input for keyword in self.keywords)


RULES = [
    Rule(
        keywords=["hello", "hi", "hey", "howdy", "greetings", "sup", "hiya"],
        responses=[
            "Hello there! Great to meet you. Type 'help' to see what I can do.",
            "Hey! I'm RuleBot. How can I help you today?",
            "Hi! Nice to see you. Ask me something!",
        ]
    ),
    Rule(
        keywords=["help", "what can you do", "commands", "options"],
        responses=[
            (
                "I understand the following topics:\n"
                "  • Greetings   — hi, hello, hey\n"
                "  • Time/Date   — time, date, today\n"
                "  • Jokes       — joke, funny\n"
                "  • My name     — who are you, your name\n"
                "  • Mood check  — how are you\n"
                "  • Exit        — bye, quit, exit\n"
                "Just type naturally and I'll match keywords!"
            )
        ]
    ),
    Rule(
        keywords=["time", "date", "today", "clock", "now", "day"],
        dynamic=lambda: (
            f"Right now it's "
            f"{datetime.now().strftime('%I:%M %p')} on "
            f"{datetime.now().strftime('%A, %B %d %Y')}."
        )
    ),
    Rule(
        keywords=["joke", "funny", "laugh", "humor", "lol", "haha"],
        responses=[
            "Why do programmers prefer dark mode?\nBecause light attracts bugs! 🐛",
            "Why did the computer go to the doctor?\nIt had a virus!",
            "How many programmers does it take to change a light bulb?\nNone — that's a hardware problem.",
            "A SQL query walks into a bar and asks two tables:\n'Can I join you?'",
        ]
    ),
    Rule(
        keywords=["name", "who are you", "what are you", "your name"],
        responses=[
            "I'm RuleBot — a simple rule-based chatbot powered by if-else logic!",
            "My name is RuleBot. I match keywords in your input to decide what to say.",
        ]
    ),
    Rule(
        keywords=["how are you", "how r you", "you okay", "you good", "feeling"],
        responses=[
            "I'm just a bunch of if-else statements, so I'm always fine!",
            "Running perfectly, thanks for asking! 😊",
        ]
    ),
    Rule(
        keywords=["bye", "exit", "quit", "goodbye", "farewell", "cya", "see you"],
        responses=[
            "Goodbye! It was nice chatting with you. 👋",
            "See you later! Take care.",
            "Bye! Come back anytime.",
        ],
        terminal=True
    ),
]

FALLBACKS = [
    "Hmm, I didn't catch that. Type 'help' to see what I understand.",
    "No rule matched your input. Try 'help' for a list of topics!",
    "I'm not sure about that one — my if-else logic didn't find a match.",
]


# ── Core logic ────────────────────────────────────────────────────────────────

def get_response(user_input: str) -> tuple[str, bool]:
    """
    Match user input against conversation rules using keyword search.
    
    Returns:
        tuple[str, bool]: (reply_text, is_terminal_flag)
    
    Decision flow:
        for each rule:
            if any keyword found in lowercased input:
                generate response (dynamic or random)
                return (reply, terminal_flag)
        return (random_fallback, False)
    """
    normalized_input = user_input.lower().strip()

    # if-else: check every rule in order
    for rule in RULES:
        if rule.matches(normalized_input):
            reply = rule.get_response()
            return reply, rule.terminal

    # No rule matched — use fallback
    return random.choice(FALLBACKS), False


def format_bot(text: str) -> str:
    """Format bot response with emoji and alignment."""
    return f"  🤖 Bot : {text}"


def format_user_prompt() -> str:
    """Format user input prompt with emoji and alignment."""
    return "  👤 You : "


# ── Session Manager ──────────────────────────────────────────────────────────

class Session:
    """Tracks session statistics and state."""
    
    def __init__(self):
        """Initialize a new session."""
        self.message_count = 0
        self.start_time = datetime.now()
    
    def on_message(self) -> None:
        """Record a new message exchange."""
        self.message_count += 1
    
    def get_duration(self) -> str:
        """Get formatted session duration."""
        elapsed = datetime.now() - self.start_time
        return f"{elapsed.total_seconds():.1f}s"


# ── Main Chatbot Interface ────────────────────────────────────────────────────

def display_header() -> None:
    """Display the welcome header."""
    print("\n" + "=" * Config.SEPARATOR_WIDTH)
    print(f"         {Config.BOT_NAME} — Rule-Based Chatbot")
    print("=" * Config.SEPARATOR_WIDTH)
    print("  Type 'help' for commands, 'bye' to exit.\n")


def display_welcome() -> None:
    """Display opening greeting."""
    print(format_bot(f"Hi! I'm {Config.BOT_NAME} 🤖 — powered by if-else logic."))
    print(format_bot("Type something to get started!\n"))


def display_footer(session: Session) -> None:
    """Display closing footer with session stats."""
    print("=" * Config.SEPARATOR_WIDTH)
    print(f"  Session ended.")
    print(f"  Messages: {session.message_count} | Duration: {session.get_duration()}")
    print("=" * Config.SEPARATOR_WIDTH + "\n")


def validate_input(user_input: str) -> bool:
    """Validate and normalize user input."""
    if not user_input or not user_input.strip():
        print(format_bot("Please type something!\n"))
        return False
    
    if len(user_input) > Config.MAX_INPUT_LENGTH:
        print(format_bot(f"Input too long (max {Config.MAX_INPUT_LENGTH} chars). Please try again.\n"))
        return False
    
    return True


def main() -> None:
    """Run the RuleBot chatbot session."""
    session = Session()
    
    display_header()
    display_welcome()

    # Continuous loop — runs until a terminal rule fires
    while True:
        try:
            user_input = input(format_user_prompt()).strip()
        except (EOFError, KeyboardInterrupt):
            print("\n" + format_bot("Interrupted. Goodbye! 👋"))
            display_footer(session)
            break

        # Validate input
        if not validate_input(user_input):
            continue

        # Get response from rule engine
        reply, is_terminal = get_response(user_input)
        session.on_message()
        
        print(format_bot(reply) + "\n")

        # Exit condition: terminal rule triggered
        if is_terminal:
            display_footer(session)
            break


if __name__ == "__main__":
    main()
