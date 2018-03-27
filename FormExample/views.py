#importing required packages
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.utils.encoding import smart_str
from django.core.mail import EmailMessage

#disabling csrf (cross site request forgery)
@csrf_exempt
def index(request):
    #if post request came
    if request.method == 'POST':
        #getting values from post
        name = request.POST.get('name')
        email = request.POST.get('email')
        Institution = request.POST.get('Institution')

        #adding the values in a context variable
        context = {
            'name': name,
            'email': email,
            'Institution': Institution
        }

        email = EmailMessage('Someone is downloading your dataset', str('full name: '+context['name']+'\n'+'email address: '+context['email']+'\n'+'Institution: '+context['Institution']
                                                                        +'\n\n Here is your paraphrase website: http://web.cse.ohio-state.edu/~lan.105/project.html'), to=['lan.105@osu.edu', 'weixu@cse.ohio-state.edu'])
        email.send()
        #getting our showdata template
        response = HttpResponse(
            content_type='application/force-download')  # mimetype is replaced by content_type for django 1.7
        response['Content-Disposition'] = 'attachment; filename=%s' % smart_str('LanguageNet.zip')
        response['X-Sendfile'] = smart_str('LanguageNet.zip')
        # It's usually a good idea to set the 'Content-Length' header too.
        # You can also set any other required headers: Cache-Control, etc.
        return response
    else:
        #if post request is not true
        #returing the form template
        template = loader.get_template('index.html')
        return HttpResponse(template.render())
