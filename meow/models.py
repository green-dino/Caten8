from django.db import models

class User(models.Model):
    UserId = models.AutoField(primary_key=True)
    # Add other user attributes here

class WorkRoleDetails(models.Model):
    WorkRoleDetailsId = models.AutoField(primary_key=True)
    Description = models.CharField(max_length=255)
    Email = models.CharField(max_length=255)
    Problem = models.CharField(max_length=255)
    Change = models.CharField(max_length=255)
    Request = models.CharField(max_length=255)
    Incident = models.CharField(max_length=255)

class PrimaryWorkRole(models.Model):
    WorkRoleId = models.AutoField(primary_key=True)
    WorkRoleDetailsId = models.ForeignKey(WorkRoleDetails, on_delete=models.CASCADE)

class TroubleTicketInput(models.Model):
    TicketId = models.AutoField(primary_key=True)
    UserId = models.ForeignKey(User, on_delete=models.CASCADE)
    Description = models.CharField(max_length=255)
    Email = models.CharField(max_length=255)
    PrimaryWorkRole = models.ForeignKey(PrimaryWorkRole, on_delete=models.CASCADE)
    ChangeControlRecord = models.ForeignKey('ChangeControlRecord', on_delete=models.CASCADE)

class WorkRoleInteraction(models.Model):
    InteractionId = models.AutoField(primary_key=True)
    Problem = models.CharField(max_length=255)
    Change = models.CharField(max_length=255)
    Request = models.CharField(max_length=255)
    Incident = models.CharField(max_length=255)
    WorkRoleDetailsId = models.ForeignKey(WorkRoleDetails, on_delete=models.CASCADE)

class ChangeControlRecord(models.Model):
    ChangeControlRecordId = models.AutoField(primary_key=True)
    ChangeRequestNumber = models.IntegerField()
    ChangeRequestDate = models.DateField()
    RequestedBy = models.CharField(max_length=255)
    DescriptionOfChange = models.CharField(max_length=255)
    JustificationForChange = models.CharField(max_length=255)
    ImpactAssessment = models.CharField(max_length=255)
    ChangePriority = models.CharField(max_length=255)
    ChangeCategory = models.CharField(max_length=255)
    ChangeImplementationDateTime = models.DateTimeField()
    ChangeApprover = models.CharField(max_length=255)
    DocumentControlInformation = models.ForeignKey('DocumentControlInformation', on_delete=models.CASCADE)
    ChangeImplementationPlan = models.ForeignKey('ChangeImplementationPlan', on_delete=models.CASCADE)
    CommunicationNotification = models.ForeignKey('CommunicationNotification', on_delete=models.CASCADE)
    RiskAssessmentControl = models.ForeignKey('RiskAssessmentControl', on_delete=models.CASCADE)
    DocumentReferences = models.ForeignKey('DocumentReferences', on_delete=models.CASCADE)

class DocumentControlInformation(models.Model):
    DocumentControlInformationId = models.AutoField(primary_key=True)
    DocumentTitle = models.CharField(max_length=255)
    DocumentNumber = models.IntegerField()
    RevisionHistory = models.CharField(max_length=255)
    DateOfLastRevision = models.DateField()
    DocumentOwner = models.CharField(max_length=255)
    DistributionList = models.CharField(max_length=255)

class ChangeImplementationPlan(models.Model):
    ChangeImplementationPlanId = models.AutoField(primary_key=True)
    ScopeOfChange = models.CharField(max_length=255)
    StepsInvolvedInImplementingChange = models.CharField(max_length=255)
    ResourcesRequiredForChange = models.CharField(max_length=255)
    TimelineForEachStep = models.CharField(max_length=255)
    TestingValidationProcedures = models.CharField(max_length=255)
    RollbackPlan = models.CharField(max_length=255)

class CommunicationNotification(models.Model):
    CommunicationNotificationId = models.AutoField(primary_key=True)
    StakeholdersAffectedByChange = models.CharField(max_length=255)
    CommunicationPlan = models.CharField(max_length=255)
    NotificationProcessForImpactedParties = models.CharField(max_length=255)
    TrainingRequirements = models.CharField(max_length=255)

class RiskAssessmentControl(models.Model):
    RiskAssessmentControlId = models.AutoField(primary_key=True)
    RiskAssessmentOfChange = models.CharField(max_length=255)
    IdentificationOfRisks = models.CharField(max_length=255)
    RiskMitigationMeasures = models.CharField(max_length=255)
    ContingencyPlans = models.CharField(max_length=255)
    MonitoringReportingMechanisms = models.CharField(max_length=255)

class DocumentReferences(models.Model):
    DocumentReferencesId = models.AutoField(primary_key=True)
    DocumentedEvidenceArtifacts = models.CharField(max_length=255)
    RecordKeepingRequirements = models.CharField(max_length=255)
    RetentionPeriod = models.CharField(max_length=255)