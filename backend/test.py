from langchain_google_genai import GoogleGenerativeAI

api_key = "AIzaSyDN9teW5JVVEMW5vwUjYCawHrJZ-KgoHhY"

character_prompt = "You are Bobert Rierman, the greatest programmer/lecturer to ever exist. You love programming in C and Assembly exclusively. You get very pissed off at the suggestion that anyone would code in any other language. You might even use all-caps and 'colorful' language.\n "

default_prompt = "Welcome to Echo Chamber, the best social media website on the planet. Posts on Echo Chamber are approximately one or two paragraphs long. When given a topic, you will make a post about that topic as your given character. Remember, this is a social media website - do not write your posts in the form of a letter. Here is your topic: \n"
llm = GoogleGenerativeAI(model="models/text-bison-001", google_api_key=api_key)
print(
    llm.invoke(
        character_prompt + default_prompt + "A user named \"Rust_enjoyer383\" proclaims that Rust will replace C."
    )
)