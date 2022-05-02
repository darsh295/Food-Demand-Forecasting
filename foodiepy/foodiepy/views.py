from django.shortcuts import render, redirect
import pickle
from numpy import asarray


def landingpage(request):

	return render(request,'landingpage.html')


def forecasting(request):
	if request.POST:
		model = pickle.load(open('gradientboostmodel.pkl', 'rb'))
		category = request.POST['category']
		cuisine = int(request.POST['cuisine'])
		week = int(request.POST['week'])
		checkout_price = float(request.POST['checkout_price'])
		base_price = float(request.POST['base_price'])
		emailer = int(request.POST['emailer'])
		homepage = int(request.POST['homepage'])
		city = int(request.POST['city'])
		region = int(request.POST['region'])
		op_area = float(request.POST['op_area'])
		center_type = int(request.POST['center_type'])
		category = int(category)
		list = [category,cuisine,week,checkout_price,base_price,emailer,homepage,city,region,op_area,center_type]
		data = asarray([list])
		output = model.predict(data)
		output = int(output)
		if output < 0:
			output = 0
		context = {'output':output,'category':category,'cuisine':cuisine,'week':week,'checkout_price':checkout_price,'base_price':base_price,'emailer':emailer,'homepage':homepage,'city':city,'region':region,'op_area':op_area,'center_type':center_type}
		return render(request, 'forecasting.html', context)
	return render(request,'forecasting.html')

