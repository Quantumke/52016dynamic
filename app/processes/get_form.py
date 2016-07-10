class GetForm():
    def run(request_data,data):
        data['qoute']=GetForm.get_details(request_data)
        print (data, request_data)
    def get_details(request_data):
        quote={}
        quote['name']=request_data.get('name')
        quote['email']=request_data.get('email')
        quote['type']=request_data.get('type')
        quote['feel']=request_data.get('feel')
        quote['description']=request_data.get('description')
        quote['budget']=request_data.get('budget')
        return quote
