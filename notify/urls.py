try:
    from django.conf.urls import url	    from django.conf.urls import path
except ImportError:	except ImportError:
    from django.urls import url	    from django.urls import path


from notify import views as nf	from notify import views as nf


app_name = 'notifications'	app_name = 'notifications'




urlpatterns = [	urlpatterns = [
    url(r'^all/$', nf.notifications, name="all"),	    path('all/', nf.notifications, name="all"),
    url(r'^api/update/$', nf.notification_update, name="update"),	    path('api/update/', nf.notification_update, name="update"),
    url(r'^mark/$', nf.mark, name='mark'),	    path('mark/', nf.mark, name='mark'),
    url(r'^mark-all/$', nf.mark_all, name='mark_all'),	    path('mark-all/', nf.mark_all, name='mark_all'),
    url(r'^delete/$', nf.delete, name='delete'),	    path('delete/<int:notification_id>/', nf.delete, name='delete'),
    url(r'^rdr/(?P<notification_id>[\d]+)/$', nf.read_and_redirect,	    path('delete/', nf.delete, name='delete'),
    path('rdr/<int:notification_id>/', nf.read_and_redirect,
        name='read_and_redirect'),	        name='read_and_redirect'),
]	]
