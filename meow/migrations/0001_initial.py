# Generated by Django 5.1 on 2024-08-27 03:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChangeImplementationPlan',
            fields=[
                ('ChangeImplementationPlanId', models.AutoField(primary_key=True, serialize=False)),
                ('ScopeOfChange', models.CharField(max_length=255)),
                ('StepsInvolvedInImplementingChange', models.CharField(max_length=255)),
                ('ResourcesRequiredForChange', models.CharField(max_length=255)),
                ('TimelineForEachStep', models.CharField(max_length=255)),
                ('TestingValidationProcedures', models.CharField(max_length=255)),
                ('RollbackPlan', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='CommunicationNotification',
            fields=[
                ('CommunicationNotificationId', models.AutoField(primary_key=True, serialize=False)),
                ('StakeholdersAffectedByChange', models.CharField(max_length=255)),
                ('CommunicationPlan', models.CharField(max_length=255)),
                ('NotificationProcessForImpactedParties', models.CharField(max_length=255)),
                ('TrainingRequirements', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='DocumentControlInformation',
            fields=[
                ('DocumentControlInformationId', models.AutoField(primary_key=True, serialize=False)),
                ('DocumentTitle', models.CharField(max_length=255)),
                ('DocumentNumber', models.IntegerField()),
                ('RevisionHistory', models.CharField(max_length=255)),
                ('DateOfLastRevision', models.DateField()),
                ('DocumentOwner', models.CharField(max_length=255)),
                ('DistributionList', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='DocumentReferences',
            fields=[
                ('DocumentReferencesId', models.AutoField(primary_key=True, serialize=False)),
                ('DocumentedEvidenceArtifacts', models.CharField(max_length=255)),
                ('RecordKeepingRequirements', models.CharField(max_length=255)),
                ('RetentionPeriod', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PrimaryWorkRole',
            fields=[
                ('WorkRoleId', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='RiskAssessmentControl',
            fields=[
                ('RiskAssessmentControlId', models.AutoField(primary_key=True, serialize=False)),
                ('RiskAssessmentOfChange', models.CharField(max_length=255)),
                ('IdentificationOfRisks', models.CharField(max_length=255)),
                ('RiskMitigationMeasures', models.CharField(max_length=255)),
                ('ContingencyPlans', models.CharField(max_length=255)),
                ('MonitoringReportingMechanisms', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('UserId', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='WorkRoleDetails',
            fields=[
                ('WorkRoleDetailsId', models.AutoField(primary_key=True, serialize=False)),
                ('Description', models.CharField(max_length=255)),
                ('Email', models.CharField(max_length=255)),
                ('Problem', models.CharField(max_length=255)),
                ('Change', models.CharField(max_length=255)),
                ('Request', models.CharField(max_length=255)),
                ('Incident', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ChangeControlRecord',
            fields=[
                ('ChangeControlRecordId', models.AutoField(primary_key=True, serialize=False)),
                ('ChangeRequestNumber', models.IntegerField()),
                ('ChangeRequestDate', models.DateField()),
                ('RequestedBy', models.CharField(max_length=255)),
                ('DescriptionOfChange', models.CharField(max_length=255)),
                ('JustificationForChange', models.CharField(max_length=255)),
                ('ImpactAssessment', models.CharField(max_length=255)),
                ('ChangePriority', models.CharField(max_length=255)),
                ('ChangeCategory', models.CharField(max_length=255)),
                ('ChangeImplementationDateTime', models.DateTimeField()),
                ('ChangeApprover', models.CharField(max_length=255)),
                ('ChangeImplementationPlan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meow.changeimplementationplan')),
                ('CommunicationNotification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meow.communicationnotification')),
                ('DocumentControlInformation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meow.documentcontrolinformation')),
                ('DocumentReferences', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meow.documentreferences')),
                ('RiskAssessmentControl', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meow.riskassessmentcontrol')),
            ],
        ),
        migrations.CreateModel(
            name='TroubleTicketInput',
            fields=[
                ('TicketId', models.AutoField(primary_key=True, serialize=False)),
                ('Description', models.CharField(max_length=255)),
                ('Email', models.CharField(max_length=255)),
                ('ChangeControlRecord', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meow.changecontrolrecord')),
                ('PrimaryWorkRole', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meow.primaryworkrole')),
                ('UserId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meow.user')),
            ],
        ),
        migrations.AddField(
            model_name='primaryworkrole',
            name='WorkRoleDetailsId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meow.workroledetails'),
        ),
        migrations.CreateModel(
            name='WorkRoleInteraction',
            fields=[
                ('InteractionId', models.AutoField(primary_key=True, serialize=False)),
                ('Problem', models.CharField(max_length=255)),
                ('Change', models.CharField(max_length=255)),
                ('Request', models.CharField(max_length=255)),
                ('Incident', models.CharField(max_length=255)),
                ('WorkRoleDetailsId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meow.workroledetails')),
            ],
        ),
    ]
