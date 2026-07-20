from django.contrib import admin
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.utils.translation import gettext as _
from django.utils.encoding import force_str
from solo.admin import SingletonModelAdmin
from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin, \
    PolymorphicChildModelFilter

from .models import Response, \
    KnowledgeResponse, RestitutionResponse, TechnologyResponse, \
    GeopoliticsResponse, MarketizationResponse, MassificationResponse, \
    Config

# Register your models here.
@admin.register(Response)
class ResponseAdmin(PolymorphicParentModelAdmin):
    child_models = (KnowledgeResponse, RestitutionResponse, TechnologyResponse, GeopoliticsResponse, MarketizationResponse, MassificationResponse)
    list_filter = [PolymorphicChildModelFilter, 'status']
    polymorphic_list = True
    ordering = ['-status', 'created']

    list_display = ('_type', 'status', 'created', '_full_response')
    list_display_links = ('_type', 'status', 'created', '_full_response')
    actions = ['update_status_pending_review', 'update_status_approved', 'update_status_denied_archive']

    def _type(self, obj):
        return obj._meta.verbose_name
    _type.short_description = 'Response Type'

    def _full_response(self, obj):
        return obj.get_full_response()
    _full_response.short_description = 'Response'

    def has_add_permission(self, request, obj=None):
        return False

    @admin.action(description="Set selected response(s) to 'pending review'")
    def update_status_pending_review(self, request, queryset):
        queryset.update(status=Response.Status.PENDING_REVIEW)

    @admin.action(description="Set selected response(s) to 'approved'")
    def update_status_approved(self, request, queryset):
        queryset.update(status=Response.Status.APPROVED)

    @admin.action(description="Set selected response(s) to 'denied' and archive them (don't delete them)")
    def update_status_denied_archive(self, request, queryset):
        queryset.update(status=Response.Status.DENIED_ARCHIVE)


@admin.register(KnowledgeResponse)
class KnowledgeResponseChildAdmin(PolymorphicChildModelAdmin):
    base_model = KnowledgeResponse

@admin.register(RestitutionResponse)
class RestitutionResponseChildAdmin(PolymorphicChildModelAdmin):
    base_model = RestitutionResponse

@admin.register(TechnologyResponse)
class TechnologyResponseChildAdmin(PolymorphicChildModelAdmin):
    base_model = TechnologyResponse

@admin.register(GeopoliticsResponse)
class GeopoliticsResponseChildAdmin(PolymorphicChildModelAdmin):
    base_model = GeopoliticsResponse

@admin.register(MarketizationResponse)
class MarketizationResponseChildAdmin(PolymorphicChildModelAdmin):
    base_model = MarketizationResponse

@admin.register(MassificationResponse)
class MassificationResponseChildAdmin(PolymorphicChildModelAdmin):
    base_model = MassificationResponse


@admin.register(Config)
class ConfigModalAdmin(SingletonModelAdmin):
    fields = ['responses_enabled']

    # Fix user message success vs info
    def response_change(self, request, obj):
        msg = _("{obj} was changed successfully.").format(obj=force_str(obj))
        if "_continue" in request.POST:
            self.message_user(request, msg + " " + _("You may edit it again below."), messages.SUCCESS)
            return HttpResponseRedirect(request.path)
        else:
            self.message_user(request, msg, messages.SUCCESS)
            return HttpResponseRedirect("../../")