from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import ListView, View

from src.apps.whisper.filters import EmailNotificationFilter
from src.apps.whisper.main import NotificationService
from src.apps.whisper.models import EmailNotification



class EmailNotificationListView( ListView):
    model = EmailNotification
    template_name = 'whisper/emailnotification_list.html'

    def get_permission_name(self):
        return "whisper.view_emailnotification"

    def get_queryset(self):
        return self.model.objects.order_by('created_at')

    def get_context_data(self, **kwargs):
        context = super(EmailNotificationListView, self).get_context_data(**kwargs)
        email_filter = EmailNotificationFilter(self.request.GET, queryset=self.get_queryset())
        context['filter_form'] = email_filter.form

        paginator = Paginator(email_filter.qs, 50)
        page_number = self.request.GET.get('page')
        user_page_object = paginator.get_page(page_number)

        context['object_list'] = user_page_object
        return context


class EmailNotificationRetryView(View):
    def get_permission_name(self):
        return "whisper.change_emailnotification"

    def get(self, request, *args, **kwargs):
        email_notification_id = kwargs.get('pk')
        email_notification = get_object_or_404(EmailNotification, id=email_notification_id)

        notification_service = NotificationService(
            heading=email_notification.subject,
            description=email_notification.body,
            obj=email_notification.content_object,
            retry_id=email_notification.id,
            recipient_list=[email_notification.recipient]
        )

        context = {
            'body': email_notification.body
        }

        # Retry sending the email
        notification_service.send_email_notification(email_notification.template_name, context,
                                                     [email_notification.recipient])

        return redirect('whisper:emailnotification-list')
