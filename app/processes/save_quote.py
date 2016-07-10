from app.models import prospects
class SaveQuote():
    def run(data):
        qoute=data.get('qoute')
        qoute=prospects(**qoute)
        print (qoute.feel)
        qoute.save()
