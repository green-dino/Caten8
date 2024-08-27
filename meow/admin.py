from django.contrib import admin
from .models import User, TroubleTicketInput, WorkRoleInteraction, PrimaryWorkRole, WorkRoleDetails, ChangeControlRecord, DocumentControlInformation, ChangeImplementationPlan, CommunicationNotification, RiskAssessmentControl, DocumentReferences

admin.site.register(User)
admin.site.register(TroubleTicketInput)
admin.site.register(WorkRoleInteraction)
admin.site.register(PrimaryWorkRole)
admin.site.register(WorkRoleDetails)
admin.site.register(ChangeControlRecord)
admin.site.register(DocumentControlInformation)
admin.site.register(ChangeImplementationPlan)
admin.site.register(CommunicationNotification)
admin.site.register(RiskAssessmentControl)
admin.site.register(DocumentReferences)