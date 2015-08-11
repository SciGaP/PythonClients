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

sys.path.append('../lib')

from apache.airavata.api import Airavata
from apache.airavata.api.ttypes import *
from apache.airavata.model.workspace.experiment.ttypes import *

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

# wrapper around airavataClient object
class AiravataClient():

    def __init__(self):
        try:
            # Read Airavata Client properties
            self.airavataConfig = ConfigParser.RawConfigParser()
            self.airavataConfig.read('../conf/airavata-client.properties')

            # Create a socket to the Airavata Server
            self.transport = TSocket.TSocket(self.airavataConfig.get('AiravataServer', 'host'),
                                            (self.airavataConfig.getint('AiravataServer', 'port')))

            # Set socket timeout
            self.transport.setTimeout(10000)

            # Use Buffered Protocol to speedup over raw sockets
            self.transport = TTransport.TBufferedTransport(self.transport)

            # Airavata currently uses Binary Protocol
            self.protocol = TBinaryProtocol.TBinaryProtocol(self.transport)

            # Create a Airavata client to use the protocol encoder
            self.airavataClient = Airavata.Client(self.protocol)

            # Read the gateway id from properties file
            self.gateway_id = self.airavataConfig.get('GatewayProperties', 'gateway_id')

        except Thrift.TException, tx:
            print '%s' % (tx.message)

    def open(self):
        self.transport.open()

    def close(self):
        self.transport.close()

    def properties(self):
        print 'host:', self.airavataConfig.get('AiravataServer', 'host')
        print 'port:', self.airavataConfig.getint('AiravataServer', 'port')
        print 'gateway_id:', self.airavataConfig.get('GatewayProperties', 'gateway_id')

    def version(self):
        print 'Airavata Server Version is:', self.airavataClient.getAPIVersion()

    def getAllAppModules(self):
        return self.airavataClient.getAllAppModules(self.gateway_id)

    def getAllComputeResourceNames(self):
        return self.airavataClient.getAllComputeResourceNames()

    def getAllApplicationInterfaceNames(self):
        return self.airavataClient.getAllApplicationInterfaceNames(self.gateway_id)

    def getExperiment(self, expId):
        experiment = self.airavataClient.getExperiment(expId)
        print 'Experiment gatewayId', experiment.gatewayId
        print 'Experiment projectId', experiment.projectId
        print 'Experiment username', experiment.userName
        print 'Experiment configurationdata->computationalResource', experiment.userConfigurationData.computationalResourceScheduling.queueName

        print 'Experimetn status int ', experiment.experimentStatus.state
        print 'Experimet Status' , ExperimentState._VALUES_TO_NAMES[experiment.experimentStatus.state]

    def createExperiment(self):
        amberId = "Amber_66ca2b6c-ef36-409d-9f2b-67630c760609"
        inputs = self.airavataClient.getApplicationInputs(amberId)
        for input in inputs:
            # print input.name
            if input.name == "Heat_Restart_File":
                input.value = "file:///home/airavata/production/appInputs/AMBER_FILES/02_Heat.rst"
            elif input.name == "Parameter_Topology_File":
                input.value ="file:///home/airavata/production/appInputs/AMBER_FILES/prmtop"
            elif input.name == "Production_Control_File":
                input.value = "file:///home/airavata/production/appInputs/AMBER_FILES/03_Prod.in"

        outputs = self.airavataClient.getApplicationOutputs(self.token, amberId)
        # for output in outputs:
            # print output.name
        projectId = "DefaultProject_f74091d6-b988-48b1-b847-59dca2fc5b80"
        stampedeHostName = "stampede.tacc.xsede.org"


        experiment = Experiment()
        experiment.gatewayId = 'default'
        experiment.projectId = projectId
        experiment.userName = "smarru"
        experiment.experimentName = "Sample_experiment"
        experiment.description = "Test experiment"
        experiment.executionId = amberId
        experiment.experimentInputs = inputs
        experiment.experimentOutputs = outputs

        computeResources = self.airavataClient.getAvailableAppInterfaceComputeResources(amberId)
        id = None
        for key, value in computeResources.iteritems():
            # print key , " " , value
            if value == stampedeHostName:
                id = key
                break

        #Create a computational resource scheduling model
        crsm = ComputationalResourceScheduling()
        crsm.totalCPUCount = 4
        crsm.nodeCount = 1
        crsm.queueName = "development"
        crsm.wallTimeLimit = 30
        crsm.totalPhysicalMemory = 1
        crsm.resourceHostId = id

        ucdm = UserConfigurationData()
        ucdm.computationalResourceScheduling = crsm
        ucdm.airavataAutoSchedule = False
        ucdm.overrideManualScheduledParams = False
        experiment.userConfigurationData  = ucdm

        expId = self.airavataClient.createExperiment("default", experiment)

        while (1):
            experiment = self.airavataClient.getExperiment(expId)
            print 'Experiment', experiment
            print 'Experimetn status int ', experiment.experimentStatus.state
            print 'Experimet Status' , ExperimentState._VALUES_TO_NAMES[experiment.experimentStatus.state]
            time.sleep(2)

def main():
    a = AiravataClient()
    a.open()
    a.properties()
    a.version()
    #print a.getAllComputeResourceNames()
    #print a.getAllAppModules()
    print a.getAllApplicationInterfaceNames()

    #expId = 'FFF_5ff48b34-2bbd-4294-8ebb-073484f4d977'
    #a.getExperiment(expId)
    a.close()


if __name__ == "__main__":
    main()