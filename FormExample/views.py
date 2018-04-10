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
																		+'\n\n Here is your paraphrase website: http://web.cse.ohio-state.edu/~lan.105/project.html'), to=['lan.105@osu.edu','weixu@cse.ohio-state.edu'])
		email.send()
		'''
		#getting our showdata template
		response = HttpResponse(
			content_type='application/force-download')  # mimetype is replaced by content_type for django 1.7
		response['Content-Disposition'] = 'attachment; filename=%s' % smart_str('LanguageNet.zip')
		response['X-Sendfile'] = smart_str('LanguageNet.zip')
		# It's usually a good idea to set the 'Content-Length' header too.
		# You can also set any other required headers: Cache-Control, etc.
		return response
		'''
		email = EmailMessage('Language-Net: The Large Scale Paraphrase Dataset', str('Hi '+context['name']+',\n\n'+'Thanks for your interest in our Twitter URL dataset. Please check this Dropbox link to download full dataset:\n https://www.dropbox.com/sh/hw32kn0k6i0d35c/AABsfTgtdJ-x2OSdRedBUzqIa?dl=0 \nThis dataset ranges from 10/10/2016 to 01/08/2017, which is the same as what we use in emnlp 2017 paper. It contains annotated training/testing set, candidate set, silver standard corpus (all pairs with predicted probability, as well as selected pairs cutting at threshold 0.5), original json file, URL webpage and annotated training/testing set. Specific readme can be found in my Github page (https://github.com/lanwuwei/language-net).\n'
+'\nURL_data_2017_prob.txt file contains a whole year data: URL based paraphrase candidate pairs in 2017 (totally 2,869,657 pairs), which are scored by PWI model (http://www.aclweb.org/anthology/N16-1108) using character embedding. The model is trained on Twitter_URL_Corpus_train.txt (collected between Oct - Dec, 2016) and evaluated on Twitter_URL_Corpus_test.txt (collected in January 2017), and the evaluation score is 0.752 F1. You can set your own threshold to select a subset of this URL-2017 data. The file format: predicted_probability \\t sent1 \\t sent2 \n'+'\n\nBest,\nWuwei'), to=[context['email']])
		email.send()
		#template = loader.get_template('index.html')
		return HttpResponse('The dataset has been sent to your email box.')
	else:
		#if post request is not true
		#returing the form template
		template = loader.get_template('index.html')
		return HttpResponse(template.render())
