#
# Autogenerated by Thrift Compiler (0.9.2)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException

from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None



class ErrorModel:
  """
  Attributes:
   - errorId
   - creationTime
   - actualErrorMessage
   - userFriendlyMessage
   - transientOrPersistent
   - rootCauseErrorIdList
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'errorId', None, "DO_NOT_SET_AT_CLIENTS", ), # 1
    (2, TType.I64, 'creationTime', None, None, ), # 2
    (3, TType.STRING, 'actualErrorMessage', None, None, ), # 3
    (4, TType.STRING, 'userFriendlyMessage', None, None, ), # 4
    (5, TType.BOOL, 'transientOrPersistent', None, False, ), # 5
    (6, TType.LIST, 'rootCauseErrorIdList', (TType.STRING,None), None, ), # 6
  )

  def __init__(self, errorId=thrift_spec[1][4], creationTime=None, actualErrorMessage=None, userFriendlyMessage=None, transientOrPersistent=thrift_spec[5][4], rootCauseErrorIdList=None,):
    self.errorId = errorId
    self.creationTime = creationTime
    self.actualErrorMessage = actualErrorMessage
    self.userFriendlyMessage = userFriendlyMessage
    self.transientOrPersistent = transientOrPersistent
    self.rootCauseErrorIdList = rootCauseErrorIdList

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
          self.errorId = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I64:
          self.creationTime = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.actualErrorMessage = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRING:
          self.userFriendlyMessage = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.BOOL:
          self.transientOrPersistent = iprot.readBool();
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.LIST:
          self.rootCauseErrorIdList = []
          (_etype3, _size0) = iprot.readListBegin()
          for _i4 in xrange(_size0):
            _elem5 = iprot.readString();
            self.rootCauseErrorIdList.append(_elem5)
          iprot.readListEnd()
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
    oprot.writeStructBegin('ErrorModel')
    if self.errorId is not None:
      oprot.writeFieldBegin('errorId', TType.STRING, 1)
      oprot.writeString(self.errorId)
      oprot.writeFieldEnd()
    if self.creationTime is not None:
      oprot.writeFieldBegin('creationTime', TType.I64, 2)
      oprot.writeI64(self.creationTime)
      oprot.writeFieldEnd()
    if self.actualErrorMessage is not None:
      oprot.writeFieldBegin('actualErrorMessage', TType.STRING, 3)
      oprot.writeString(self.actualErrorMessage)
      oprot.writeFieldEnd()
    if self.userFriendlyMessage is not None:
      oprot.writeFieldBegin('userFriendlyMessage', TType.STRING, 4)
      oprot.writeString(self.userFriendlyMessage)
      oprot.writeFieldEnd()
    if self.transientOrPersistent is not None:
      oprot.writeFieldBegin('transientOrPersistent', TType.BOOL, 5)
      oprot.writeBool(self.transientOrPersistent)
      oprot.writeFieldEnd()
    if self.rootCauseErrorIdList is not None:
      oprot.writeFieldBegin('rootCauseErrorIdList', TType.LIST, 6)
      oprot.writeListBegin(TType.STRING, len(self.rootCauseErrorIdList))
      for iter6 in self.rootCauseErrorIdList:
        oprot.writeString(iter6)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.errorId is None:
      raise TProtocol.TProtocolException(message='Required field errorId is unset!')
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.errorId)
    value = (value * 31) ^ hash(self.creationTime)
    value = (value * 31) ^ hash(self.actualErrorMessage)
    value = (value * 31) ^ hash(self.userFriendlyMessage)
    value = (value * 31) ^ hash(self.transientOrPersistent)
    value = (value * 31) ^ hash(self.rootCauseErrorIdList)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class ValidatorResult:
  """
  This data structure can be used to store the validation results
  captured during validation step and during the launchExperiment
  operation it can be easilly checked to see the errors occured
  during the experiment launch operation


  Attributes:
   - result
   - errorDetails
  """

  thrift_spec = (
    None, # 0
    (1, TType.BOOL, 'result', None, None, ), # 1
    (2, TType.STRING, 'errorDetails', None, None, ), # 2
  )

  def __init__(self, result=None, errorDetails=None,):
    self.result = result
    self.errorDetails = errorDetails

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
        if ftype == TType.BOOL:
          self.result = iprot.readBool();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.errorDetails = iprot.readString();
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
    oprot.writeStructBegin('ValidatorResult')
    if self.result is not None:
      oprot.writeFieldBegin('result', TType.BOOL, 1)
      oprot.writeBool(self.result)
      oprot.writeFieldEnd()
    if self.errorDetails is not None:
      oprot.writeFieldBegin('errorDetails', TType.STRING, 2)
      oprot.writeString(self.errorDetails)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.result is None:
      raise TProtocol.TProtocolException(message='Required field result is unset!')
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.result)
    value = (value * 31) ^ hash(self.errorDetails)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class ValidationResults:
  """
  Attributes:
   - validationState
   - validationResultList
  """

  thrift_spec = (
    None, # 0
    (1, TType.BOOL, 'validationState', None, None, ), # 1
    (2, TType.LIST, 'validationResultList', (TType.STRUCT,(ValidatorResult, ValidatorResult.thrift_spec)), None, ), # 2
  )

  def __init__(self, validationState=None, validationResultList=None,):
    self.validationState = validationState
    self.validationResultList = validationResultList

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
        if ftype == TType.BOOL:
          self.validationState = iprot.readBool();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.LIST:
          self.validationResultList = []
          (_etype10, _size7) = iprot.readListBegin()
          for _i11 in xrange(_size7):
            _elem12 = ValidatorResult()
            _elem12.read(iprot)
            self.validationResultList.append(_elem12)
          iprot.readListEnd()
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
    oprot.writeStructBegin('ValidationResults')
    if self.validationState is not None:
      oprot.writeFieldBegin('validationState', TType.BOOL, 1)
      oprot.writeBool(self.validationState)
      oprot.writeFieldEnd()
    if self.validationResultList is not None:
      oprot.writeFieldBegin('validationResultList', TType.LIST, 2)
      oprot.writeListBegin(TType.STRUCT, len(self.validationResultList))
      for iter13 in self.validationResultList:
        iter13.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.validationState is None:
      raise TProtocol.TProtocolException(message='Required field validationState is unset!')
    if self.validationResultList is None:
      raise TProtocol.TProtocolException(message='Required field validationResultList is unset!')
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.validationState)
    value = (value * 31) ^ hash(self.validationResultList)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)
