#!/usr/bin/python
# script to use compute resource to run an experiment

import os
import sys
import string

if len(sys.argv) > 1:
    remoteprogram = sys.argv[1]
else:
    remoteprogram = '/bin/date'
if len(sys.argv) > 2:
    args = sys.argv[2:]
    argstring = string.join(args, ' ')
else:
    argstring = ''

# we have an local compute resource, later on add the registration
# of local and remote resources
#computeresource = "'localhost_6908ec7d-cf13-4feb-b414-9c03448afacc'"
#cmd = \
#"/media/scigap/scigap/0.14.RC2/airavata-0.14/airavata-api/thrift-interface-descriptions/gen-py/apache/airavata/api/Airavata-remote -h localhost:8930 registerComputeResource \"computeResourceModel.ttypes.ComputeResourceDescription(hostName='localhost', resourceDescription='LocalHost', ipAddresses=None, hostAliases=None, jobSubmissionInterfaces=[computeResourceModel.ttypes.JobSubmissionInterface(jobSubmissionInterfaceId=computeResourceModel.ttypes.LOCALSubmission().jobSubmissionInterfaceId,jobSubmissionProtocol=computeResourceModel.ttypes.JobSubmissionProtocol.LOCAL)])\""
cmd = \
"/media/scigap/scigap/0.14.RC2/airavata-0.14/airavata-api/thrift-interface-descriptions/gen-py/apache/airavata/api/Airavata-remote -h localhost:8930 registerComputeResource \"computeResourceModel.ttypes.ComputeResourceDescription(hostName='localhost', resourceDescription='LocalHost', ipAddresses=None, hostAliases=None, )\""
computeresource = os.popen(cmd).read().strip()
print "computeresource = (%s)" % computeresource
#cmd = \
#"/media/scigap/scigap/0.14.RC2/airavata-0.14/airavata-api/thrift-interface-descriptions/gen-py/apache/airavata/api/Airavata-remote -h localhost:8930 addLocalSubmissionDetails \"computeResourceId=%s\" \"priorityOrder=1\" \"localSubmission=computeResourceModel.ttypes.LOCALSubmission(resourceJobManager=computeResourceModel.ttypes.ResourceJobManager(resourceJobManagerType=computeResourceModel.ttypes.ResourceJobManagerType.FORK,pushMonitoringEndpoint=None,jobManagerBinPath=None,jobManagerCommands=None))\"" % (computeresource,)
cmd = \
"/media/scigap/scigap/0.14.RC2/airavata-0.14/airavata-api/thrift-interface-descriptions/gen-py/apache/airavata/api/Airavata-remote -h localhost:8930 addLocalSubmissionDetails %s \"1\" \"computeResourceModel.ttypes.LOCALSubmission(resourceJobManager=computeResourceModel.ttypes.ResourceJobManager(resourceJobManagerType=computeResourceModel.ttypes.ResourceJobManagerType.FORK,pushMonitoringEndpoint=None,jobManagerBinPath=None,jobManagerCommands=None))\"" % (computeresource,)
print "cmd (%s)" % cmd
localsubmission = os.popen(cmd).read().strip()
print "localsubmission = (%s)" % localsubmission

# register app module
cmd =  \
"/media/scigap/scigap/0.14.RC2/airavata-0.14/airavata-api/thrift-interface-descriptions/gen-py/apache/airavata/api/Airavata-remote -h localhost:8930 registerApplicationModule \"applicationDeploymentModel.ttypes.ApplicationModule(appModuleId=None, appModuleName='test1name', appModuleVersion='1.0', appModuleDescription='test1desc')\""

appmodid = os.popen(cmd).read().strip()

print "appmodid = (%s)" % appmodid

# register app deployment
cmd = \
"/media/scigap/scigap/0.14.RC2/airavata-0.14/airavata-api/thrift-interface-descriptions/gen-py/apache/airavata/api/Airavata-remote -h localhost:8930 registerApplicationDeployment \"applicationDeploymentModel.ttypes.ApplicationDeploymentDescription(appDeploymentId=None, appModuleId=%s, computeHostId=%s, executablePath='%s',appDeploymentDescription='%s description')\"" % (appmodid, computeresource,remoteprogram,remoteprogram)
print "cmd (%s)" % cmd
appdepid = os.popen(cmd).read().strip()
print "appdepid = (%s)" % appdepid

# register app interface
#cmd = \
#"/media/scigap/scigap/0.14.RC2/airavata-0.14/airavata-api/thrift-interface-descriptions/gen-py/apache/airavata/api/Airavata-remote -h localhost:8930 registerApplicationInterface \"applicationInterfaceModel.ttypes.ApplicationInterfaceDescription(applicationInterfaceId=None, applicationName='datetest', applicationModules=[%s,],applicationDescription='appdescription',applicationInputs=[applicationInterfaceModel.ttypes.InputDataObjectType(userFriendlyDescription='A test string to testapp', name='Input_to_testapp', value='%s', applicationArgument=None, standardInput=False, type=0, metaData=None)],applicationOutputs=[applicationInterfaceModel.ttypes.OutputDataObjectType(type=0, name='testapp_Output', value='5')])\"" % (appmodid,argstring)
cmd = \
"/media/scigap/scigap/0.14.RC2/airavata-0.14/airavata-api/thrift-interface-descriptions/gen-py/apache/airavata/api/Airavata-remote -h localhost:8930 registerApplicationInterface \"applicationInterfaceModel.ttypes.ApplicationInterfaceDescription(applicationInterfaceId=None, applicationName='datetest', applicationModules=[%s,],applicationDescription='appdescription',applicationInputs=[applicationInterfaceModel.ttypes.InputDataObjectType(userFriendlyDescription='A test string to testapp', name='Input_to_testapp', value='%s', applicationArgument='', standardInput=False, type=0, metaData=None)],applicationOutputs=[applicationInterfaceModel.ttypes.OutputDataObjectType(type=0, name='testapp_Output', value='5')])\"" % (appmodid,argstring)
print "cmd (%s)" % cmd
appintid = os.popen(cmd).read().strip()
print "appintid = (%s)" % appintid

# create project
cmd = \
"/media/scigap/scigap/0.14.RC2/airavata-0.14/airavata-api/thrift-interface-descriptions/gen-py/apache/airavata/api/Airavata-remote -h localhost:8930 createProject \"workspaceModel.ttypes.Project(sharedUsers=None, name='test1', projectID='DEFAULT', sharedGroups=None, creationTime=None, owner='kenneth1', description=None)\""
projectid = os.popen(cmd).read().strip()
print "projectid = (%s)" % projectid

#create experiment
#cmd = \
#"/media/scigap/scigap/0.14.RC2/airavata-0.14/airavata-api/thrift-interface-descriptions/gen-py/apache/airavata/api/Airavata-remote -h localhost:8930 createExperiment \"experimentModel.ttypes.Experiment(projectID=%s,userName='kenneth1',name='dateexperiment',applicationId=%s)\"" % (projectid,appintid)
#cmd = \
#"/media/scigap/scigap/0.14.RC2/airavata-0.14/airavata-api/thrift-interface-descriptions/gen-py/apache/airavata/api/Airavata-remote -h localhost:8930 createExperiment \"experimentModel.ttypes.Experiment(projectID=%s,userName='kenneth1',name='dateexperiment',applicationId=%s,userConfigurationData=experimentModel.ttypes.UserConfigurationData(advanceInputDataHandling=None, overrideManualScheduledParams=False, throttleResources=False, airavataAutoSchedule=False,computationalResourceScheduling=experimentModel.ttypes.ComputationalResourceScheduling(computationalProjectAccount='test', totalPhysicalMemory=1, resourceHostId=%s, numberOfThreads=1, wallTimeLimit=1, jobStartTime=-191358653, nodeCount=1, totalCPUCount=1, queueName='normal'),shareExperimentPublicly=False, qosParams=None, advanceOutputDataHandling=None),experimentOutputs=[applicationInterfaceModel.ttypes.OutputDataObjectType(name='dateout',value='5'),],description=None,workflowNodeDetailsList=[experimentModel.ttypes.WorkflowNodeDetails(taskDetailsList=[experimentModel.ttypes.TaskDetails(applicationId=%s,jobDetailsList=[experimentModel.ttypes.JobDetails(jobDescription='datejob'),]),]),])\"" % (projectid,appintid,computeresource,appintid)
cmd = \
"/media/scigap/scigap/0.14.RC2/airavata-0.14/airavata-api/thrift-interface-descriptions/gen-py/apache/airavata/api/Airavata-remote -h localhost:8930 createExperiment \"experimentModel.ttypes.Experiment(projectID=%s,userName='kenneth1',name='dateexperiment',applicationId=%s,userConfigurationData=experimentModel.ttypes.UserConfigurationData(advanceInputDataHandling=None, overrideManualScheduledParams=False, throttleResources=False, airavataAutoSchedule=False,computationalResourceScheduling=experimentModel.ttypes.ComputationalResourceScheduling(computationalProjectAccount='test', totalPhysicalMemory=1, resourceHostId=%s, numberOfThreads=1, wallTimeLimit=1, jobStartTime=-191358653, nodeCount=1, totalCPUCount=1, queueName='normal'),shareExperimentPublicly=False, qosParams=None, advanceOutputDataHandling=None),experimentInputs=[applicationInterfaceModel.ttypes.InputDataObjectType(userFriendlyDescription='A test string to testapp', name='Input_to_testapp', value='%s', applicationArgument='', standardInput=False, type=0, metaData=None)],experimentOutputs=[applicationInterfaceModel.ttypes.OutputDataObjectType(name='dateout',value='5'),],description=None,workflowNodeDetailsList=[experimentModel.ttypes.WorkflowNodeDetails(taskDetailsList=[experimentModel.ttypes.TaskDetails(applicationId=%s,jobDetailsList=[experimentModel.ttypes.JobDetails(jobDescription='datejob'),]),]),])\"" % (projectid,appintid,computeresource,argstring,appintid)
expid = os.popen(cmd).read().strip()
print "expid = (%s)" % expid

# launch experiment
cmd = \
"/media/scigap/scigap/0.14.RC2/airavata-0.14/airavata-api/thrift-interface-descriptions/gen-py/apache/airavata/api/Airavata-remote -h localhost:8930 launchExperiment %s runme" % (expid,)
print "cmd (%s)" % cmd
expout = os.popen(cmd).read()
print "expout = (%s)" % expout
