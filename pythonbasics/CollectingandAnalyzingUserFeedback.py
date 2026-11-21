feedbacks=[
    "Great services",
    "Very satisfied",
    "Could be better",
    "Excellent service",
    "Not happy with the services"
]
positive_feedback_count=0
for comment in feedbacks:
    if "great" in comment.lower() or "excellent" in comment.lower():
        positive_feedback_count+=1
print("Positive feedback count:",positive_feedback_count)
print("User feedback:")
for comment in feedbacks:
    print(comment)        