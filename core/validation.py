'''to validate the data of form from client '''


def form_validation(request):
    error_list=[]

    firstname = request.POST.get('firstname')
    lastname = request.POST.get('lastname')
    service = request.POST.get('service')
    email = request.POST.get('email')
    phone = request.POST.get('country-code')+request.POST.get('phone')
    message = request.POST.get('message')

    return firstname,lastname,service,email,phone,message
    
      

