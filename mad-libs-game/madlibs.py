### Mad Libs game
## Game created to practice the following:
# Creating a function.
# Request input from user.
# Inject values from input into text, allowing for variable values to be embedded using f-string.
# Use of triple-quotes (""") to allow multi-line strings without needing to use \n.
# strip() to clean up whitespace
# condtional to ensure the script is only run directly.

def mad_libs():                 # Defines a function
    print("Welcome to the Mad Libs Game!")
    print("Please provide the following words:\n")

    # Collect words to be used:
    adjective = input("Enter and adjective: ")
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    adverb = input("Enter an adverb: ")
    place = input("Enter a place: ")
    plural_noun = input("Enter a plural noun: ")

    # Use f""" to embed variable values and use multiple lines without needing \n
    story = f"""
    Today I went to the {place}. It was a really {adjective} day.
    I saw a {noun} that {verb} {adverb} past a group of {plural_noun}.
    Everyone around was amazed and couldn't stop talking about it!
    """

    # Output the story:
    print("\nHere is your Mad Lib storay:")
    print(story.strip())        # Removes leading and trailing newlines or spaces.

# Run the game:
if __name__ == "__main__":      # Checks whether the script is being run directly and not inported as a module
    mad_libs()                  # If it is then call mad_libs() function created above