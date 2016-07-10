from app.models import feedback
class SaveFeedback():
    def run(data):
        save_feedback=data.get('feedback')
        save_feedback=feedback(**save_feedback)
        save_feedback.save()
