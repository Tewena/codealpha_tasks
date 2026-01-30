from nltk.tokenize import word_tokenize


faq_dict = {
    "How do I stay productive when I don’t feel motivated?": "Start with a tiny action (2–5 minutes). Action creates motivation.",
    "What do I do on days I feel lazy or tired?": "Lower the bar, don’t stop. Do the minimum version.",
    "How can I be productive every day?": "Do one non-negotiable task daily.",
    "How do I build consistency without burning out?": "Consistency beats intensity. Keep days light.",
    "How can I actually achieve my goals?": "Turn goals into daily behaviors.",
    "Why do I set goals but never reach them?": "Goals without systems rely on willpower.",
    "What should I do in the next few days to change my life?": "Fix sleep, clean environment, choose 1 focus.",
    "How do I get my life back on track quickly?": "Stop adding goals. Stabilize routines.",
    "What do I do when everything feels overwhelming?": "Pause. Write everything down. Choose one task.",
    "How do I decide what to work on first?": "Ask: 'What makes everything else easier?'",
    "How do I stay productive without burning out?": "Work in cycles, not all day.",
    "How do I build discipline?": "Remove choices. Use rules.",
    "How do I stop procrastinating?": "Make tasks smaller and obvious.",
    "How do I create structure in my life?": "Fixed wake time, fixed work blocks, fixed shutdown."
}

faq_tokens = {}
for question in faq_dict:
    tokens = word_tokenize(question.lower()) #Tokenizing and lowercasing
    tokens = [token for token in tokens if token.isalpha()] #Removing punctuation
    faq_tokens[question] = tokens #Dictionary of Original FAQs: Preprocessed FAQs


#User Input
print("Im Probot! Your Productivity Bot")
text = input("How can I help you?: ").lower()

user_tokens = word_tokenize(text)
user_tokens = [word for word in user_tokens if word.isalpha()]


best_question = None
max_score = 0

for question, tokens in faq_tokens.items():
    score = len(set(user_tokens) & set(tokens))  # Count words in common
    if score > max_score:
        max_score = score
        best_question = question

# Display answer
if best_question:
    print("Probot:", faq_dict[best_question])
else:
    print("Probot: Sorry, I don’t know the answer to that.")