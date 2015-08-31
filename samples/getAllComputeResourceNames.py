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
from apache.airavata.model.security.ttypes import AuthzToken
from apache.airavata.api.ttypes import *
from apache.airavata.model.workspace.ttypes import *

from thrift import Thrift
from thrift.transport import TSocket, TSSLSocket, TTransport
from thrift.protocol import TBinaryProtocol

try:
    # Read Airavata Client properties
    airavataConfig = ConfigParser.RawConfigParser()
    airavataConfig.read('../conf/airavata-client.properties')

    host = airavataConfig.get('AiravataServer', 'host')
    port = airavataConfig.getint('AiravataServer', 'port')

    # Create transport object. Comment and uncomment TLS or nonTLS according to server configuration
    # transport = TSocket.TSocket(host, port)
    transport = TSSLSocket.TSSLSocket(host, port, "True", \
         airavataConfig.get('AiravataServer', 'server_ca_cert'), \
         airavataConfig.get('AiravataServer', 'client_key'), \
         airavataConfig.get('AiravataServer', 'server_cert'))

    # Use Buffered Protocol to speedup over raw sockets
    transport = TTransport.TBufferedTransport(transport)

    # Airavata currently uses Binary Protocol
    protocol = TBinaryProtocol.TBinaryProtocol(transport)

    # Create a Airavata client to use the protocol encoder
    airavataClient = Airavata.Client(protocol)

    # Connect to Airavata Server
    transport.open()

    # Create a dummy OAuth2 Token object
    oauthDummyToken = AuthzToken("default-token")

    computeResourceNames = airavataClient.getAllComputeResourceNames(oauthDummyToken);

    print computeResourceNames

    # Close Connection to Airavata Server
    transport.close()

except Thrift.TException, tx:
    print '%s' % (tx.message)

