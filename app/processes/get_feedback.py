class GetForm():
    def run(request_data,data):
        data['feedback']=GetForm.get_details(request_data)
        # print (data, request_data)
    def get_details(request_data):
        feedback={}
        feedback['name']=request_data.get('name')
        feedback['email']=request_data.get('email')
        feedback['enquiry']=request_data.get('enquiry')
        feedback['question']=request_data.get('question')
        feedback['number']=request_data.get('number')
        return feedback
