# anagram.py

def is_anagram(str1: str, str2: str) -> bool:
    # Remove spaces and lowercase
    s1 = "".join(ch.lower() for ch in str1 if ch != " ")
    s2 = "".join(ch.lower() for ch in str2 if ch != " ")
    # Quick length check
    if len(s1) != len(s2):
        return False
    # Compare sorted characters
    return sorted(s1) == sorted(s2)

# Example usage
if __name__ == "__main__":
    print(is_anagram("listen", "silent"))    # True
    print(is_anagram("Hello", "Olelh"))      # True
    print(is_anagram("hello", "world"))      # False
    print(is_anagram("Conversation", "Voices rant on"))  # True
