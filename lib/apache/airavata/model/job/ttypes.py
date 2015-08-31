#
# Autogenerated by Thrift Compiler (0.9.2)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException
import apache.airavata.model.status.ttypes


from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None



class JobModel:
  """
  Attributes:
   - jobId
   - taskId
   - processId
   - jobDescription
   - creationTime
   - jobStatus
   - computeResourceConsumed
   - jobName
   - workingDir
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'jobId', None, None, ), # 1
    (2, TType.STRING, 'taskId', None, None, ), # 2
    (3, TType.STRING, 'processId', None, None, ), # 3
    (4, TType.STRING, 'jobDescription', None, None, ), # 4
    (5, TType.I64, 'creationTime', None, None, ), # 5
    (6, TType.STRUCT, 'jobStatus', (apache.airavata.model.status.ttypes.JobStatus, apache.airavata.model.status.ttypes.JobStatus.thrift_spec), None, ), # 6
    (7, TType.STRING, 'computeResourceConsumed', None, None, ), # 7
    (8, TType.STRING, 'jobName', None, None, ), # 8
    (9, TType.STRING, 'workingDir', None, None, ), # 9
  )

  def __init__(self, jobId=None, taskId=None, processId=None, jobDescription=None, creationTime=None, jobStatus=None, computeResourceConsumed=None, jobName=None, workingDir=None,):
    self.jobId = jobId
    self.taskId = taskId
    self.processId = processId
    self.jobDescription = jobDescription
    self.creationTime = creationTime
    self.jobStatus = jobStatus
    self.computeResourceConsumed = computeResourceConsumed
    self.jobName = jobName
    self.workingDir = workingDir

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.jobId = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.taskId = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.processId = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRING:
          self.jobDescription = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.I64:
          self.creationTime = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.STRUCT:
          self.jobStatus = apache.airavata.model.status.ttypes.JobStatus()
          self.jobStatus.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 7:
        if ftype == TType.STRING:
          self.computeResourceConsumed = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 8:
        if ftype == TType.STRING:
          self.jobName = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 9:
        if ftype == TType.STRING:
          self.workingDir = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('JobModel')
    if self.jobId is not None:
      oprot.writeFieldBegin('jobId', TType.STRING, 1)
      oprot.writeString(self.jobId)
      oprot.writeFieldEnd()
    if self.taskId is not None:
      oprot.writeFieldBegin('taskId', TType.STRING, 2)
      oprot.writeString(self.taskId)
      oprot.writeFieldEnd()
    if self.processId is not None:
      oprot.writeFieldBegin('processId', TType.STRING, 3)
      oprot.writeString(self.processId)
      oprot.writeFieldEnd()
    if self.jobDescription is not None:
      oprot.writeFieldBegin('jobDescription', TType.STRING, 4)
      oprot.writeString(self.jobDescription)
      oprot.writeFieldEnd()
    if self.creationTime is not None:
      oprot.writeFieldBegin('creationTime', TType.I64, 5)
      oprot.writeI64(self.creationTime)
      oprot.writeFieldEnd()
    if self.jobStatus is not None:
      oprot.writeFieldBegin('jobStatus', TType.STRUCT, 6)
      self.jobStatus.write(oprot)
      oprot.writeFieldEnd()
    if self.computeResourceConsumed is not None:
      oprot.writeFieldBegin('computeResourceConsumed', TType.STRING, 7)
      oprot.writeString(self.computeResourceConsumed)
      oprot.writeFieldEnd()
    if self.jobName is not None:
      oprot.writeFieldBegin('jobName', TType.STRING, 8)
      oprot.writeString(self.jobName)
      oprot.writeFieldEnd()
    if self.workingDir is not None:
      oprot.writeFieldBegin('workingDir', TType.STRING, 9)
      oprot.writeString(self.workingDir)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.jobId is None:
      raise TProtocol.TProtocolException(message='Required field jobId is unset!')
    if self.taskId is None:
      raise TProtocol.TProtocolException(message='Required field taskId is unset!')
    if self.processId is None:
      raise TProtocol.TProtocolException(message='Required field processId is unset!')
    if self.jobDescription is None:
      raise TProtocol.TProtocolException(message='Required field jobDescription is unset!')
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.jobId)
    value = (value * 31) ^ hash(self.taskId)
    value = (value * 31) ^ hash(self.processId)
    value = (value * 31) ^ hash(self.jobDescription)
    value = (value * 31) ^ hash(self.creationTime)
    value = (value * 31) ^ hash(self.jobStatus)
    value = (value * 31) ^ hash(self.computeResourceConsumed)
    value = (value * 31) ^ hash(self.jobName)
    value = (value * 31) ^ hash(self.workingDir)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)
