#!/usr/bin/env python

#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements. See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership. The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License. You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied. See the License for the
# specific language governing permissions and limitations
# under the License.
#

import sys, ConfigParser
import time
from transport.TSSLSocket import TSSLSocket

sys.path.append('../lib')

from airavata.api import Airavata
from airavata.model.experiment.ttypes import ExperimentModel, UserConfigurationDataModel, ExperimentType
from airavata.model.scheduling.ttypes import ComputationalResourceSchedulingModel
from airavata.model.security.ttypes import AuthzToken
from airavata.model.status.ttypes import ExperimentState

import Thrift
from transport import TSocket, TTransport
from protocol import TBinaryProtocol


# from apache.airavata.api import Airavata
# from apache.airavata.model.experiment.ttypes import *
# from apache.airavata.model.security.ttypes import *
# from apache.airavata.model.status.ttypes import *
# from apache.airavata.model.scheduling.ttypes import *

# from thrift import Thrift
# from thrift.transport import TSocket
# from thrift.transport import TTransport
# from thrift.protocol import TBinaryProtocol

try:
    # Read Airavata Client properties
    airavataConfig = ConfigParser.RawConfigParser()
    airavataConfig.read('../conf/airavata-client.properties')

    # Create a socket to the Airavata Server
    transport = TSSLSocket(airavataConfig.get('AiravataServer', 'host'), airavataConfig.get('AiravataServer', 'port') ,\
                           True,'/Users/syodage/Projects/codestation/pytry/Airavata/conf/cacert.pem','keyfile/path',\
                           'cert/file/path',None)

    # Use Buffered Protocol to speedup over raw sockets
    transport = TTransport.TBufferedTransport(transport)

    # Airavata currently uses Binary Protocol
    protocol = TBinaryProtocol.TBinaryProtocol(transport)

    # Create a Airavata client to use the protocol encoder
    airavataClient = Airavata.Client(protocol)

    # Connect to Airavata Server
    transport.open()

    # create dummy token
    token =  AuthzToken("default-token")
    # gateway id
    gatewayId = "default"
    #check airavata server is up and running.
    print 'Airavata Server Version is:', airavataClient.getAPIVersion(token)

    appId = "Python_Echo_069ea651-4937-4b89-9684-fb0682ac52f5"
    inputs = airavataClient.getApplicationInputs(token,appId)
    for input in inputs:
        # print input.name
        if input.name == "Heat_Restart_File":
            input.value = "file:///home/airavata/production/appInputs/AMBER_FILES/02_Heat.rst"
        elif input.name == "Parameter_Topology_File":
            input.value ="file:///home/airavata/production/appInputs/AMBER_FILES/prmtop"
        elif input.name == "Production_Control_File":
            input.value = "file:///home/airavata/production/appInputs/AMBER_FILES/03_Prod.in"

    outputs = airavataClient.getApplicationOutputs(token, appId)
    for output in outputs:
        print output.name
    projectId = "gsoc_2015_ad32cf8f-90dd-42a0-8e11-04320530659e"
    projectId = "Sample_546ded4b-3b73-43fe-a275-fa2513e9bfa6"
    stampedeHostName = "stampede.tacc.xsede.org"

    # create ExperimentModel for the experiment
    experiment = ExperimentModel()
    experiment.gatewayId = 'default'
    experiment.projectId = projectId
    experiment.experimentType = ExperimentType.SINGLE_APPLICATION
    experiment.userName = "admin"
    experiment.experimentName = "Sample_experiment"
    experiment.description = "Test experiment"
    experiment.executionId = appId
    # experiment.experimentInputs = inputs
    # experiment.experimentOutputs = outputs

    computeResources = airavataClient.getAvailableAppInterfaceComputeResources(token, appId)
    id = None
    for key, value in computeResources.iteritems():
        # print key , " " , value
        if value == stampedeHostName:
            id = key
            break

    # Create a computational resource scheduling model
    crsm = ComputationalResourceSchedulingModel()
    crsm.totalCPUCount = 4
    crsm.nodeCount = 1
    crsm.queueName = "development"
    crsm.wallTimeLimit = 30
    crsm.totalPhysicalMemory = 1
    crsm.resourceHostId = id

    # Create a User configuration data model
    ucdm = UserConfigurationDataModel()
    ucdm.computationalResourceScheduling = crsm
    ucdm.airavataAutoSchedule = False
    ucdm.overrideManualScheduledParams = False
    experiment.userConfigurationData  = ucdm

    # Create experiment
    expId = airavataClient.createExperiment(token, gatewayId, experiment)

    # launch experiment
    airavataClient.launchExperiment(token, expId, airavataConfig.get('GatewayProperties','cred_token_id'))

    while (1):
        experiment = airavataClient.getExperiment(token, expId)
        #print 'Experiment', experiment
        #print 'Experimetn status int ', experiment.experimentStatus.state
        expStatusInt = experiment.experimentStatus.state
        expStatus = ExperimentState._VALUES_TO_NAMES[experiment.experimentStatus.state]
        print 'Experimet Status' , expStatus
        if expStatusInt == ExperimentState.COMPLETED or expStatusInt == ExperimentState.CANCELED \
                or expStatusInt == ExperimentState.FAILED:
            break
        time.sleep(2)

    # Close Connection to Airavata S"erver
    transport.close()

except Thrift.TException, tx:
    print '%s' % (tx.message)

